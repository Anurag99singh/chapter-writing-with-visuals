import copy,importlib.util,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('guard',ROOT/'skills/chapter-writing-with-visuals/scripts/workflow_guard.py');g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)

def initial():return {'run_id':'synthetic-test','chapter_topic':'Synthetic chapter','workspace_account':'reviewer@example.invalid','destination_folder_id':'folder','outline':{'id':'outline','revision':'o1','subsection_ids':['1.1','2.1']},'evidence':{'id':'evidence','revision':'e1'}}
def canonical():
 s=initial();s['canonical']={'id':'A','revision':'a1','outline_revision':'o1','evidence_revision':'e1','native_presentation':{'passed':True,'report_id':'native-proof','artifact_id':'A','artifact_revision':'a1'},'evaluation':{'passed':True,'score':.85,'report_id':'eval-a','artifact_id':'A','artifact_revision':'a1','checks':{k:{'passed':True,'evidence':'synthetic fixture paragraph'}for k in g.CHECKS}}};return s
def planned():
 s=canonical();s['generation_plan']={'id':'plan','canonical_revision':'a1','evidence_revision':'e1','entries':[{'subsection_id':'1.1','required':True,'reason':'mechanism'},{'subsection_id':'2.1','required':False,'reason':'prose sufficient'}]};return s
def reviewed():
 s=planned();sha='a'*64;c={'id':'GEN-001','origin':'GENERATED_EXPLAINER','subsection_id':'1.1','canonical_revision':'a1','evidence_revision':'e1','mode':'TOPIC_EXPLAINER','attempt':1,'brief_id':'brief','asset_id':'asset','asset_sha256':sha,'installed_review':{'passed':True,'report_id':'installed-review','asset_sha256':sha},'evidence_review':{'passed':True,'score':.90,'report_id':'image-eval','asset_sha256':sha}};s['candidates']=[c];s['visual_review']={'id':'review','revision':'v1','canonical_revision':'a1','evidence_revision':'e1','candidate_ids':['GEN-001'],'asset_hashes':{'GEN-001':sha},'evaluation':{'passed':True,'score':.95,'report_id':'review-eval','artifact_id':'review','artifact_revision':'v1'}};return s
def decided():
 s=reviewed();s['visual_decisions']={'review_id':'review','review_revision':'v1','reviewer':'author','recorded_at':'2026-10-15T00:00:00Z','evidence_locator':'decision-record','values':{'GEN-001':'KEEP'}};return s
def final():
 s=decided();s['final']={'id':'B','revision':'b1','canonical_id':'A','canonical_revision':'a1','visual_review_id':'review','visual_review_revision':'v1','placement_report_id':'placement-report','prose_preserved':True,'formatting_preserved':True,'placements':{'GEN-001':{'status':'INSERTED','asset_sha256':'a'*64}},'evaluation':{'passed':True,'score':.90,'report_id':'eval-b','artifact_id':'B','artifact_revision':'b1'}};return s

