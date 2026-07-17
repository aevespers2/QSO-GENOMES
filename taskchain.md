# Task Chain

## Repository role

Canonical declarative genomes, immutable ethics, and supervisory Sprite definitions. This repository is an upstream dependency of `QuantumStateObjects` and `QSO-FABRIC` and must not contain executable behavior.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Reconcile canonical PR #2 with current `main` without losing review provenance, exclude the unapproved Socrates identity and repair-authority additions from the current four-genome release scope, freeze one immutable mergeable submitted head, and only then resume exact-head conformance and review disposition.
- **User outcome:** A consuming runtime can retrieve one reviewed Atlas/Nova/Orion/Lyra contract set, verify exact paths, schema versions, immutable ethics, migration, the approved Aequitas identity and references, canonical bytes, complete manifest identity metadata, and hashes, and fail closed without importing repository code or relying on an ambiguous branch or supervisory identity.
- **MVP scope:** preserve PR #2 as the sole review path; integrate current `main` and every intended in-scope candidate remediation without force-rewriting reviewed history; retain Socrates files and their history as non-authoritative follow-on evidence or remove them from the reconciled release candidate, but do not include Socrates, Aequitas compatibility aliases, or repair-pull-request authority in the `0.1.0-alpha.1` compatibility set; record old base, old head, reconciliation method, conflicts, retained and excluded paths, and resulting head; freeze that head; re-enumerate findings; validate the deterministic four-genome and Aequitas contract set; accept or reject the candidate dependency and workflow corrections through exact-head replay; complete adversarial fixtures; disposition review threads; and validate the accepted manifest read-only in `QuantumStateObjects` and `QSO-FABRIC`.
- **Priority:** QSO-GENOMES remains the highest portfolio unblocker. Portfolio priority has not changed. Reconciliation and scope containment remain first because the PR is materially diverged from `main`, and further remediation on a moving head invalidates exact-head evidence. Ahead/behind counts are review snapshots, not durable task identifiers.
- **Success criteria:** PR #2 remains the single review path and becomes mergeable; one frozen reconciled head contains every intended in-scope candidate and governance change; reviewed history is preserved; Socrates, compatibility aliases, and repair authority are absent from the accepted manifest and release artifacts unless separately approved through a versioned migration and security review; the deterministic suite passes at that head; every material finding is resolved or explicitly dispositioned; CI certifies the submitted head; dependencies are reproducible; exact artifacts and source identities are validated; digest scopes are unambiguous; negative fixtures fail closed; and both downstream consumers validate the same accepted commit and identities.
- **Non-goals:** opening a competing release PR; force-pushing or rebasing away review provenance without explicit approval; continuing acceptance-remediation commits on an unfrozen diverged head without an Architect exception; adding Socrates or repair authority to the current alpha candidate; executable agent behavior; network access; credentials; mutation activation; autonomous policy changes; payment authority; runtime implementation; or treating configured workflows, candidate reports, focused tests, or unresolved review findings as accepted release evidence.
- **Release rationale:** QSO-GENOMES is the narrowest upstream contract needed by the runtime repositories. Keeping the first accepted candidate limited to four genomes and the already reviewed Aequitas boundary reduces authority and migration risk while reconciliation restores a stable evidence target.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0a | Reconcile PR #2, contain Socrates scope, and freeze a canonical head | Architect | — | READY | Existing PR #2 remains the sole path; current `main` and all intended in-scope candidate commits are integrated without force-rewriting reviewed history; Socrates, aliases, and repair authority are removed from or explicitly quarantined outside the release candidate; conflicts and retained/excluded changes are documented; the resulting head is mergeable and immutable for review. |
| P0b | Repair and replay the deterministic suite and resolve exact-head findings | QSOBuilder | P0a | BLOCKED | Every intended in-scope remediation is present on the frozen head; dependency and workflow corrections are accepted through exact-head evidence; all current and material outdated findings are fixed or dispositioned; and evidence is tied to the immutable submitted head. |
| P1 | Run independent clean-checkout and CI conformance replay | Architect | P0b | BLOCKED | Supported Python environments install from checked-in instructions; schema, immutable, migration, Aequitas, manifest, canonicalization, duplicate/conflict, overflow, activation-rule, scope-exclusion, and negative tests pass at the exact reviewed head with retained logs and hashes. |
| P2 | Accept and publish the versioned compatibility manifest | Architect | P1 | BLOCKED | One immutable candidate commit and complete manifest identity are approved; source archive, reports, checksums, provenance, rollback notes, scope exclusions, and compatibility status are published without executable or repair authority. |
| P3 | Verify read-only downstream consumption | Builder | P2 | BLOCKED | `QuantumStateObjects` and `QSO-FABRIC` reject missing, stale, mutated, duplicate, conflicting, overflowed, unapproved-supervisor, or incompatible artifacts and accept the exact published version/hash set. |
| P4 | Evaluate Socrates as a separately versioned supervisory migration | Architect | P2 and explicit product/security approval | BLOCKED | A follow-on proposal defines identity migration, alias semantics, authority limits, security review, compatibility impact, tests, and rollback without altering the accepted four-genome alpha. |

