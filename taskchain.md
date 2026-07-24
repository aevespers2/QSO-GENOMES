# Task Chain

## Repository role

QSO-GENOMES is the declarative contract authority for QSO identity, purpose, immutable policy, lineage, migration, compatibility manifests, and genome-specific canonicalization. It is an upstream dependency of `QuantumStateObjects`, `QSO-FABRIC`, `qsio-kernel` or another approved generic format package, Repository `1` or another approved capability authority, and read-only interfaces.

A genome is data. This repository does not own runtime execution, capability issuance, credentials, deployment, payment execution, repository mutation, or canonical operational state.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

### Next objective

Reconcile the compatibility-set, identity-migration, workflow-repair, historical QSIO-adapter, and documentation candidates into one explicitly ordered review plan, then prove a four-boundary integration model—declarative validity, neutral conformance, operational admission, and runtime projection—without force-rewriting history or allowing any branch, genome, passing test, successful benchmark, or successful execution to become authoritative by existence alone.

### Intended user outcome

A downstream consumer can retrieve one reviewed Atlas/Nova/Orion/Lyra contract set; verify exact paths, schema versions, canonical bytes, digest scopes, immutable policy, lineage, migrations, references, public/protected projections, and manifest identity; distinguish declared from demonstrated capability; distinguish declarative validity from neutral conformance, Repository `1` operational admission, runtime projection, execution, and canonical reconciliation; and fail closed when any artifact, alias, version, capability, admission, receipt, correction, revocation, or recovery reference is missing or inconsistent.

### Current candidate map

| Candidate | Purpose | Observed state | Authority boundary |
|---|---|---|---|
| PR #2 | Four-genome compatibility-set review path | Draft, non-mergeable, exact head `1259693433814129f44d0255b5e0ecf741d9a79b`; no surfaced exact-head workflow evidence for that head | Candidate artifacts only; not accepted, published, or downstream-authoritative |
| PR #12 | Remove active Aequitas and Socrates governance identities and transfer review responsibility to Jacob Thomas Redmond | Draft, non-mergeable, exact head `622530232248a8df8c24c91ed09ce58f66988e63`; bounded conformance and reconciliation checks reported successful | Identity-migration candidate only; historical provenance remains reachable |
| PR #13 | Reconciliation and Consent Capacity Lock repair path | Draft, non-mergeable, exact head `4a638f064d0d4e11cbc94eb14b23ad60586e8a60`; later focused repairs merged through PRs #16 and #18 | No automatic final merge, publication, or runtime authority |
| PR #14 | Historical QSIO cross-repository adapter | Closed unmerged at exact head `992d8263bf62666fd6a05152cc0f6ad16791706c`; retained as historical evidence only | No active adapter, generic format ownership, or compatibility claim |
| PR #15 | Pages, architecture, onboarding, gluing, genome admission/runtime projection, capability evidence, bounded self-edit review, and lifecycle documentation | Draft, mergeable at current candidate head; documentation-only | No genome, schema, alias, self-edit, runtime, capability, admission, release, or publication approval |

These snapshots are review evidence, not durable release identifiers. Reconfirm exact states before any acceptance action.

### Capability evidence and self-edit review state

The [capability evidence and self-edit review](docs/capability-evidence-and-self-edit-review.md) records status `DOCUMENTED_NOT_ADMITTED`. It separates declaration, structural validity, fixture demonstration, benchmark demonstration, independent reproduction, admission eligibility, operational admission, and resulting-state verification.

Ordinary mutable-field changes require exact-field deltas, cumulative drift, schema authority, evidence, consumer-impact review, independent disposition, rollback, and restored-state verification. New keys or semantic rules require a versioned migration. Immutable-policy, forbidden-capability, credential, capability, repository-write, release, deployment, payment, signing, or canonical-state changes are not genome self-edits.

Passing schema, digest, workflow, benchmark, runtime, or interface checks does not certify general capability or authorize self-commit, self-approval, self-admission, activation, release, or publication.

### Priority

**P0 — BLOCKED on identity, ownership, canonical-head, admission-authority, shared-fixture, and external-disposition decisions.**

The portfolio must not accept PR #2 while PR #12 proposes a conflicting active identity model, must not reactivate the historical PR #14 adapter while generic QSO format ownership is unresolved, and must not treat PR #15 documentation, evidence-ladder, benchmark, or self-edit packet success as compatibility-set acceptance, Repository `1` admission, runtime activation, capability certification, or Pages publication approval.

## Success criteria

