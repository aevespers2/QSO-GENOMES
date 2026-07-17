# Task Chain

## Repository role

Canonical declarative genomes, immutable ethics, and supervisory Sprite definitions. This repository is an upstream dependency of `QuantumStateObjects` and `QSO-FABRIC` and must not contain executable behavior.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Stop further acceptance-head churn, reconcile canonical PR #2 with current `main` without losing review provenance, freeze one new immutable submitted head, and only then resume deterministic-suite repair and exact-head disposition of the remaining four-genome compatibility-set findings.
- **User outcome:** A consuming runtime can retrieve one reviewed Atlas/Nova/Orion/Lyra contract set, verify exact paths, schema versions, immutable ethics, migration, Aequitas references, canonical bytes, complete manifest identity metadata, and hashes, and fail closed without importing repository code or relying on an ambiguous branch state.
- **MVP scope:** preserve PR #2 as the sole review path; preserve the five candidate commits added after head `cacd9dda3d4d9c933c917306374cdde0afdab991`; integrate current `main` into the existing PR branch or document an Architect-approved alternative that preserves every commit and review thread; resolve conflicts without dropping candidate artifacts or default-branch governance records; record old base, old head, reconciliation method, conflicts, and resulting head; freeze that head; correct the stale manifest-digest assertion; re-enumerate all review findings; validate immutable protocol identity and approved contents, migration identity/source profile/boundary, local-ethics conflicts, Aequitas activation and per-surface oversight, non-finite-number rejection, source-derived manifest identities, and digest scopes; declare reproducible dependencies; correct workflow checkout/cache semantics; complete adversarial fixtures; disposition review threads; replay clean checkout and CI; and validate the accepted manifest read-only in `QuantumStateObjects` and `QSO-FABRIC`.
- **Priority:** QSO-GENOMES remains the highest portfolio unblocker. Portfolio priority has not changed. The documented local order remains reconciliation before further remediation because PR #2 advanced by five additional commits after that gate was established, increasing divergence and invalidating any claim that earlier exact-head evidence describes the current submission.
- **Success criteria:** PR #2 remains the single review path and becomes mergeable; one frozen reconciled head contains every intended candidate and governance change; no reviewed history is force-rewritten or lost; the deterministic suite passes at that head; every current and still-material outdated finding is resolved or explicitly dispositioned against it; CI certifies the submitted head; dependencies are reproducible; exact artifacts and identity-bearing source fields are validated; immutable migration and local additions fail closed on identity, content, boundary, conflict, and duplication errors; Aequitas references, surfaces, activation rules, and oversight mappings are unique and source-consistent; manifest digest scopes are unambiguous; clean replays produce identical hashes; negative fixtures fail closed; and both downstream consumers validate the same accepted commit and identities.
- **Non-goals:** opening a competing release PR; force-pushing or rebasing away review provenance without explicit approval; continuing acceptance-remediation commits on an unfrozen diverged head without an Architect exception and documented reason; executable agent behavior; network access; credentials; mutation activation; autonomous policy changes; payment authority; runtime implementation; or treating candidate reports, configured workflows, unresolved findings, or unverified branch tests as accepted release evidence.
- **Release rationale:** QSO-GENOMES is the narrowest upstream contract needed by the runtime repositories. A provenance-preserving reconciliation and immutable review head are prerequisites to meaningful evidence; accepting one evidence-backed data-only set then removes the dependency without granting execution authority or widening product scope.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0a | Reconcile PR #2 with `main` and freeze a canonical head | Architect | — | READY | Existing PR #2 remains the sole path; current `main` and all five post-snapshot candidate commits are integrated without force-rewriting reviewed history; conflicts and retained changes are documented; the resulting head is mergeable, immutable for review, and recorded with a reconciliation manifest. |
| P0b | Repair the deterministic suite and resolve exact-head integrity, identity, dependency, CI, and review findings | QSOBuilder | P0a | BLOCKED | The stale manifest-digest assertion is corrected; every intended remediation is present on the frozen head; all current and material outdated findings are fixed or dispositioned; exact-head checks pass; and evidence is tied to the final immutable head. |
| P1 | Run independent clean-checkout and CI conformance replay | Architect | P0b | BLOCKED | Supported Python environments install from checked-in instructions; schema, immutable, migration, Aequitas, manifest, canonicalization, duplicate/conflict, overflow, activation-rule, and negative tests pass at the exact reviewed head with retained logs and hashes. |
| P2 | Accept and publish the versioned compatibility manifest | Architect | P1 | BLOCKED | One immutable candidate commit and complete manifest identity are approved; source archive, reports, checksums, provenance, rollback notes, and compatibility status are published without executable authority. |
| P3 | Verify read-only downstream consumption | Builder | P2 | BLOCKED | `QuantumStateObjects` and `QSO-FABRIC` independently reject missing, stale, mutated, duplicate, conflicting, overflowed, or incompatible artifacts and accept the exact published version/hash set. |
| P4 | Define a declarative payment-policy extension | Architect | P2 and approved settlement boundary | BLOCKED | Any extension remains data-only, grants no credentials or transfer authority, and has approved versioning and migration rules. |

