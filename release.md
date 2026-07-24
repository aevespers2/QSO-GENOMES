# Release Plan

## Current decision

Status: `BLOCKED — IDENTITY, CANONICAL HEAD, FORMAT OWNERSHIP, CAPABILITY EVIDENCE, ADMISSION AUTHORITY, GLUING EVIDENCE, AND APPROVAL REQUIRED`

QSO-GENOMES remains the declarative upstream contract authority for the initial Atlas/Nova/Orion/Lyra set. No compatibility release or capability certification is ready. The repository currently has several interacting or historical candidates:

- PR #2 — four-genome compatibility-set review path, draft and non-mergeable at observed head `1259693433814129f44d0255b5e0ecf741d9a79b`;
- PR #12 — active-identity migration removing Aequitas and Socrates governance surfaces and transferring review responsibility to Jacob Thomas Redmond, draft and non-mergeable at `622530232248a8df8c24c91ed09ce58f66988e63`;
- PR #13 — reconciliation and Consent Capacity Lock repair path, draft and non-mergeable at `4a638f064d0d4e11cbc94eb14b23ad60586e8a60`, with focused repairs later merged through PRs #16 and #18;
- PR #14 — closed unmerged historical QSIO adapter candidate at `992d8263bf62666fd6a05152cc0f6ad16791706c`; no active adapter or generic format ownership follows from it;
- PR #15 — Pages, architecture, onboarding, gluing, genome admission/runtime projection, capability-evidence, bounded self-edit, and lifecycle documentation candidate, draft and mergeable.

The capability-evidence and self-edit packet remains `DOCUMENTED_NOT_ADMITTED`. These states must be recaptured before any acceptance action. Candidate existence, mergeability, passing checks, documentation success, local validity, fixture success, benchmark success, neutral conformance, runtime admission, or successful execution does not establish release, competence, or operational authority.

## Versioning

- Scheme: Semantic Versioning for compatibility manifests and genome-specific profiles.
- First eligible compatibility candidate: `0.1.0-alpha.1` after identity, scope, format, evidence, admission, and projection reconciliation.
- Compatible corrections may be patch versions.
- Compatible optional fields, genomes, projections, or fixtures may be minor versions.
- Schema, immutable-policy, canonicalization, digest-scope, supervisory-identity, lineage, migration, forbidden-capability, self-edit vocabulary, admission, projection, correction, revocation, or reference breaks require a declared breaking version and migration fixtures.
- Generic QSO envelope, identity namespace, registry, or serialization versions must be owned separately from genome-specific profiles unless an explicit ownership decision states otherwise.
- Capability-evidence profiles, benchmark protocols, and self-edit review packets require their own versions, source identities, correction routes, and supersession records.
- No version or tag may be assigned until one immutable accepted head and complete evidence bundle exist.

## Candidate release scope

The first eligible release may contain only:

- approved Atlas, Nova, Orion, and Lyra genome documents;
- approved declarative supervisory or role records, if any;
- genome and Sprite schemas;
- approved immutable-policy and forbidden-capability contracts;
- lineage and migration records;
- genome-specific canonicalization and domain-separated digest profiles;
- one complete compatibility manifest with source-derived identity fields;
- approved admission and projection profile definitions that remain non-operational;
- approved capability-evidence and self-edit review profile definitions that remain non-operational;
- deterministic positive, negative, boundary, duplicate, conflict, unknown-field, alias, tamper, stale, replay, non-finite-number, unsupported-version, wrong-device, wrong-workspace, migration, correction, revocation, freeze, recovery, and rollback fixtures;
- exact-head validation and downstream read-only replay evidence;
- provenance, review dispositions, security/privacy classification, supersession, and rollback records.

Explicitly excluded unless separately approved:

- runtime execution, scheduling, message routing, ledgers, checkpoints, orchestration, or runtime state;
- capability issuance, credentials, repository writes, payment execution, deployment, infrastructure changes, or canonical operational state;
- unapproved Aequitas or Socrates aliases or authority;
- repair-pull-request authority inside compatibility artifacts;
- PR-control-plane or scheduled governance automation;
- generic QSO format ownership asserted solely by repository location;
- operational admission, activation, capability authority, or self-edit commitment implemented inside QSO-GENOMES;
- capability certification inferred from genome declarations, schema validation, fixtures, benchmarks, conformance, or runtime success;
- Pages, package, profile, or manifest publication without explicit publication approval.

## Identity and authority gate

Release cannot proceed until the portfolio approves or replaces ADR-0003 and records distinct treatment for:

- historical provenance identities;
- declarative contract identities;
- current human review authority;
- compatibility aliases;
- retired aliases;
- operational service principals;
- Repository `1` or successor admission, capability, revocation, reconciliation, and recovery authority.

A genome or Sprite may constrain operational behavior but cannot itself grant credentials, capabilities, admissions, approvals, merges, releases, deployments, payments, or canonical state.

## Capability evidence and self-edit gate

Release and capability claims cannot proceed until:

- `DECLARED`, `STRUCTURALLY_VALID`, `FIXTURE_DEMONSTRATED`, `BENCHMARK_DEMONSTRATED`, `INDEPENDENTLY_REPRODUCED`, `ADMISSION_ELIGIBLE`, `OPERATIONALLY_ADMITTED`, and `RESULTING_STATE_VERIFIED` remain distinct;
- every capability claim names its exact genome artifact, manifest, policy, fixture or benchmark, environment, limitations, uncertainty, and independent reproduction state;
- every ordinary mutable-field proposal identifies exact paths, prior and proposed values, per-freeze delta, cumulative drift, schema authority, rationale, consumer impact, and rollback;
- every new field, interpretation rule, schema change, canonicalization change, or semantic broadening uses a versioned migration rather than an ordinary mutable edit;
- immutable policy and forbidden capabilities remain outside genome-writable state;
- independent ethics, safety, privacy, compatibility, and manipulation-resistance review passes;
- an external authorized reviewer records disposition and a separate admission authority remains required;
- rollback is rehearsed and resulting restored state is independently verified.

No genome signature, preference, benchmark score, workflow result, or successful execution may authorize a self-edit or promote evidence into authority.

## Format and digest gate

Release cannot proceed until:

- the generic QSO envelope, registry, identity namespace, serialization, canonicalization interface, and package owner are designated;
- QSO-GENOMES owns a bounded genome-specific canonicalization profile rather than an ambiguous portfolio-wide format;
- artifact-byte and complete-manifest digest scopes are named, versioned, domain-separated, and independently reproduced;
- duplicate keys, invalid UTF-8, non-finite numbers, unsupported versions, unknown critical fields, and tampering fail closed;
- any future QSIO adapter passes approved round-trip and cross-implementation golden vectors.

## Admission and projection gate

Release cannot proceed until `docs/genome-admission-and-runtime-projection-profile.md` is accepted or revised and the portfolio proves four distinct boundaries:

1. **Declarative validity** — QSO-GENOMES verifies artifact, policy, lineage, migration, manifest, and genome-specific canonicalization integrity.
2. **Neutral conformance** — an approved independent contract implementation reproduces canonical vectors without granting operational authority.
3. **Operational admission** — Repository `1` or an approved successor admits, rejects, revokes, reconciles, and recovers an exact genome set under explicit policy.
4. **Runtime projection and execution** — QuantumStateObjects and QSO-FABRIC derive bounded views, enforce separate capabilities, and produce receipts without creating canonical acceptance.

The following record identities must remain distinct: genome artifact, revision, compatibility manifest, policy commitment, self-edit proposal, capability-evidence record, benchmark record, independent-review record, admission request, quarantine record, admission decision, capability, runtime admission, runtime instance, Fabric experiment, conformance run, execution receipt, reconciliation, correction, revocation, and recovery checkpoint.

## Gluing gate

The following pairwise profiles must be versioned and tested:

- `genome-admission-request/v0`;
- `genome-authority-admission/v0`;
- `genome-runtime-projection/v0`;
- `genome-fabric-projection/v0`;
- any future `genome-qsio-adapter` profile under an approved owner;
- `genome-public-projection/v0`;
- `qso-genome-self-edit-review/v1`.

The following triple-overlap witnesses must pass at immutable commits:

1. genome → Repository `1` → runtime;
2. genome → runtime → Fabric;
3. genome → neutral contract → conformance implementation;
4. identity migration → admission → downstream cache;
5. immutable policy → capability → execution;
6. declared capability → independent evidence → admission decision;
7. self-edit proposal → immutable-policy review → rollback/restored state;
8. correction/revocation → runtime/Fabric → interface;
9. freeze → evidence preservation → recovery;
10. replacement environment → re-admission → bounded restart.

## Acceptance gates

| Gate | Status | Requirement |
|---|---|---|
| Candidate inventory | REVIEW | Reconfirm PR #2/#12/#13/historical #14/#15 heads, bases, mergeability, checks, artifacts, review threads, supersession, and protected history. |
| Review order | BLOCKED | Approve one merge, reconciliation, and supersession sequence. |
| Identity model | BLOCKED | Approve Aequitas/Socrates/Jacob Thomas Redmond migration and historical alias treatment. |
| Canonical compatibility head | FAIL | Produce one mergeable immutable PR #2 head without losing review provenance. |
| Declarative authority boundary | REVIEW | Accept or revise ADR-0003 and prove genome records cannot issue operational authority. |
| Capability evidence and self-edit review | REVIEW / BLOCKED | Packet is `DOCUMENTED_NOT_ADMITTED`; frozen-head evidence, independent reproduction, external disposition, admission authority, rollback, and resulting-state verification remain absent. |
| Deterministic conformance | NO EVIDENCE | Complete suite must pass at the frozen head with retained evidence. |
| Digest and manifest identity | PARTIAL | Candidate mechanisms exist; final scope, domain separation, and independent replay remain. |
| Generic format ownership | BLOCKED | Designate envelope, registry, namespaces, serialization, fixture, and package owner. |
| QSIO adapter | WITHDRAWN / HISTORICAL | PR #14 is closed unmerged; any future route requires approved ownership and compatibility fixtures. |
| Genome admission profile | REVIEW | Candidate profile exists; Repository `1` authority, record identities, schemas, and fixtures remain unapproved. |
| Downstream runtime/Fabric | BLOCKED | Both consumers must derive compatible projections from the same admitted commit and hostile fixtures. |
| Neutral conformance | BLOCKED | `qsio-kernel` or another verifier must reproduce vectors without becoming operational authority. |
| Repository `1` admission | BLOCKED | Local validity and conformance must remain distinct from admission, capability, activation, revocation, reconciliation, and recovery. |
| Privacy and public projection | BLOCKED | Classify projections, commitments, evidence, identifiers, retention, correction, and publication. |
| Freeze and recovery | BLOCKED | Prove policy violation, revocation, runtime/Fabric stop, evidence preservation, no automatic unlock, re-admission, and bounded restart. |
| Documentation | REVIEW | Pages-ready documentation, capability-review validation, strict build, and consent lock pass on the current non-default candidate; this is not acceptance. |
| Publication | PENDING | Explicit approval required for Pages, manifest, package, tag, profile, compatibility, or capability claims. |
| Final approval | PENDING | Human approval only after every blocking gate passes. |