- One explicit merge and supersession order is approved for PRs #2, #12, #13, historical PR #14, and PR #15.
- One active supervisory and human-review identity model is approved, including historical aliases, retirement, cache invalidation, and rollback.
- One immutable compatibility-set head becomes mergeable and passes exact-head conformance with retained evidence.
- QSO-GENOMES remains declarative and non-executing.
- Declared, structurally valid, fixture-demonstrated, benchmark-demonstrated, independently reproduced, admitted, and resulting-state-verified capability states remain distinct.
- Every proposed self-edit is field-addressed, drift-bounded, independently reviewed, ethics-compatible, consumer-assessed, reversible, and externally dispositioned.
- Generic QSO envelope, registry, serialization, and capability ownership are assigned outside or explicitly shared with genome-specific profiles.
- Artifact-byte and complete-manifest digest scopes are versioned and domain-separated.
- Repository `1` or another approved authority distinguishes local genome validity from operational admission, capability issuance, activation, revocation, reconciliation, and recovery.
- QuantumStateObjects and QSO-FABRIC derive compatible projections from the same admitted genome commit and reject the same hostile fixtures.
- `qsio-kernel` or another verifier reproduces neutral conformance vectors without becoming the operational runtime or authority.
- Public interfaces expose only approved projections and preserve provenance, correction, revocation, redaction, uncertainty, and admission state.
- Release evidence distinguishes proposed, declared, implemented, structurally valid, fixture-demonstrated, benchmark-demonstrated, independently reproduced, conformant, admitted, runtime-eligible, executed, reconciled, accepted, published, released, deployed, superseded, frozen, and revoked states.

## Non-goals

- Executable agent behavior or unrestricted autonomous mutation.
- Treating a genome, Sprite, alias, reviewer record, workflow, passing test, benchmark, adapter result, runtime projection, or successful execution as a credential or approval.
- Adding network, repository-write, payment, deployment, infrastructure, or secret authority.
- Force-pushing or rebasing away reviewed provenance without explicit approval.
- Merging competing candidates merely to make the repository appear consistent.
- Publishing Pages, packages, manifests, compatibility claims, or capability certifications before their own approval gates pass.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0A | Freeze candidate inventory and review order | Architect | — | READY | Exact heads, bases, mergeability, workflows, review threads, supersession relationships, and protected history are recorded for PRs #2, #12, #13, historical PR #14, and PR #15. |
| P0B | Approve active identity and authority model | Architect + human authority | P0A | BLOCKED | Aequitas, Socrates, Jacob Thomas Redmond, historical aliases, declarative role records, human authority, and operational principals have distinct approved treatment with migration and rollback. |
| P0C | Reconcile one canonical compatibility-set head | Architect | P0A, P0B | BLOCKED | Existing review provenance is preserved; intended artifacts are integrated; retired or excluded identities and workflow authority are absent or explicitly quarantined; the resulting PR #2 head is mergeable and frozen. |
| P0D | Validate capability evidence and bounded self-edit review | Architect + independent reviewer | P0A | REVIEW | Evidence levels, genome review prompts, mutable-field scope, migration boundary, immutable-policy checks, hostile regressions, external disposition, rollback, and resulting-state requirements remain complete and non-authorizing. |
| P1 | Replay deterministic conformance at the frozen head | QSOBuilder | P0C | BLOCKED | Schemas, canonicalization, digest scopes, immutable policy, migrations, references, manifests, duplicates, conflicts, non-finite numbers, aliases, unknown fields, and hostile fixtures pass or fail closed as required. |
| P2 | Approve declarative identity versus operational authority ADR | Architect | P0B, P1 | REVIEW | ADR-0003 is accepted or revised; a valid genome cannot issue capabilities, credentials, approvals, or canonical state. |
| P3 | Assign format and adapter ownership | Architect | P1, portfolio format decision | BLOCKED | Generic QSO envelope/registry owner, genome-specific profile owner, any future QSIO adapter namespace, versions, round-trip rules, and golden vectors are approved. |
| P3A | Approve genome admission and runtime projection profile | Architect + Repository `1` owner + runtime owners | P2, P3 | REVIEW | Declarative validity, neutral conformance, Repository `1` admission, runtime/Fabric projections, execution receipts, reconciliation, correction, revocation, and recovery remain distinct and versioned. |
| P4 | Validate pairwise and triple-overlap gluing | Builders + independent verifier | P1, P2, P3, P3A | BLOCKED | Genome→Repository `1`→runtime, genome→runtime→Fabric, genome→neutral contract→conformance implementation, identity migration→admission→cache, immutable policy→capability→execution, correction/revocation→runtime/Fabric→interface, freeze→evidence→recovery, and replacement environment→re-admission→restart fixtures pass at immutable commits. |
| P5 | Accept and publish compatibility release | Architect + human authority | P4 | BLOCKED | One approved manifest, source archive, checksums, provenance, review dispositions, security/privacy report, downstream replay, rollback plan, and explicit publication approval exist. |
| P6 | Evaluate follow-on identities, experimenters, and governance automation | Architect | P5 and separate approvals | BLOCKED | Follow-on scope is independently versioned and cannot mutate the accepted compatibility set or grant runtime authority. |

