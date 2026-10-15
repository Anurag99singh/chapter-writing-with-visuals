---
name: visual-generation-v3
description: "Generate explanatory article visuals after passing Chapter Writing. Use the completed canonical chapter and approved evidence; execute the pinned Adapt, Render and Review packages in isolated contexts, apply the evidence gate and leave KEEP/EXCLUDE to the human. No extraction."
---

# VISUAL GENERATION V3

## Role

Run AFTER the canonical chapter has been written, formatted, humanised, natively verified and independently passed clean evaluation. Read that exact Artifact A and its approved evidence. Never generate from a hypothetical or unfinished draft.

Do not perform new research, image search or extraction, and do not rewrite chapter prose. Produce generated explanatory candidates only. Human KEEP/EXCLUDE remains mandatory. Generated images are not evidence sources.

## Required inputs

- `canonical_chapter_doc_id` and current `canonical_revision_id` — passing completed Artifact A.
- `canonical_evaluation_report_id` — passing independent report bound to A.
- `deep_research_doc_id` — approved supporting evidence package, supplied externally.
- `chapter_blueprint_doc_id` — approved outline/Research Mapping, supplied externally.
- `generation_folder_id` — destination for generation plans, manifests and reviews.
- `visual_assets_folder_id` — generated image destination.
- `version` — current generation version.

Resolve all roots relative to the standalone skill root, including `installed/` in the dependency manifest.

Optional decision-application mode:
- `visual_review_doc_id` — current Unified Visual Review.
- `visual_decisions` — exact human KEEP/EXCLUDE decisions keyed by VIS/GEN ID.

If required inputs are missing, stale, unreadable, or not bound to the passing Artifact A and current approved evidence, stop. Never infer IDs.

## Isolated execution boundary

This skill is the post-writing Visual Generation role. Its internal skill executions remain context-isolated:

1. Selector execution — fresh context.
2. For every generated candidate separately:
   - Adapt execution — fresh context for that subsection only.
   - Render execution — fresh context for that candidate only.
   - Installed Render Review execution — fresh context for that candidate only.
   - Generated Visual Evaluate — fresh context for that candidate only.
3. Unified Review build/verification — fresh context.

Never reuse one candidate's Adapt/Render/review/evaluation conversation for another candidate. Never expose a renderer to another subsection's brief, image, or prior render conversation.

If fresh isolated execution is unavailable in production, stop rather than emulating isolation inside one accumulated conversation.

## Mode A — generation + unified review

### Step 1 — plan from the completed chapter

Read the completed Artifact A reader prose, approved ordered subsection mapping and evidence package. Bind the plan to all exact document IDs/revisions. For every subsection record its exact A location, purpose, evidence basis and `GENERATION_REQUIRED: YES | NO` with a reason.

Choose YES only when a single visual adds understanding through data, mechanism/comparison or a faithful explanatory metaphor. Choose NO for prose that needs no visual or lacks enough supported content. Do not force an image per paragraph or subsection. Do not fabricate a source-review artifact or pretend extraction was attempted. No source-visual states or VIS candidates exist in this workflow.

### Step 2 — select generation mode

Apply `references/generation-mode-selector.md` exactly to every generation target.

Allowed modes:
- `DATA_EXPLAINER`
- `TOPIC_EXPLAINER`
- `HUMOUR_METAPHOR`

Create one native Google Doc named like:
`<Chapter> — Visual Generation Plan <version>`

For every subsection record:
- canonical chapter subsection/paragraph locator;
- GENERATION_REQUIRED YES/NO;
- DATA/TOPIC/HUMOUR scores;
- selected mode when required;
- one-sentence reason.

Do not generate an image for a subsection marked NO.

### Step 3 — Adapt

For each generation target independently, execute the full pinned installed package identified in `references/skill-sources.json`:
`adapt-linkedin-visual-content`.

Do not paraphrase the skill into a homemade prompt. Load its installed `SKILL.md` and all required installed references, including its article-section behavior and Visual Story Brief contract.

The Adapt context receives only that subsection's bounded packet:
- subsection title/purpose;
- completed canonical subsection text and its approved evidence;
- approved outline/evidence source references needed to preserve factual meaning;
- exact statistics and caveats relevant to the visual;
- selected generation mode.

It must not receive another subsection's evidence or another GEN brief.

The resulting Visual Story Brief must preserve the approved meaning and contain the skill-required fields, including semantic spine, communication mode, visual embodiment, binding map, reading path, mandatory content, prohibited decomposition, core insight, reader shift, and copy/mechanism constraints.

For DATA_EXPLAINER also apply `references/data-lock-contract.md`.

### Step 4 — Render + installed Render Review

For each candidate independently, execute the full pinned installed package identified in `references/skill-sources.json`:
`render-linkedin-visual-post`.

Hard requirements:
- use ChatGPT native image generation only;
- run installed Article-section visual mode;
- load the installed article visual rules, design systems, gold-standard quality bar, and installed reference assets automatically;
- the human must never have to supply style references manually;
- generate exactly ONE standalone image for the current subsection;
- never batch candidates;
- never create a collage or multi-section page;
- use one semantic field / one main explanatory mechanism;
- keep article nuance in the article, not dense raster text;
- no signature/author identity block unless the installed article mode explicitly requires one (book mode defaults to none).

