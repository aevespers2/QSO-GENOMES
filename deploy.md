# Deployment Record

## Current Decision

Status: `BLOCKED — RELEASE NOT READY, CANDIDATE HEAD UNSTABLE, SUPERVISORY SCOPE UNAPPROVED, AND GOVERNANCE MERGE ORDER GATED`

No QSO-GENOMES artifact, package, manifest, documentation site, consumer pin, tag, governance workflow, or downstream integration is authorized for deployment. `release.md` remains explicitly blocked, PR #2 is open and non-mergeable, the submitted compatibility head has continued moving after a freeze directive, Socrates remains outside the approved manifest/supervisory scope, and draft PR #3 introduces a separately reviewed governance control plane whose merge order must not invalidate PR #2 reconciliation or exact-head evidence.

## Deployment Review — 2026-07-17

| Check | Evidence | Result |
|---|---|---|
| Release authorization | `release.md` remains explicitly blocked and was refreshed at commit `57df4fa963a34a5e9f78d2c3508c7e081a44cf11`; later default-branch documentation commits do not authorize release. | BLOCKED |
| Environment | Candidate `requirements.txt` pins `jsonschema==4.26.0`; the conformance workflow proposes Python 3.11, 3.12, and 3.13 on `ubuntu-latest`. No clean-checkout exact-head run or supported-environment report is retained. | PARTIAL |
| Repository permission | Repository write access was used only to synchronize deployment evidence. No tag, release, Pages environment, package registry, downstream repository, secret, production permission, or workflow activation was exercised. | BOUNDED |
| Artifacts | An eleven-artifact compatibility candidate and reports exist on PR #2, but no accepted source archive, SBOM/dependency record, checksum bundle, provenance manifest, signed attestation, consumer-validation bundle, or rollback artifact is attached to one immutable accepted head. Socrates artifacts remain outside the approved compatibility manifest. | BLOCKED |
| Configuration | PR #2 proposes submitted-head checkout and SHA recording, while PR #3 proposes governance workflows. Neither current head has exact-head workflow evidence, and the governance workflows are not approved for default-branch activation. | UNVERIFIED |
| Health checks | PR #2 head `e51a814cd329c55e45a1599b205ef234859e4848` has no combined commit statuses and no pull-request workflow runs. GitHub reports PR #2 open and non-mergeable with 40 review threads, 36 unresolved. Draft PR #3 head `91db1a9176e8274140a48a9fcfc8ba08af40ac43` is also non-mergeable and has no combined statuses or pull-request workflow runs. | FAIL |
| Observability | Review threads, commit comparisons, workflow definitions, release records, and PR metadata are visible, but no exact-head CI logs, retained current-head artifacts, downstream compatibility results, deployment telemetry, or approved governance audit output exists. | PARTIAL |
| Rollback readiness | Rejected heads, review history, and both PR branches remain reachable. A provenance-preserving reconciliation record, immutable accepted head, artifact checksums, consumer unpin procedure, governance-workflow disablement drill, and tested restoration are absent. | BLOCKED |
| Post-deployment validation | Not applicable because no deployment, publication, tag, workflow activation, package release, or downstream pin was executed. | NOT RUN |

## Bounded Action Completed

The deployment record was synchronized with the current release evidence: PR #2 remains non-mergeable at `e51a814...` with no exact-head status or workflow run; 36 review threads remain unresolved; Socrates remains an unapproved supervisory-scope addition; and draft PR #3 at `91db1a9...` is a separate governance candidate with no current-head CI evidence. No executable, public, governance, or downstream deployment action was attempted.

## Required Decisions

### Socrates disposition

Approve one disposition before candidate reconciliation:

1. remove both Socrates artifacts from the current candidate;
2. quarantine them as explicitly non-authoritative, non-manifested, and non-consumer-visible experimental material; or
3. approve a separately versioned Aequitas-to-Socrates migration with equivalent-or-stronger human-review guarantees and independent security/authority review.

### Governance merge order

The bounded default is to keep PR #3 draft and excluded, reconcile and freeze PR #2 first, obtain exact-head conformance and independent review, and only then refresh PR #3 against the accepted `main`. Any alternate sequence requires explicit Architect approval plus a provenance-preserving migration record, renewed PR #2 comparison and conflict review, exact-head evidence, legacy-PR migration planning, workflow-permission review, and rollback instructions.

## Next Eligible Deployment Preparation

After `release.md` is explicitly marked ready, the first bounded deployment preparation step is a read-only candidate packaging rehearsal: export the accepted source and eleven-artifact compatibility set at the immutable commit, generate SHA-256 checksums and provenance, replay validators in a clean environment, and verify that `QuantumStateObjects` and `QSO-FABRIC` reject every mismatched version or hash. Do not publish, tag, activate governance workflows, or update downstream pins until that rehearsal and rollback evidence are reviewed.