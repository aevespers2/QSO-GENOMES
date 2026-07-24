# Project overview

## Purpose

QSO-GENOMES defines the portable, declarative contract layer used to describe bounded Quantum State Objects before any runtime is allowed to instantiate or coordinate them. The repository separates **what a QSO is permitted to be** from **how another repository executes or schedules it**.

The near-term product objective is deliberately narrow: publish one independently reviewed Atlas/Nova/Orion/Lyra compatibility set whose schemas, immutable rules, references, canonical bytes, manifest identity, migrations, provenance, and downstream behavior can be reproduced from one accepted commit.

## Intended readers

| Reader | What this repository provides |
|---|---|
| Contract authors | schemas, identity rules, migration requirements, canonicalization, and review expectations |
| Runtime developers | a read-only manifest and fail-closed consumer contract |
| Security reviewers | explicit authority exclusions, immutable constraints, hostile-input cases, and provenance requirements |
| Release reviewers | gate definitions, evidence requirements, versioning, rollback, and downstream replay expectations |
| Documentation contributors | a traceable vocabulary that distinguishes proposal, candidate, accepted, released, and deployed states |

## Product boundaries

### In scope

- Declarative QSO identity and purpose.
- Immutable ethics and forbidden-capability rules.
- Mutable preference boundaries and proposal-only change semantics.
- Resource, communication, and freeze-point limits.
- Schema validation and unknown-field policy.
- Canonical serialization and cryptographic digest scopes.
- Compatibility manifests and source-derived identity fields.
- Supervisory definitions approved for the versioned compatibility set.
- Migration records, fixtures, and rollback metadata.
- Provenance, evidence, and downstream verification requirements.

### Out of scope

- Executing a genome.
- Fetching external knowledge.
- Running tools, shell commands, installers, or arbitrary code.
- Holding credentials or making account changes.
- Performing transactions or settlement.
- Deploying a service or coordinating production workloads.
- Allowing a QSO to commit its own genome changes.
- Treating documentation, a generated report, or a configured workflow as release approval.

## Dependency direction

The intended dependency direction is one-way:

1. QSO-GENOMES publishes an approved declarative compatibility set.
2. `QuantumStateObjects` validates and consumes that set without writing back to it.
3. `QSO-FABRIC` validates the same accepted identities when coordinating bounded experiments.
4. `QSO-SEEKER` supplies sanitized knowledge records through its own contract; genomes do not retrieve network content directly.

A downstream repository may add stricter local limits. It may not weaken, reinterpret, silently normalize, or replace an upstream immutable rule.

## Lifecycle vocabulary

| State | Meaning |
|---|---|
| Proposed | an idea or design record exists; implementation is not implied |
| Candidate | artifacts exist for review; acceptance is not implied |
| Verified | named checks passed against an exact immutable head with retained evidence |
| Accepted | authorized reviewers approved the exact versioned artifact set |
| Released | a versioned manifest and evidence bundle were published from the accepted head |
| Deployed | a runtime or service is operating; this repository does not own that state |

These terms must not be collapsed. A candidate may be complete enough to review while still being unsafe or unsuitable to release.

## Current objective and hold points

The root task chain places reconciliation and scope containment before further acceptance work. The current alpha path requires:

1. preserve one canonical compatibility-review path;
2. reconcile it with current `main` without rewriting reviewed history;
3. exclude or separately quarantine unapproved supervisory and governance additions;
4. freeze one mergeable submitted head;
5. replay the complete deterministic and hostile-input suite;
6. disposition material review findings against that head;
7. validate the same accepted manifest read-only in both downstream consumers;
8. publish only after explicit approval.

Any documentation that appears to bypass these hold points is incorrect and must be repaired before merge.

## Success measures

A successful first release is not measured by file count. It is measured by whether an independent consumer can:

- locate one approved manifest without branch ambiguity;
- derive artifact identities from the source documents;
- reproduce canonical bytes and digests;
- verify immutable and forbidden-capability rules;
- reject duplicate, conflicting, stale, unknown, weakened, non-finite, overflowed, or unresolved data;
- confirm the approved supervisory identity and references;
- replay migration and rollback fixtures;
- preserve evidence linking every claim to one accepted commit.

## Documentation maintenance rule

Every material documentation change should answer four questions:

1. Which existing repository contract or lifecycle record does this explain?
2. Does it describe current accepted behavior, a candidate, or a future design?
3. What evidence would prove the statement?
4. Could a consumer mistake the statement for new authority or implementation scope?

If the fourth answer is yes, revise the wording or add an explicit boundary.

<!-- QSO-CONSENT-CAPACITY-LOCK-v1 -->
