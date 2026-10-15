# Chapter Writing with Visuals

Start with an approved outline and Deep Research document. Use your own connected Google Workspace and output destination.

**Flow:** Chapter Writing → independent evaluation → Visual Generation → your KEEP/EXCLUDE decisions → Visual Placement → final evaluation and approval.

## Start here

The complete installable package is [skills/chapter-writing-with-visuals](skills/chapter-writing-with-visuals/SKILL.md). Keep that whole folder together, including its references, scripts and visual assets. It works without files outside the package.

Paste this into a fresh ChatGPT Work or Codex chat that can access this repository:

> Read `skills/chapter-writing-with-visuals/SKILL.md` and all references it requires. Use this standalone workflow with my connected Google Workspace. I will provide my approved outline, Deep Research document and destination. Write, format, humanise and independently evaluate Artifact A first. Then generate and review visuals using the bundled skills. Stop for my KEEP/EXCLUDE decisions before placing the exact approved images in a separate Artifact B. Preserve context isolation, quality gates, logs and recovery state. Do not run research or image extraction.

The host needs fresh subagents, GPT-6 Sol with reasoning controls, native image generation, local Python, and Google Docs/Sheets access. Writing uses **Sol medium**; supporting roles use **Sol low**. Missing capabilities block the run.

## Where to look

| Folder | Purpose |
| --- | --- |
| [Chapter Writing](skills/chapter-writing-with-visuals/workers/chapter-writing/SKILL.md) | Storytelling, Anshul writing style, formatting and internal humanisation |
| [Visual Generation](skills/chapter-writing-with-visuals/workers/visual-generation/SKILL.md) | Visual selection, Adapt, Render and image reviews |
| [Visual Placement](skills/chapter-writing-with-visuals/workers/visual-placement/SKILL.md) | Exact approved images added to B; no prose rewrite |
| [Evaluation](skills/chapter-writing-with-visuals/workers/clean-evaluate/SKILL.md) | Independent chapter reports and rubrics |
| [Bundled visual skills](skills/chapter-writing-with-visuals/installed) | Original Adapt, Render and Review packages, including their reference assets |
| [Workflow references](skills/chapter-writing-with-visuals/references) | Order, runtime, recovery and the single integrity record |

`AGENTS.md` is the coding-agent entry point. Nested `agents/openai.yaml` files inside the original visual packages are UI metadata, not additional workflow agents. Those original packages remain intact.

## Check the package

Run from the repository root:

```bash
python skills/chapter-writing-with-visuals/scripts/validate_bundle.py
```

The check verifies every package file, pinned source hashes, reference links, stage order and thresholds. Source commits and file hashes live together in `references/integrity.json` inside the skill. Prior packaging history and development tests remain available in Git history.

This cleanup preserves the existing workflow and source snapshots; it does not update to a newer upstream version. Consistent instructions and checks preserve the method, not identical generated prose or image pixels.
