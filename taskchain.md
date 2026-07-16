# Task Chain

## Repository role

Canonical declarative genomes, immutable ethics, and supervisory Sprite definitions. This repository is an upstream dependency of `QuantumStateObjects` and `QSO-FABRIC` and must not contain executable behavior.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Independently accept or reject PR #2 as the first deterministic four-genome compatibility-set candidate.
- **User outcome:** A consuming runtime can retrieve one reviewed Atlas/Nova/Orion/Lyra contract set, verify exact paths, schema versions, immutable ethics, Aequitas references, canonical bytes, manifest metadata, and hashes, and fail closed without importing repository code.
- **MVP scope:** review the candidate Atlas genome, immutable baseline, Aequitas binding, canonicalization profile, nine-artifact manifest, tests, reports, and conformance workflow; resolve integrity and provenance findings; replay from a clean checkout or CI; add remaining fail-closed fixtures; validate the accepted manifest in `QuantumStateObjects` and `QSO-FABRIC` as read-only data.
- **Priority:** This acceptance remains the highest portfolio unblocker. The objective has advanced from creating the missing set to proving that the submitted candidate is complete, reproducible, internally consistent, and safe to consume.
- **Success criteria:** all current review findings are resolved or explicitly dispositioned; CI checks out and certifies the submitted PR head; dependencies are declared; the exact required artifact set is asserted; immutable protections match the approved protocol; Aequitas references/invariants are unique and source-consistent; digest semantics cover all identity-bearing metadata or are explicitly scoped; clean replays produce identical canonical hashes; negative fixtures fail closed; downstream consumers validate the same accepted commit and digest.
- **Non-goals:** executable agent behavior, network access, credentials, mutation activation, autonomous policy changes, payment authority, runtime implementation, or treating self-reported PR results as accepted release evidence.
- **Release rationale:** QSO-GENOMES is the narrowest upstream contract needed by the runtime repositories. Accepting one evidence-backed data-only set removes a concrete dependency without granting execution authority or widening the product surface.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Resolve PR #2 integrity, provenance, and CI review findings | QSOBuilder | — | IN PROGRESS | Reachable submitted-state provenance is complete; exact four-genome assertion, full immutable-protocol equivalence, Aequitas invariant/reference validation, unambiguous digest semantics, declared dependencies, PR-head checkout, and review-thread disposition remain. |
| P1 | Run independent clean-checkout and CI conformance replay | Architect | P0 | BLOCKED | Supported Python environments install from checked-in instructions; schema, immutable, Aequitas, manifest, canonicalization, and negative tests pass at the exact reviewed head with retained logs and hashes. |
| P2 | Accept and publish the versioned compatibility manifest | Architect | P1 | BLOCKED | One immutable candidate commit and set digest are approved; source archive, reports, checksums, provenance, rollback notes, and compatibility status are published without executable authority. |
| P3 | Verify read-only downstream consumption | Builder | P2 | BLOCKED | `QuantumStateObjects` and `QSO-FABRIC` independently reject missing, stale, mutated, or incompatible artifacts and accept the exact published version/hash set. |
| P4 | Define a declarative payment-policy extension | Architect | P2 and approved settlement boundary | BLOCKED | Any extension remains data-only, grants no credentials or transfer authority, and has approved versioning and migration rules. |

## Current candidate evidence

PR #2 reports Atlas plus a nine-artifact candidate manifest, deterministic canonicalization, immutable and Aequitas tests, sixteen passing tests, and set digest `4ed083cb204a77d1f1878aea8dbf9c61f996541c9b4de83c812bb461530d3eac`. These are candidate claims, not accepted capabilities: the head has no attached status checks or workflow runs, and review findings remain open.

## Cross-repository gate

`QuantumStateObjects` and `QSO-FABRIC` may not claim a verified four-object integration until P0-P3 are complete and both consumers validate the same accepted commit, manifest version, canonicalization profile, and digest.

## Builder rules

Work only on the highest-priority unresolved acceptance finding. Do not add runtime behavior or new product scope while the candidate's provenance, immutable-policy equivalence, manifest identity, dependency, and CI semantics remain unresolved.

## Builder Log

Record reviewed commit, reachable provenance, validation commands/results, Python/tool versions, schema and fixture versions, canonical hashes, workflow URLs, unresolved review threads, residual risks, downstream replay results, and rollback evidence.

- 2026-07-16 — Advanced P0 from compatibility-set creation to independent acceptance of PR #2 after the candidate added the missing artifacts but remained blocked by unresolved integrity, provenance, dependency, workflow, and downstream-verification findings.
- 2026-07-16 — QSOBuilder completed the first P0 acceptance finding by replacing branch-local intermediate commit pointers with reachable submitted source state `9de3db6a33308346d09b7004e6702e997dce9ba8` and exact file hashes in `reports/submitted-state-provenance.md` plus all four P0 validation reports. P0 remains `IN PROGRESS`; the next unblocked item is exact four-genome artifact-set assertion.
