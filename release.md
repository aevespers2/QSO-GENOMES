# Release Plan

## Current Decision
Status: `BLOCKED — INCOMPLETE COMPATIBILITY SET`

No genome contract is eligible for release. The repository defines the genome and Sprite schemas, three genome documents (`Nova`, `Orion`, and `Lyra`), immutable/attribution ethics protocols, and the Aequitas Sprite, but the declared four-genome set is incomplete because `genomes/atlas.json` is absent. P0 remains `READY`, every punch-list item is unchecked, no validation tooling or CI workflow is present, and no canonical hash, compatibility manifest, fixture, security-boundary report, or provenance bundle is attached to reviewed head `42df94d9f9810ac68f69a9f042bc74c60471b023`.

## Versioning
- Scheme: Semantic Versioning for the compatibility set and each published contract manifest.
- First eligible candidate: `0.1.0-alpha.1`.
- Canonical data corrections that preserve declared compatibility may be patch releases.
- New backward-compatible fields, genomes, or fixtures are minor changes.
- Incompatible schema, immutable-ethics, forbidden-capability, canonicalization, or Sprite-reference changes require a declared breaking version and migration fixtures.

## Candidate Scope
- Complete Atlas, Nova, Orion, and Lyra genome documents as one compatibility set.
- Genome schema, Sprite schema, immutable ethics, attribution ethics, forbidden-capability requirements, and Aequitas references.
- Deterministic canonical serialization and SHA-256 hashes.
- Machine-readable cross-repository contract manifest for `QuantumStateObjects`.
- Positive and negative fixtures covering required fields, immutable mutation, unresolved references, unknown fields, incompatible versions, and canonicalization stability.
- Reproducible validation, documentation, security-boundary review, checksums, and provenance.

## Existing Candidate Assets
- `schema/qso-genome.schema.json` and `schema/qso-sprite.schema.json` exist.
- `genomes/nova.json`, `genomes/orion.json`, and `genomes/lyra.json` exist.
- Immutable and attribution ethics protocols and `sprites/aequitas.json` exist.
- Repository documentation clearly declares a data-only, non-executing boundary.

These files are candidate inputs, not a releasable compatibility set until Atlas is added and the complete set passes deterministic validation.

## Selected Completed Work
None. The declared four-genome set is incomplete, and no accepted task or reproducible validation evidence establishes a release candidate.

## Planned Changelog Entries
- `Added`: complete validated four-genome compatibility set and machine-readable contract manifest.
- `Security`: immutable ethics, forbidden-capability validation, external-review activation rules, data-only boundary checks, and fail-closed version/reference handling.
- `Changed`: explicit canonicalization, compatibility, and migration policy.
- `Fixed`: schema/reference inconsistencies and missing Atlas definition found during baseline validation.
- `Documentation`: exact validation commands, canonicalization rules, hash set, fields, references, limitations, and consumer guidance.
- `Release`: fixture bundle, reports, checksums, provenance, and approval decision.

## Acceptance Gates
| Gate | Status | Requirement |
|---|---|---|
| Compatibility-set completeness | FAIL | `genomes/atlas.json`, Nova, Orion, and Lyra all exist and are included in one manifest. |
| Task completion | FAIL | P0 and P1 are `DONE` with commit, command, and hash evidence. |
| Schema/reference validation | NO EVIDENCE | All genomes, ethics protocols, Sprite data, and cross-file references validate. |
| Canonicalization | NO EVIDENCE | Repeated serialization produces identical bytes and hashes across supported environments. |
| Negative fixtures | NO EVIDENCE | Immutable mutations, unknown fields, unresolved references, and incompatible versions fail closed. |
| Security/boundaries | PARTIAL | Files are declarative; automated checks must prove no executable authority or prohibited capability is introduced. |
| Documentation | PARTIAL | Role and principles exist; schema/field/reference, canonicalization, compatibility, migration, and exact-command guidance require verification. |
| Provenance | NO EVIDENCE | Candidate commit, tool versions, schema/fixture paths, commands, canonical hashes, checksums, SBOM if tooling is packaged, and attestations recorded. |
| Approval | PENDING | Explicit release approval after all blocking gates pass. |

## Artifact Requirements
- Versioned genome and Sprite schemas.
- Four canonical genome documents, immutable/attribution ethics protocols, and Aequitas definition.
- Machine-readable compatibility manifest with stable paths, schema versions, references, and hashes.
- Positive/negative fixture bundle and deterministic validation report.
- Source archive, validation tooling if added, security-boundary report, SHA-256 checksums, SBOM where applicable, and provenance manifest.

## Rollback Criteria
Rollback if any declared genome is missing, canonical hashes change without an approved version change, immutable fields can be altered, forbidden capabilities are absent or inconsistent, references cannot be resolved, incompatible consumers do not fail closed, or executable authority is introduced. Restore the previous verified contract set and preserve the rejected candidate's manifest, fixtures, hashes, and reports.

## Unresolved Blockers
- `genomes/atlas.json` is missing although README, taskchain, and `QuantumStateObjects/config/instances.json` declare Atlas as part of the four-object set.
- P0 validation and P1 manifest work are incomplete; every punch-list item is unchecked.
- No validator, CI workflow, canonicalization implementation, deterministic hash set, positive/negative fixtures, compatibility report, or provenance evidence is recorded.
- `QuantumStateObjects` remains blocked from a verified multi-object run and currently references the missing Atlas path.
- Payment-policy genome fields remain excluded pending approved settlement and migration boundaries.

## Release Log
- 2026-07-16: Recorded the incomplete compatibility set and missing Atlas genome; candidate remains `BLOCKED — INCOMPLETE COMPATIBILITY SET`.