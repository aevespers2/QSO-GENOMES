# Release Plan

## Current Decision

Status: `BLOCKED — CANONICAL-HEAD RECONCILIATION, SCOPE APPROVAL, EXACT-HEAD REVIEW, AND CONFORMANCE EVIDENCE REQUIRED`

QSO-GENOMES remains the portfolio's highest-priority declarative contract dependency. PR #2 is the single canonical submission path, but GitHub reports it open, non-mergeable, and diverged from `main`. Reconciliation must preserve the existing pull request, commit lineage, review history, and all intended candidate commits; produce one immutable mergeable head; and restart exact-head review and conformance evidence.

The latest observed comparison used PR head `7af2c7eac9f4bf14c98367500f23657f2230db9b` and default-branch head `5dc663aaca9de57a5ef79261b119ddabfc5fdb90`: the PR is 82 commits ahead and 27 commits behind, with merge base `c6c6ccdd61391da5fae5a268022c510069016b33`. These counts are timestamped evidence and must be recaptured immediately before reconciliation. The branch advanced eight commits after the prior frozen-head directive, so previous exact-head evidence no longer identifies the current submission.

The stale hard-coded manifest digest was corrected on the current candidate head to `99f33227247ef39fef3e1c3206c8ea49b9be9af86148298f07bdbf00b0cd6921`, and source-derived manifest identity validation was added. This removes the previously demonstrated digest-assertion failure, but it does not establish that the complete deterministic suite passes at the current head: no combined status checks and no pull-request workflow runs are attached to `7af2c7e...`, and the retained focused-test evidence is tied to earlier implementation ancestors rather than an independent clean replay of the current submission.

The current branch also adds `sprites/socrates.json` and `contracts/socrates-review-binding.json`. Those files introduce a new supervisory identity, compatibility aliases to Aequitas, and declarative authority to open repair pull requests. They are not part of the eleven-artifact compatibility manifest and are outside the currently approved release scope. They must be removed from this candidate, explicitly excluded with a documented non-authoritative status, or approved through a versioned Aequitas-to-Socrates migration and independent security/authority review.

The review timeline contains 34 threads: four resolved/outdated and 30 unresolved, including current and still-material outdated findings. Candidate reports, tests, manifests, and focused local replays remain implementation evidence, not independent release verification.

## Versioning

- Scheme: Semantic Versioning for the compatibility set and machine-readable manifest.
- First eligible candidate: `0.1.0-alpha.1`.
- Compatible data corrections may be patches; compatible fields, genomes, or fixtures are minor changes.
- Schema, immutable-ethics, forbidden-capability, canonicalization, manifest-identity, supervisory-identity, authority, or reference breaks require a declared major/breaking version and migration fixtures.
- Digest names and scopes must distinguish artifact-byte identity from complete compatibility-manifest identity.
- No version or tag may be assigned until every release artifact is generated and independently replayed from one immutable accepted head.

## Release Scope

- Canonical Atlas, Nova, Orion, and Lyra genome documents.
- Genome/Sprite schemas, authoritative immutable-ethics protocol, approved migration, forbidden-capability rules, and the approved Aequitas references/invariants.
- Deterministic canonical JSON and explicitly scoped SHA-256 identities.
- Machine-readable manifest containing stable paths, source-derived identifiers/versions, references, hashes, canonicalization, compatibility state, and all identity-bearing metadata.
- Positive, negative, boundary, duplicate, conflict, unknown-field, unresolved-reference, immutable-mutation, numeric-overflow, incompatible-version, and migration fixtures.
- Clean-checkout and CI replay at the exact submitted and accepted commit.
- Read-only downstream validation in `QuantumStateObjects` and `QSO-FABRIC`.

Explicitly excluded pending approval: Socrates supervisory identity, Aequitas compatibility aliases, repair-pull-request authority, runtime execution, network access, credentials, autonomous mutation, payment authority, deployment, and self-replication.

## Candidate Evidence Under Review

PR #2 and repository reports currently record:

- Atlas plus an eleven-artifact compatibility-set candidate;
- deterministic `qso-canonical-json-v1` serialization;
- exact four-genome set enforcement;
- `QSO-GENOME-IMMUTABLE-ETHICS-MIGRATION-v1` and the authoritative immutable protocol in the manifest candidate;
- Aequitas reference/invariant validation and review-surface hardening;
- local-ethics conflict and duplicate migration-path rejection;
- source-derived manifest artifact identifiers and versions;
- a corrected candidate digest assertion;
- focused reports for schema, exact-set, immutable-contract, migration, Aequitas, manifest, source identity, and provenance work.

These are candidate claims. They do not establish a mergeable final state, a passing exact-head test suite, accepted digest semantics, complete immutable enforcement, reproducible installation, exact-head CI, independent clean replay, downstream compatibility, supervisory-scope approval, or release approval.

## Current Blocking Findings

