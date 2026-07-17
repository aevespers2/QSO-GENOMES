# Release Plan

## Current Decision

Status: `BLOCKED — CANONICAL-HEAD RECONCILIATION, SCOPE APPROVAL, EXACT-HEAD REVIEW, AND CONFORMANCE EVIDENCE REQUIRED`

QSO-GENOMES remains the portfolio's highest-priority declarative contract dependency. PR #2 is the single canonical submission path, but GitHub reports it open, non-mergeable, and diverged from `main`. Reconciliation must preserve the existing pull request, commit lineage, review history, and all intended candidate commits; produce one immutable mergeable head; and restart exact-head review and conformance evidence.

The latest comparison snapshot before this release-record update used PR head `e51a814cd329c55e45a1599b205ef234859e4848` and default-branch head `90cf6896f532bb7f9628d2140c76759109318761`: the PR was 86 commits ahead and 34 commits behind, with merge base `c6c6ccdd61391da5fae5a268022c510069016b33`. The branch advanced four additional commits after the prior `7af2c7e...` release snapshot and at least twelve commits after the earlier freeze directive, so all earlier exact-head evidence is superseded. Counts are historical evidence and must be recaptured immediately before reconciliation.

The current candidate now includes `requirements.txt` pinning `jsonschema==4.26.0`, changes the workflow to check out the submitted head, and records the checked-out SHA before validation. Those changes address earlier dependency/cache and synthetic-merge concerns in candidate code, but they are not release evidence: no combined status checks and no pull-request workflow runs are attached to `e51a814...`, and no independent clean replay has been retained.

The branch still adds `sprites/socrates.json` and `contracts/socrates-review-binding.json`. The Sprite itself is non-executing and denies repository writes, but the binding aliases `aequitas-external-review-v1`, permits a `human_or_bounded_repair_agent`, specifies draft-pull-request repair delivery, and declares authority to propose and open repair pull requests. These artifacts remain outside the eleven-artifact compatibility manifest and the approved release scope. They must be removed, explicitly quarantined as non-authoritative and non-consumer-visible, or approved through a versioned Aequitas-to-Socrates migration plus independent security/authority review.

Draft PR #3 is a separate governance-control-plane candidate and is not part of this release. Its current head is `91db1a9176e8274140a48a9fcfc8ba08af40ac43`, while its retained workflow claim is tied to earlier head `8ba56bcc...`; GitHub currently reports no combined status checks and no pull-request workflow runs for `91db1a9...`. PR #3 must remain draft and excluded until PR #2 is reconciled and frozen. Merging it first would move `main`, invalidate the current reconciliation snapshot, and require a fresh PR #2 comparison, conflict review, and exact-head evidence cycle; any alternate merge order requires explicit Architect approval and a provenance-preserving migration record.

The review timeline for PR #2 contains 40 threads: four resolved/outdated and 36 unresolved, including current and still-material outdated findings. Candidate reports, tests, manifests, and focused local replays remain implementation evidence, not independent release verification.

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

Explicitly excluded pending approval: Socrates supervisory identity, Aequitas compatibility aliases, repair-pull-request authority, PR #3 governance workflows and scheduled Inspector automation, portfolio-wide PR ontology adoption, issue mutation/escalation automation, runtime execution, network access, credentials, autonomous mutation, payment authority, deployment, and self-replication.

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
- a pinned schema-validation dependency and exact-head checkout assertions in the workflow candidate;
- focused reports for schema, exact-set, immutable-contract, migration, Aequitas, manifest, source identity, and provenance work.

These are candidate claims. They do not establish a mergeable final state, a passing exact-head test suite, accepted digest semantics, complete immutable enforcement, reproducible installation, exact-head CI, independent clean replay, downstream compatibility, supervisory-scope approval, governance-control-plane adoption, or release approval.

## Current Blocking Findings

