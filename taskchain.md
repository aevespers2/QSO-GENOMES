# Task Chain

## Repository role

QSO-GENOMES is the declarative contract authority for QSO identity, purpose, immutable policy, lineage, migration, compatibility manifests, and genome-specific canonicalization. It is an upstream dependency of `QuantumStateObjects`, `QSO-FABRIC`, `qsio-kernel` or another approved generic format package, Repository `1` or another approved capability authority, and read-only interfaces.

A genome is data. This repository does not own runtime execution, capability issuance, credentials, deployment, payment execution, repository mutation, or canonical operational state.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

### Next objective

Reconcile the compatibility-set, identity-migration, workflow-repair, QSIO-adapter, and documentation candidates into one explicitly ordered review plan, then prove a four-boundary integration model—declarative validity, neutral conformance, operational admission, and runtime projection—without force-rewriting history or allowing any branch, genome, passing test, or successful execution to become authoritative by existence alone.

### Intended user outcome

A downstream consumer can retrieve one reviewed Atlas/Nova/Orion/Lyra contract set; verify exact paths, schema versions, canonical bytes, digest scopes, immutable policy, lineage, migrations, references, public/protected projections, and manifest identity; distinguish declarative validity from neutral conformance, Repository `1` operational admission, runtime projection, execution, and canonical reconciliation; and fail closed when any artifact, alias, version, capability, admission, receipt, correction, revocation, or recovery reference is missing or inconsistent.

### Current candidate map

| Candidate | Purpose | Observed state | Authority boundary |
|---|---|---|---|
| PR #2 | Four-genome compatibility-set review path | Draft, non-mergeable, exact head `1259693433814129f44d0255b5e0ecf741d9a79b`; no surfaced exact-head workflow evidence for that head | Candidate artifacts only; not accepted, published, or downstream-authoritative |
| PR #12 | Remove active Aequitas and Socrates governance identities and transfer review responsibility to Jacob Thomas Redmond | Draft, non-mergeable, exact head `622530232248a8df8c24c91ed09ce58f66988e63`; bounded conformance and reconciliation checks reported successful | Identity-migration candidate only; historical provenance remains reachable |
| PR #13 | Reconciliation and Consent Capacity Lock repair path | Draft, non-mergeable, exact head `4a638f064d0d4e11cbc94eb14b23ad60586e8a60`; later focused repairs merged through PRs #16 and #18 | No automatic final merge, publication, or runtime authority |
| PR #14 | QSIO cross-repository adapter | Draft, mergeable, exact head `992d8263bf62666fd6a05152cc0f6ad16791706c`; contract and replay fixtures remain | Disabled integration candidate; generic QSIO ownership remains unresolved |
| PR #15 | Pages, architecture, onboarding, gluing, genome admission/runtime projection, and lifecycle documentation | Draft, mergeable; documentation-only | No genome, schema, alias, runtime, capability, admission, release, or publication approval |

These snapshots are review evidence, not durable release identifiers. Reconfirm exact states before any acceptance action.

### Priority

**P0 — BLOCKED on identity, ownership, canonical-head, admission-authority, and shared-fixture decisions.**

The portfolio must not accept PR #2 while PR #12 proposes a conflicting active identity model, must not activate PR #14 while generic QSO format ownership is unresolved, and must not treat PR #15 documentation success as compatibility-set acceptance, Repository `1` admission, runtime activation, or Pages publication approval.

## Success criteria

- One explicit merge and supersession order is approved for PRs #2, #12, #13, #14, and #15.
- One active supervisory and human-review identity model is approved, including historical aliases, retirement, cache invalidation, and rollback.
- One immutable compatibility-set head becomes mergeable and passes exact-head conformance with retained evidence.
- QSO-GENOMES remains declarative and non-executing.
- Generic QSO envelope, registry, serialization, and capability ownership are assigned outside or explicitly shared with genome-specific profiles.
- Artifact-byte and complete-manifest digest scopes are versioned and domain-separated.
- Repository `1` or another approved authority distinguishes local genome validity from operational admission, capability issuance, activation, revocation, reconciliation, and recovery.
- QuantumStateObjects and QSO-FABRIC derive compatible projections from the same admitted genome commit and reject the same hostile fixtures.
- `qsio-kernel` or another verifier reproduces neutral conformance vectors without becoming the operational runtime or authority.
- Public interfaces expose only approved projections and preserve provenance, correction, revocation, redaction, uncertainty, and admission state.
- Release evidence distinguishes proposed, implemented, locally valid, conformant, admitted, runtime-eligible, executed, reconciled, accepted, published, released, deployed, superseded, frozen, and revoked states.