- PR #2 is diverged from `main` and non-mergeable; reconciliation will create a new head requiring renewed review and evidence.
- The submitted head continued moving after the freeze directive, invalidating earlier exact-head snapshots and increasing review churn.
- Socrates files add an unapproved supervisory identity, Aequitas aliases, and repair-PR authority outside the current manifest and release scope.
- Thirty review threads remain unresolved; all current and still-material outdated findings require final-head disposition.
- Complete digest-scope semantics remain undefined for artifact bytes versus all consumer-relevant manifest metadata.
- The immutable migration validator must require exact migration identity and source profile, exact `QSO-IMMUTABLE-ETHICS-v1` identity and approved contents, immutable status, approved external enforcement boundary, exact consumer-requirement key set, and unique migration paths.
- Complete immutable-statement enforcement remains unresolved or undispositioned.
- Aequitas validation must pin the approved Sprite identity and validate references, invariants, activation mode, human-review semantics, per-surface oversight, uniqueness, source consistency, and numeric finiteness.
- Schema-validation dependencies and pip-cache inputs are not reproducibly accepted.
- Pull-request workflow semantics do not yet certify and retain the submitted head identity.
- Exact-head CI, clean-checkout replay, complete negative fixtures, downstream validation, provenance bundle, checksums, rollback evidence, and explicit approval remain incomplete.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Canonical path | PASS | PR #2 remains the sole submitted review path; no competing release PR is authorized. |
| Head stability | FAIL | Stop candidate-head churn, reconcile current `main`, freeze one immutable submitted head, and require an approved exception for any later change. |
| Mergeability/reconciliation | FAIL | Integrate current `main` and all intended candidate commits without force-rewriting reviewed history, document conflicts, then review one mergeable immutable head. |
| Scope integrity | FAIL | Remove, explicitly quarantine, or approve and version the Socrates/Aequitas alias and repair-authority additions. |
| Deterministic suite | NO EVIDENCE | The stale digest assertion is corrected, but the complete suite must pass at the frozen current head with retained logs. |
| Candidate review | FAIL | Re-enumerate and resolve or disposition all current and material outdated threads against the frozen reconciled head. |
| Set completeness | REVIEW | The exact Atlas/Nova/Orion/Lyra and eleven-artifact candidate exists; reconciliation and acceptance replay remain. |
| Immutable policy | FAIL | Enforce the complete approved migration identity, source profile, protocol identity/content, status, boundary, migration shape, and local-conflict rules. |
| Aequitas integrity | FAIL | Pin the approved Aequitas identity and validate references, invariants, activation rules, per-surface oversight, uniqueness, source consistency, and numeric finiteness. |
| Manifest identity | PARTIAL | Source identities are candidate-validated; complete digest scopes and independent exact-head replay remain. |
| Dependencies/environment | FAIL | Check in reproducible dependency and supported-environment instructions. |
| CI semantics | FAIL | Certify the frozen submitted head and retain exact workflow evidence. |
| Negative fixtures | INCOMPLETE | All missing, stale, duplicate, conflicting, mutated, overflowed, weakened-review, alias-drift, and incompatible cases must fail closed. |
| Downstream consumption | BLOCKED | Both runtime consumers must verify the same accepted commit and identities read-only. |
| Status checks | NO EVIDENCE | The observed head has no combined statuses and no pull-request workflow runs. |
| Security | PARTIAL | Data-only boundary is declared; supervisory aliases and repair authority require independent review, and final-state verification remains. |
| Documentation | PARTIAL | Scope and reports exist, but branch/default directives conflict and final-head synchronization is absent. |
| Provenance | PARTIAL | Candidate lineage exists; reconciliation record and final immutable-head evidence are absent. |
| Approval | PENDING | Explicit release approval only after every blocking gate passes. |

## Artifact Requirements

- Versioned schemas, four genomes, immutable protocol and migration, approved Aequitas definition, and forbidden-capability rules.
- Complete compatibility manifest with source-derived identity fields and explicit digest scopes.
- Validator and deterministic positive/negative/boundary/migration/duplicate/conflict/activation-rule/numeric-overflow/alias-drift fixture bundles.
- Branch-reconciliation record showing old base/head, current default head, method, conflict resolutions, resulting immutable head, and preservation of review provenance.
- Scope-disposition record for Socrates and every Aequitas compatibility alias or repair-authority field.
- Review-thread disposition map tied to the final head.
- Exact-head CI logs, clean-checkout report, downstream reports, source archive, security-boundary report, dependency/SBOM record where applicable, SHA-256 checksums, provenance manifest, and rollback instructions.

## Rollback Criteria

Reject or roll back the candidate if branch reconciliation loses reviewed changes or review provenance; the reviewed and released heads differ; head churn resumes without approval; unapproved Socrates/Aequitas aliases or repair authority enter the accepted set; any required artifact or identity binding is missing; the deterministic suite fails; hashes, digest assertions, or metadata disagree; immutable protections are weakened or contradicted; migration or protocol identity/content/status/boundary drifts; activation or human-review semantics weaken; duplicate paths, references, surfaces, oversight definitions, aliases, or identities pass; non-finite or overflowed numbers pass; dependencies are undeclared; CI certifies the wrong state; provenance is unreachable; consumers do not fail closed; or executable authority is introduced. Preserve rejected heads, manifests, fixtures, reports, workflow logs, hashes, review dispositions, and supersession records.

## Release Log

- 2026-07-16 — Confirmed the complete four-genome contract as the highest-priority portfolio unblocker.
- 2026-07-16 — Advanced the objective to independent acceptance of PR #2 and held release blocked on review, CI, provenance, identity, and downstream evidence.
- 2026-07-16 — Preserved PR #2 as the singular review path without changing release priority or approval state.
- 2026-07-16 — Made provenance-preserving reconciliation the first release gate after the PR diverged from `main` and became non-mergeable.
- 2026-07-16 — Recorded a deterministic-suite failure caused by a stale hard-coded manifest digest on an earlier candidate head.
- 2026-07-16 — Observed the branch advance five remediation commits to `46f3248…`, with no statuses or workflow runs and 30 unresolved threads.
- 2026-07-16 — Observed eight further commits advancing PR #2 to `7af2c7e…`, now 82 commits ahead and 27 behind `main`. The digest assertion and source-identity candidate work improved, but no exact-head run exists, and unapproved Socrates/Aequitas alias and repair-authority files create a new scope decision. Release remains blocked.