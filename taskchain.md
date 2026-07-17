# Task Chain

## Repository role

Canonical declarative genomes, immutable ethics, and supervisory Sprite definitions. This repository is an upstream dependency of `QuantumStateObjects` and `QSO-FABRIC` and must not contain executable behavior.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Reconcile canonical PR #2 with current `main` without losing review provenance, freeze one new immutable submitted head, and only then resume exact-head resolution and independent replay of the remaining four-genome compatibility-set findings.
- **User outcome:** A consuming runtime can retrieve one reviewed Atlas/Nova/Orion/Lyra contract set, verify exact paths, schema versions, immutable ethics, migration, Aequitas references, canonical bytes, complete manifest identity metadata, and hashes, and fail closed without importing repository code or relying on an ambiguous branch state.
- **MVP scope:** preserve PR #2 as the sole compatibility-set review path; merge current `main` into the existing PR branch or document an Architect-approved alternative that preserves every commit and review thread; resolve conflicts without dropping candidate artifacts or default-branch product/release records; record old base, old head, reconciliation method, conflicts, and resulting head; freeze that head; re-enumerate review findings against it; validate immutable protocol/migration manifest binding, local-ethics conflict rejection, duplicate migration and Aequitas-surface rejection, source-derived manifest identities, and digest scopes; declare reproducible dependencies; correct workflow checkout/cache semantics; complete adversarial fixtures; disposition review threads; replay clean checkout and CI; and validate the accepted manifest read-only in `QuantumStateObjects` and `QSO-FABRIC`.
- **Priority:** QSO-GENOMES remains the highest portfolio unblocker. Portfolio priority has not changed; only the local execution order changed because PR #2 is non-mergeable and diverged from `main`, so additional remediation or unrelated default-branch merges before reconciliation would create more evidence churn.
- **Success criteria:** PR #2 remains the single compatibility-set review path and becomes mergeable; one frozen reconciled head contains every intended candidate and governance change selected for that head; no reviewed history is force-rewritten or lost; every finding is resolved or explicitly dispositioned against that head; CI certifies the submitted head; dependencies are reproducible; exact artifacts and identity-bearing source fields are validated; immutable migration and local additions fail closed on conflict or duplication; Aequitas references and surfaces are unique and source-consistent; manifest digest scopes are unambiguous; clean replays produce identical hashes; negative fixtures fail closed; and both downstream consumers validate the same accepted commit and identities.
- **Non-goals:** opening a competing compatibility-set release PR; force-pushing or rebasing away review provenance without explicit approval; continuing unrelated feature work before reconciliation; executable agent behavior; network access; credentials; mutation activation; autonomous policy changes; payment authority; runtime implementation; or treating candidate reports, configured workflows, unresolved findings, or unverified branch tests as accepted release evidence.
- **Release rationale:** QSO-GENOMES is the narrowest upstream contract needed by the runtime repositories. A provenance-preserving reconciliation is required before the candidate can be reviewed as one coherent, mergeable state; accepting one evidence-backed data-only set then removes the dependency without granting execution authority or widening product scope.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0a | Reconcile PR #2 with `main` and freeze a canonical head | Architect | — | READY | Existing PR #2 remains the sole compatibility-set path; current `main` is integrated without force-rewriting reviewed history; conflicts and retained changes are documented; the resulting head is mergeable, immutable for review, and recorded with a reconciliation manifest. |
| P0b | Resolve exact-head integrity, manifest-identity, dependency, CI, and review findings | QSOBuilder | P0a | BLOCKED | Every candidate remediation is present on the frozen head; remaining findings are fixed or dispositioned; exact-head checks pass; and evidence is tied to the final immutable head. |
| P1 | Run independent clean-checkout and CI conformance replay | Architect | P0b | BLOCKED | Supported Python environments install from checked-in instructions; schema, immutable, migration, Aequitas, manifest, canonicalization, duplicate/conflict, and negative tests pass at the exact reviewed head with retained logs and hashes. |
| P2 | Accept and publish the versioned compatibility manifest | Architect | P1 | BLOCKED | One immutable candidate commit and complete manifest identity are approved; source archive, reports, checksums, provenance, rollback notes, and compatibility status are published without executable authority. |
| P3 | Verify read-only downstream consumption | Builder | P2 | BLOCKED | `QuantumStateObjects` and `QSO-FABRIC` independently reject missing, stale, mutated, duplicate, conflicting, or incompatible artifacts and accept the exact published version/hash set. |
| P4 | Define a declarative payment-policy extension | Architect | P2 and approved settlement boundary | BLOCKED | Any extension remains data-only, grants no credentials or transfer authority, and has approved versioning and migration rules. |

## Concurrent governance control-plane candidate — draft PR #3

