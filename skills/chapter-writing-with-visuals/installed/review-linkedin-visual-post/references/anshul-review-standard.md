# Anshul's LinkedIn visual review standard

These standards consolidate repeated user feedback. Treat them as binding review criteria, not generic suggestions.

## Core principle

The visual must feel conceived as one idea. Text, image, diagram, signature, whitespace, and accents must share one composition and one design language.

Visual unity and production integrity are separate gates. One SVG, canvas, generation pass, or export can still contain assembled modules. Review appearance first and provenance last.

## Article-section exception

Apply the article-section mode in SKILL.md before these standalone-post tests. Judge meaning from diagram and concise copy together. Respect approved landscape canvas and identity omission, allow meaningful connected callouts, and reject excessive prose or decorative scenery.

## Historical feedback translated into tests

### Understanding over decoration

- Text is more important; graphics support the text.
- Understanding is more important than a graphic using a large share of the canvas.
- Do not merely name concepts. Explain what each concept tests, changes, or means.
- A reader should understand the intuition without needing the caption or source.
- Choose a design system and information architecture that can support the amount of explanation required.
- Default to text-led composition for conceptual arguments and unfamiliar ideas. The copy must answer what it is, how or why it works, and why it matters.
- Prefer simple, connected sentences and one or two short paragraphs over fragments distributed around artwork.
- In text-led mode, reserve approximately 55–70% of usable canvas for text communication and approximately 25–35% for supporting illustration.
- On a 1080 px-wide canvas, require at least 30 px explanatory body text, 28 px necessary diagram labels, and 34 px takeaway text.

### One semantic field

- Use one diagram, metaphor, scene, or typographic field to carry the claim, relationship, and conclusion.
- Fail when headline, explanation, cards, hero art, takeaway, and signature behave as independently designed regions.
- Fail when a diagram is concept-specific but the surrounding architecture remains generic.
- Allow separate cells or sides only when the source relationship requires them and one governing structure remains dominant.
- Share brand language across posts, not silhouettes or information architecture.

Use these tests:

1. **Composition sentence:** Can one mechanism carry the claim, progression, and conclusion without listing modules?
2. **Region inventory:** Which areas are independently framed or independently understandable? Several major regions indicate assembly.
3. **Crop test:** Can a major region be removed or replaced while the rest still works? If yes, it was bolted on.
4. **Swap-title test:** Would another AI topic still fit the architecture? If yes, it is generic.
5. **Production test:** Does the base contain every semantic element, and does the final differ only inside the portrait circle? This test cannot prove visual unity.

### Space and mobile readability

- Use 1080 × 1350 portrait unless explicitly overridden.
- Preserve approximately 64 px side margins, 56 px top margin, and 48 px bottom clearance.
- Keep title wrapping intentional and subtitle directly supportive and large enough.
- Enlarge axes, labels, and data values for phone viewing.
- Avoid both empty space with no purpose and dense, force-fitted content.
- Do not let a concluding line approach the lower border because the signature consumed the remaining space.
- Visible breathing room is good when it strengthens hierarchy; it is not a license to leave a dead band.

### Signature and portrait

- Exact name: `Anshul Jain`
- Exact tag: `AI & Gen AI Product Mgmt`
- Use the approved real photograph; never generate or restyle the face.
- Target a compact 90 px outer portrait diameter on a 1080 px canvas, allowing 85–95 px.
- Design the portrait frame, name, tag, divider, and surrounding space with the base composition.
- Portrait placement may later replace only the empty circle interior.
- Reject a purple pill, generic badge, contrasting signature strip, or any signature treatment that uses a different visual language from the post.
- Reject unused space to the right of a signature or a full-width row created only to contain it.
- The portrait must neither dominate the story nor disappear when the post is personal.

### Tone and emotional fit

- Choose the design system from the idea's emotional tone, not habit.
- Dark treatments can make a positive story feel sad; reject them when they distort the intended emotion.
- Balance the user's portrait with the surrounding story: the image is about the person, but the context around the person must still carry meaningful information.

## Hard failures

Any of these normally requires `REBUILD`:

- assembled-pieces composition
- full-canvas artwork followed by semantic overlays
- missing portrait-ready base, render trace, or portrait-difference verification
- generic or repeated template unrelated to the topic
- dominant artwork that does not explain the idea
- missing or misleading mechanism
- cryptic content caused by excessive minimalism
- text-led post dominated by artwork or written as disconnected labels
- signature or portrait designed as a separate visual system
- positive or transformational message given a contradictory emotional treatment

Use `REVISE` only when the semantic field is already coherent and the remaining issues are local: line break, font size, spacing, exact wording, small portrait correction, or safe-margin fix.
