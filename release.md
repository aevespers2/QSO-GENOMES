# Release Plan

## Current Decision

Status: `BLOCKED — PR RECONCILIATION, EXACT-HEAD REVIEW, AND CONFORMANCE EVIDENCE REQUIRED`

QSO-GENOMES remains the portfolio's highest-priority declarative contract dependency. PR #2 is the single canonical submission path, but GitHub currently reports it non-mergeable and diverged from `main`. The exact base, head, ahead/behind counts, and review state must be captured again immediately before reconciliation because continued commits make embedded “current head” references self-staling.

At the latest product review, the PR branch was 62 commits ahead and 20 commits behind the then-current default branch, with merge base `c6c6ccdd61391da5fae5a268022c510069016b33`; no combined status checks were attached to the observed PR head. Reconciliation must preserve the existing PR and review lineage, integrate current default-branch governance records and candidate changes, produce one new immutable mergeable head, and trigger renewed review and exact-head evidence.

Candidate reports, tests, manifests, and focused local replays are implementation evidence, not independent release verification. More recent branch work appears to bind the immutable protocol and migration into an eleven-artifact candidate manifest, but that remediation is not accepted until it survives reconciliation and exact-head review.

## Versioning

- Scheme: Semantic Versioning for the compatibility set and machine-readable manifest.
- First eligible candidate: `0.1.0-alpha.1`.
- Compatible data corrections may be patches; compatible fields, genomes, or fixtures are minor changes.
- Schema, immutable-ethics, forbidden-capability, canonicalization, manifest-identity, or reference breaks require a declared major/breaking version and migration fixtures.
- Digest names and scopes must distinguish artifact-byte identity from complete compatibility-manifest identity.
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

PR #2 and repository reports record:

- Atlas plus an initial nine-artifact compatibility-set candidate;
- deterministic `qso-canonical-json-v1` serialization;
- earlier reports of sixteen passing tests, a nine-artifact replay, and candidate digest `4ed083cb204a77d1f1878aea8dbf9c61f996541c9b4de83c812bb461530d3eac`;
- exact four-genome set enforcement;
- `QSO-GENOME-IMMUTABLE-ETHICS-MIGRATION-v1` binding the authoritative protocol digest;
- Aequitas reference/invariant validation;
- focused reports of four exact-set tests, five migration tests, and eight Aequitas reference-integrity tests under CPython 3.13.5;
- later candidate work adding the immutable protocol and migration to an eleven-artifact manifest with a focused deterministic replay;
- reachable provenance and product/release documentation.

These are candidate claims. They do not establish a mergeable final state, accepted digest semantics, complete immutable enforcement, reproducible installation, exact-head CI, independent clean replay, downstream compatibility, or release approval.

## Current Blocking Findings

- PR #2 is diverged from `main` and non-mergeable; reconciliation will create a new head requiring renewed review and evidence.
- Candidate immutable protocol/migration manifest binding requires reconciliation and review acceptance.
- Local ethics additions are not yet accepted as fail-closed against conflicts with the authoritative protocol.
- Duplicate migration paths and duplicate Aequitas review surfaces require pre-normalization rejection and accepted fixtures.
- Manifest artifact identifiers, versions, and other identity-bearing values must be derived from or verified against source documents.
- Compatibility-set digest scopes must unambiguously identify all consumer-relevant metadata.
- Complete immutable-statement enforcement and original Aequitas/source-integrity findings remain unresolved or undispositioned.
- Schema-validation dependencies and pip-cache inputs are not reproducibly accepted.
- Pull-request workflow semantics do not yet certify and retain the submitted head identity.
- Review threads, exact-head CI, clean-checkout replay, negative fixtures, downstream validation, provenance bundle, checksums, rollback evidence, and explicit approval remain incomplete.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Canonical path | PASS | PR #2 remains the sole submitted review path; no competing release PR is authorized. |
| Mergeability/reconciliation | FAIL | Integrate current `main` without force-rewriting reviewed history, document conflicts, then freeze and review one mergeable immutable head. |
| Candidate review | FAIL | Re-enumerate and resolve or disposition all review threads against the frozen reconciled head. |
| Set completeness | REVIEW | Exact Atlas/Nova/Orion/Lyra enforcement and later eleven-artifact binding exist as candidate work; reconciliation and acceptance replay remain. |
| Immutable policy | FAIL | Accept protocol/migration identity binding and reject conflicting or duplicate local migration entries. |
| Aequitas integrity | FAIL | Resolve invariant/source findings and reject duplicate references and review surfaces before normalization. |
| Manifest identity | FAIL | Validate source identities and define complete, explicit digest scopes. |
| Dependencies/environment | FAIL | Check in reproducible dependency and supported-environment instructions. |
| CI semantics | FAIL | Certify the frozen submitted head and retain exact workflow evidence. |
| Negative fixtures | INCOMPLETE | All missing, stale, duplicate, conflicting, mutated, and incompatible cases must fail closed. |
| Downstream consumption | BLOCKED | Both runtime consumers must verify the same accepted commit and identities read-only. |
| Status checks | NO EVIDENCE | No accepted status-check record is attached to the reviewed candidate state. |
| Security | PARTIAL | Data-only boundary is declared; independent final-state verification remains. |
| Approval | PENDING | Explicit release approval only after every blocking gate passes. |

## Artifact Requirements

- Versioned schemas, four genomes, immutable protocol and migration, Aequitas definition, and forbidden-capability rules.
- Complete compatibility manifest with source-derived identity fields and explicit digest scopes.
- Validator and deterministic positive/negative/boundary/migration/duplicate/conflict fixture bundles.
- Branch-reconciliation record showing old base/head, current default head, method, conflict resolutions, resulting immutable head, and preservation of review provenance.
- Review-thread disposition map tied to the final head.
- Exact-head CI logs, clean-checkout report, downstream reports, source archive, security-boundary report, dependency/SBOM record where applicable, SHA-256 checksums, provenance manifest, and rollback instructions.

## Rollback Criteria

Reject or roll back the candidate if branch reconciliation loses reviewed changes or review provenance; the reviewed and released heads differ; any required artifact or identity binding is missing; hashes or metadata change without approved versioning; immutable protections are weakened or contradicted; duplicate paths, references, surfaces, or identities pass; dependencies are undeclared; CI certifies the wrong state; provenance is unreachable; consumers do not fail closed; or executable authority is introduced. Preserve rejected heads, manifests, fixtures, reports, workflow logs, hashes, review dispositions, and supersession records.

## Release Log

- 2026-07-16 — Confirmed the complete four-genome contract as the highest-priority portfolio unblocker.
- 2026-07-16 — Advanced the objective to independent acceptance of PR #2 and held release blocked on review, CI, provenance, identity, and downstream evidence.
- 2026-07-16 — Preserved PR #2 as the singular review path without changing release priority or approval state.
- 2026-07-16 — Recorded additional candidate integrity findings and later immutable-manifest binding work while preserving the distinction between implemented remediation and accepted evidence.
- 2026-07-16 — Made provenance-preserving reconciliation the first release gate after the PR diverged from `main` and became non-mergeable; release remains blocked pending one frozen mergeable head and complete renewed acceptance evidence.
