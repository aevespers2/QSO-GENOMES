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

PR #2 is the single canonical submission path. Its submitted head includes the exact-set, immutable-migration, Aequitas-reference, provenance, documentation, immutable artifact-binding, local-ethics conflict, review-surface uniqueness, and source-derived manifest-identity remediation lineage. The manifest generator now resolves every artifact ID and version from source fields, schema `$id` paths, the immutable protocol `-vN` suffix, or the immutable-baseline path/version convention, and fails closed when source identity drifts from the declared set. CPython 3.13.5 bytecode compilation and five focused positive/negative tests passed with exit code 0 against a standard-library artifact fixture at implementation/test ancestor `76b2c461e226bb18de152da5fba828ec313bad18`. The candidate set digest remains `99f33227247ef39fef3e1c3206c8ea49b9be9af86148298f07bdbf00b0cd6921`. These remain candidate evidence, not accepted capability.

The remaining integrity gaps begin with complete digest-scope semantics, followed by dependency and workflow correction, exact-head clean replay, and review-thread disposition. No accepted workflow run is attached to the candidate.

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
- 2026-07-16 — QSOBuilder completed local-ethics conflict and duplicate migration-path rejection on implementation/test ancestor `a75f23c3e91dea925ee5b97cc265bddb5ec7b1fc`, based directly on canonical PR #2 head `8c65748cfaa9a213d29d7f03d250a3f797bbb1a1`. The migration now binds exact canonical local-ethics list digests and rejects duplicate migration and binding paths before conversion, so all unreviewed additions or mutations fail closed pending a new migration version. CPython 3.13.5 compilation, direct validator replay, and eight focused tests passed against an exact relevant-data fixture mirror. Clean-checkout CI and review acceptance remain open; the next unblocked item is duplicate Aequitas review-surface and conflicting oversight-definition rejection.
- 2026-07-16 — QSOBuilder completed duplicate Aequitas review-surface and conflicting oversight-definition rejection on implementation/test head `6c6ad0b02e83126c24411cc27e129cda8cc58bdc`, based directly on canonical PR #2 head `cacd9dda3d4d9c933c917306374cdde0afdab991`. The standard-library validator rejects duplicate and conflicting surface definitions before de-duplication, duplicate oversight entries within a surface, unknown or disabled Sprite oversight definitions, missing or unexpected surfaces, and incomplete coverage of enabled oversight. CPython 3.13.5 compilation, direct validator replay, and fourteen focused/existing tests passed with exit code 0 against an exact relevant-data fixture mirror. Evidence is recorded in `reports/p0-aequitas-review-surface-integrity-validation.md`. P0 remains `REVIEW`; the next unblocked item is source-derived manifest identity validation, while clean-checkout CI and final review disposition remain open.
- 2026-07-16 — QSOBuilder completed source-derived manifest identity validation on implementation/test ancestor `76b2c461e226bb18de152da5fba828ec313bad18`, descended from canonical PR #2 head `46f3248d8f67b7f0cc734159d2fa0a27e6051ea7`. The generator now derives or verifies all eleven artifact IDs and versions from source fields, schema `$id` paths, the protocol `-vN` suffix, or the immutable-baseline path/version convention, and rejects missing, malformed, duplicate, whitespace-padded, path-inconsistent, or declaration-conflicting identities. CPython 3.13.5 bytecode compilation and five focused tests passed with exit code 0 against a standard-library artifact fixture. Evidence and limitations are recorded in `reports/p0-manifest-source-identity-validation.md`. P0 remains `REVIEW`; the next unblocked item is complete digest-scope semantics, while exact-head CI and review acceptance remain open.
