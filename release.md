# Release Plan

## Current Decision

Status: `BLOCKED — PR RECONCILIATION, FAILING DETERMINISTIC SUITE, EXACT-HEAD REVIEW, AND CONFORMANCE EVIDENCE REQUIRED`

QSO-GENOMES remains the portfolio's highest-priority declarative contract dependency. PR #2 is the single canonical submission path, but GitHub reports it open, non-mergeable, and diverged from `main`. Reconciliation must preserve the existing pull request, commit lineage, review history, and the five candidate commits added after the prior product snapshot; produce one new immutable mergeable head; and restart exact-head review and conformance evidence.

The latest pre-release-update comparison observed PR head `46f3248d8f67b7f0cc734159d2fa0a27e6051ea7` against default-branch head `17b010dfc38ec6daf09325bef8d814952291c561`: 74 commits ahead, 26 commits behind, with merge base `c6c6ccdd61391da5fae5a268022c510069016b33`. This release-plan maintenance commit advances `main` again, so embedded ahead/behind counts are historical evidence rather than a stable current-state identifier. The exact base, head, comparison, and review state must be captured immediately before reconciliation.

No combined status checks and no pull-request workflow runs are attached to the observed PR head. The committed eleven-artifact manifest reports set digest `99f33227247ef39fef3e1c3206c8ea49b9be9af86148298f07bdbf00b0cd6921`, while `tests/test_contract_manifest.py` still hard-codes the superseded digest `6d9b0ca8c6766fbb63b4613df5b2baee455f1e63c848d6f75e56726efbc57cac`; the deterministic contract suite therefore cannot pass at that exact head.

The review timeline currently contains 34 threads: four resolved/outdated and 30 unresolved, including 23 current findings and seven unresolved outdated findings. The newest findings cover migration source-profile identity, migration contract identity, overflowed JSON-number rejection, and pinning the approved immutable-protocol contents. Candidate reports, tests, manifests, and focused local replays remain implementation evidence, not independent release verification.

The branch continued acceptance-remediation work after reconciliation became the first product gate. That work may improve Aequitas review-surface validation, but it also moves the submitted head and increases divergence. Further remediation on the unfrozen branch requires an explicit Architect exception with a bounded scope and evidence-preservation rationale; portfolio priority is unchanged.

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
- Positive, negative, boundary, duplicate, conflict, unknown-field, unresolved-reference, immutable-mutation, numeric-overflow, incompatible-version, and migration fixtures.
- Clean-checkout and CI replay at the exact submitted and accepted commit.
- Read-only downstream validation in `QuantumStateObjects` and `QSO-FABRIC`.

## Candidate Evidence Under Review

PR #2 and repository reports record:

- Atlas plus an eleven-artifact compatibility-set candidate;
- deterministic `qso-canonical-json-v1` serialization;
- exact four-genome set enforcement;
- `QSO-GENOME-IMMUTABLE-ETHICS-MIGRATION-v1` and the authoritative immutable protocol included in the manifest candidate;
- Aequitas reference/invariant validation and later review-surface hardening;
- focused reports for schema, exact-set, immutable-contract, migration, Aequitas, manifest, and provenance work;
- reachable candidate lineage and product/release documentation.

These are candidate claims. They do not establish a mergeable final state, a passing exact-head test suite, accepted digest semantics, complete immutable enforcement, reproducible installation, exact-head CI, independent clean replay, downstream compatibility, or release approval.

## Current Blocking Findings