## Current repository health and candidate evidence

At the start of this review, GitHub reported PR #2 open and non-mergeable at head `e51a814cd329c55e45a1599b205ef234859e4848`. Comparison against then-current default head `20efbbf2f869b48a921519943580d2b491c686eb` showed the PR 86 commits ahead and 28 commits behind, with merge base `c6c6ccdd61391da5fae5a268022c510069016b33`. Subsequent governance-document commits on `main` intentionally make those counts historical; the Architect must recapture the complete state immediately before reconciliation.

The branch contains candidate corrections for a declared `jsonschema==4.26.0` dependency, cache-key input, exact submitted-head checkout/verification, and validation of both `aequitas.json` and `socrates.json`. These are implemented candidate changes, not accepted capabilities: no exact-head workflow run is attached, mergeability is unresolved, and validating Socrates does not approve it for the current release.

The branch also contains `sprites/socrates.json` and `contracts/socrates-review-binding.json`, including Aequitas compatibility aliases and declarative repair-pull-request authority. They are outside the eleven-artifact manifest and current approved release scope. Product disposition for the first alpha is exclusion/quarantine; inclusion requires a separate versioned migration and explicit approval.

## Cross-repository gate

`QuantumStateObjects` and `QSO-FABRIC` may not claim a verified four-object integration until P0a-P3 are complete and both consumers validate the same accepted commit, manifest version, canonicalization profile, digest scopes, and approved Aequitas identity. Socrates must not become an implicit downstream dependency.

## Builder rules

Do not add unrelated runtime or product scope. Pause additional acceptance-remediation commits until P0a is complete unless the Architect records an explicit exception, rationale, bounded scope, and evidence-preservation plan. Preserve the PR branch, review threads, default-branch governance commits, and excluded Socrates evidence; do not force-push, publish, tag, or claim acceptance. After reconciliation, work only on the highest-priority unresolved acceptance finding and attach every claim to the frozen submitted head.

## Builder log

Record old and new bases/heads, reconciliation method, conflict resolutions, retained and excluded paths, Socrates disposition, review-thread mapping, validation commands/results, Python/tool versions, schema and fixture versions, canonical hashes, workflow URLs, residual risks, downstream replay results, and rollback evidence.

- 2026-07-16 — Advanced P0 from compatibility-set creation to independent acceptance of PR #2 after the candidate added the missing artifacts but remained blocked by integrity, provenance, dependency, workflow, and downstream-verification findings.
- 2026-07-16 — Consolidated the initial remediation lineage onto existing PR #2, preserving the original review path and eliminating a competing-head decision.
- 2026-07-16 — Detected that PR #2 had diverged from `main`, remained non-mergeable, and had no status checks on the observed head. Portfolio priority remained unchanged; provenance-preserving reconciliation became P0a because continuing remediation before reconciliation invalidates exact-head evidence and increases review churn.
- 2026-07-17 — Recorded candidate dependency, cache, submitted-head workflow, and two-Sprite validation changes at PR head `e51a814…`. These narrow several implementation gaps but remain unaccepted until reconciliation and exact-head replay.
- 2026-07-17 — Product scope decision: keep the first alpha limited to the four-genome set and approved Aequitas boundary. Socrates, Aequitas aliases, and repair-pull-request authority are quarantined as a follow-on proposal unless explicit product and security approval authorizes a versioned migration.