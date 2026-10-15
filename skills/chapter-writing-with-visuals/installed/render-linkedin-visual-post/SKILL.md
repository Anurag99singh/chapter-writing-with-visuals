---
name: render-linkedin-visual-post
description: Turn approved copy and a concept-specific visual-story brief into a polished 1080 × 1350 LinkedIn single-image post using Anshul Jain's saved design systems or screenshot-inspired dense reference layouts. Use when the user asks to generate, render, restyle, or create a LinkedIn visual from finalized text, wants bespoke visual storytelling comparable to the saved Beyond the Model gold standards, requests style options, or needs consistent branding with an integrated name, tag, and portrait slot rather than a separately designed signature overlay.
---

## Article-section visual mode

For article-section visuals, this mode overrides standalone-post format, identity, density and architecture defaults below. Read references/article-visuals.md and inspect the bundled approved examples before rendering. Default to landscape 1536 × 1024, simple explanatory whiteboard linework, short annotations and no signature/portrait unless requested. The diagram must carry a real comparison or mechanism; do not reproduce the article in the image or use elaborate scenery. Do not impose a fixed text/graphic percentage. Connected comparison regions, explanatory callouts and a closing question are allowed when they complete the same argument. Generate the complete image together; preserve exact approved meaning. Identify humans and agents distinctly (human figure versus robot, clearly labelled if needed). Record article-section mode, canvas, identity_mode, exact copy and prompt in the trace. Use review-linkedin-visual-post's article validator rather than the portrait-only validator when identity is omitted.

# Render LinkedIn Visual Post

Render approved copy without changing its meaning. Treat design systems as styling, never as layouts. Build one semantic visual field in which text, diagram, conclusion, whitespace, and signature belong to the same idea.

## Dense screenshot-inspired layouts

When the user asks for the saved influencer screenshot themes, dense single-image reference posts, or the way the references pack information into one post, use [references/dense-reference-layouts.md](references/dense-reference-layouts.md). Inspect the selected bundled screenshot and provide it to image generation as visual guidance when supported. Preserve its information architecture, density, type hierarchy and drawing treatment; changing only colours does not fulfil this mode.

This is an explicit alternative to the sparse default. In this mode, the reference-specific layout and density rules take precedence over this skill's default anti-panel architecture rules, large-text minimums and generic design-system tokens. Keep the original unified-generation method and factual accuracy. Use the chosen reference to determine structure before selecting colours. Do not apply this mode to unrelated requests or remove the existing styles.

## Required inputs

- Approved on-image copy
- A Visual Story Brief containing the communication mode, comprehension chain, semantic spine, visual embodiment, binding map, reading path, content constraints, and prohibited decomposition
- One named design system, or permission to choose one
- Any required supporting visual asset; do not provide the author portrait to the image model

If the brief is missing, derive it from the source and approved copy before rendering. If the copy is not approved, use `$adapt-linkedin-visual-content` or request approval first.

## Gold-standard quality bar

Read [references/gold-standard-quality-bar.md](references/gold-standard-quality-bar.md) before every render. Inspect the matching examples in `assets/gold-standards/` as quality references:

- `visual-notebook-program-dont-prompt.png`
- `neon-human-control.png`
- `editorial-operating-layer.png`

Use them to calibrate hierarchy, visual intelligence, polish, content density, and branding. Do not reproduce their content structures unless the new idea genuinely has the same semantic structure.

## Design systems

Read [references/design-systems.md](references/design-systems.md) before designing. Use the matching reference image in `assets/references/` and the exact tokens in `assets/design_tokens.json`.

- **Editorial Impact** — consequential, urgent, editorial
- **Data Signal** — credible, calm, analytical
- **Neon Intelligence** — futuristic, provocative, high-energy
- **Visual Notebook** — personal, exploratory, explanatory
- **News Signal** — current company/person-led news with a photo-referenced recognizable figure, accurate logo, factual headline and short factual subheadline; keep interpretation in the caption and read [references/news-signal.md](references/news-signal.md)
- **Source Card** — source-first resharing when the original X post or announcement should remain the main evidence; preserve the source card faithfully and add only concise context
- **Author Insight Card** — a short original observation or question in a clean author-post layout; use the approved portrait and signature treatment, without simulated engagement counts

Any system may be used for any content. Select by desired tone, not by whether the content is a chart, framework, quote, flow, or comparison.

## Workflow

