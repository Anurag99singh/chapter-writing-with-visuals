#!/usr/bin/env python3
"""Check observable provenance for complete article images without identity."""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageChops


def validate(trace_path):
    trace = json.loads(Path(trace_path).read_text())
    errors = []
    base = Image.open(trace['base']).convert('RGB')
    final = Image.open(trace['final']).convert('RGB')
    expected = (trace['canvas']['width'], trace['canvas']['height'])
    if base.size != expected or final.size != expected:
        errors.append('Canvas differs from the requested dimensions')
    elif ImageChops.difference(base, final).getbbox() is not None:
        errors.append('No-identity final differs from the complete generated base')
    if Image.open(trace['mobile_preview']).width != 390:
        errors.append('Mobile preview must be 390 pixels wide')
    for field, value in {
        'mode': 'article-section', 'identity_mode': 'none',
        'render_method': 'integrated-image-generation',
        'complete_poster_generated_together': True,
        'separate_component_assets': False,
        'semantic_edits_after_generation': False,
    }.items():
        if trace.get(field) != value:
            errors.append('Invalid provenance field: ' + field)
    for field in ['generation_prompt', 'exact_copy', 'composition_sentence']:
        if not isinstance(trace.get(field), str) or len(trace[field].strip()) < 20:
            errors.append('Missing or incomplete ' + field)
    allowed = {'validate-dimensions', 'mobile-preview', 'review', 'format-preserving-export'}
    if not isinstance(trace.get('operations_after_base'), list):
        errors.append('Missing operations_after_base')
    elif set(trace['operations_after_base']) - allowed:
        errors.append('Unsupported operations after generation')
    return {'verdict': 'PASS' if not errors else 'FAIL', 'errors': errors}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--trace', type=Path, required=True)
    result = validate(parser.parse_args().trace)
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['verdict'] == 'PASS' else 1)
