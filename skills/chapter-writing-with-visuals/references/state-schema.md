# Durable snapshot schema

Use schema version 1. Every receipt points to actual read-back artifacts; these fields do not manufacture evidence.

Required run identity: `run_id`, `chapter_topic`, `workspace_account`, `destination_folder_id`, `outline: {id,revision,subsection_ids}`, `evidence: {id,revision}`. The ordered unique subsection IDs come from direct reading of the approved outline. Audience and author instructions are optional, with the existing worker's nontechnical-reader default. Record exact model dispatches and stable operation IDs in Activity/Events. `in_flight_operation` records uncertain operations; `paused_limit` blocks new dispatch until explicitly reconciled/released.

`canonical`: `{id, revision, outline_revision, evidence_revision, native_presentation: {passed, report_id, artifact_id, artifact_revision}, evaluation: {passed, score, report_id, artifact_id, artifact_revision, checks}}`. Checks have all five named checks with `{passed,evidence}`. A native report/plan locator and real revision are required.

`generation_plan`: `{id, canonical_revision, evidence_revision, entries:[{subsection_id, required, reason}]}`. Every approved subsection must occur once in order; compare directly with approved outline/current A. `candidates`: list of `{id, subsection_id, origin, canonical_revision, evidence_revision, mode, attempt, brief_id, asset_id, asset_sha256, installed_review, evidence_review}`. Receipt fields: `{passed,report_id,asset_sha256}` plus evidence score. Each actual candidate ID begins GEN-, origin GENERATED_EXPLAINER; attempt is 1 or 2. `data_lock_passed` is required for DATA_EXPLAINER; inspection must cover actual image vs lock. A failed target records `generation_failed:true`; omission requires an author `failure_acknowledgement` with reviewer/time/evidence locator.

`visual_review`: `{id, revision, canonical_revision, evidence_revision, candidate_ids, asset_hashes, evaluation:{passed,score,report_id,artifact_id,artifact_revision}}`. `visual_decisions`: `{review_id,review_revision,reviewer,recorded_at,evidence_locator,values:{GEN-ID: KEEP|EXCLUDE}}`. No automatic inference. An empty candidate set needs an evaluated explicit all-NO generation plan and still a bound review/decision receipt verifying no PENDING candidates.

`final`: `{id,revision,canonical_id,canonical_revision,visual_review_id,visual_review_revision,placement_report_id,prose_preserved,formatting_preserved,placements:{GEN-ID:{status,asset_sha256}},evaluation:{passed,score,report_id,artifact_id,artifact_revision}}`. B must differ from A. Every KEEP is INSERTED with exact approved hash; every EXCLUDE is EXCLUDED. A failed placement is not complete.

`final_approval`: `{artifact_id,artifact_revision,reviewer,recorded_at,evidence_locator}`. Bind approval to current passed B. Never reuse approval by title. `revision_requested` includes explicit request/report locator and target scope; `diagnose_attempts` is bounded 0–3.

Re-read current input/artifact revisions before transitions. Equality of saved revisions alone does not establish freshness. After any native write, bind the final revision in a separate durable receipt; do not append its revision to the same document and invalidate it.
