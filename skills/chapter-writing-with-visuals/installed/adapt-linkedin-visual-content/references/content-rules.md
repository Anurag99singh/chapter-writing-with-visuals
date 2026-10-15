# Content adaptation rules

## Fidelity

Preserve:

- factual claims and numeric values
- framework names and technical vocabulary
- logical relationships such as cause, contrast, sequence, trade-off, and dependency
- the source's central conclusion

Do not add evidence, certainty, examples, or implications not supported by the source.

## Originality

Rewrite:

- headline and opening frame
- full explanatory sentences
- labels that are not established technical terms
- takeaway language

Avoid retaining distinctive source sentences. Short technical phrases, proper nouns, numbers, and framework names are exempt when paraphrasing would reduce accuracy.

## Article-section exception

For article images, apply the SKILL.md article-section mode: visual relationships and short annotations carry one central realisation, with nuance in surrounding prose. The standalone text-led word ranges and text-alone test below do not apply.

## Single-image adaptation

- Hook: usually 6–14 words; up to three short lines when the phrasing earns it.
- Choose **text-led** or **diagram-led** before compressing the copy. Default to text-led for conceptual explanations, arguments, philosophies, and unfamiliar terminology. Use diagram-led only when the source is inherently a matrix, process, chart, taxonomy, loop, sequence, or other spatial relationship.
- Build a self-contained comprehension chain: what it is → how or why it works → why it matters. The hook introduces it. Use a separate takeaway only when it adds a conclusion rather than repeating the chain.
- Text-led posts: normally 70–120 meaningful words; allow up to 150 when the additional explanation is necessary and remains readable. Use one or two short connected paragraphs rather than scattering the thought across fragments.
- Diagram-led posts: normally 45–100 meaningful words. Use labels only for true parts, axes, stages, or relationships; explain unfamiliar concepts in sentences outside the labels.
- Content elements: use only as many as the source requires. Describe their relationship; do not imply that each needs its own box or panel.
- Each named concept must say what it means, changes, tests, prevents, or enables. A noun phrase alone does not count as explanation.
- Annotation: optional; use it only when it clarifies the visual relationship.
- Conclusion: normally 8–18 words when needed. It may be embedded in the main mechanism; do not require a separate takeaway region.
- Avoid dense paragraphs, long caveats, repeated definitions, hashtags, and calls to follow/repost inside the image. Do not ban short paragraphs merely because fragments look more visual.

Conciseness is a readability tool, not the goal. Preserve the mechanism and consequence plus any essential contrast, trade-off, causal link, decision rule, or caveat. If a reader cannot explain the idea without the caption, rebuild the adaptation or split the post.

## Comprehension checks

- **What-is-it test:** State what an unfamiliar concept means before expecting the reader to interpret it.
- **Explain-don't-name test:** Reject labels that merely name the parts when the reader still cannot say what they do.
- **Text-alone test:** Hide the graphic mentally. The remaining copy must still communicate the central claim and intuition.
- **Example-over-decoration test:** For an abstract idea, prefer one concrete source-supported example over an additional decorative object or icon.
- **Split test:** If the explanation cannot fit at phone-readable type sizes, create another post instead of shortening the reasoning into cryptic fragments.

## Hook quality

A good hook makes the source's tension immediately understandable. Prefer:

- a surprising contrast
- a consequential choice
- a familiar assumption being corrected
- a clear problem framing

Avoid unsupported superlatives, fear language, vague claims, and generic AI hype.

## Approval checkpoint

Before rendering, show the user the adapted copy and explain what was preserved and what was changed. If the user has already approved exact copy, return it without reopening content decisions.

## Example: cognitive loops

Source meaning:

- ReAct: fast iteration; short-horizon view
- Reflection: slower loops; complex problem solving
- Plan-and-Execute: goal-oriented; less adaptable to change
- Tree of Thoughts: exploratory; computationally expensive
- Critic-Refine: improves a specific output; depends on a good critic

Social-friendly adaptation:

> Not every AI agent should think the same way.
>
> Need speed? ReAct.  
> Need deeper thinking? Reflection.  
> Have a clear goal? Plan-and-Execute.  
> Need alternatives? Tree of Thoughts.  
> Need polish? Critic-Refine.
>
> Start simple. Add deeper reasoning only when the task earns it.

This preserves the taxonomy and trade-offs while replacing the source's title and explanatory phrasing.

Visual-story handoff:

- Story form: a left-to-right spectrum of five reasoning modes.
- Meaning: movement from fast reaction toward deeper, more expensive refinement.
- Required relationships: each mode must connect to the job it is best suited for; do not present five equal decorative cards.
- Emphasis: the choice depends on task need, not a universal ranking.
- Takeaway role: close the spectrum with “Start simple...” as a decision rule.
