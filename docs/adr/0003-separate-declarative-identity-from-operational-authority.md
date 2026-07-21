# ADR-0003: Separate Declarative Identity from Operational Authority

- Status: proposed
- Date: 2026-07-20
- Scope: QSO-GENOMES and downstream A.L.I.S.T.A.I.R.E. consumers

## Context

QSO-GENOMES stores declarative identity, policy, lineage, migration, and supervisory-role records. Several repository candidates also discuss active reviewers, repair agents, capabilities, runtime roles, and canonical state. This creates a recurring ambiguity: a valid declarative record can be mistaken for a credential, approval, runtime activation, or authority grant.

The conflict is visible in the current review paths. PR #2 carries Aequitas-oriented compatibility semantics, while PR #12 proposes removal of active Aequitas and Socrates governance surfaces and transfer of review responsibility to Jacob Thomas Redmond. PR #14 maps genome records into a QSIO adapter while generic format and capability ownership remain unresolved.

## Decision candidate

QSO-GENOMES will remain the authority for **declarative identity and policy data only**. Operational authority will remain external and independently granted.

Under this separation:

1. A genome or Sprite record may describe an identity, responsibility, policy, constraint, lineage, or compatibility requirement.
2. A genome or Sprite record cannot itself issue credentials, capabilities, approvals, merge authority, deployment authority, payment authority, or canonical operational state.
3. Repository `1` or another explicitly approved authority service decides operational admission, capability issuance, expiry, revocation, and recovery.
4. Human review authority is recorded in governance decisions and repository protections; a historical persona alias does not grant current authority.
5. Runtime consumers must verify both the accepted declarative artifact set and any independently issued operational capability.
6. Execution success is evidence only and does not retroactively make the genome, capability, or result canonical.

## Identity migration rule

An identity migration must distinguish:

- historical provenance identity;
- declarative contract identity;
- current human or service authority identity;
- compatibility alias;
- retired alias;
- operational principal.

Aliases are inert unless an approved migration explicitly assigns a bounded resolution purpose. Retired aliases remain reachable for provenance but cannot resolve to active authority. Downstream caches must receive correction or revocation evidence when an active identity changes.

## Consequences

### Positive

- prevents a data file from becoming a credential or approval channel;
- allows genome history to remain immutable while operational authority expires or is revoked;
- reduces overlap between QSO-GENOMES, Repository `1`, QuantumStateObjects, QSO-FABRIC, and governance workflows;
- supports clear negative fixtures for retired identities, unsupported aliases, stale capabilities, and wrong-device or wrong-environment activation;
- preserves human control over consequential actions.

### Costs

- consumers must validate two related but distinct layers: declarative compatibility and operational authority;
- identity migration requires cache invalidation and explicit historical treatment;
- shared schemas and fixtures are required across multiple repositories;
- existing candidate records may require reclassification or migration.

## Alternatives considered

### Genome records directly grant authority

Rejected because repository data would become a credential and capability-issuance channel, weakening separation of duties and revocation.

### Runtime consumers infer authority from accepted genomes

Rejected because different consumers could infer different permissions and because acceptance does not establish current operational context.

### Remove all supervisory and human identity references from genome contracts

Not universally required. Declarative role references may be useful, but they must remain non-operational and versioned. Specific active identities still require explicit approval.

## Acceptance conditions

This ADR is ready for acceptance when:

- the active Aequitas/Socrates/Jacob Thomas Redmond identity migration is approved or replaced;
- the Repository `1` or successor admission and capability contract is approved;
- genome, capability, execution-receipt, correction, and revocation schemas have named owners;
- QuantumStateObjects and QSO-FABRIC pass shared positive, negative, stale, alias, revocation, and recovery fixtures;
- public interfaces display declarative identity separately from operational authority;
- rollback and historical-provenance treatment are documented.

## Non-decision

This ADR does not approve any current identity migration, genome artifact, compatibility set, capability authority, adapter, release, publication, or deployment.

<!-- QSO-CONSENT-CAPACITY-LOCK-v1 -->