**Status:** `REVIEW — EXACT-HEAD WORKFLOW PASSED; MERGE ORDER REQUIRES ARCHITECT DECISION`

Draft PR #3 adds a machine-readable PR ontology, Change Analyst, PR Steward, independent Inspector, PR-body validation, retained evidence, and daily audit automation. At head `c456434b660a380d67f5bcb8a56a46d21c1dc3e3`, GitHub Actions run `29556170567` completed successfully: the submitted PR head was checked out, the ontology declaration and derived controls validated, and artifact `pr-ontology-c456434b660a380d67f5bcb8a56a46d21c1dc3e3` was retained with digest `sha256:41c7f2d090b4f0bc9da99940762c9fdf7808c328ca01fab6c495e99f04b401af`.

This verifies the configured ontology workflow at that exact head. It does not establish portfolio-wide adoption, semantic execution of every domain-specific control package, migration of legacy PRs, compatibility-set acceptance, release readiness, or deployment authority.

A merge-order conflict now requires an Architect decision. PR #2 is non-mergeable and currently diverged from default-branch head `1901b0c303cc48f0ea2fa8bf76bf60cf9e1ba79d` by 69 commits ahead and 23 behind, with merge base `c6c6ccdd61391da5fae5a268022c510069016b33`. Merging PR #3 to `main` before PR #2 reconciliation would add more default-branch drift and invalidate the current reconciliation counts.

**Recommended sequence:** keep PR #3 draft; complete P0a and freeze PR #2's reconciled head; then refresh PR #3 against the resulting `main`, rerun exact-head validation, and review it as a separate governance change. An alternative sequence may be approved only if it documents how review provenance, ontology migration, conflicts, exact-head evidence, and rollback are preserved. This sequencing decision does not change QSO-GENOMES' portfolio priority or authorize compatibility-set release.

## Current repository health and candidate evidence

GitHub currently reports PR #2 as open and non-mergeable at head `cacd9dda3d4d9c933c917306374cdde0afdab991`. Comparison with default-branch head `1901b0c303cc48f0ea2fa8bf76bf60cf9e1ba79d` shows the PR branch 69 commits ahead and 23 commits behind, with merge base `c6c6ccdd61391da5fae5a268022c510069016b33`.

The PR branch contains candidate Atlas/Nova/Orion/Lyra artifacts, exact-set enforcement, immutable-ethics protocol and migration work, Aequitas validation, canonicalization, manifest generation, tests, workflows, reports, provenance, and product/release documentation. These are implemented candidate code and self-reported evidence, not accepted capability; reconciliation can change the reviewed state and therefore requires renewed exact-head review.

## Cross-repository gate

`QuantumStateObjects` and `QSO-FABRIC` may not claim a verified four-object integration until P0a-P3 are complete and both consumers validate the same accepted commit, manifest version, canonicalization profile, and digest scopes.

## Builder rules

Do not add unrelated runtime or product scope. Until P0a is complete, preserve the PR branch, review threads, and default-branch governance commits; do not force-push, rebase away history, publish, tag, or claim acceptance. Keep PR #3 draft unless the Architect records a different merge-order decision. After reconciliation, work only on the highest-priority unresolved acceptance finding and attach every claim to the frozen submitted head.

## Builder log

Record old and new bases/heads, merge or alternative reconciliation method, conflict resolutions, retained/dropped paths, review-thread mapping, validation commands/results, Python/tool versions, schema and fixture versions, canonical hashes, workflow URLs, residual risks, downstream replay results, governance migration decisions, and rollback evidence.

- 2026-07-16 — Advanced P0 from compatibility-set creation to independent acceptance of PR #2 after the candidate added the missing artifacts but remained blocked by integrity, provenance, dependency, workflow, and downstream-verification findings.
- 2026-07-16 — Consolidated the initial remediation lineage onto existing PR #2, preserving the original review path and eliminating a competing-head decision.
- 2026-07-16 — Recorded additional candidate immutable-manifest binding work while keeping it classified as unaccepted implementation evidence.
- 2026-07-16 — Detected that PR #2 had diverged to 62 commits ahead and 20 behind `main`, remained non-mergeable, and had no status checks on the observed head. Portfolio priority remained unchanged; provenance-preserving reconciliation became P0a.
- 2026-07-17 — Verified draft PR #3's ontology workflow at exact head `c456434b660a380d67f5bcb8a56a46d21c1dc3e3` with retained artifact digest `sha256:41c7f2d090b4f0bc9da99940762c9fdf7808c328ca01fab6c495e99f04b401af`; recorded that PR #2 is now 69 ahead and 23 behind `main`; recommended keeping PR #3 draft until PR #2 reconciliation is frozen so governance adoption does not increase drift or invalidate exact-head evidence.