## Cross-repository contract edges

The following contracts remain proposals until versioned and approved:

- `genome-admission-request/v0` — requester to Repository `1` quarantine;
- `genome-authority-admission/v0` — QSO-GENOMES evidence to Repository `1` operational decision;
- `genome-runtime-projection/v0` — admitted QSO-GENOMES set to QuantumStateObjects;
- `genome-fabric-projection/v0` — admitted QSO-GENOMES set to QSO-FABRIC;
- `genome-qsio-adapter/v0` — historical candidate; any future route requires an approved generic format/kernel owner;
- `genome-public-projection/v0` — QSO-GENOMES to QSO-STUDIO and AionUi;
- `qso-genome-self-edit-review/v1` — documentation-only proposal packet to independent review and external admission authority.

See `docs/genome-admission-and-runtime-projection-profile.md` for the candidate state machine, envelope, identities, checks, and witnesses; `docs/capability-evidence-and-self-edit-review.md` for evidence and mutation review; and `docs/obstruction-and-gluing.md` for the broader obstruction ledger.

## Builder rules

- Work only on the highest-priority `READY` task.
- Preserve every candidate branch, review thread, workflow result, artifact digest, and supersession record.
- Do not execute candidate repository code in a privileged workflow.
- Do not add runtime, credential, deployment, payment, or repository-write authority to genome artifacts.
- Do not infer active authority or demonstrated competence from aliases, persona names, workflow labels, local validity, conformance, benchmark results, runtime projection, or successful execution.
- Any change after a frozen review head requires an explicit exception, new exact-head evidence, and renewed downstream replay.

## Evidence rules

For every task, record:

- exact repository, branch, base, head, merge base, and review path;
- observed facts versus declarations, demonstrations, proposals, admissions, and approvals;
- commands, environments, tool and dependency versions;
- schema, profile, fixture, benchmark, and reason-code versions;
- canonical bytes and domain-separated digest scopes;
- exact self-edit paths, old and proposed values, per-freeze deltas, cumulative drift, and schema authority;
- request, quarantine, admission, capability, runtime-admission, execution, reconciliation, correction, revocation, and recovery identities;
- workflow URLs, logs, artifacts, hashes, and retention;
- identity migration, alias, correction, revocation, cache, and recovery effects;
- downstream acceptance and rejection results;
- limitations, residual risks, supersession, and rollback.

## Builder log

- 2026-07-23 — Added and synchronized the capability evidence and self-edit review packet, separating eight evidence levels, four self-edit classes, immutable ethics and authority boundaries, exact-field delta and drift accounting, independent disposition, rollback, restored-state verification, and FYSA-120 gap `031-T`; status remains `DOCUMENTED_NOT_ADMITTED`.
- 2026-07-21 — Added the genome admission and runtime projection profile, preserving distinct identities and state transitions across QSO-GENOMES, Repository `1`, QuantumStateObjects, QSO-FABRIC, `qsio-kernel`, and review interfaces without granting operational authority.
- 2026-07-20 — Added a portfolio obstruction and gluing ledger covering identity, authority, format, digest, lifecycle, mutation, freeze, manifest, downstream, QSIO, privacy, correction, freshness, governance, evidence, and recovery conflicts.
- 2026-07-20 — Added ADR-0003 proposing separation of declarative identity and policy from operational capability and canonical-state authority.
- 2026-07-20 — Reframed the active chain around explicit reconciliation of PRs #2, #12, #13, historical PR #14, and PR #15 before compatibility acceptance.
- 2026-07-16 to 2026-07-19 — Preserved PR #2 as the compatibility-set review path, identified default-branch divergence and identity scope conflict, and developed bounded validation and reconciliation repairs without authorizing release.

<!-- QSO-CONSENT-CAPACITY-LOCK-v1 -->