1. Lock the approved copy. Verify that it explains what the idea is, how or why it works, and why it matters. Return to adaptation when labels are carrying missing reasoning.
2. Read the quality bar and selected design-system reference. Choose the system by tone, not content type.
3. Write one composition sentence: `One [mechanism or scene] carries [the claim], [the progression or relationship], and [the conclusion] as the reader moves [path].`
4. Run the architecture preflight below. Reject the plan before rendering if it decomposes into independent modules.
5. Design a 1080 × 1350 semantic field around that mechanism. Integrate the hook, explanation, required labels, conclusion, whitespace, and signature into its reading path.
6. Build the exact name `Anshul Jain`, exact tag `AI & Gen AI Product Mgmt`, and an empty 85–95 px circular portrait slot into the field. Record `x`, `y`, `diameter`, and `inset`. Never give the portrait to an image model.
7. Generate and preserve one complete portrait-ready base using the integrated-image-generation procedure below.
8. Use `$place-anshul-portrait` to replace only the recorded circle interior with the approved photograph.
9. Validate dimensions, create a 390 px-wide preview, and record the trace fields defined below.
10. Run `$review-linkedin-visual-post`. `REBUILD` requires a new composition sentence and architecture; do not patch the rejected layout. Deliver only after `PASS`.

## Architecture preflight

Reject the architecture when any condition is true:

- It can be described as a header, explanatory block, cards, central illustration, takeaway box, and footer.
- The main diagram or image can be removed while the remaining poster still forms a complete generic layout.
- The hook, explanation, stages, or conclusion can be independently cropped or replaced without breaking the mechanism.
- A loop, sequence, or process is represented by detached cards around a decorative centre instead of one continuous path or scene.
- Copy roles from the brief have become visual containers by default.

Distinct regions are allowed only when the source relationship requires them—such as matrix cells, opposing sides, or true independent peers—and the governing relationship remains visually dominant.

## Semantic-unity contract

- Use one continuous scene, diagram, or typographic field to carry the argument. The visual must do more than sit beside correct copy.
- In text-led mode, let connected copy form the primary field and embed one supporting image or relationship within it. Reserve roughly 55–70% of usable space for text and no more than roughly 35% for supporting graphics.
- In diagram-led mode, place explanation on the path, inside the scene, or within the actual structure. Do not surround the mechanism with a second card system.
- Let the conclusion emerge from the mechanism. Use a separate takeaway container only when the source itself requires a distinct decision rule or result.
- Keep the signature on the same surface and reading rhythm. Use existing negative space or attach it to an active edge, line, or content band; never create a row solely for identity.
- Reuse brand language across a series, not information architecture. Each topic needs its own silhouette and mechanism.

## Integrated-image-generation procedure

`integrated-image-generation` is the only permitted production method. It means the image-generation model creates the complete portrait-ready post as one composition in one generation call. It is an audit value recorded in the trace, not a separate tool or built-in ChatGPT mode.

1. Write one generation prompt containing the composition sentence, exact approved copy, selected design system, reading path, text and graphic allocation, signature treatment, empty portrait-slot requirement, and prohibited decomposition.
2. Ask the image-generation model to render the entire 1080 × 1350 post together: hook, explanation, mechanism or scene, labels, connectors, conclusion, whitespace, exact name, exact tag, portrait frame, texture, and accents.
3. Do not create, generate, draw, import, or assemble separate artwork, backgrounds, icons, diagrams, text layers, cards, signature elements, or other components for later placement. Reference images may guide style or source fidelity, but must not become poster fragments.
4. Inspect the complete candidate. If wording, hierarchy, signature text, visual logic, readability, or composition is wrong, revise the prompt and generate a new complete candidate. Never repair a candidate with overlays, native-layout tools, compositing, inpainting, or targeted semantic edits.
5. Treat each regeneration as a new complete attempt. "One generation" means every candidate is born complete; it does not limit the number of discarded attempts.
6. Preserve the accepted generation as the portrait-ready base. If its aspect ratio or safe margins are wrong, regenerate it; do not crop away or rearrange meaning-bearing content.
7. After accepting the base, allow only dimension validation, format-preserving export, mobile preview, review, and insertion of the approved portrait inside the recorded circle. Any other change requires a new complete generation.

Record: base and final paths, communication mode, exact copy, exact generation prompt, `render_method: integrated-image-generation`, `complete_poster_generated_together: true`, `separate_component_assets: false`, `semantic_edits_after_generation: false`, composition sentence, slot geometry, canvas, font sizes, space allocation, `discarded_complete_attempts`, and `operations_after_base`.

## Fit and identity rules

- Use at least 30 px explanatory body text, 28 px necessary labels, and 34 px conclusion text on a 1080 px canvas. Signature metadata may be smaller.
- Prefer connected copy to fragments. Reduce graphics before reducing text size; split the post if the explanation still does not fit.
- Keep the portrait photographic, visually subordinate, and 85–95 px in outer diameter. Do not enlarge the identity block to fill space.
- Match the signature's typography, colour, line weight, texture, and spacing to the composition. Reject pills, badges, contrasting footer strips, and dead space created for the signature.
- Omit event or summit branding unless requested. Never paste the source screenshot into the visual.

## Multiple variants

For two or more requested styles, render the same approved copy in each design system. Keep the message identical so the user can compare design rather than copy.

## Delivery

Return:

- final PNG file(s)
- selected design-system name(s)
- `$review-linkedin-visual-post` verdict
- portrait-ready base and render trace supplied to the reviewer
- a short note if any approved text could not be used exactly