## Artifact requirements

- approved schemas, four-genome set, immutable policy, migrations, lineage, and any approved supervisory records;
- compatibility manifest with exact source identities and digest scopes;
- generic-format ownership decision and genome-specific profile;
- identity-migration and historical-alias record;
- capability-evidence records, benchmarks, independent reproductions, self-edit packets, dispositions, and limitations;
- Repository `1` admission/capability/revocation/reconciliation/recovery boundary;
- runtime and Fabric projection profiles;
- positive, negative, stale, replay, tamper, duplicate, conflict, alias, wrong-device, wrong-workspace, broadened-capability, correction, revocation, freeze, partial-failure, recovery, and rollback fixtures;
- pairwise and triple-overlap reports;
- clean-checkout exact-head conformance logs;
- downstream QuantumStateObjects, QSO-FABRIC, and neutral verifier reports;
- public/protected data-classification and retention record;
- review-thread disposition map;
- source archive, dependency record, checksums, provenance manifest, supersession record, incident plan, and rollback instructions.

## Rollback criteria

Reject, supersede, or roll back the candidate if:

- reconciliation loses reviewed history or changes the accepted artifact set without renewed review;
- a retired identity or alias regains active authority;
- declarative data becomes a credential, capability, admission, approval, or runtime control channel;
- a declaration, schema pass, fixture, benchmark, conformance run, projection, display, or execution is presented as broader competence or authority than its evidence supports;
- a self-edit weakens immutable ethics, expands forbidden capabilities, lacks exact delta/drift accounting, bypasses external review, or cannot be restored;
- generic format and genome-specific profile ownership conflict;
- canonical bytes, digest scopes, manifests, or source identities disagree;
- local validity, conformance, admission, runtime projection, execution, reconciliation, and release states collapse;
- runtime and Fabric interpret the same field differently;
- Repository `1`, runtime, Fabric, or an interface treats local validation, conformance, display, or execution success as automatic canonical acceptance;
- wrong-device, wrong-workspace, wrong-runtime, stale, replayed, expired, revoked, or superseded inputs are admitted;
- correction, revocation, cache invalidation, freeze, re-admission, or recovery does not propagate consistently;
- private or protected data appears in public Pages or artifacts;
- exact-head evidence is missing, stale, or tied to another commit;
- any required fixture fails;
- publication or release occurs without explicit approval.

Preserve all failed candidates, evidence, hashes, review dispositions, admissions, receipts, corrections, revocations, and supersession records.

## Release log

- 2026-07-23 — Added and synchronized the `DOCUMENTED_NOT_ADMITTED` capability-evidence and bounded self-edit review packet, evidence ladder, immutable ethics gates, external disposition, rollback, hostile validation, exact-head evidence, and FYSA-120 mapping; no capability, self-edit, admission, release, or publication was approved.
- 2026-07-21 — Added the genome admission and runtime projection profile and new release gates separating declarative validity, neutral conformance, Repository `1` admission, runtime/Fabric projection, execution, reconciliation, and recovery.
- 2026-07-20 — Added portfolio obstruction and gluing analysis and ADR-0003 separating declarative identity from operational authority.
- 2026-07-20 — Reframed release gating around explicit reconciliation of PRs #2, #12, #13, historical PR #14, and PR #15; generic format ownership; Repository `1` admission; pairwise and triple-overlap witnesses; privacy; correction; revocation; freeze; and recovery.
- 2026-07-19 — Added a comprehensive Pages-ready documentation candidate with strict exact-head validation.
- 2026-07-16 to 2026-07-18 — Established PR #2 as the compatibility-set review path, identified branch divergence and identity-scope conflict, and added bounded validation and reconciliation repairs without release approval.

<!-- QSO-CONSENT-CAPACITY-LOCK-v1 -->
