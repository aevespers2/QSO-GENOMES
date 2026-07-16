# Release Plan

## Current Decision
Status: `BLOCKED`

No genome contract work is currently eligible for release. P0 is only `READY`, every immediate and quality-gate item is unchecked, no canonical hash or validation evidence is recorded, and reviewed commit `5d390ae6f6f4453b4ac44bf8b8d7c34492ad3eb5` has no reported commit-status checks.

## Versioning
- Scheme: Semantic Versioning for the compatibility set and each published contract manifest.
- First eligible candidate: `0.1.0-alpha.1`.
- Canonical data-only corrections that preserve compatibility may be patch releases; new backward-compatible fields or fixtures are minor releases; incompatible schema, immutable-ethics, or Sprite-reference changes require a declared breaking version and migration plan.

## Candidate Scope
- Validated Atlas, Nova, Orion, and Lyra genomes as one compatibility set.
- Validated genome schema, immutable ethics, forbidden-capability requirements, and Aequitas Sprite references.
- Deterministic canonical serialization and hashes.
- Versioned cross-repository contract manifest for `QuantumStateObjects`.
- Negative fixtures proving immutable fields cannot change and incompatible versions fail closed.

## Selected Completed Work
None. The repository role is defined, but no validation, manifest, fixture, or hash evidence is complete.

## Planned Changelog Entries
- `Added`: validated four-genome compatibility set and machine-readable contract manifest.
- `Security`: immutable ethics, forbidden-capability validation, external-review activation rules, and fail-closed version checks.
- `Changed`: explicit schema compatibility and migration policy.
- `Documentation`: exact validation commands, canonicalization rules, hash set, and consumer guidance.

## Acceptance Gates
| Gate | Status | Requirement |
|---|---|---|
| Task completion | FAIL | P0 and P1 are `DONE` with commit and command evidence. |
| Schema validation | NO EVIDENCE | All four genomes and referenced ethics/Sprite data validate. |
| Canonicalization | NO EVIDENCE | Repeated serialization produces identical bytes and hashes. |
| Negative fixtures | NO EVIDENCE | Immutable mutations and incompatible schema versions fail closed. |
| Security/boundaries | NO EVIDENCE | Repository remains declarative; no shell, network, credential, package-install, write, or replication authority exists. |
| Documentation | NO EVIDENCE | Schema, fields, references, compatibility, migration, and exact commands are current. |
| Provenance | NO EVIDENCE | Commit, tool versions, schema/fixture files, commands, canonical hashes, checksums, and attestations recorded. |
| Approval | PENDING | Release approval after all blocking gates pass. |

## Artifact Requirements
- Versioned genome schema and four canonical genome documents.
- Immutable ethics and Aequitas Sprite definitions referenced by stable paths and hashes.
- Machine-readable compatibility manifest.
- Positive and negative fixture bundle with test report.
- Source archive, checksums, SBOM if tooling is packaged, and provenance manifest.

## Rollback Criteria
Rollback if canonical hashes change without an approved version change, immutable fields can be altered, forbidden capabilities are absent or inconsistent, references cannot be resolved, incompatible consumers do not fail closed, or executable authority is introduced. Restore the previous verified contract set and preserve the rejected candidate's manifest and evidence.

## Unresolved Blockers
- P0 validation and P1 manifest work are not complete.
- No canonicalization, schema, fixture, security-boundary, documentation, or provenance evidence is recorded.
- `QuantumStateObjects` remains blocked from claiming a verified multi-object run until P0 and P1 pass.
- Payment-policy genome fields remain excluded pending approved settlement and migration boundaries.
- No CI status is attached to the reviewed commit.

## Release Log
- 2026-07-16: Genome contract candidate evaluated and held `BLOCKED`; no completed work selected.