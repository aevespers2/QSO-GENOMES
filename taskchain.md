# Task Chain

## Repository role

Canonical declarative genomes, immutable ethics, and supervisory Sprite definitions. This repository is an upstream dependency of `QuantumStateObjects` and `QSO-FABRIC` and must not contain executable behavior.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Complete and publish one deterministic four-genome compatibility set.
- **User outcome:** A consuming runtime can validate Atlas, Nova, Orion, and Lyra by schema version, stable path, references, canonical bytes, and hash without importing repository code.
- **MVP scope:** add the missing Atlas genome; validate all four genomes, immutable/attribution ethics, forbidden capabilities, and Aequitas Sprite; define canonical JSON; publish a machine-readable compatibility manifest; add positive, negative, boundary, unknown-field, unresolved-reference, immutable-mutation, and incompatible-version fixtures.
- **Priority:** Compatibility-set completeness and deterministic validation are the highest portfolio unblocker.
- **Success criteria:** every artifact validates; repeated canonicalization produces identical SHA-256 hashes; immutable and prohibited fields fail closed; consumers can validate fixtures independently; all commands, versions, paths, hashes, and provenance are retained.
- **Non-goals:** executable agent behavior, network access, credentials, mutation activation, autonomous policy changes, payment authority, or runtime implementation.
- **Release rationale:** This contract is required before QuantumStateObjects or QSO-FABRIC can claim a verified four-object run. A small data-only release removes the most concrete upstream blocker with minimal execution risk.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Complete and validate the four-genome compatibility set | QSOBuilder | — | IN PROGRESS | Atlas, Nova, Orion, and Lyra validate with ethics/Sprite references and required forbidden-capability rules; exact commands and canonical hashes are recorded. |
| P1 | Publish the versioned cross-repository genome manifest | QSOBuilder | P0 | PROPOSED | One machine-readable manifest identifies schema versions, paths, references, hashes, canonicalization rules, and compatibility state for independent consumers. |
| P2 | Add mutation, migration, and fail-closed fixtures | Builder | P1 | PROPOSED | Immutable mutations, unknown fields, unresolved references, incompatible versions, and canonicalization drift fail deterministically. |
| P3 | Define a declarative payment-policy extension | Architect | P1 and approved settlement boundary | BLOCKED | Any extension remains data-only, grants no credentials or transfer authority, and has approved versioning and migration rules. |

## Cross-repository gate

`QuantumStateObjects` and `QSO-FABRIC` may not claim a verified four-object integration until P0 and P1 are complete and their published hashes are consumed successfully.

## Builder Log

- 2026-07-16 — Claimed P0's first unblocked item. Added `genomes/atlas.json`; validated Atlas, Lyra, Nova, and Orion against the Draft 2020-12 schema with `jsonschema 4.26.0`; all four passed. Evidence: `reports/p0-four-genome-schema-validation.md`. Remaining P0 work: immutable-ethics/forbidden-capability equivalence, Aequitas Sprite references, and canonical hash recording.
- 2026-07-16 — Completed P0's immutable-contract item. Added `contracts/immutable-baseline.json` and `tests/test_immutable_contracts.py`; five standard-library tests passed for the exact four-genome set, shared ethics slots, approved ethics variants, ordered forbidden capabilities, identity, safety priority, uniqueness, and immutable object shape. Evidence: `reports/p0-immutable-contract-validation.md`. Remaining P0 work: Aequitas Sprite references/external-review rules and canonical hash recording.