- PR #2 is diverged from `main` and non-mergeable; reconciliation will create a new head requiring renewed review and evidence.
- The exact observed PR head fails the deterministic manifest test because its hard-coded expected digest does not match the committed manifest digest.
- Thirty review threads remain unresolved; all current and still-material outdated findings require final-head disposition.
- The immutable migration validator must require the exact migration identity and source profile, exact `QSO-IMMUTABLE-ETHICS-v1` protocol identity, approved protocol contents, immutable status, approved external enforcement boundary, exact consumer-requirement key set, and unique migration paths.
- Local ethics additions are not yet accepted as fail-closed against conflicts with the authoritative protocol.
- Aequitas validation must pin the binding to the Aequitas Sprite, validate activation mode and human-review semantics, require approved non-empty oversight per review surface, reject duplicate/conflicting references or surfaces before normalization, and reject non-finite constants and numeric overflow.
- Manifest artifact identifiers, versions, and other identity-bearing values must be derived from or verified against source documents.
- Compatibility-set digest scopes must unambiguously identify all consumer-relevant metadata.
- Complete immutable-statement enforcement and original Aequitas/source-integrity findings remain unresolved or undispositioned.
- Schema-validation dependencies and pip-cache inputs are not reproducibly accepted.
- Pull-request workflow semantics do not yet certify and retain the submitted head identity.
- Exact-head CI, clean-checkout replay, negative fixtures, downstream validation, provenance bundle, checksums, rollback evidence, and explicit approval remain incomplete.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Canonical path | PASS | PR #2 remains the sole submitted review path; no competing release PR is authorized. |
| Mergeability/reconciliation | FAIL | Integrate current `main` and all intended candidate commits without force-rewriting reviewed history, document conflicts, then freeze and review one mergeable immutable head. |
| Deterministic suite | FAIL | Correct the stale manifest-digest assertion and pass the complete suite at the frozen submitted head. |
| Candidate review | FAIL | Re-enumerate and resolve or disposition all current and material outdated threads against the frozen reconciled head. |
| Set completeness | REVIEW | The exact Atlas/Nova/Orion/Lyra and eleven-artifact candidate exists; reconciliation and acceptance replay remain. |
| Immutable policy | FAIL | Enforce the complete approved migration identity, source profile, protocol identity/content, status, boundary, migration shape, and local-conflict rules. |
| Aequitas integrity | FAIL | Pin Aequitas identity and validate references, invariants, activation rules, per-surface oversight, uniqueness, source consistency, and numeric finiteness. |
| Manifest identity | FAIL | Validate source identities and define complete, explicit digest scopes. |
| Dependencies/environment | FAIL | Check in reproducible dependency and supported-environment instructions. |
| CI semantics | FAIL | Certify the frozen submitted head and retain exact workflow evidence. |
| Negative fixtures | INCOMPLETE | All missing, stale, duplicate, conflicting, mutated, overflowed, weakened-review, and incompatible cases must fail closed. |
| Downstream consumption | BLOCKED | Both runtime consumers must verify the same accepted commit and identities read-only. |
| Status checks | NO EVIDENCE | The observed head has no combined statuses and no pull-request workflow runs. |
| Security | PARTIAL | Data-only boundary is declared; independent final-state verification remains. |
| Documentation | PARTIAL | Scope and reports exist, but stale digest evidence, branch-local/default-branch directive conflict, and final-head synchronization must be corrected. |
| Provenance | PARTIAL | Candidate lineage exists; reconciliation record and final immutable-head evidence are absent. |
| Approval | PENDING | Explicit release approval only after every blocking gate passes. |

## Artifact Requirements

- Versioned schemas, four genomes, immutable protocol and migration, Aequitas definition, and forbidden-capability rules.
- Complete compatibility manifest with source-derived identity fields and explicit digest scopes.
- Validator and deterministic positive/negative/boundary/migration/duplicate/conflict/activation-rule/numeric-overflow fixture bundles.
- Branch-reconciliation record showing old base/head, current default head, method, conflict resolutions, resulting immutable head, and preservation of review provenance.
- Review-thread disposition map tied to the final head.
- Exact-head CI logs, clean-checkout report, downstream reports, source archive, security-boundary report, dependency/SBOM record where applicable, SHA-256 checksums, provenance manifest, and rollback instructions.

## Rollback Criteria

Reject or roll back the candidate if branch reconciliation loses reviewed changes or review provenance; the reviewed and released heads differ; any required artifact or identity binding is missing; the deterministic suite fails; hashes, digest assertions, or metadata disagree; immutable protections are weakened or contradicted; migration or protocol identity/content/status/boundary drifts; activation or human-review semantics weaken; duplicate paths, references, surfaces, oversight definitions, or identities pass; non-finite or overflowed numbers pass; dependencies are undeclared; CI certifies the wrong state; provenance is unreachable; consumers do not fail closed; or executable authority is introduced. Preserve rejected heads, manifests, fixtures, reports, workflow logs, hashes, review dispositions, and supersession records.

## Release Log

- 2026-07-16 — Confirmed the complete four-genome contract as the highest-priority portfolio unblocker.
- 2026-07-16 — Advanced the objective to independent acceptance of PR #2 and held release blocked on review, CI, provenance, identity, and downstream evidence.
- 2026-07-16 — Preserved PR #2 as the singular review path without changing release priority or approval state.
- 2026-07-16 — Recorded additional candidate integrity findings and immutable-manifest binding work while preserving the distinction between implemented remediation and accepted evidence.
- 2026-07-16 — Made provenance-preserving reconciliation the first release gate after the PR diverged from `main` and became non-mergeable.
- 2026-07-16 — Recorded PR head `cacd9dda…` as 69 commits ahead and 23 behind the pre-maintenance default head, with no statuses or workflow runs, 26 unresolved review threads, and a deterministic-suite failure caused by a stale hard-coded manifest digest.
- 2026-07-16 — Observed the branch advance five more remediation commits to `46f3248…`; the latest pre-update comparison showed 74 commits ahead and 26 behind, no statuses or workflow runs, and 30 unresolved threads. Reconciliation remains the first gate, and release remains blocked.