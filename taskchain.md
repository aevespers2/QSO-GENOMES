# Task Chain

## Repository role

Canonical declarative genomes, immutable ethics, and supervisory Sprite definitions. This repository is an upstream dependency of `QuantumStateObjects` and `QSO-FABRIC` and contains data contracts rather than runtime behavior.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Complete and publish one deterministic four-genome compatibility set.
- **User outcome:** A consuming runtime can validate Atlas, Nova, Orion, and Lyra by schema version, stable path, references, canonical bytes, and hash without importing repository code.
- **MVP scope:** add Atlas; validate all four genomes, immutable ethics, prohibited capabilities, and Aequitas Sprite references; define canonical JSON; publish a machine-readable compatibility manifest; add positive, negative, boundary, unknown-field, unresolved-reference, immutable-mutation, and incompatible-version fixtures.
- **Priority:** Compatibility-set completeness and deterministic validation are the highest portfolio unblocker.
- **Success criteria:** every artifact validates; repeated canonicalization produces identical SHA-256 hashes; immutable and prohibited fields fail closed; consumers can validate fixtures independently; commands, versions, paths, hashes, and provenance are retained.
- **Non-goals:** runtime implementation, external access, credentials, autonomous policy changes, or financial operations.
- **Release rationale:** This contract is required before downstream repositories can claim a verified four-object run.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Complete and validate the four-genome compatibility set | QSOBuilder | — | REVIEW | Atlas, Nova, Orion, and Lyra validate with ethics/Sprite references and required prohibited-capability rules; exact commands and canonical hashes are recorded. Clean-checkout or CI replay is required for acceptance. |
| P1 | Publish the versioned cross-repository genome manifest | QSOBuilder | P0 | PROPOSED | One machine-readable manifest identifies schema versions, paths, references, hashes, canonicalization rules, and compatibility state for independent consumers. |
| P2 | Add mutation, migration, and fail-closed fixtures | Builder | P1 | PROPOSED | Immutable mutations, unknown fields, unresolved references, incompatible versions, and canonicalization drift fail deterministically. |
| P3 | Define a declarative payment-policy extension | Architect | P1 and approved settlement boundary | BLOCKED | Any extension remains data-only and has approved versioning and migration rules. |

## Cross-repository gate

`QuantumStateObjects` and `QSO-FABRIC` may not claim a verified four-object integration until P0 and P1 are complete and their published hashes are consumed successfully.

## Builder Log

- 2026-07-16 — Claimed P0's first unblocked item. Added `genomes/atlas.json`; validated Atlas, Lyra, Nova, and Orion against the Draft 2020-12 schema with `jsonschema 4.26.0`; all four passed. Evidence: `reports/p0-four-genome-schema-validation.md`.
- 2026-07-16 — Completed P0's immutable-contract item. Added `contracts/immutable-baseline.json` and `tests/test_immutable_contracts.py`; five standard-library tests passed. Evidence: `reports/p0-immutable-contract-validation.md`.
- 2026-07-16 — Completed P0's Aequitas reference and external-review item. Added `contracts/aequitas-review-binding.json` and `tests/test_aequitas_review_binding.py`; five standard-library tests passed. Evidence: `reports/p0-aequitas-review-binding-validation.md`.
- 2026-07-16 — Completed P0's deterministic-manifest item. Added `scripts/generate_contract_manifest.py`, `manifests/qso-genomes-compatibility-v1.json`, and six tests. All sixteen tests passed; manifest replay verified nine artifacts and set digest `4ed083cb204a77d1f1878aea8dbf9c61f996541c9b4de83c812bb461530d3eac`. P0 moved to `REVIEW`; P1 remains dependent on clean-checkout or CI acceptance. Evidence: `reports/p0-contract-manifest-validation.md`.