class Flow(unittest.TestCase):
 def blocked(self,s):self.assertTrue(g.next_action(s).startswith('BLOCKED:'),g.next_action(s))
 def test_starts_with_writing_without_visuals(self):self.assertEqual(g.next_action(initial()),'WRITE_CANONICAL')
 def test_missing_evidence_blocks(self):s=initial();del s['evidence'];self.blocked(s)
 def test_limit_reconciles_only(self):s=initial();s['paused_limit']=True;self.assertEqual(g.next_action(s),'RECONCILE_LIMIT_ONLY')
 def test_inflight_reconciles_before_duplicate(self):s=initial();s['in_flight_operation']='op';self.assertEqual(g.next_action(s),'RECONCILE_OPERATION')
 def test_requires_native_presentation(self):s=canonical();s['canonical']['native_presentation']={};self.assertEqual(g.next_action(s),'VERIFY_OR_REPAIR_CANONICAL_PRESENTATION')
 def test_requires_independent_evaluation(self):s=canonical();del s['canonical']['evaluation'];self.assertEqual(g.next_action(s),'EVALUATE_CANONICAL')
 def test_passing_a_starts_visual_plan(self):self.assertEqual(g.next_action(canonical()),'PLAN_VISUALS_FROM_CANONICAL')
 def test_failed_a_revises_before_generation(self):s=canonical();s['canonical']['evaluation']['score']=.84;self.assertEqual(g.next_action(s),'REVISE_CANONICAL')
 def test_missing_execution_check_blocks(self):s=canonical();del s['canonical']['evaluation']['checks']['story_integrity'];self.blocked(s)
 def test_empty_execution_locator_blocks(self):s=canonical();s['canonical']['evaluation']['checks']['story_integrity']['evidence']='';self.blocked(s)
 def test_stale_native_revision_blocks(self):s=canonical();s['canonical']['native_presentation']['artifact_revision']='old';self.blocked(s)
 def test_stale_evidence_blocks(self):s=canonical();s['evidence']['revision']='e2';self.blocked(s)
 def test_stale_outline_blocks(self):s=canonical();s['outline']['revision']='o2';self.blocked(s)
 def test_plan_starts_generation_after_a(self):self.assertEqual(g.next_action(planned()),'GENERATE_AND_EVALUATE_VISUALS')
 def test_plan_order_mismatch_blocks(self):s=planned();s['generation_plan']['entries'].reverse();self.blocked(s)
 def test_missing_plan_subsection_blocks(self):s=planned();s['generation_plan']['entries'].pop();self.blocked(s)
 def test_stale_plan_blocks(self):s=planned();s['generation_plan']['canonical_revision']='old';self.blocked(s)
 def test_review_waits_for_human(self):self.assertEqual(g.next_action(reviewed()),'WAIT_HUMAN_VISUAL_REVIEW')
 def test_pending_cannot_place(self):s=decided();s['visual_decisions']['values']['GEN-001']='PENDING';self.blocked(s)
 def test_missing_decision_cannot_place(self):s=decided();s['visual_decisions']['values']={};self.blocked(s)
 def test_extra_decision_cannot_place(self):s=decided();s['visual_decisions']['values']['GEN-002']='KEEP';self.blocked(s)
 def test_stale_decision_cannot_place(self):s=decided();s['visual_decisions']['review_revision']='old';self.blocked(s)
 def test_unverified_decision_cannot_place(self):s=decided();del s['visual_decisions']['evidence_locator'];self.blocked(s)
 def test_resolved_review_starts_placement(self):self.assertEqual(g.next_action(decided()),'PLACE_APPROVED_VISUALS')
 def test_source_origin_rejected(self):s=reviewed();s['candidates'][0]['origin']='PRIMARY_SOURCE';self.blocked(s)
 def test_duplicate_candidates_rejected(self):s=reviewed();s['candidates']*=2;self.blocked(s)
 def test_unplanned_candidate_rejected(self):s=reviewed();s['candidates'][0]['subsection_id']='2.1';self.blocked(s)
 def test_attempt_three_rejected(self):s=reviewed();s['candidates'][0]['attempt']=3;self.blocked(s)
 def test_missing_installed_review_rejected(self):s=reviewed();s['candidates'][0]['installed_review']={};self.blocked(s)
 def test_failed_installed_review_rejected(self):s=reviewed();s['candidates'][0]['installed_review']['passed']=False;self.blocked(s)
 def test_low_image_evidence_score_rejected(self):s=reviewed();s['candidates'][0]['evidence_review']['score']=.89;self.blocked(s)
 def test_changed_render_hash_rejected(self):s=reviewed();s['candidates'][0]['asset_sha256']='b'*64;self.blocked(s)
 def test_missing_data_lock_rejected(self):s=reviewed();s['candidates'][0]['mode']='DATA_EXPLAINER';self.blocked(s)
 def test_verified_data_lock_accepted(self):s=reviewed();s['candidates'][0].update(mode='DATA_EXPLAINER',data_lock_passed=True,data_lock_locator='lock');self.assertEqual(g.next_action(s),'WAIT_HUMAN_VISUAL_REVIEW')
 def test_visual_review_low_score_rejected(self):s=reviewed();s['visual_review']['evaluation']['score']=.94;self.blocked(s)
 def test_failed_required_target_not_hidden(self):s=reviewed();s['candidates']=[];s['visual_review']['candidate_ids']=[];s['visual_review']['asset_hashes']={};self.blocked(s)
 def test_empty_plan_only_when_explicit_no(self):s=reviewed();s['generation_plan']['entries'][0]['required']=False;s['candidates']=[];s['visual_review']['candidate_ids']=[];s['visual_review']['asset_hashes']={};self.assertEqual(g.next_action(s),'WAIT_HUMAN_VISUAL_REVIEW')
 def test_failed_target_requires_explicit_omission_ack(self):s=reviewed();s['candidates']=[];s['visual_review']['candidate_ids']=[];s['visual_review']['asset_hashes']={};s['generation_plan']['entries'][0].update(generation_failed=True,failure_acknowledgement={'reviewer':'author','recorded_at':'time','evidence_locator':'exception'});self.assertEqual(g.next_action(s),'WAIT_HUMAN_VISUAL_REVIEW')
 def test_final_requires_its_evaluation(self):s=final();del s['final']['evaluation'];self.assertEqual(g.next_action(s),'EVALUATE_FINAL')
 def test_exact_keep_asset_verified(self):s=final();s['final']['placements']['GEN-001']['asset_sha256']='b'*64;self.blocked(s)
 def test_failed_placement_not_complete(self):s=final();s['final']['placements']['GEN-001']['status']='FAILED';self.blocked(s)
 def test_exclude_must_stay_absent(self):s=final();s['visual_decisions']['values']['GEN-001']='EXCLUDE';self.blocked(s)
 def test_separate_a_b(self):s=final();s['final']['id']='A';self.blocked(s)
 def test_prose_drift_blocks(self):s=final();s['final']['prose_preserved']=False;self.blocked(s)
 def test_formatting_drift_blocks(self):s=final();s['final']['formatting_preserved']=False;self.blocked(s)
 def test_stale_b_binding_blocks(self):s=final();s['final']['canonical_revision']='old';self.blocked(s)
 def test_final_waits_for_human(self):self.assertEqual(g.next_action(final()),'WAIT_HUMAN_FINAL_APPROVAL')
 def test_stale_final_approval_blocks(self):s=final();s['final_approval']={'artifact_id':'B','artifact_revision':'old','reviewer':'author','recorded_at':'time','evidence_locator':'decision'};self.blocked(s)
 def test_complete_requires_exact_approval(self):s=final();s['final_approval']={'artifact_id':'B','artifact_revision':'b1','reviewer':'author','recorded_at':'time','evidence_locator':'decision'};self.assertEqual(g.next_action(s),'COMPLETE')
 def test_passing_content_not_regenerated(self):self.assertEqual(g.next_action(final()),'WAIT_HUMAN_FINAL_APPROVAL')
 def test_explicit_feedback_revises(self):s=final();s['revision_requested']={'scope':'writing','evidence_locator':'human-comment'};self.assertEqual(g.next_action(s),'REVISE_CANONICAL')
 def test_revision_limit_blocks(self):s=final();s['revision_requested']={'scope':'writing','evidence_locator':'human-comment'};s['diagnose_attempts']=3;self.blocked(s)
 def test_dispatch_real_settings(self):self.assertTrue(g.dispatch('chapter_writing','gpt-6-sol','medium','none'))
 def test_no_context_fork(self):
  with self.assertRaises(g.Blocked):g.dispatch('chapter_writing','gpt-6-sol','medium','all')
 def test_no_luna(self):
  with self.assertRaises(g.Blocked):g.dispatch('render','gpt-6-luna','low','none')
 def test_no_wrong_reasoning(self):
  with self.assertRaises(g.Blocked):g.dispatch('visual_placement','gpt-6-sol','medium','none')
 def test_no_unknown_role(self):
  with self.assertRaises(g.Blocked):g.dispatch('source_extraction','gpt-6-sol','low','none')
 def test_missing_topic_blocks(self):s=initial();del s['chapter_topic'];self.blocked(s)
 def test_stale_visual_evaluation_blocks(self):s=reviewed();s['visual_review']['evaluation']['artifact_revision']='old';self.blocked(s)
 def test_wrong_visual_evaluation_id_blocks(self):s=reviewed();s['visual_review']['evaluation']['artifact_id']='other';self.blocked(s)
 def test_placement_revision_cannot_bypass_pending(self):s=reviewed();s['revision_requested']={'scope':'placement','evidence_locator':'comment'};self.blocked(s)
 def test_negative_retry_budget_rejected(self):s=final();s['revision_requested']={'scope':'writing','evidence_locator':'comment'};s['diagnose_attempts']=-1;self.blocked(s)
 def test_writing_feedback_in_final_routes_to_a(self):s=final();s['final']['evaluation'].update(passed=False,revision_scope='writing');self.assertEqual(g.next_action(s),'REVISE_CANONICAL')
 def test_nan_score_rejected(self):s=reviewed();s['candidates'][0]['evidence_review']['score']=float('nan');self.blocked(s)

if __name__=='__main__':unittest.main()
