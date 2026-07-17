# Task Chain

## Repository role

Canonical declarative genomes, immutable ethics, and supervisory Sprite definitions. This repository is an upstream dependency of `QuantumStateObjects` and `QSO-FABRIC` and must not contain executable behavior.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Independently accept or reject PR #2 as the first deterministic four-genome compatibility-set candidate, after consolidating all accepted remediation work onto one canonical submitted head.
- **User outcome:** A consuming runtime can retrieve one reviewed Atlas/Nova/Orion/Lyra contract set, verify exact paths, schema versions, immutable ethics, Aequitas references, canonical bytes, manifest metadata, and hashes, and fail closed without importing repository code.
- **MVP scope:** review the candidate Atlas genome, immutable baseline or approved migration, Aequitas binding, canonicalization profile, manifest, tests, reports, and conformance workflow; consolidate branch-only remediations; resolve integrity and provenance findings; replay from a clean checkout or CI; add remaining fail-closed fixtures; validate the accepted manifest in `QuantumStateObjects` and `QSO-FABRIC` as read-only data.
- **Priority:** This acceptance remains the highest portfolio unblocker. The objective has advanced from creating the missing set to proving that one submitted candidate is complete, reproducible, internally consistent, and safe to consume.
- **Success criteria:** one canonical PR head contains every claimed remediation; all current review findings are resolved or explicitly dispositioned against that exact head; CI checks out and certifies the submitted head; dependencies are declared; the exact required artifact set is asserted; immutable protections match the approved protocol or versioned migration; Aequitas references/invariants are unique and source-consistent; digest semantics cover all identity-bearing metadata or are explicitly scoped; clean replays produce identical canonical hashes; negative fixtures fail closed; downstream consumers validate the same accepted commit and digest.
- **Non-goals:** executable agent behavior, network access, credentials, mutation activation, autonomous policy changes, payment authority, runtime implementation, or treating self-reported or branch-only results as accepted release evidence.
- **Release rationale:** QSO-GENOMES is the narrowest upstream contract needed by the runtime repositories. Accepting one evidence-backed data-only set removes a concrete dependency without granting execution authority or widening the product surface.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Consolidate and resolve PR #2 integrity, provenance, CI, and review findings | QSOBuilder | — | REVIEW | One canonical submitted head includes the approved remediation chain; provenance is reachable; the exact four-genome set, full immutable-policy equivalence or migration, Aequitas integrity, digest semantics, dependencies, PR-head checkout, and all review-thread dispositions are verified against that head. |
| P1 | Run independent clean-checkout and CI conformance replay | Architect | P0 | BLOCKED | Supported Python environments install from checked-in instructions; schema, immutable, Aequitas, manifest, canonicalization, and negative tests pass at the exact reviewed head with retained logs and hashes. |
| P2 | Accept and publish the versioned compatibility manifest | Architect | P1 | BLOCKED | One immutable candidate commit and set digest are approved; source archive, reports, checksums, provenance, rollback notes, and compatibility status are published without executable authority. |
| P3 | Verify read-only downstream consumption | Builder | P2 | BLOCKED | `QuantumStateObjects` and `QSO-FABRIC` independently reject missing, stale, mutated, or incompatible artifacts and accept the exact published version/hash set. |
| P4 | Define a declarative payment-policy extension | Architect | P2 and approved settlement boundary | BLOCKED | Any extension remains data-only, grants no credentials or transfer authority, and has approved versioning and migration rules. |

## Current candidate evidence

PR #2 head `5a435807487fd713c87465f3d23aaf9cd7cdd2b4` reports Atlas plus a nine-artifact candidate manifest, deterministic canonicalization, immutable and Aequitas tests, sixteen passing tests, and set digest `4ed083cb204a77d1f1878aea8dbf9c61f996541c9b4de83c812bb461530d3eac`. These are candidate claims, not accepted capabilities.

The review timeline contains fifteen threads: four earlier provenance threads are resolved and outdated, while eleven remain unresolved, including one outdated release-sync thread and ten current integrity/workflow findings. No accepted exact-head CI or downstream-consumer evidence has been established.

## Candidate consolidation gate

The latest documented remediation head, `8c3d4ad3a8fc8cae864586d873cca319225c3e1d`, is fifteen commits ahead of PR #2 head and zero commits behind. It contains branch-only work for exact genome-set enforcement, a versioned immutable-ethics migration, and Aequitas reference/invariant validation, but PR #2 has not been advanced to that state. Those changes are useful candidate evidence; they are not yet the reviewed submission and cannot close PR-head findings or unlock P1.

**Directive:** before starting another acceptance finding, select one canonical submission path: advance PR #2 to the consolidated remediation head, or open a replacement PR that clearly supersedes PR #2 while preserving review provenance. Re-run review-thread, workflow, manifest, and provenance checks against that exact submitted head. Do not mark release gates complete from side-branch commits alone.

## Cross-repository gate

`QuantumStateObjects` and `QSO-FABRIC` may not claim a verified four-object integration until P0-P3 are complete and both consumers validate the same accepted commit, manifest version, canonicalization profile, and digest.

## Builder rules

Work only on the highest-priority unresolved acceptance finding after the current remediation chain is consolidated. Do not add runtime behavior or new product scope while the candidate's submission identity, provenance, immutable-policy equivalence, manifest identity, dependency, and CI semantics remain unresolved. Do not create additional remediation branches unless the canonical submission path and ancestry are recorded first.

## Builder Log

Record reviewed commit, reachable provenance, validation commands/results, Python/tool versions, schema and fixture versions, canonical hashes, workflow URLs, unresolved review threads, residual risks, downstream replay results, and rollback evidence.

- 2026-07-16 — Advanced P0 from compatibility-set creation to independent acceptance of PR #2 after the candidate added the missing artifacts but remained blocked by unresolved integrity, provenance, dependency, workflow, and downstream-verification findings.
- 2026-07-16 — Synchronized review progress: four prior provenance threads are resolved/outdated, eleven threads remain unresolved, and the replacement submitted-state provenance still references a source state not reachable from the reviewed candidate. Priority remains unchanged.
- 2026-07-16 — Added a consolidation gate after exact-set, immutable-migration, and Aequitas-integrity remediations accumulated on a fifteen-commit side chain while PR #2 remained at its earlier head. Portfolio priority is unchanged; the immediate P0 directive is now to establish one canonical review head before further acceptance work.