- PR #2 is diverged from `main` and non-mergeable; reconciliation will create a new head requiring renewed review and evidence.
- The submitted head continued moving after the freeze directive, invalidating earlier exact-head snapshots and increasing review churn.
- Socrates files add an unapproved supervisory identity, Aequitas alias, bounded-repair-agent semantics, and repair-PR authority outside the current manifest and release scope.
- Draft PR #3 introduces a separate governance control plane; its current head lacks exact-head status/workflow evidence, and merging it before PR #2 reconciliation would create additional default-branch drift and invalidate the current reconciliation target.
- Thirty-six PR #2 review threads remain unresolved; all current and still-material outdated findings require final-head disposition.
- Complete digest-scope semantics remain undefined for artifact bytes versus all consumer-relevant manifest metadata.
- The immutable migration validator must require exact migration identity and source profile, exact `QSO-IMMUTABLE-ETHICS-v1` identity and approved contents, immutable status, approved external enforcement boundary, exact consumer-requirement key set, and unique migration paths.
- Complete immutable-statement enforcement remains unresolved or undispositioned.
- Aequitas validation must pin the approved Sprite identity and validate references, invariants, activation mode, human-review semantics, per-surface oversight, uniqueness, source consistency, and numeric finiteness.
- Socrates must either be schema-validated and included in an approved versioned manifest/migration or remain outside the candidate and consumer contract.
- Dependency and workflow improvements have no exact-head run, retained logs, or independent replay.
- Exact-head CI, clean-checkout replay, complete negative fixtures, downstream validation, provenance bundle, checksums, rollback evidence, and explicit approval remain incomplete.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Canonical path | PASS | PR #2 remains the sole submitted compatibility-set review path; PR #3 is a separate draft governance candidate and is excluded. |
| Head stability | FAIL | Stop candidate-head churn, reconcile current `main`, freeze one immutable submitted head, and require an approved exception for any later change. |
| Mergeability/reconciliation | FAIL | Integrate current `main` and all intended in-scope candidate commits without force-rewriting reviewed history, document conflicts, then review one mergeable immutable head. |
| Merge order/governance isolation | FAIL | Keep PR #3 draft and excluded until PR #2 is reconciled and frozen, or approve an alternate order with exact provenance, conflict, migration, and rollback controls. |
| Scope integrity | FAIL | Remove, explicitly quarantine, or approve and version the Socrates/Aequitas alias and repair-authority additions. |
| Deterministic suite | NO EVIDENCE | The complete suite must pass at the frozen current head with retained logs. |
| Candidate review | FAIL | Re-enumerate and resolve or disposition all 36 unresolved PR #2 threads against the frozen reconciled head. |
| Set completeness | REVIEW | The exact Atlas/Nova/Orion/Lyra and eleven-artifact candidate exists; reconciliation and acceptance replay remain. |
| Immutable policy | FAIL | Enforce the complete approved migration identity, source profile, protocol identity/content, status, boundary, migration shape, and local-conflict rules. |
| Aequitas integrity | FAIL | Pin the approved Aequitas identity and validate references, invariants, activation rules, per-surface oversight, uniqueness, source consistency, and numeric finiteness. |
| Manifest identity | PARTIAL | Source identities are candidate-validated; complete digest scopes and independent exact-head replay remain. |
| Dependencies/environment | PARTIAL | `jsonschema==4.26.0` is pinned in the candidate; supported-environment documentation and clean reproducibility evidence remain absent. |
| CI semantics | PARTIAL | Exact-head checkout assertions are candidate code, but no workflow run certifies or retains evidence for the submitted head. |
| Governance candidate evidence | FAIL | PR #3 head `91db1a9...` has no attached status checks or pull-request workflow runs; earlier-head evidence cannot certify it or authorize adoption. |
| Negative fixtures | INCOMPLETE | All missing, stale, duplicate, conflicting, mutated, overflowed, weakened-review, alias-drift, and incompatible cases must fail closed. |
| Downstream consumption | BLOCKED | Both runtime consumers must verify the same accepted commit and identities read-only. |
| Status checks | NO EVIDENCE | PR #2 head `e51a814...` has no combined statuses and no pull-request workflow runs. |
| Security | PARTIAL | Data-only boundary is declared; supervisory aliases, repair authority, and governance automation require independent review, and final-state verification remains. |
| Documentation | PARTIAL | Scope and reports exist, but branch/default directives conflict and final-head synchronization is absent. |
| Provenance | PARTIAL | Candidate lineage exists; reconciliation record, governance merge-order record, and final immutable-head evidence are absent. |
| Approval | PENDING | Explicit release approval only after every blocking gate passes. |