## Current repository health and candidate evidence

At the latest observed snapshot, GitHub reported PR #2 open and non-mergeable at head `46f3248d8f67b7f0cc734159d2fa0a27e6051ea7`. Comparison against default-branch head `0ac8960db20dba6ef083d928a44f4ca756d44713` showed the PR branch 74 commits ahead and 24 commits behind, with merge base `c6c6ccdd61391da5fae5a268022c510069016b33`. No combined status checks or pull-request workflow runs were attached to that head. These counts are a timestamped snapshot and must be recaptured immediately before reconciliation.

The branch advanced five commits after the prior product snapshot. Those commits modify the Aequitas validator and focused tests, add an Aequitas review-surface report, and update branch-local task and punch-list records. They are candidate hardening work, not accepted evidence. They do not modify `tests/test_contract_manifest.py`, which still expects digest `6d9b0ca8c6766fbb63b4613df5b2baee455f1e63c848d6f75e56726efbc57cac`, while the committed manifest reports `99f33227247ef39fef3e1c3206c8ea49b9be9af86148298f07bdbf00b0cd6921`; the deterministic suite remains failing at the observed head.

The review timeline contains 34 threads: four resolved/outdated and 30 unresolved, including 23 current findings and seven unresolved outdated findings. The newest findings cover migration source-profile identity, migration contract identity, overflowed JSON-number rejection, and pinning the approved immutable-protocol contents. Counts may change with further review and must be regenerated for the frozen head.

## Cross-repository gate

`QuantumStateObjects` and `QSO-FABRIC` may not claim a verified four-object integration until P0a-P3 are complete and both consumers validate the same accepted commit, manifest version, canonicalization profile, and digest scopes.

## Builder rules

Do not add unrelated runtime or product scope. Pause additional acceptance-remediation commits until P0a is complete unless the Architect records an explicit exception, rationale, bounded scope, and evidence-preservation plan. Preserve the PR branch, review threads, and default-branch governance commits; do not force-push, rebase away history, publish, tag, or claim acceptance. After reconciliation, work only on the highest-priority unresolved acceptance finding and attach every claim to the frozen submitted head.

## Builder log

Record old and new bases/heads, merge or alternative reconciliation method, conflict resolutions, retained/dropped paths, review-thread mapping, validation commands/results, Python/tool versions, schema and fixture versions, canonical hashes, workflow URLs, residual risks, downstream replay results, and rollback evidence.

- 2026-07-16 — Advanced P0 from compatibility-set creation to independent acceptance of PR #2 after the candidate added the missing artifacts but remained blocked by integrity, provenance, dependency, workflow, and downstream-verification findings.
- 2026-07-16 — Consolidated the initial remediation lineage onto existing PR #2, preserving the original review path and eliminating a competing-head decision.
- 2026-07-16 — Recorded additional candidate immutable-manifest binding work while keeping it classified as unaccepted implementation evidence.
- 2026-07-16 — Detected that PR #2 had diverged from `main`, remained non-mergeable, and had no status checks on the observed head. Portfolio priority remained unchanged; provenance-preserving reconciliation became P0a because continuing remediation before reconciliation invalidates exact-head evidence and increases review churn.
- 2026-07-16 — Observed five additional acceptance-remediation commits after the reconciliation gate was established. The branch reached head `46f3248…`, 74 commits ahead and 24 behind the observed default head, with 30 unresolved review threads and a still-failing manifest-digest test. P0a remains first; further head movement requires an explicit Architect exception.