---
name: adapt-linkedin-visual-content
description: Convert source material—including screenshots, photos, slide sequences, videos, YouTube links, podcasts, audio, transcripts, articles, URLs, PDFs, notes, diagrams, and charts—into source-faithful LinkedIn single-image content or a coherent post series plus a rich visual-story handoff. Use when meaning must stay close to a source while avoiding copied phrasing, preserving mechanisms and relationships, auditing coverage across a long or multi-part source, creating strong hooks, or preparing exact on-image copy, concept-specific visual briefs, and optional LinkedIn captions before rendering.
---

## Article-section visual mode

When called by storytelling-article or adapting images embedded in an article, apply this mode before standalone-post defaults. Preserve each section's central realisation and mechanism, not every paragraph. First ask whether a comparison, sequence, loop, hierarchy or annotated example can explain it. Use short labels and 1–2 concise explanatory sentences where necessary; never convert the section into paragraphs pasted inside an image. Aim for roughly 40–80 words as a flexible guide, not a quota. Keep qualifications in the article unless omitting one would make the visual misleading. Evaluate text and diagram together rather than requiring text alone to carry the entire argument. Use actual section-title sentences. Retain established user-approved terms such as institution, but define them immediately in plain language. Pass article-section mode, requested aspect ratio and identity preference explicitly to the renderer.

# Adapt LinkedIn Visual Content

Create source-faithful on-image copy and a visual handoff that explain one idea without the caption. Preserve the source's reasoning and define one semantic structure the renderer can embody. Stop before visual styling or image generation.

## Source normalization

1. Resolve the complete accessible source before selecting topics. For video or audio, obtain a transcript and retain meaningful visual references or timestamps. For articles and PDFs, preserve headings, figures, tables, examples, and caveats. For photo or slide sets, restore their sequence and group adjacent frames into arguments.
2. Separate source units from post ideas. A frame, paragraph, chapter, timestamp, or chart may support one idea, while one source unit may contain several independently valuable ideas.
3. Build the coverage ledger in [references/coverage-ledger.md](references/coverage-ledger.md) for any multi-part source or batch. Do this before compression.
4. Exclude a source unit only with an explicit reason: exact duplicate, unreadable, logistical/personal, already covered, supporting evidence linked to a post, or out of scope. Similar topic is not sufficient reason to exclude a distinct mechanism, framework, example, trade-off, or consequence.
5. Treat a connected sequence as one argument before deciding whether it fits one post or requires a series.

## Workflow

1. Read or transcribe every supplied source closely. Use OCR, visual inspection, transcript retrieval, or document extraction when needed.
2. Extract the source's non-negotiable meaning:
   - facts and numbers
   - named concepts or frameworks
   - comparisons and causal relationships
   - caveats and conclusion
3. Separate technical terms that must remain verbatim from distinctive prose that must be rewritten.
4. Map each candidate idea before compressing it: premise, mechanism, relationships, consequence, conclusion, and supporting source units.
5. Run the series decision. Keep one post only when its mechanism and implication remain legible within the single-image limits. Split when compression would erase a stage, quadrant, component, example, optimization method, trade-off, or distinct consequence.
6. Choose the communication mode before drafting copy:
   - Default to **text-led** for unfamiliar concepts, arguments, philosophies, causal explanations, or ideas that need connected reasoning.
   - Use **diagram-led** only when the source is inherently spatial or relational: a matrix, chart, taxonomy, process, loop, sequence, or comparable structure.
   - Never choose diagram-led merely because a graphic would look more impressive.
7. Draft three hook options per post. Prefer a clear insight over clickbait.
8. Draft one comprehension chain: hook → what it is → how or why it works → why it matters. Add a separate takeaway only when it contributes a new conclusion; do not create one merely to fill a closing box.
9. Write in simple, connected language. Use short paragraphs when they explain better than fragments. Use labels only for true stages, parts, axes, or decisions.
   - Write for an educated general reader: state what changed, why it matters, and what the reader should notice or do. Define unavoidable acronyms and explain specialist terms in context.
10. Create a Visual Story Brief using [references/visual-story-brief.md](references/visual-story-brief.md). Define one semantic spine and map every meaning-bearing element onto it. Copy roles describe hierarchy, not separate layout zones.
11. Run the fidelity, originality, comprehension, and split checks in [references/content-rules.md](references/content-rules.md). Reconcile the coverage ledger.
12. Present the adapted copy and visual handoff for approval. Render only when the user requested the complete pipeline or separately requested image creation.
13. Draft a LinkedIn caption only when requested or when the user asks for a complete post.

## Output contract

Return these sections:

1. **Coverage ledger** — source units, idea clusters, disposition, post mapping, and exclusion reasons; include for multi-part sources or batches.
2. **Series map** — post order, relationship between posts, and why each deserves its own visual; include when more than one post is proposed.
3. **Source fidelity capsule** — premise, mechanism, implication, supporting source units, and terminology or facts that must survive.
4. **Hook options** — three concise alternatives.
5. **Communication mode and comprehension test** — text-led or diagram-led; show how the image will answer what it is, how or why it works, and why it matters.
6. **Recommended on-image copy** — exact text tagged by meaning and hierarchy, not by proposed containers.
7. **Visual Story Brief** — communication mode, semantic spine, visual embodiment, binding map, reading path, mandatory content, flexible content, and prohibited decomposition. Follow [references/visual-story-brief.md](references/visual-story-brief.md).
8. **What changed from the source** — meaningful rewrites, retained terms, and compression choices.
9. **LinkedIn caption** — only when requested.

## Boundaries

- Do not choose a template, palette, font, or decorative style. Do specify the source-grounded semantic structure: sequence, loop, matrix, layered system, contrast, orbit, spectrum, funnel, gate, or another necessary relationship.
- Do not paste a screenshot into the proposed post.
- Do not mention an event, summit, speaker, or source unless the user requests attribution.
- Do not change a framework merely to make it sound original. Preserve named concepts and change the explanation around them.
- Optimize for one 4:5 image unless the source cannot fit responsibly; then propose a small series instead of shrinking or fragmenting the explanation.
- Do not use an unfamiliar concept as a standalone label. Explain what it means, changes, tests, prevents, or enables in this context.
- Do not assume minimal copy is more readable. Connected, plain-language explanation is preferred when fragments would make the intuition cryptic.
- Do not cap the number of posts before the coverage ledger is complete. Consolidate only after proving that no distinct idea or relationship is lost.
- Do not classify a source unit as supporting material without linking it to the exact post and claim it supports.
- Do not infer completeness from a transcript alone when the source contains important diagrams, charts, demonstrations, or on-screen frameworks.
- Do not invent a generic list when the source contains a meaningful relationship.
- Do not make the brief so abstract that any unrelated title could be placed on the same visual.
