"""Validate a pinned standalone package without accessing another account's files."""
from pathlib import Path
import hashlib,json,re,sys

ROOT=Path(__file__).resolve().parents[1]
def validate(root=ROOT):
    root=Path(root)
    integrity_path=root/'references/integrity.json'
    lock=json.loads(integrity_path.read_text())
    actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p!=integrity_path}
    if actual!=set(lock['files']):raise ValueError('Release file inventory differs from lock')
    for rel,expected in lock['files'].items():
        p=root/rel
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=expected:raise ValueError('Missing/changed locked file: '+rel)
    provenance=lock
    for f in provenance['visual_dependency_files']:
        data=(root/f['path']).read_bytes();sha=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        if sha!=f['source_blob_sha']:raise ValueError('Pinned visual dependency changed: '+f['path'])
    manifest=json.loads((root/'workers/chapter-writing/references/skill-sources.json').read_text())
    for d in manifest['dependencies']:
        p=root/'workers/chapter-writing'/d['path']
        if hashlib.sha256(p.read_bytes()).hexdigest()!=d['sha256']:raise ValueError('Pinned writing dependency changed: '+d['name'])
    gen=json.loads((root/'workers/visual-generation/references/skill-sources.json').read_text())
    for name,d in gen['dependencies'].items():
        p=root/d['skill_path'];data=p.read_bytes()
        if hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()!=d['skill_blob_sha']:raise ValueError('Pinned skill mismatch: '+name)
        for ref,sha in d.get('required_references',{}).items():
            q=root/d['root']/'references'/ref;b=q.read_bytes()
            if hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()!=sha:raise ValueError('Pinned reference mismatch: '+ref)
    for p in root.rglob('*.md'):
        for ref in re.findall(r'\]\(([^)]+)\)',p.read_text()):
            if '://' in ref or ref.startswith(('#','mailto:')):continue
            q=ref.split('#')[0]
            if q and not (p.parent/q).exists():raise ValueError('Broken relative reference: '+str(p.relative_to(root))+' -> '+ref)
    pipeline=json.loads((root/'pipeline.json').read_text())
    expected=['chapter_writing','canonical_clean_evaluate','visual_generation','human_visual_review','visual_placement','final_clean_evaluate','human_final_approval']
    if pipeline['stages']!=expected or pipeline['image_extraction'] or pipeline['requires_visual_review_before_writing'] or not pipeline['requires_visual_review_before_placement'] or pipeline['visual_placement_rewrites_prose']:raise ValueError('Standalone ordering/scope drift')
    if pipeline['thresholds']!={'canonical':.85,'generated_visual':.90,'visual_review':.95,'final':.90}:raise ValueError('Quality thresholds changed')
    required=['SKILL.md','references/workflow.md','references/runtime.md','references/state-schema.md','references/revisions.md']
    for rel in required:
        if not (root/rel).is_file():raise ValueError('Missing required reference: '+rel)
    return {'valid':True,'locked_files':len(lock['files']),'pinned_visual_files':len(provenance['visual_dependency_files']),'pinned_writing_skills':len(manifest['dependencies']),'order':expected}

if __name__=='__main__':
    try:print(json.dumps(validate(),indent=2))
    except (ValueError,OSError,KeyError) as e:print('INVALID: '+str(e),file=sys.stderr);sys.exit(1)
