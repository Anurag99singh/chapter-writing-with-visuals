"""Fail-closed metadata guards. The host must independently read actual artifacts."""
from __future__ import annotations
import argparse,json,math,re

CHECKS=('references_verified','story_architecture','write_format_humanize','story_integrity','formatted_document_verified')

class Blocked(ValueError):pass

def need(condition,message):
    if not condition:raise Blocked(message)

def score_ok(value,threshold):
    return isinstance(value,(int,float)) and not isinstance(value,bool) and math.isfinite(value) and threshold<=value<=1

def dispatch(role,model,reasoning_effort,fork_turns):
    roles={'controller','chapter_writing','canonical_clean_evaluate','visual_generation','selector','adapt','render','installed_review','generated_evaluate','unified_review','visual_decisions','visual_placement','final_clean_evaluate','writing_revision','placement_revision'}
    need(role in roles,'Unknown role')
    need(model=='gpt-6-sol','Required model: gpt-6-sol')
    need(reasoning_effort==('medium' if role in {'chapter_writing','writing_revision'} else 'low'),'Incorrect reasoning setting')
    need(fork_turns=='none','Actual fresh context required')
    return True

def _receipt(r,artifact_id,revision,threshold):
    need(r.get('passed') is True and score_ok(r.get('score'),threshold),'Independent evaluation has not passed')
    need(bool(r.get('report_id')),'Missing independent evaluation report')
    need(r.get('artifact_id')==artifact_id and r.get('artifact_revision')==revision,'Stale evaluation receipt')

def canonical_ready(s):
    a=s.get('canonical') or {};need(a.get('id') and a.get('revision'),'Missing canonical chapter')
    need(a.get('outline_revision')==s['outline']['revision'] and a.get('evidence_revision')==s['evidence']['revision'],'Canonical inputs stale')
    p=a.get('native_presentation') or {}
    need(p.get('passed') is True and p.get('report_id') and p.get('artifact_id')==a['id'] and p.get('artifact_revision')==a['revision'],'Missing or stale native presentation proof')
    e=a.get('evaluation') or {};_receipt(e,a['id'],a['revision'],.85)
    need(all(e.get('checks',{}).get(k,{}).get('passed') is True and e['checks'][k].get('evidence') for k in CHECKS),'Missing integrated execution evidence')
    return a

def plan_ready(s):
    a=canonical_ready(s);p=s.get('generation_plan') or {}
    need(p.get('id') and p.get('canonical_revision')==a['revision'] and p.get('evidence_revision')==s['evidence']['revision'],'Missing or stale generation plan')
    expected=s['outline'].get('subsection_ids');need(isinstance(expected,list) and expected and len(expected)==len(set(expected)),'Missing unique approved subsection IDs')
    entries=p.get('entries');need(isinstance(entries,list) and [x.get('subsection_id') for x in entries]==expected,'Plan subsection coverage/order mismatch')
    need(all(type(x.get('required')) is bool and x.get('reason') for x in entries),'Missing generation requirement/reason')
    return p

def candidate_ready(c,s):
    need(re.fullmatch(r'GEN-\d+',c.get('id','')) and c.get('origin')=='GENERATED_EXPLAINER','Only generated candidates are valid')
    need(c.get('canonical_revision')==s['canonical']['revision'] and c.get('evidence_revision')==s['evidence']['revision'],'Stale generated candidate')
    need(c.get('mode') in {'DATA_EXPLAINER','TOPIC_EXPLAINER','HUMOUR_METAPHOR'},'Unknown visual mode')
    need(type(c.get('attempt')) is int and 1<=c['attempt']<=2,'Render attempt limit exceeded')
    need(c.get('brief_id') and c.get('asset_id') and re.fullmatch(r'[0-9a-f]{64}',c.get('asset_sha256','')),'Missing exact asset/brief provenance')
    for key in ('installed_review','evidence_review'):
        r=c.get(key) or {};need(r.get('passed') is True and r.get('report_id') and r.get('asset_sha256')==c['asset_sha256'],'Missing/stale image acceptance receipt')
    need(score_ok(c['evidence_review'].get('score'),.90),'Generated evidence threshold not met')
    if c['mode']=='DATA_EXPLAINER':need(c.get('data_lock_passed') is True and c.get('data_lock_locator'),'DATA_LOCK not verified')
    return True

def visual_ready(s,decisions=True):
    p=plan_ready(s);cs=s.get('candidates',[]);need(isinstance(cs,list),'Invalid candidate set')
    ids=[c.get('id') for c in cs];need(len(ids)==len(set(ids)),'Duplicate candidate IDs')
    entries={e['subsection_id']:e for e in p['entries']};covered=set()
    for c in cs:
        need(c.get('subsection_id') in entries and entries[c['subsection_id']]['required'],'Candidate outside approved generation plan')
        need(c['subsection_id'] not in covered,'Multiple images for one planned target')
        candidate_ready(c,s);covered.add(c['subsection_id'])
    for e in p['entries']:
        if e['required'] and e['subsection_id'] not in covered:
            ack=e.get('failure_acknowledgement') or {}
            need(e.get('generation_failed') is True and ack.get('reviewer') and ack.get('recorded_at') and ack.get('evidence_locator'),'Required visual missing without explicit author acknowledgement')
    r=s.get('visual_review') or {};need(r.get('id') and r.get('revision'),'Missing current visual review')
    need(r.get('canonical_revision')==s['canonical']['revision'] and r.get('evidence_revision')==s['evidence']['revision'],'Stale visual review')
    need(isinstance(r.get('candidate_ids'),list) and len(r['candidate_ids'])==len(ids) and set(r['candidate_ids'])==set(ids),'Review candidate set mismatch')
    need(r.get('asset_hashes')=={c['id']:c['asset_sha256'] for c in cs},'Review exact assets mismatch')
    ev=r.get('evaluation') or {};_receipt(ev,r['id'],r['revision'],.95)
    if decisions:
        d=s.get('visual_decisions') or {};need(d.get('review_id')==r['id'] and d.get('review_revision')==r['revision'],'Missing/stale human visual decisions')
        need(d.get('reviewer') and d.get('recorded_at') and d.get('evidence_locator'),'Human decision provenance missing')
        vals=d.get('values') or {};need(set(vals)==set(ids) and all(v in {'KEEP','EXCLUDE'} for v in vals.values()),'Incomplete or PENDING human decisions')
    return r

