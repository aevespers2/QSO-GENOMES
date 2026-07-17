# Task Chain

## Repository role

Canonical declarative genomes, immutable ethics, and supervisory Sprite definitions. This repository is an upstream dependency of `QuantumStateObjects` and `QSO-FABRIC` and must not contain executable behavior.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Independently accept or reject PR #2 as the first deterministic four-genome compatibility-set candidate.
- **User outcome:** A consuming runtime can retrieve one reviewed Atlas/Nova/Orion/Lyra contract set, verify exact paths, schema versions, immutable ethics, Aequitas references, canonical bytes, manifest metadata, and hashes, and fail closed without importing repository code.
- **MVP scope:** review the candidate Atlas genome, immutable baseline, Aequitas binding, canonicalization profile, nine-artifact manifest, tests, reports, and conformance workflow; resolve integrity and provenance findings; replay from a clean checkout or CI; add remaining fail-closed fixtures; validate the accepted manifest in `QuantumStateObjects` and `QSO-FABRIC` as read-only data.
- **Priority:** This acceptance remains the highest portfolio unblocker. The objective has advanced from creating the missing set to proving that the submitted candidate is complete, reproducible, internally consistent, and safe to consume.
- **Success criteria:** all current review findings are resolved or explicitly dispositioned; CI checks out and certifies the submitted PR head; dependencies are declared; the exact required artifact set is asserted; immutable protections bind the approved protocol through an accepted versioned migration; Aequitas references/invariants are unique and source-consistent; digest semantics cover all identity-bearing metadata or are explicitly scoped; clean replays produce identical canonical hashes; negative fixtures fail closed; downstream consumers validate the same accepted commit and digest.
- **Non-goals:** executable agent behavior, network access, credentials, mutation activation, autonomous policy changes, payment authority, runtime implementation, or treating self-reported PR results as accepted release evidence.
- **Release rationale:** QSO-GENOMES is the narrowest upstream contract needed by the runtime repositories. Accepting one evidence-backed data-only set removes a concrete dependency without granting execution authority or widening the product surface.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Resolve PR #2 integrity, provenance, and CI review findings | QSOBuilder | — | IN PROGRESS | Reachable submitted-state provenance, exact four-genome artifact-set assertion, and an explicit full immutable-protocol migration are complete; Aequitas invariant/reference validation, unambiguous digest semantics, declared dependencies, PR-head checkout, and review-thread disposition remain. |
| P1 | Run independent clean-checkout and CI conformance replay | Architect | P0 | BLOCKED | Supported Python environments install from checked-in instructions; schema, immutable, Aequitas, manifest, canonicalization, and negative tests pass at the exact reviewed head with retained logs and hashes. |
| P2 | Accept and publish the versioned compatibility manifest | Architect | P1 | BLOCKED | One immutable candidate commit and set digest are approved; source archive, reports, checksums, provenance, rollback notes, and compatibility status are published without executable authority. |
| P3 | Verify read-only downstream consumption | Builder | P2 | BLOCKED | `QuantumStateObjects` and `QSO-FABRIC` independently reject missing, stale, mutated, or incompatible artifacts and accept the exact published version/hash set. |
| P4 | Define a declarative payment-policy extension | Architect | P2 and approved settlement boundary | BLOCKED | Any extension remains data-only, grants no credentials or transfer authority, and has approved versioning and migration rules. |

## Current candidate evidence

PR #2 reports Atlas plus a nine-artifact candidate manifest, deterministic canonicalization, immutable and Aequitas tests, sixteen passing tests, and set digest `4ed083cb204a77d1f1878aea8dbf9c61f996541c9b4de83c812bb461530d3eac`. The exact schema-bound genome directory is asserted as Atlas, Lyra, Nova, and Orion. Builder branch evidence now adds explicit migration `QSO-GENOME-IMMUTABLE-ETHICS-MIGRATION-v1`, binding the authoritative full protocol digest `ecbab42031461161e91e511ce5f1ba19f1d2d75d81a8351a32f185b181c206af` and requiring fail-closed validation, additive-only local ethics, human review, and a new protocol ID plus migration version for changes. Four exact-set tests and five migration tests passed in focused replays. These remain candidate claims, not accepted capabilities: clean-checkout/CI acceptance, manifest inclusion, downstream enforcement, and remaining review findings stay open.

## Cross-repository gate

`QuantumStateObjects` and `QSO-FABRIC` may not claim a verified four-object integration until P0-P3 are complete and both consumers validate the same accepted commit, manifest version, canonicalization profile, and digest.

## Builder rules

Work only on the highest-priority unresolved acceptance finding. Do not add runtime behavior or new product scope while the candidate's Aequitas integrity, manifest identity, dependency, and CI semantics remain unresolved.

## Builder Log

Record reviewed commit, reachable provenance, validation commands/results, Python/tool versions, schema and fixture versions, canonical hashes, workflow URLs, unresolved review threads, residual risks, downstream replay results, and rollback evidence.

- 2026-07-16 — Advanced P0 from compatibility-set creation to independent acceptance of PR #2 after the candidate added the missing artifacts but remained blocked by unresolved integrity, provenance, dependency, workflow, and downstream-verification findings.
- 2026-07-16 — QSOBuilder completed the first P0 acceptance finding by replacing branch-local intermediate commit pointers with reachable submitted source state `9de3db6a33308346d09b7004e6702e997dce9ba8` and exact file hashes in `reports/submitted-state-provenance.md` plus all four P0 validation reports. P0 remains `IN PROGRESS`; the next unblocked item is exact four-genome artifact-set assertion.
- 2026-07-16 — QSOBuilder completed the exact four-genome artifact-set assertion on reachable implementation/test ancestor `28f419e60dd16a1cc482076f6dc3e3e56bf2ab79`. Schema validation now rejects missing or additional JSON genome artifacts before document validation; four focused tests and bytecode compilation passed under CPython 3.13.5 with `jsonschema` 4.26.0. Evidence is recorded in `reports/p0-exact-genome-artifact-set-validation.md`. P0 remains `IN PROGRESS`; the next unblocked finding is immutable-protocol equivalence or a versioned migration.
- 2026-07-16 — QSOBuilder completed the immutable-policy finding on reachable implementation/test ancestor `257839316082faf2a3ab115a65fb1550b74ecc06`. `contracts/immutable-ethics-migration-v1.json` explicitly migrates all four genome paths from local schema-v1 ethics text to authoritative `QSO-IMMUTABLE-ETHICS-v1`, binds QSO Canonical JSON v1 digest `ecbab42031461161e91e511ce5f1ba19f1d2d75d81a8351a32f185b181c206af`, and requires fail-closed path/ID/status/hash validation, verbatim full-protocol retention, additive-only local ethics, human review, and new protocol plus migration versions for changes. Five focused standard-library tests passed under CPython 3.13.5; evidence is recorded in `reports/p0-immutable-ethics-migration-validation.md`. P0 remains `IN PROGRESS`; the next unblocked finding is Aequitas invariant and reference validation before de-duplication.