## Artifact Requirements

- Versioned schemas, four genomes, immutable protocol and migration, approved Aequitas definition, and forbidden-capability rules.
- Complete compatibility manifest with source-derived identity fields and explicit digest scopes.
- Validator and deterministic positive/negative/boundary/migration/duplicate/conflict/activation-rule/numeric-overflow/alias-drift fixture bundles.
- Branch-reconciliation record showing old base/head, current default head, method, conflict resolutions, resulting immutable head, and preservation of review provenance.
- Governance merge-order and exclusion record identifying PR #3 heads/evidence, approved sequence, default-branch impact, conflict handling, and rollback.
- Scope-disposition record for Socrates and every Aequitas compatibility alias or repair-authority field.
- Review-thread disposition map tied to the final head.
- Exact-head CI logs, clean-checkout report, downstream reports, source archive, security-boundary report, dependency/SBOM record where applicable, SHA-256 checksums, provenance manifest, and rollback instructions.

## Rollback Criteria

Reject or roll back the candidate if branch reconciliation loses reviewed changes or review provenance; the reviewed and released heads differ; head churn resumes without approval; PR #3 or another governance/control-plane change moves the base or enters the compatibility-set candidate without an approved merge-order record and fresh exact-head replay; unapproved Socrates/Aequitas aliases or repair authority enter the accepted set; any required artifact or identity binding is missing; the deterministic suite fails; hashes, digest assertions, or metadata disagree; immutable protections are weakened or contradicted; migration or protocol identity/content/status/boundary drifts; activation or human-review semantics weaken; duplicate paths, references, surfaces, oversight definitions, aliases, or identities pass; non-finite or overflowed numbers pass; dependencies are undeclared; CI certifies the wrong state; provenance is unreachable; consumers do not fail closed; or executable authority is introduced. Preserve rejected heads, manifests, fixtures, reports, workflow logs, hashes, review dispositions, merge-order decisions, and supersession records.

## Release Log

- 2026-07-16 — Confirmed the complete four-genome contract as the highest-priority portfolio unblocker.
- 2026-07-16 — Advanced the objective to independent acceptance of PR #2 and held release blocked on review, CI, provenance, identity, and downstream evidence.
- 2026-07-16 — Preserved PR #2 as the singular review path without changing release priority or approval state.
- 2026-07-16 — Made provenance-preserving reconciliation the first release gate after the PR diverged from `main` and became non-mergeable.
- 2026-07-16 — Recorded a deterministic-suite failure caused by a stale hard-coded manifest digest on an earlier candidate head.
- 2026-07-16 — Observed the branch advance five remediation commits to `46f3248...`, with no statuses or workflow runs and 30 unresolved threads.
- 2026-07-16 — Observed eight further commits advancing PR #2 to `7af2c7e...`, now 82 commits ahead and 27 behind `main`; unapproved Socrates/Aequitas alias and repair-authority files created a new scope decision.
- 2026-07-17 — Refreshed the deployment review against PR head `e51a814...`: four more candidate commits added dependency and exact-head workflow improvements, but the branch remained non-mergeable, 86 ahead/34 behind the pre-update default head, without status checks or workflow runs, and with 36 unresolved review threads. Release and deployment remain blocked pending provenance-preserving reconciliation and explicit Socrates scope disposition.
- 2026-07-17 — Classified draft PR #3 as a separate, excluded governance-control-plane candidate. Its current head `91db1a9...` has no exact-head status/workflow evidence, and merging it before PR #2 reconciliation would create new base drift; approval is required for any merge order other than PR #2 reconciliation/freeze first.