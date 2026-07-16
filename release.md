# Release Plan

## Current Decision

Status: `BLOCKED — CANDIDATE IN REVIEW; INDEPENDENT ACCEPTANCE INCOMPLETE`

PR #2 materially addresses the missing-Atlas and candidate-manifest blockers by adding Atlas, an immutable baseline, an Aequitas external-review binding, deterministic canonicalization, a nine-artifact compatibility manifest, tests, and validation reports. The branch reports sixteen passing tests and compatibility-set digest `4ed083cb204a77d1f1878aea8dbf9c61f996541c9b4de83c812bb461530d3eac`, but the evidence was replayed in a repository-shaped tree rather than a direct clean checkout, no GitHub status checks are attached, required adversarial/migration fixtures remain incomplete, and no release approval is recorded.

The candidate is reviewable but not publishable. Downstream repositories remain blocked from claiming a verified four-object integration.

## Versioning

- Scheme: Semantic Versioning for the compatibility set and machine-readable manifest.
- First eligible candidate: `0.1.0-alpha.1` after independent acceptance.
- Compatible data corrections may be patches; compatible fields, genomes, or fixtures are minor changes.
- Schema, immutable-ethics, prohibited-capability, canonicalization, or reference breaks require a declared major/breaking version and migration fixtures.

## Release Scope

- Canonical Atlas, Nova, Orion, and Lyra genome documents.
- Genome/Sprite schemas, immutable ethics, prohibited-capability rules, and Aequitas review binding.
- Deterministic canonical JSON and SHA-256 hashes.
- Machine-readable manifest containing schema versions, stable paths, references, canonical byte counts, hashes, canonicalization, and compatibility state.
- Positive, negative, boundary, unknown-field, unresolved-reference, immutable-mutation, incompatible-version, duplicate-key, non-finite-number, canonicalization-drift, and migration fixtures.
- One independent downstream consumer validation fixture.

## Selected Candidate Work

The following work is selected for review, not release:

- `genomes/atlas.json` and schema validation of Atlas, Lyra, Nova, and Orion.
- `contracts/immutable-baseline.json` and immutable-contract tests.
- `contracts/aequitas-review-binding.json` and external-review boundary tests.
- `scripts/generate_contract_manifest.py` and `manifests/qso-genomes-compatibility-v1.json`.
- Candidate validation reports under `reports/`.

No item is accepted as `DONE` until independent replay and the remaining release gates pass.

## Planned Changelog Entries

- `Added`: complete four-genome set, compatibility manifest, validator, conformance fixtures, and downstream consumer fixture.
- `Security`: immutable ethics, prohibited capabilities, fail-closed references/versions/canonicalization, and data-only boundary checks.
- `Changed`: canonicalization, compatibility, acceptance, and migration policy.
- `Fixed`: missing Atlas and any schema/reference defects found during independent validation.
- `Release`: CI or clean-checkout reports, source artifact, checksums, provenance, rollback evidence, and approval.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Set completeness | CANDIDATE PASS | PR #2 contains Atlas, Nova, Orion, and Lyra and lists nine artifacts in one candidate manifest; independent verification is pending. |
| Task completion | REVIEW | Candidate construction is in review; independent conformance acceptance and publication are not `DONE`. |
| Schema/references | CANDIDATE PASS | Branch evidence reports all four genomes and declared references passing; replay from a clean checkout or CI is required. |
| Canonicalization | CANDIDATE PASS | Branch evidence reports deterministic replay and the recorded set digest; cross-environment replay is required. |
| Negative/boundary fixtures | FAIL | Unknown-field, unresolved-reference, immutable-mutation, incompatible-version, duplicate-key, non-finite-number, canonicalization-drift, and migration coverage is incomplete. |
| Security/boundary | PARTIAL | Candidate is declarative and tests selected non-executing boundaries; a complete automated data-only authority check is still required. |
| Downstream consumption | NO EVIDENCE | QuantumStateObjects or QSO-FABRIC has not independently validated the exact accepted set by schema version, path, reference, canonical bytes, and hash. |
| Documentation | PARTIAL | Candidate reports exist; clean setup, validation, compatibility, migration, and consumer instructions require verification. |
| Provenance | PARTIAL | Candidate commits, commands, and hashes are recorded; workflow URLs, clean environment evidence, release checksums, and attestations are missing. |
| Approval | PENDING | Explicit release approval may be recorded only after all blocking gates pass. |

## Artifact Requirements

- Versioned schemas, four canonical genomes, ethics baseline, and Aequitas binding.
- Accepted machine-readable compatibility manifest with stable paths, references, schema versions, canonical byte counts, artifact hashes, and one set digest.
- Validator plus positive/negative/boundary/migration fixture bundle and deterministic report.
- Independent consumer validation report.
- Source archive, security-boundary report, SBOM where applicable, SHA-256 checksums, provenance manifest, and rollback instructions.

## Rollback Criteria

Rollback if any genome is missing, hashes change without approved versioning, immutable fields can be altered, prohibited capabilities are absent or inconsistent, references fail, incompatible consumers do not fail closed, canonicalization is ambiguous, or executable authority is introduced. Restore the previous verified contract set and preserve rejected manifests, fixtures, hashes, reports, and review findings.

## Unresolved Blockers

- No clean-checkout or GitHub Actions replay is attached to the current PR head.
- Required adversarial, boundary, canonicalization-drift, and migration fixtures are incomplete.
- No independent downstream consumer validation exists.
- Security-boundary, release provenance, checksums, and explicit approval remain incomplete.
- QuantumStateObjects and QSO-FABRIC cannot claim a verified four-object integration until the manifest is accepted, published, and consumed successfully.

## Release Log

- 2026-07-16: Confirmed the complete four-genome contract as the highest-priority portfolio unblocker; release was blocked by missing Atlas and validation evidence.
- 2026-07-16: PR #2 supplied a reviewable candidate and branch-local validation evidence. Release remains blocked pending independent replay, fail-closed fixtures, downstream consumption, provenance, and approval.