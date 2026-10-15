# Chapter Writing with Visuals

A standalone, subscription-runtime chapter workflow extracted from `anshulprojectmgmt/Writing-agent` production commit `03c4a06b46d137aa7fa70304b9b177c28fa83616`.

**Order:** Chapter Writing → native formatting verification → independent A evaluation → Visual Generation → human KEEP/EXCLUDE → Visual Placement → independent B evaluation → final human approval.

No upstream research workers, source-image extraction, source-image search or second LinkedIn-style rewrite are included. Supply an existing approved outline/Research Mapping and approved evidence package. The existing writing method and pinned visual packages are preserved; only standalone routing/input dependencies are adapted.

## What it produces

- **Artifact A:** the completed story-developed, written, formatted and humanised chapter, plus separate workflow appendices in that canonical Doc.
- **Visual package:** a generation plan based on completed A, actual generated images, image-review/evidence reports, a manifest and human image review.
- **Artifact B:** a separate clean reader-facing chapter preserving A wording and formatting with exact approved images inserted. Appendices and review metadata are not included in B.

Original artifacts remain immutable. Generated images explain evidence; they are not research evidence themselves.

## Start in ChatGPT Work or Codex

Connect your own Google Workspace account and provide an authorized destination. Ensure the host supports actual fresh subagents, GPT-6 Sol with the specified reasoning controls, local script execution, native image generation and Google Docs/Sheets tools. If a required capability is missing, the workflow blocks rather than pretending it ran.

Install the **complete** `skills/chapter-writing-with-visuals/` directory through your host's supported skill installation mechanism. Keep its workers, installed packages, scripts, references and image assets together. Copying only SKILL.md is insufficient. In a coding workspace, open this repository and read `WORK_START.md`; `AGENTS.md` routes the agent to the same package.

Paste this prompt after setup:

> Use the standalone chapter-writing-with-visuals workflow in this repository. Read WORK_START.md and the complete active skill references. Use my connected Google Workspace and the destination I supply. Start from my approved outline and evidence package. Write, format, humanise and evaluate Artifact A first; then generate visuals from that completed chapter using the bundled pinned packages. Stop for my KEEP/EXCLUDE decisions, then place the exact approved images in Artifact B and evaluate it. Preserve separate role contexts, all quality gates and durable recovery state. Do not run research or image extraction.

Then supply title, audience, exact approved outline/evidence links and your destination. A fresh account never uses the original account's folder, sheet or reviewer configuration. The included presentation profile carries historical baseline provenance but does not require access to the original private sample chapter.

## Models and isolation

| Role | Model | Reasoning |
|---|---|---|
| Chapter Writing / targeted writing revision | GPT-6 Sol | medium |
| Controller, visual roles, reviewers, evaluators and placement | GPT-6 Sol | low |

Every role/candidate step uses a genuinely fresh context (`fork_turns: none`). Native image generation runs inside Render. These instructions do not change a model by naming it: the host must set and record actual dispatch controls.

## Preserved quality contracts

The writing worker loads storytelling-article, anshul-writing-style, internal ai-humanizer-core, anshul-voice, writing-style, output-formatting and the approved presentation contract/profile. Selective meaningful bold openings, functional icons, explanatory bullets, concise italic evidence attribution and accessible language remain part of writing—not a later styling node.

Visual Generation loads the complete pinned Adapt, Render and Review packages, including all bundled article/design/reference assets. The existing DATA/TOPIC/HUMOUR selector, DATA_LOCK, installed article review, generated evidence evaluation and two-complete-attempt limit are retained. The extraction-based fallback test is replaced by a plan grounded in the finished chapter; this is the intentional routing change.

Thresholds: canonical chapter 0.85; generated-image evidence 0.90; visual-review package 0.95; final chapter 0.90. Hard gates override scores. Clean evaluators write separate reports only. Revisions are targeted and occur only after failed evaluation or explicit feedback, maximum three diagnosis attempts per cycle.

## Validate the package

Python 3.10+ is needed for guards and checks. The host may also need its existing document/rendering tools; pinned visual image validators use Pillow. No inference service or API key is installed by these commands.

```bash
python skills/chapter-writing-with-visuals/scripts/validate_bundle.py
python -m unittest discover -s tests -v
```

The bundle validator checks release file hashes, copied dependency Git blob hashes, registry skill hashes, reference paths and routing. Workflow tests verify ordering, stale receipts, approval gates, exact assets and retry limits. These tests do not prove literary quality or constitute a live chapter/image-generation run. See `VALIDATION.md` for the recorded release checks and remaining live-test boundary.

## Portability and recovery

Logs and Resume Record contain artifact IDs/revisions, operation IDs, input bindings, role dispatch settings, review decisions and checkpoints. Browser/chat history is not the durable state. Quota limits pause the run; no reset time is invented. Installation does not create a scheduler. A recovery task is configured only on an explicit request and only through supported host capabilities.

The package is a pinned release. Other accounts need the full package and their own connections; updating the original production repository does not silently replace this version. Preserve hashes and run the checks after any update. Identical instructions preserve methods and acceptance rules, not identical stochastic wording or image pixels.

## Source provenance

`SOURCE_PROVENANCE.json` records the production commit, registry pin and copied source paths. `ADAPTATIONS.json` identifies the intentionally changed worker files. `PACKAGE_LOCK.json` records the exact standalone release bytes. No private runtime documents, credentials or generated chapter assets are included.
