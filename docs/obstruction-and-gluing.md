# Obstruction and Gluing Analysis

## Purpose

This ledger tests whether QSO-GENOMES can compose with the rest of A.L.I.S.T.A.I.R.E. without silently duplicating authority or allowing incompatible local definitions to appear globally consistent.

The method is engineering-oriented. Repositories are treated as local sections, versioned contracts as gluing maps, and shared fixtures or receipts as compatibility witnesses. The language is inspired by obstruction theory and homology, but this document does not claim a completed formal cohomology computation.

## Repository-local section

QSO-GENOMES owns declarative, non-executing definitions for:

- genome identity, purpose, traits, constraints, and lineage;
- immutable policy and forbidden-capability declarations;
- schema, migration, reference, and compatibility-manifest rules;
- canonical genome-byte and digest profiles;
- public projection and protected-commitment boundaries;
- deterministic validation expectations and release evidence.

It does not own runtime scheduling, message routing, ledger state, checkpoint execution, capability issuance, credentials, deployment, payment execution, repository mutation, or canonical operational state.

## Active obstructions

| ID | Obstruction | Conflicting local meanings | Risk | Required repair witness |
|---|---|---|---|---|
| G-01 | Review identity conflict | PR #2 retains Aequitas-bound compatibility semantics while PR #12 removes Aequitas and Socrates from active governance and transfers review responsibility to Jacob Thomas Redmond | A consumer may treat a retired persona or alias as active authority | One approved identity-migration record, exact artifact set, negative alias fixtures, downstream cache invalidation, and explicit human-authority boundary |
| G-02 | Declarative identity versus operational authority | Genome or Sprite records can describe roles, while Repository `1` is the candidate capability and canonical-state authority | A declarative record may be mistaken for a live credential or approval | Shared fixture proving genome policy constrains but never issues an operational capability |
| G-03 | Canonical format ownership | QSO-GENOMES defines `qso-canonical-json-v1`; QSO-FABRIC, `qsio-kernel`, and QSIO candidates also describe envelopes, registries, hashes, and serialization | Multiple canonical byte streams or registries can produce incompatible identities | Named owner for the generic envelope/registry plus a genome-specific canonicalization profile and cross-implementation golden vectors |
| G-04 | Digest-scope ambiguity | Artifact-byte digests and compatibility-manifest digests do not yet bind the same metadata set | A manifest may remain hash-valid while consumer-relevant identity fields drift | Versioned digest-scope schema, canonical field ordering, domain separation, and tamper fixtures |
| G-05 | Genome lifecycle versus runtime lifecycle | Genome revision and migration states overlap runtime states in QuantumStateObjects, QSO-FABRIC, and `qsio-kernel` | A declarative revision may be treated as a running-state transition | Separate state machines and a mapping table that forbids implicit activation |
| G-06 | Mutation semantics | QSO-GENOMES declares bounded mutations and migrations while runtime and Fabric candidates define mutation classes and application behavior | Different mutation classes can bypass immutable fields or lineage rules | Shared mutation vocabulary, immutable-field negative fixtures, and accepted migration receipts |
| G-07 | Freeze and Quietus semantics | Immutable policy can declare freeze constraints while runtime repositories own actual freeze, shutdown, and recovery | A declaration may be reported as an enforced stop when no runtime action occurred | Triple-overlap fixture linking genome rule, Repository `1` revocation or freeze decision, and runtime stop receipt |
| G-08 | Manifest acceptance versus canonical state | A compatibility manifest can pass local validation without being accepted by Repository `1` or replayed downstream | Local validation may be mistaken for portfolio acceptance | Explicit candidate/validated/accepted/superseded states and an authoritative acceptance receipt |
| G-09 | Downstream interpretation drift | QuantumStateObjects and QSO-FABRIC can independently map the same genome fields | Consumers may derive different identity, policy, or default behavior | Identical read-only fixtures and normalized consumer reports pinned to the same genome commit and manifest digest |
| G-10 | QSIO adapter overlap | PR #14 maps genome identity, revisions, traits, provenance, projections, commitments, and validation records into QSIO, while ownership of the generic QSIO contract remains unsettled | Adapter-local fields may become de facto portfolio schema | Adapter protocol owner, package namespace, supported-version matrix, and round-trip/tamper fixtures |
| G-11 | Public projection and protected commitment boundary | Public projections, protected commitments, evidence bundles, Pages, and interfaces have different exposure models | Sensitive fields or stable correlators may leak through documentation or UI | Data-classification matrix, redaction profile, non-correlation tests, and publication review |
| G-12 | Correction, supersession, and revocation | Immutable history, compatibility-set supersession, alias retirement, Repository `1` revocation, and downstream caches are not joined by one protocol | Retired identity or policy can remain active in a consumer | Versioned correction/revocation envelope, cache invalidation receipt, and bounded restart fixture |
| G-13 | Clock and freshness semantics | Genome artifacts are versioned by content and lineage, while operational consumers use time, expiry, and replay windows | A historically valid artifact may be operationally stale | Separate content identity from operational freshness and require Repository `1` policy at activation time |
| G-14 | Governance workflow versus genome contract | Repository workflows, reviewer identities, repair agents, and PR control planes can be represented beside compatibility artifacts | Repository automation may enter a runtime compatibility set accidentally | Explicit artifact classes and manifest allowlist excluding workflows, reviewers, and repair authority from runtime consumption |
| G-15 | Evidence vocabulary drift | `PASS`, `FAIL`, `UNKNOWN`, candidate, validated, accepted, released, deployed, superseded, and revoked are not uniformly mapped across repositories | Evidence can be promoted by terminology rather than authority | Portfolio reason-code and lifecycle mapping with fail-closed unknown-state fixtures |
| G-16 | Emergency recovery ownership | Genome rollback describes artifact supersession, but portfolio emergency stop and recovery are assigned elsewhere | Recovery may restore an artifact without restoring capability, runtime, or cache state consistently | One portfolio recovery sequence spanning genome manifest, Repository `1`, runtime, Fabric, interfaces, and evidence stores |