def final_ready(s):
    r=visual_ready(s);a=s['canonical'];b=s.get('final') or {}
    need(b.get('id') and b.get('revision') and b['id']!=a['id'],'Distinct final artifact required')
    need(b.get('canonical_id')==a['id'] and b.get('canonical_revision')==a['revision'],'Final canonical binding stale')
    need(b.get('visual_review_id')==r['id'] and b.get('visual_review_revision')==r['revision'],'Final review binding stale')
    need(b.get('placement_report_id') and b.get('prose_preserved') is True and b.get('formatting_preserved') is True,'Placement preservation proof missing')
    placements=b.get('placements') or {};need(set(placements)==set(r['candidate_ids']),'Placement accounting incomplete')
    for cid,decision in s['visual_decisions']['values'].items():
        q=placements[cid]
        if decision=='KEEP':need(q.get('status')=='INSERTED' and q.get('asset_sha256')==r['asset_hashes'][cid],'KEEP asset not inserted exactly')
        else:need(q.get('status')=='EXCLUDED','EXCLUDE was inserted')
    _receipt(b.get('evaluation') or {},b['id'],b['revision'],.90)
    return b

def next_action(s):
    try:
        need(s.get('run_id') and s.get('chapter_topic') and s.get('workspace_account') and s.get('destination_folder_id'),'Run setup incomplete')
        for name in ('outline','evidence'):need(s.get(name,{}).get('id') and s[name].get('revision'),'Approved input missing: '+name)
        if s.get('paused_limit'):return 'RECONCILE_LIMIT_ONLY'
        if s.get('in_flight_operation'):return 'RECONCILE_OPERATION'
        if s.get('revision_requested'):
            need(s['revision_requested'].get('evidence_locator'),'Revision request lacks explicit evidence')
            attempts=s.get('diagnose_attempts',0)
            need(type(attempts) is int and 0<=attempts<3,'Diagnosis limit exhausted or invalid')
            scope=s['revision_requested']['scope']
            if scope=='visual':canonical_ready(s)
            if scope=='placement':visual_ready(s)
            return {'writing':'REVISE_CANONICAL','visual':'REVISE_VISUALS','placement':'REVISE_PLACEMENT'}[scope]
        a=s.get('canonical')
        if not a:return 'WRITE_CANONICAL'
        need(a.get('outline_revision')==s['outline']['revision'] and a.get('evidence_revision')==s['evidence']['revision'],'Canonical inputs stale; explicit revision required')
        p=a.get('native_presentation') or {}
        if p.get('passed') is not True:return 'VERIFY_OR_REPAIR_CANONICAL_PRESENTATION'
        e=a.get('evaluation') or {}
        if not e or e.get('artifact_revision')!=a.get('revision'):return 'EVALUATE_CANONICAL'
        if e.get('passed') is not True or not score_ok(e.get('score'),.85):
            need(s.get('diagnose_attempts',0)<3,'Diagnosis limit exhausted');return 'REVISE_CANONICAL'
        canonical_ready(s)
        if not s.get('generation_plan'):return 'PLAN_VISUALS_FROM_CANONICAL'
        plan_ready(s)
        if not s.get('visual_review'):return 'GENERATE_AND_EVALUATE_VISUALS'
        visual_ready(s,False)
        if not s.get('visual_decisions'):return 'WAIT_HUMAN_VISUAL_REVIEW'
        visual_ready(s)
        b=s.get('final')
        if not b:return 'PLACE_APPROVED_VISUALS'
        if not b.get('evaluation'):return 'EVALUATE_FINAL'
        if b['evaluation'].get('passed') is not True or not score_ok(b['evaluation'].get('score'),.90):
            need(s.get('diagnose_attempts',0)<3,'Diagnosis limit exhausted')
            return 'REVISE_CANONICAL' if b['evaluation'].get('revision_scope')=='writing' else 'REVISE_PLACEMENT'
        b=final_ready(s);d=s.get('final_approval')
        if not d:return 'WAIT_HUMAN_FINAL_APPROVAL'
        need(d.get('artifact_id')==b['id'] and d.get('artifact_revision')==b['revision'] and d.get('reviewer') and d.get('recorded_at') and d.get('evidence_locator'),'Final approval stale or unverified')
        return 'COMPLETE'
    except (Blocked,KeyError,TypeError,ValueError) as e:return 'BLOCKED: '+str(e)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('snapshot');args=ap.parse_args();print(next_action(json.load(open(args.snapshot))))
