# Unified Visual Review Format

Create one section for every approved chapter subsection in Blueprint/Research Mapping order.

## Generated candidates

For every passing generated candidate:

`GEN ID: GEN-###`
`ORIGIN: GENERATED_EXPLAINER`
`SUBSECTION: <id/title>`
`MODE: DATA_EXPLAINER | TOPIC_EXPLAINER | HUMOUR_METAPHOR`
`CANONICAL CHAPTER: <Artifact A ID/revision/paragraph locator>`
`EVIDENCE BASIS: <approved evidence ID/revision/locator(s)>`
`ADAPT BRIEF: <locator>`
`RENDER ASSET: <exact Drive asset ID/path>`
`GENERATED EVALUATION: PASS`
`DATA_LOCK: <summary or N/A>`
`HUMAN DECISION: PENDING`

Embed/show the exact generated visual that the human is deciding on.

## Subsection with no candidate

For each subsection without a candidate, state:

`GENERATION_REQUIRED: NO | YES`
`GENERATED VISUAL: NOT PLANNED | GENERATION FAILED`
`REASON: <concise verified reason>`

No Human Decision field is required when no candidate exists.

## Rules

- GEN IDs must be globally unique within the review.
- Do not turn GEN images into evidence/source citations.
- Do not hide failed generation or NO-target reasons. Bind the review to current Artifact A and evidence revisions.
- Every actual candidate starts PENDING in a newly created review.
- Every candidate is GENERATED_EXPLAINER. A failed planned target requires explicit human acknowledgement before omission; it is not silently treated as EXCLUDE.
- Do not include evaluator chain-of-thought or workflow prose in the reader-facing chapter; this review is an audit artifact only.
