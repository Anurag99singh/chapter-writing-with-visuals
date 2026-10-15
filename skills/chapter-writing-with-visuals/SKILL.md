---
name: chapter-writing-with-visuals
description: Write a complete formatted Anshul-style chapter from an approved outline and evidence, then generate explanatory visuals, pause for human KEEP/EXCLUDE, and place the exact approved images in a separate final chapter. Use for standalone chapter creation, approval, feedback and recovery without running research or image extraction.
---

# Chapter Writing with Visuals

Execute this order only:
`Chapter Writing A -> native verification -> clean evaluation A -> Visual Generation -> human image approval -> Visual Placement B -> clean evaluation B -> final human approval`.

Read [references/workflow.md](references/workflow.md), [references/runtime.md](references/runtime.md), [references/state-schema.md](references/state-schema.md) and `pipeline.json` before startup/resume. Run `python scripts/validate_bundle.py` from this skill directory. A missing or changed pinned dependency blocks dispatch. There is no image extraction, image search, upstream research node or pre-writing visual gate.

## Input and setup

Resolve the user's own connected Google Workspace account and destination. Never reuse the source project's personal folder, control sheet, reviewer or runtime file IDs. Accept an approved ordered outline/Research Mapping (`chapter_blueprint_doc_id`) and approved research/evidence package (`deep_research_doc_id`), title, audience and author instructions. Existing input documents fulfil those roles; do not run research or create invented evidence. Missing inputs require an explicit user decision before writing.

Create/reuse one unambiguous run folder, chapter Logs workbook and Resume Record in that destination. Each run contains Chapter Writing, Visual Generation, Visual Assets/Generated, Evaluations and Final folders. Keep all prior published versions immutable. Installation is not an active run or enabled scheduler.

## Role execution

Use a fresh actual host context for every worker/evaluator/revision role and every candidate's Adapt, Render, installed Review and evidence evaluator: `fork_turns="none"`. Chapter Writing uses GPT-6 Sol medium; all supporting roles/controllers use GPT-6 Sol low (the approved available controller fallback). Never emulate isolation with role labels in one chat, use Astra/Luna/GPT-5.x or replace native image generation. If host capabilities/settings are unavailable, block and state the limitation.

Pass exact input IDs, runtime values and instruction paths only. Roles read their own full source documents; the controller carries metadata, not chapter prose. Load the matching worker and required references immediately before execution:

| Action | Package |
|---|---|
| Write or revise A | `workers/chapter-writing/SKILL.md`, `instruction.md` and every dependency listed there |
| Evaluate A or B | `workers/clean-evaluate/SKILL.md`, `instruction.md`, matching rubric and full writing/presentation references |
| Plan/generate/review images or apply decisions | `workers/visual-generation/SKILL.md`, `instruction.md`, references and full pinned `installed/` packages |
| Place images or repair placement | `workers/visual-placement/SKILL.md`, `instruction.md`, `references/placement-contract.md` |

Load `references/revisions.md` for failed evaluation or human feedback. Do not regenerate passing content without an explicit change request. A formatting repair belongs inside the writing worker, never a separate formatting node.

## Gates and state

Use `scripts/workflow_guard.py` with the durable snapshot before every transition. Validate actual dispatch settings, canonical receipts, candidate review receipts, exact human decisions and revision bindings. Record BEFORE and AFTER receipts with stable operation IDs, task IDs, model/reasoning/fork settings, inputs, output IDs, result and attempt. Record unknown token/credit usage as unavailable, never invented.

A must pass native formatting and independent evaluation before generation. Generation reads the completed A reader text PLUS approved evidence. Generated images are explanatory artifacts, never evidence. Each candidate uses full Adapt -> native Render -> installed article Review -> generated evidence evaluation, at most two complete render attempts across both gates. A fresh human review begins PENDING. Failed required targets require explicit author acknowledgement before omission.

No PENDING candidate may enter placement. B must use the exact KEEP assets, preserve A reader prose/native formatting and strip only named workflow appendices. Placement may not rewrite, regenerate, extract or substitute. Independently evaluate B before final human approval.

Changed outline/evidence invalidates A and everything downstream; changed A invalidates its evaluation and all visual/final bindings; changed image/review invalidates human decisions and B. Do not silently transfer approval to another revision.

On ambiguous operations reconcile existing artifacts before retrying. Pause at usage limits and persist the exact pending step/candidate/attempt; do not infer quota reset times or bypass limits. A scheduler is optional and is created only when explicitly requested and supported; instructions alone do not enable it.

## Output

Return concise status, exact verified Doc/report/asset links and the pending human action. Keep Artifact A, Artifact B, evaluation reports, generation plan/manifest/review and placement report separate. Do not claim that a structurally validated package has already produced an end-to-end live chapter.
