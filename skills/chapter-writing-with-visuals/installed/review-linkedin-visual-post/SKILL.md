---
name: review-linkedin-visual-post
description: Strictly audit a LinkedIn single-image post before delivery or when the user asks to review, critique, check, approve, or diagnose a visual. Verify that the intended LinkedIn visual pipeline was followed; the approved portrait and exact signature are present; the design is one coherent, concept-specific composition rather than separate pieces assembled together; the content explains the intuition accurately; and the 1080 × 1350 post remains readable on a phone. Return PASS, REVISE, or REBUILD with evidence and required fixes. Review only; do not edit unless explicitly asked.
---

## Article-section visual mode

When reviewing images embedded in an article, apply this mode before standalone-post defaults. Require the central realisation to be clear from the visual relationship and concise annotations together; reject paragraphs duplicated from the article or scenery that merely decorates them. Use the approved Product:Engineer and leverage examples bundled with the renderer to calibrate density. Do not enforce standalone-post word counts, text-area percentages, portrait canvas or identity when article mode overrides them. Allow connected comparison regions, callouts and conclusion bands that explain one argument; cropping one region alone is not sufficient evidence of assembly. Distinguish humans from agents. Inspect full size and a 390 px-wide preview. Validate the requested canvas and whole-image provenance using scripts/validate_article_visual.py for identity_mode=none. Retain the existing portrait validator for images with author identity. Record the user override and all per-image review findings.

# Review LinkedIn Visual Post

Apply a release gate, not a polite critique. Judge the final image before reading the renderer's rationale or production trace so valid provenance cannot bias the composition verdict.

Read [references/anshul-review-standard.md](references/anshul-review-standard.md) before every review.

## Required inputs

Inspect:

- final image and 390 px-wide mobile preview
- approved on-image copy and source material
- Visual Story Brief or equivalent concept plan
- design-system choice
- portrait-ready base and recorded slot geometry
- generation or rendering trace showing which stages ran
- portrait-placement verification JSON

For pre-delivery review, all evidence is mandatory. For an old or external image, mark unobservable pipeline items `NOT VERIFIABLE` and continue.

## Review sequence

### Phase 1: Blind artifact review

View only the final image at full size and 390 px-wide feed scale. Do not inspect the brief, composition sentence, trace, validator, or renderer comments yet.

#### Unified composition

Write one sentence: `One [mechanism or scene] carries [the claim], [the progression or relationship], and [the conclusion].`

Then inventory the independently framed regions. Treat the result as assembled and return `REBUILD` when:

- the sentence requires more than one mechanism or a list of modules
- the image decomposes into a headline block, explanation panel, cards, illustration, takeaway box, and signature row
- the central diagram or hero can be removed while the remaining layout still works
- a major region can be cropped or replaced without breaking the visual argument
- stages in one loop or sequence are rendered as detached cards around a decorative centre
- a generic template remains plausible after replacing the topic

Do not award unity because the image contains one central diagram, uses one style, or was exported once. Distinct regions pass only when the source relationship requires them and one governing mechanism visibly binds them.

#### Content and visual hierarchy

Without the caption or source, confirm that a reasonable reader can state what the idea is, how or why it works, and why it matters. Reject named-but-unexplained concepts, missing relationships, decorative graphics, fragmented reasoning, silent copy changes, or a hook without a completed argument.

Text-led posts should normally use 70–120 meaningful words and reserve roughly 55–70% of usable space for text. Diagram-led posts should normally use 45–100 words and let spatial structure create understanding. These are fit guides, not quotas.

#### Portrait, signature, and mobile

Require the approved photograph, exact name `Anshul Jain`, and exact tag `AI & Gen AI Product Mgmt`. The portrait should normally be 85–95 px in outer diameter on a 1080 px canvas and remain subordinate.

Reject a generated or distorted face, mismatched identity treatment, dedicated signature strip, dead space created for the author block, content forced against the lower border, illegible text, clipping, weak contrast, or unsafe margins.

Require 1080 × 1350 unless another format was requested. On that canvas, require at least 30 px explanatory body text, 28 px necessary labels, 34 px conclusion text, and 48 px bottom clearance. Signature metadata may be smaller.

### Phase 2: Fidelity review

Now inspect the source, approved copy, and Visual Story Brief. Confirm factual fidelity, exact required wording, the declared communication mode, and whether the final image embodies the semantic spine and binding map. A polished but source-inaccurate mechanism fails.

### Phase 3: Production integrity

Inspect the base, final, slot geometry, trace, and portrait verification. Run `scripts/validate_post_pipeline.py` and require `PASS`.

Confirm that:

- the base already contains all meaning-bearing elements and the complete signature treatment
- the trace uses only `integrated-image-generation`
- `complete_poster_generated_together` is true, `separate_component_assets` is false, and `semantic_edits_after_generation` is false
- the trace contains the exact whole-post generation prompt and records every discarded complete attempt
- no native-layout, compositing, overlay, inpainting, or targeted semantic-edit step created or repaired the accepted base
- only validation, format-preserving export, preview, review, and portrait placement occurred after the accepted generation
- the final differs from the base only inside the portrait circle

This gate proves production integrity, not visual unity. A validator `PASS` cannot overturn a Phase 1 failure.

## Verdict

Use exactly one:

- `PASS` — every observable gate passes; no material fix remains.
- `REVISE` — the semantic field is sound and only local corrections remain.
- `REBUILD` — the composition is assembled, the mechanism is wrong, the reasoning is incomplete, or semantic overlays invalidated the base. Start from a new composition sentence when architecture failed; rerender the approved architecture when only production method failed.

Missing evidence or any failed phase prevents `PASS`. Assembled composition always requires `REBUILD`, never spacing or typography patches.

## Output format

Lead with the verdict and one-sentence diagnosis. Then provide:

| Gate | Result | Evidence |
| --- | --- | --- |
| Unified composition | PASS / FAIL | The dominant mechanism or the assembled-pieces failure |
| Content and fidelity | PASS / FAIL | What a reader understands and whether it matches the source |
| Portrait and signature | PASS / FAIL | Accuracy, integration, scale, and exact text |
| Mobile and technical | PASS / FAIL | Dimensions, readability, margins, clipping |
| Production integrity | PASS / FAIL / NOT VERIFIABLE | Base, trace, portrait delta, and validator result |

Finish with no more than five required changes. For `REBUILD`, give one replacement composition sentence and its semantic field; do not prescribe cosmetic patches to the rejected layout.