## Pairwise gluing edges

| Edge | Producer responsibility | Consumer responsibility | Required contract |
|---|---|---|---|
| QSO-GENOMES → QuantumStateObjects | Publish accepted declarative artifacts and compatibility manifest | Verify exact commit, paths, schema, canonical bytes, digests, references, immutable constraints, and lifecycle mapping | `genome-runtime-profile/v0` candidate |
| QSO-GENOMES → QSO-FABRIC | Publish collaboration-relevant identity and policy fields without runtime authority | Verify exact artifacts and refuse to redefine genome identity, immutable policy, or migration | `genome-fabric-profile/v0` candidate |
| QSO-GENOMES → `qsio-kernel` | Supply genome-specific serialization and identity profile | Provide generic semantic/format interfaces without owning genome policy | `genome-qsio-adapter/v0` candidate |
| QSO-GENOMES → Repository `1` | Supply reviewed policy, compatibility, and lineage evidence | Decide acceptance, capability compatibility, activation, revocation, and canonical disposition | `genome-authority-admission/v0` candidate |
| QSO-GENOMES → QSO-STUDIO/AionUi | Supply approved public projections and evidence summaries | Present read-only state with provenance, redaction, correction, and revocation indicators | `genome-public-projection/v0` candidate |
| ALISTAIRE- → QSO-GENOMES | Define constitutional role taxonomy and portfolio governance | Encode only approved declarative QSO identities and policy references | Governance-to-genome decision record and version pin |

## Required triple-overlap witnesses

### 1. Genome → runtime → Fabric

Prove that QuantumStateObjects and QSO-FABRIC consume the same immutable genome commit, manifest digest, canonicalization profile, identity, and policy values; reject stale, mutated, duplicate, conflicting, or unsupported artifacts identically; and do not infer authority from local execution.

### 2. Genome → Repository `1` → runtime

Prove that a locally valid genome is not operationally active until Repository `1` or an approved successor admits the exact artifact set under an explicit policy and issues any required bounded capability. Revocation or expiry must prevent new activation without rewriting genome history.

### 3. Genome → QSIO/kernel → runtime

Prove byte-stable round trips, domain-separated hashes, unknown-field behavior, supported-version negotiation, protected-field handling, and rejection of adapter-specific fields that are not in the genome contract.

### 4. Identity migration → alias resolver → downstream cache

Prove that approved migrations resolve only declared historical aliases, retired identities cannot regain active authority, stale caches are invalidated, historical provenance remains reachable, and unsupported aliases fail closed.

### 5. Immutable policy → freeze/revocation → recovery

Prove that an immutable-policy violation produces a Repository `1` freeze or revocation decision, a runtime and Fabric stop receipt, preserved evidence, no automatic unlock, and a bounded recovery using an approved manifest.

### 6. Public projection → interface → correction

Prove that QSO-STUDIO and AionUi display only approved projections, preserve exact source identity and redaction status, show correction/revocation state, and do not expose protected commitments or convert a display action into operational approval.

## Lowest-coupling ownership candidate

The smallest-overlap model is:

- QSO-GENOMES owns declarative genome schemas, immutable policy, lineage, migrations, compatibility manifests, and genome-specific canonicalization profiles.
- `qsio-kernel` or another explicitly approved package owns generic QSO envelope and serialization interfaces.
- QuantumStateObjects owns bounded local runtime interpretation and execution receipts.
- QSO-FABRIC owns multi-QSO collaboration and experiment orchestration.
- Repository `1` or an approved successor owns operational admission, capability issuance, revocation, canonical disposition, and recovery authority.
- `ALISTAIRE-` owns constitutional governance and role taxonomy.
- QSO-STUDIO and AionUi own read-only presentation of approved projections.

Repository location, file name, passing tests, or successful execution does not by itself establish canonical ownership.

## Architectural decisions still required

1. Approve the active supervisory and human-review identity model, including the Aequitas/Socrates/Jacob Thomas Redmond migration and historical-alias treatment.
2. Designate the generic QSO format, registry, envelope, and canonicalization owner.
3. Approve genome-specific digest scopes, domain separation, and manifest identity rules.
4. Assign ownership for mutation classes, lifecycle mapping, freeze, revocation, correction, supersession, and recovery.
5. Approve the Repository `1` admission and capability route for genome activation.
6. Approve public/protected projection, privacy, retention, publication, and cache-invalidation policy.
7. Pin shared pairwise and triple-overlap fixtures to immutable commits before any compatibility set becomes downstream-authoritative.

## Scope boundary

This analysis adds documentation and test requirements only. It does not alter genome artifacts, schemas, migrations, aliases, immutable policy, runtime behavior, adapters, credentials, capabilities, release state, publication, deployment, or canonical operational state.

<!-- QSO-CONSENT-CAPACITY-LOCK-v1 -->
