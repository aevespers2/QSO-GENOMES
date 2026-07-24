# ADR-0001: Keep QSO-GENOMES declarative and non-executing

- **Status:** Accepted repository boundary; release implementation remains pending.
- **Decision owners:** Repository and release reviewers.
- **Scope:** QSO-GENOMES architecture.

## Context

Genome definitions influence what downstream Quantum State Objects may do. Combining those definitions with executable behavior, network access, credentials, package installation, or self-modifying repository logic would blur the distinction between reviewed policy data and runtime authority. It would also make independent canonicalization, hashing, migration, and downstream verification substantially harder.

## Decision

QSO-GENOMES remains a declarative contract authority.

- Genome, policy, supervisory, migration, and manifest artifacts are data.
- Runtime execution belongs in downstream repositories.
- External knowledge retrieval belongs behind the QSO-SEEKER contract.
- Immutable fields are enforced outside QSO-writable state.
- A QSO may propose a mutable preference change but cannot commit its own upstream contract.
- No genome grants shell, arbitrary-code, package-install, credential, direct-network, payment, deployment, or self-replication authority.
- Consumers load approved artifacts read only and fail closed.

## Consequences

### Positive

- Contracts can be reviewed and hashed independently of runtime code.
- Authority is easier to audit and minimize.
- Downstream consumers can reproduce the same interpretation.
- Immutable rules remain outside the state they constrain.
- Releases can be versioned as portable data bundles.

### Costs

- Runtime features require explicit contracts between repositories.
- Contract changes may require coordinated migrations and downstream replay.
- Proposals cannot take effect until an external review and release process commits them.
- Validation must include semantic authority checks, not only schema parsing.

## Rejected alternatives

### Embed executable hooks in genomes

Rejected because code identity, dependencies, sandboxing, and tool authority would become part of the genome contract and greatly expand the attack and review surface.

### Permit runtime write-back to upstream genomes

Rejected because the constrained object could alter the rules constraining it and because repository provenance would no longer remain human controlled.

### Treat schemas as sufficient safety enforcement

Rejected because schema-valid data can still introduce excessive authority, ambiguous aliases, weakened policies, or inconsistent cross-document references.

## Verification

This boundary is verified through:

- file and schema review;
- forbidden-capability validation;
- semantic authority checks;
- complete-set manifest review;
- exact-head evidence;
- downstream read-only consumption tests;
- rejection of any artifact requiring execution to interpret.

## Change rule

Changing this decision requires a separately approved architecture, security review, versioned migration, downstream compatibility plan, hostile-input suite, rollback plan, and explicit product approval. It must not be introduced as an incidental field or documentation clarification.

<!-- QSO-CONSENT-CAPACITY-LOCK-v1 -->
