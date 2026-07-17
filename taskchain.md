# Task Chain

## Repository role

Canonical declarative genomes, immutable ethics, and supervisory Sprite definitions. This repository is an upstream dependency of `QuantumStateObjects` and `QSO-FABRIC` and must not contain executable behavior.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Resolve and independently replay the remaining findings on the single canonical PR #2 head as the first deterministic four-genome compatibility-set candidate.
- **User outcome:** A consuming runtime can retrieve one reviewed Atlas/Nova/Orion/Lyra contract set, verify exact paths, schema versions, immutable ethics, Aequitas references, canonical bytes, manifest identity metadata, and hashes, and fail closed without importing repository code.
- **MVP scope:** review the canonical PR head; bind the immutable protocol and migration into the compatibility-set identity; resolve conflict/duplicate, digest, and source-identity semantics; declare reproducible dependencies; correct exact-head workflow behavior; complete adversarial fixtures; disposition all review threads; replay from clean checkout or CI; validate the accepted manifest read-only in `QuantumStateObjects` and `QSO-FABRIC`.
- **Priority:** This remains the highest portfolio unblocker. The immediate product priority did not change when the remediation chain was consolidated; the work moved from submission identity repair to exact-head integrity and conformance review.
- **Success criteria:** one canonical PR head contains every claimed remediation; every review finding is resolved or explicitly dispositioned against that exact head; CI certifies the submitted head; dependencies are reproducible; the exact artifact set and every identity-bearing source field are validated; immutable migration and local additions fail closed on conflict or duplication; Aequitas references and surfaces are unique and source-consistent; manifest digests have unambiguous semantics; clean replays produce identical hashes; negative fixtures fail closed; both downstream consumers validate the same accepted commit and digest.
- **Non-goals:** executable agent behavior, network access, credentials, mutation activation, autonomous policy changes, payment authority, runtime implementation, or treating local reports, unresolved review findings, or unverified branch tests as accepted release evidence.
- **Release rationale:** QSO-GENOMES is the narrowest upstream contract needed by the runtime repositories. Accepting one evidence-backed data-only set removes a concrete dependency without granting execution authority or widening the product surface.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Resolve PR #2 integrity, provenance, manifest-identity, dependency, CI, and review findings | QSOBuilder | — | REVIEW | Canonical submitted head contains the remediation lineage; remaining findings are fixed or dispositioned, exact-head checks pass, and evidence is tied to the final immutable head. |
| P1 | Run independent clean-checkout and CI conformance replay | Architect | P0 | BLOCKED | Supported Python environments install from checked-in instructions; schema, immutable, Aequitas, manifest, canonicalization, duplicate/conflict, and negative tests pass at the exact reviewed head with retained logs and hashes. |
| P2 | Accept and publish the versioned compatibility manifest | Architect | P1 | BLOCKED | One immutable candidate commit and complete manifest identity are approved; source archive, reports, checksums, provenance, rollback notes, and compatibility status are published without executable authority. |
| P3 | Verify read-only downstream consumption | Builder | P2 | BLOCKED | `QuantumStateObjects` and `QSO-FABRIC` independently reject missing, stale, mutated, duplicate, conflicting, or incompatible artifacts and accept the exact published version/hash set. |
| P4 | Define a declarative payment-policy extension | Architect | P2 and approved settlement boundary | BLOCKED | Any extension remains data-only, grants no credentials or transfer authority, and has approved versioning and migration rules. |

## Current candidate evidence

PR #2 is the single canonical submission path. Its submitted head includes the exact-set, immutable-migration, Aequitas-integrity, provenance, and documentation remediation lineage. The bounded immutable-manifest binding branch now extends submitted head `2d42c960cefb70fdaada969e75debf50fb06f36c` with an eleven-artifact candidate manifest that includes `protocols/immutable-ethics-v1.json` and `contracts/immutable-ethics-migration-v1.json`. The protocol canonical digest is `ecbab42031461161e91e511ce5f1ba19f1d2d75d81a8351a32f185b181c206af`, the migration digest is `d56994e90dd9d57a65db62b558d4acbd99b8b28ac8b1e124ed48257a9e29fb30`, and the updated path/hash set digest is `6d9b0ca8c6766fbb63b4613df5b2baee455f1e63c848d6f75e56726efbc57cac`. CPython 3.13.5 bytecode compilation and focused deterministic canonical replay passed at implementation/test head `74c7d714a14123f52903178e805a614f2ead1bf1`. These remain candidate evidence, not accepted capability.

The remaining integrity gaps begin with local ethics conflict rejection and duplicate migration-path rejection, followed by duplicate Aequitas review-surface rejection, source-derived manifest identities, digest-scope semantics, dependency and workflow correction, exact-head clean replay, and review-thread disposition. No accepted workflow run is attached to the candidate.

## Cross-repository gate

`QuantumStateObjects` and `QSO-FABRIC` may not claim a verified four-object integration until P0-P3 are complete and both consumers validate the same accepted commit, manifest version, canonicalization profile, and digest.

## Builder rules

Work only on the highest-priority unresolved acceptance finding. Do not add runtime behavior or new product scope while manifest identity, immutable binding, duplicate/conflict validation, dependency, CI, and review semantics remain unresolved. Keep every evidence claim tied to the canonical submitted head and preserve rejected or superseded results for audit.

## Builder Log

Record reviewed commit, reachable provenance, validation commands/results, Python/tool versions, schema and fixture versions, canonical hashes, workflow URLs, review-thread dispositions, residual risks, downstream replay results, and rollback evidence.

- 2026-07-16 — Advanced P0 from compatibility-set creation to independent acceptance of PR #2 after the candidate added the missing artifacts but remained blocked by integrity, provenance, dependency, workflow, and downstream-verification findings.
- 2026-07-16 — Consolidated the fifteen-commit remediation lineage onto existing PR #2, preserving the original review path and eliminating competing-head ambiguity.
- 2026-07-16 — Synchronized the product directive after consolidation. Priority remains unchanged; P0 is still in review because current integrity findings and exact-head workflow acceptance remain unresolved.
- 2026-07-16 — QSOBuilder completed the highest-priority immutable artifact binding on implementation/test head `74c7d714a14123f52903178e805a614f2ead1bf1`, based directly on submitted head `2d42c960cefb70fdaada969e75debf50fb06f36c`. The generator and committed candidate manifest now bind the authoritative immutable protocol and explicit migration as two additional canonical artifacts; a focused test requires both paths and IDs and cross-checks the migration's protocol digest. Bytecode compilation and deterministic canonical replay passed under CPython 3.13.5. P0 remains `REVIEW`; the next unblocked item is local-ethics conflict and duplicate migration-path rejection.