Before the render is eligible for the Writing Agent evidence gate, run the full pinned installed `review-linkedin-visual-post` dependency required by the Render skill, using its article-section validator/review behavior. This is the Render skill's own visual-quality acceptance step and remains an internal Visual Generation step, not another research node.

A Render candidate that does not pass the installed article review is discarded and counts as a render attempt. Do not patch it with overlays or semantic edits; regenerate a complete candidate as the installed Render skill requires.

Persist an accepted generated asset under `Visual Assets/Generated` with a stable GEN ID (`GEN-001`, `GEN-002`, ...). Never overwrite an earlier attempt; retries use attempt metadata/new asset receipt.

### Step 5 — Writing Agent Generated Visual Evaluate

Only after the installed Render article review passes, evaluate the actual rendered image — not only its prompt or brief — using `references/rubrics/generated_visual.yaml` in a fresh evaluator context.

This second gate is book/evidence-specific and complements, rather than replaces, the installed visual reviewer.

Required gates:
1. factual fidelity;
2. selected-mode fit;
3. explanatory value;
4. render accuracy;
5. visual quality.

DATA_EXPLAINER must match DATA_LOCK exactly.

Hard failure includes invented/changed numbers, unsupported claims, wrong relationships, humour that changes meaning, unreadable core copy, decorative-only output, or collage/multi-section output.

Allow at most two complete render attempts per GEN candidate across Render + installed review + generated evaluation. If attempt 2 still fails either acceptance layer, mark that candidate `GENERATION FAILED`; do not put it in the human candidate set and do not loop indefinitely.

### Step 6 — Generated Visual Manifest

Create one native Google Doc named like:
`<Chapter> — Generated Visual Manifest <version>`

For every target record:
- GEN ID;
- subsection;
- selected mode;
- evidence basis/Deep Research locator;
- Adapt brief locator;
- render asset ID/path;
- render attempt count;
- installed Render review verdict/locator;
- Writing Agent generated evaluator status/report locator;
- DATA_LOCK when applicable;
- final status PASS or GENERATION FAILED.

### Step 7 — Unified Visual Review

Build one new native Google Doc named `<Chapter> — Unified Visual Review <version>`. Use `references/unified-visual-review-format.md`. Cover every approved subsection in order. Include only GEN candidates passing BOTH acceptance gates. Record NO-target reasons or exhausted failures separately; never invent a candidate or omit a planned subsection.

Bind the review to current A, A revision and approved evidence. All candidates have `ORIGIN: GENERATED_EXPLAINER` and begin `HUMAN DECISION: PENDING`. Embed the actual exact rendered assets. Generated images explain the existing chapter; they do not become new evidence. A changed A or evidence revision invalidates this review.

### Step 8 — Unified Review Evaluate

Evaluate the Unified Visual Review using `references/rubrics/unified_visual_review_v3.yaml` in a fresh evaluator context.

The review must fail closed if candidate provenance is missing, a generated candidate did not pass both required acceptance gates, a stale canonical chapter/evidence revision is mixed in, IDs collide, an approved subsection is missing, or a candidate lacks a Human Decision field.

Only a passing Unified Visual Review may be returned to the parent node for human review.

## Mode B — apply visual decisions

When `visual_review_doc_id` and exact `visual_decisions` are supplied:
- verify `visual_review_doc_id` is the current Unified Visual Review;
- do not rerun Selector, Adapt, Render, extraction, or evaluation;
- accept only KEEP or EXCLUDE values;
- update only matching `HUMAN DECISION` fields for exact GEN IDs;
- never alter origin, source/evidence basis, asset ID, mode, or evaluator status;
- verify the current candidate set and decision set match exactly.

Return `visual_review_status: resolved` only when no candidate remains PENDING.

## Logging contract

The standalone controller owns durable logs, state and routing. Return enough metadata for it to log each internal execution separately while keeping `Subagent = Visual Generation`:
- Selector
- Adapt <GEN-ID>
- Render <GEN-ID> attempt N
- Review Render <GEN-ID> attempt N
- Evaluate <GEN-ID> attempt N
- Unified Review
- Evaluate Unified Review
- Apply Visual Decisions

Each logged step must include operation ID, input artifact IDs, output artifact/asset ID, result, and retry count where applicable.

## Hard prohibitions

- No new research source.
- No image search, extraction, source-visual review dependency or VIS candidate.
- No manually reimplemented/summarized version of the pinned Adapt/Render/Render-review skills.
- No external image generator such as Runway.
- No cross-candidate render context reuse.
- No generated visual presented as primary-source evidence.
- No human decision inference.
- No chapter placement; Visual Placement owns that later.
- No regeneration after a GEN asset has been human-KEEP for placement; placement must use the exact reviewed asset.

## Output

Generation success:
{
  "version":"<version>",
  "visual_review_doc_id":"<unified_visual_review_doc_id>",
  "visual_assets_folder_id":"<visual_assets_folder_id>",
  "visual_review_status":"pending",
  "generation_plan_doc_id":"<generation_plan_doc_id>",
  "generated_visual_manifest_doc_id":"<generated_visual_manifest_doc_id>",
  "comment":"Visual Generation complete: <G> passing GEN candidates; Unified Visual Review contains <G> generated candidates; human decisions pending"
}

Decision-application returns the same shape and sets status `resolved` only when every current VIS/GEN candidate is KEEP/EXCLUDE.

On failure, never fabricate IDs. Return the valid artifact IDs that exist plus a `Failed:` comment naming the exact blocked step.