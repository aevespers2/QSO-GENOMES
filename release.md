# Release Plan

## Current Decision

Status: `BLOCKED — MISSING ATLAS AND VALIDATION EVIDENCE`

QSO-GENOMES is the portfolio's declarative genome and ethics-contract repository, but no contract release is eligible. Nova, Orion, Lyra, schemas, ethics protocols, and Aequitas exist; `genomes/atlas.json` is still missing, P0 remains `READY`, all punch-list items are unchecked, and candidate head `c6c6ccdd61391da5fae5a268022c510069016b33` lacks validation tooling, CI, canonical hashes, a compatibility manifest, negative fixtures, security-boundary evidence, provenance, and rollback artifacts.

## Versioning

- Scheme: Semantic Versioning for the compatibility set and machine-readable manifest.
- First eligible candidate: `0.1.0-alpha.1`.
- Compatible data corrections may be patches; compatible fields/genomes/fixtures are minor changes.
- Schema, immutable-ethics, forbidden-capability, canonicalization, or reference breaks require a declared major/breaking version and migration fixtures.

## Release Scope

- Canonical Atlas, Nova, Orion, and Lyra genome documents.
- Genome/Sprite schemas, immutable and attribution ethics, forbidden-capability rules, and Aequitas references.
- Deterministic canonical JSON and SHA-256 hashes.
- Machine-readable manifest containing schema versions, stable paths, references, hashes, canonicalization, and compatibility state.
- Positive, negative, boundary, unknown-field, unresolved-reference, immutable-mutation, incompatible-version, and migration fixtures.

## Selected Completed Work

None selected. Existing declarative assets are candidate inputs, but the declared four-genome set is incomplete and no accepted deterministic validation evidence exists.

## Planned Changelog Entries

- `Added`: complete four-genome set, compatibility manifest, validator, and conformance fixtures.
- `Security`: immutable ethics, forbidden capabilities, fail-closed references/versions, and data-only boundary checks.
- `Changed`: canonicalization, compatibility, and migration policy.
- `Fixed`: missing Atlas and any schema/reference defects found during validation.
- `Release`: validation reports, source artifact, checksums, provenance, and approval.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Set completeness | FAIL | Atlas, Nova, Orion, and Lyra exist and are listed in one manifest. |
| Task completion | FAIL | P0 and P1 are `DONE` with commits, commands, and hashes. |
| Schema/references | NO EVIDENCE | All genomes, protocols, Sprite data, and cross-file references validate. |
| Canonicalization | NO EVIDENCE | Repeated serialization yields identical bytes and hashes across supported environments. |
| Negative fixtures | NO EVIDENCE | Immutable mutation, unknown fields, unresolved references, and incompatible versions fail closed. |
| Security/boundary | PARTIAL | Assets are declarative; automated checks prove no executable authority or prohibited capability. |
| Documentation | PARTIAL | Role is documented; exact fields, references, canonicalization, compatibility, migration, and commands are unverified. |
| Provenance | NO EVIDENCE | Candidate commit, tools, paths, commands, hashes, artifacts, checksums, and attestations are retained. |
| Approval | PENDING | Explicit release approval after all blocking gates pass. |

## Artifact Requirements

- Versioned schemas, four canonical genomes, ethics protocols, and Aequitas definition.
- Machine-readable compatibility manifest with stable paths, references, schema versions, and hashes.
- Validator plus positive/negative/boundary/migration fixture bundle and deterministic report.
- Source archive, security-boundary report, SBOM where applicable, SHA-256 checksums, provenance, and rollback instructions.

## Rollback Criteria

Rollback if any genome is missing, hashes change without approved versioning, immutable fields can be altered, forbidden capabilities are absent/inconsistent, references fail, incompatible consumers do not fail closed, or executable authority is introduced. Restore the previous verified contract set and preserve rejected manifests, fixtures, hashes, and reports.

## Unresolved Blockers

- `genomes/atlas.json` is missing despite being declared by portfolio consumers.
- P0 validation and P1 manifest work are incomplete; punch-list evidence is absent.
- No validator, CI workflow, canonicalization implementation, deterministic hash set, conformance fixtures, security report, provenance, or rollback artifact exists.
- QuantumStateObjects and QSO-FABRIC cannot claim a verified four-object integration until this contract set is published and consumed successfully.

## Release Log

- 2026-07-16: Confirmed the complete four-genome contract as the highest-priority portfolio unblocker; release remains blocked by missing Atlas and validation evidence.