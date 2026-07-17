# Release Plan

## Current Decision

Status: `BLOCKED — EXACT-HEAD REVIEW AND CONFORMANCE EVIDENCE REQUIRED`

QSO-GENOMES remains the portfolio's highest-priority declarative contract dependency. PR #2 is the single canonical submission path. The prior fifteen-commit remediation lineage was fast-forwarded onto that branch, resolving the competing-head decision without promoting the candidate.

The review timeline contains twenty threads: four resolved/outdated, one unresolved/outdated release-sync thread, and fifteen current unresolved findings. No GitHub Actions workflow run is attached to the current head. Candidate reports and focused local tests are preserved as implementation evidence, not independent release verification.

## Versioning

- Scheme: Semantic Versioning for the compatibility set and machine-readable manifest.
- First eligible candidate: `0.1.0-alpha.1`.
- Compatible data corrections may be patches; compatible fields, genomes, or fixtures are minor changes.
- Schema, immutable-ethics, forbidden-capability, canonicalization, manifest-identity, or reference breaks require a declared major/breaking version and migration fixtures.
- Digest names and scopes must distinguish artifact-byte identity from full compatibility-manifest identity.
- No version or tag may be assigned until every release artifact is generated and independently replayed from one immutable accepted head.

## Release Scope

- Canonical Atlas, Nova, Orion, and Lyra genome documents.
- Genome/Sprite schemas, authoritative immutable-ethics protocol, approved migration, forbidden-capability rules, and Aequitas references/invariants.
- Deterministic canonical JSON and explicitly scoped SHA-256 identities.
- Machine-readable manifest containing stable paths, source-derived identifiers/versions, references, hashes, canonicalization, compatibility state, and all identity-bearing metadata.
- Positive, negative, boundary, duplicate, conflict, unknown-field, unresolved-reference, immutable-mutation, incompatible-version, and migration fixtures.
- Clean-checkout and CI replay at the exact submitted and accepted commit.
- Read-only downstream validation in `QuantumStateObjects` and `QSO-FABRIC`.

## Candidate Evidence Under Review

PR #2 and its reports record:

- Atlas plus a nine-artifact compatibility-set candidate;
- deterministic `qso-canonical-json-v1` serialization;
- earlier reports of sixteen passing tests, a nine-artifact replay, and candidate digest `4ed083cb204a77d1f1878aea8dbf9c61f996541c9b4de83c812bb461530d3eac`;
- exact four-genome set enforcement;
- `QSO-GENOME-IMMUTABLE-ETHICS-MIGRATION-v1` binding the authoritative protocol digest;
- Aequitas reference/invariant validation;
- focused reports of four exact-set tests, five migration tests, and eight Aequitas reference-integrity tests under CPython 3.13.5;
- reachable provenance and documentation describing the canonical-head consolidation.

These are candidate claims. They do not establish accepted digest semantics, complete immutable enforcement, reproducible installation, exact-head CI, independent clean replay, downstream compatibility, or release approval.

## Current Blocking Findings

- The compatibility manifest does not bind the immutable protocol and migration that establish the full protection boundary.
- Local ethics additions are not validated for conflict with the authoritative protocol.
- Duplicate migration paths can pass after set conversion.
- Aequitas review-surface duplicates can pass after set conversion.
- Manifest artifact identifiers and versions are not verified against source documents.
- The compatibility-set digest does not yet unambiguously identify all consumer-relevant metadata.
- Complete immutable-statement enforcement and original Aequitas/source-integrity review threads remain unresolved.
- Schema-validation dependencies and pip-cache inputs are not reproducibly declared.
- Pull-request workflow semantics do not yet certify or explicitly record the submitted head.
- Review threads, exact-head CI, clean-checkout replay, negative fixtures, downstream validation, provenance bundle, checksums, rollback evidence, and explicit approval remain incomplete.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Canonical submission | PASS | Existing PR #2 is the sole submitted path and contains the consolidated remediation lineage. |
| Candidate review | FAIL | Resolve or disposition all sixteen unresolved threads against the final immutable submitted head. |
| Set completeness | REVIEW | Exact Atlas/Nova/Orion/Lyra enforcement exists as candidate code; replay and review acceptance remain. |
| Immutable policy | FAIL | Bind protocol/migration into set identity and reject conflicting or duplicate local migration entries. |
| Aequitas integrity | FAIL | Resolve invariant/source findings and reject duplicate references and review surfaces before normalization. |
| Manifest identity | FAIL | Validate source identities and define complete, explicit digest scopes. |
| Dependencies/environment | FAIL | Check in reproducible dependency and supported-environment instructions. |
| CI semantics | FAIL | Certify the submitted head and retain exact workflow evidence. |
| Negative fixtures | INCOMPLETE | All missing, stale, duplicate, conflicting, mutated, and incompatible cases must fail closed. |
| Downstream consumption | BLOCKED | Both runtime consumers must verify the same accepted commit and identities read-only. |
| Status checks | NO EVIDENCE | No workflow run is attached to the current PR head. |
| Security | PARTIAL | Data-only boundary is declared; independent final-state verification remains. |
| Approval | PENDING | Explicit release approval only after every blocking gate passes. |

## Artifact Requirements

- Versioned schemas, four genomes, immutable protocol and migration, Aequitas definition, and forbidden-capability rules.
- Complete compatibility manifest with source-derived identity fields and explicit digest scopes.
- Validator and deterministic positive/negative/boundary/migration/duplicate/conflict fixture bundles.
- Review-thread disposition map tied to the final head.
- Exact-head CI logs, clean-checkout report, downstream reports, source archive, security-boundary report, dependency/SBOM record where applicable, SHA-256 checksums, provenance manifest, and rollback instructions.

## Rollback Criteria

Reject or roll back the candidate if the reviewed and released heads differ; any required artifact or identity binding is missing; hashes or metadata change without approved versioning; immutable protections are weakened or contradicted; duplicate paths, references, surfaces, or identities pass; dependencies are undeclared; CI certifies the wrong state; provenance is unreachable; consumers do not fail closed; or executable authority is introduced. Preserve rejected manifests, fixtures, reports, workflow logs, hashes, review dispositions, and supersession records.

## Release Log

- 2026-07-16 — Confirmed the complete four-genome contract as the highest-priority portfolio unblocker.
- 2026-07-16 — Advanced the objective to independent acceptance of PR #2 and held release blocked on review, CI, provenance, identity, and downstream evidence.
- 2026-07-16 — Consolidated the fifteen-commit remediation lineage onto PR #2, making canonical submission `PASS` without changing release priority or approval state.
- 2026-07-16 — Recorded five additional integrity findings and the absence of an exact-head workflow run; release remains blocked.
