# Standalone release verification — 15 October 2026

The approved order is implemented: Chapter Writing and its canonical evaluation precede Visual Generation; human image approval precedes Visual Placement; final evaluation precedes final approval.

Completed checks:

- Skill frontmatter/name validation passed.
- Bundle verification checks complete file inventory/release hashes, 46 exact pinned visual-package files, three exact bundled writing skill snapshots, required reference links and pipeline order/thresholds.
- All 77 workflow and native-presentation regression tests passed. The 13 original presentation cases were retained and adapted from pytest to standard-library unittest without changing the validator's acceptance logic.
- Workflow cases cover writing-first operation, no pre-writing image gate, independent/native evidence, stale revisions/reports, candidate/hash provenance, dual image-review gates, DATA_LOCK, two-render limit, missing/partial decisions, required-target failures, exact approved placement, separate A/B, final approval and isolated actual model settings.
- An independent fresh GPT-6 Sol low context read the standalone skill and evaluated five synthetic resume requests. It identified initial writing, post-A visual planning, pending human image review, approved placement, and stale-review blocking. It found no routing/dependency contradiction. Synthetic input deficiencies were recorded; the run schema now explicitly requires a chapter topic and records default-audience behavior.
- All visual Adapt/Render/Review files, including their original reference images and scripts, are byte-identical to pinned registry commit `30a5d06b12cf6baf29c7ff0977595018179529c7`.
- The source production branch and existing installed writing workflow were not modified by this standalone implementation.

This is package and synthetic workflow verification, not an end-to-end live chapter/image-generation run. No chapter was generated, no image was rendered, no existing Drive artifact was changed, and no new scheduler was enabled for these checks. Literary quality, actual image quality and all connected-account capabilities must still be checked on the first explicitly authorized live run. Identical stochastic wording/pixels cannot be guaranteed.

Commands:

```bash
python skills/chapter-writing-with-visuals/scripts/validate_bundle.py
python -m unittest discover -s tests -v
```