## Non-goals

- Executable agent behavior or unrestricted autonomous mutation.
- Treating a genome, Sprite, alias, reviewer record, workflow, passing test, adapter result, runtime projection, or successful execution as a credential or approval.
- Adding network, repository-write, payment, deployment, infrastructure, or secret authority.
- Force-pushing or rebasing away reviewed provenance without explicit approval.
- Merging competing candidates merely to make the repository appear consistent.
- Publishing Pages, packages, manifests, or compatibility claims before their own approval gates pass.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0A | Freeze candidate inventory and review order | Architect | — | READY | Exact heads, bases, mergeability, workflows, review threads, supersession relationships, and protected history are recorded for PRs #2, #12, #13, #14, and #15. |
| P0B | Approve active identity and authority model | Architect + human authority | P0A | BLOCKED | Aequitas, Socrates, Jacob Thomas Redmond, historical aliases, declarative role records, human authority, and operational principals have distinct approved treatment with migration and rollback. |
| P0C | Reconcile one canonical compatibility-set head | Architect | P0A, P0B | BLOCKED | Existing review provenance is preserved; intended artifacts are integrated; retired or excluded identities and workflow authority are absent or explicitly quarantined; the resulting PR #2 head is mergeable and frozen. |
| P1 | Replay deterministic conformance at the frozen head | QSOBuilder | P0C | BLOCKED | Schemas, canonicalization, digest scopes, immutable policy, migrations, references, manifests, duplicates, conflicts, non-finite numbers, aliases, unknown fields, and hostile fixtures pass or fail closed as required. |
| P2 | Approve declarative identity versus operational authority ADR | Architect | P0B, P1 | REVIEW | ADR-0003 is accepted or revised; a valid genome cannot issue capabilities, credentials, approvals, or canonical state. |
| P3 | Assign format and adapter ownership | Architect | P1, portfolio format decision | BLOCKED | Generic QSO envelope/registry owner, genome-specific profile owner, QSIO adapter namespace, versions, round-trip rules, and golden vectors are approved. |
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
- `genome-qsio-adapter/v0` — QSO-GENOMES to the approved generic format/kernel owner;
- `genome-public-projection/v0` — QSO-GENOMES to QSO-STUDIO and AionUi.

See `docs/genome-admission-and-runtime-projection-profile.md` for the candidate state machine, envelope, identities, checks, and witnesses, and `docs/obstruction-and-gluing.md` for the broader obstruction ledger.

## Builder rules

- Work only on the highest-priority `READY` task.
- Preserve every candidate branch, review thread, workflow result, artifact digest, and supersession record.
- Do not execute candidate repository code in a privileged workflow.
- Do not add runtime, credential, deployment, payment, or repository-write authority to genome artifacts.
- Do not infer active authority from aliases, persona names, workflow labels, local validity, conformance, runtime projection, or successful execution.
- Any change after a frozen review head requires an explicit exception, new exact-head evidence, and renewed downstream replay.

## Evidence rules

For every task, record:

- exact repository, branch, base, head, merge base, and review path;
- observed facts versus proposals and approvals;
- commands, environments, tool and dependency versions;
- schema, profile, fixture, and reason-code versions;
- canonical bytes and domain-separated digest scopes;
- request, quarantine, admission, capability, runtime-admission, execution, reconciliation, correction, revocation, and recovery identities;
- workflow URLs, logs, artifacts, hashes, and retention;
- identity migration, alias, correction, revocation, cache, and recovery effects;
- downstream acceptance and rejection results;
- limitations, residual risks, supersession, and rollback.

## Builder log

- 2026-07-21 — Added the genome admission and runtime projection profile, preserving distinct identities and state transitions across QSO-GENOMES, Repository `1`, QuantumStateObjects, QSO-FABRIC, `qsio-kernel`, and review interfaces without granting operational authority.
- 2026-07-20 — Added a portfolio obstruction and gluing ledger covering identity, authority, format, digest, lifecycle, mutation, freeze, manifest, downstream, QSIO, privacy, correction, freshness, governance, evidence, and recovery conflicts.
- 2026-07-20 — Added ADR-0003 proposing separation of declarative identity and policy from operational capability and canonical-state authority.
- 2026-07-20 — Reframed the active chain around explicit reconciliation of PRs #2, #12, #13, #14, and #15 before compatibility acceptance.
- 2026-07-16 to 2026-07-19 — Preserved PR #2 as the compatibility-set review path, identified default-branch divergence and identity scope conflict, and developed bounded validation and reconciliation repairs without authorizing release.

<!-- QSO-CONSENT-CAPACITY-LOCK-v1 -->
