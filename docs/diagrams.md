# Diagrams

The diagrams in this page are explanatory. They do not override schemas, lifecycle records, accepted manifests, or review decisions.

## Portfolio dependency direction

```mermaid
flowchart LR
    G[QSO-GENOMES\nDeclarative contracts]
    S[QSO-SEEKER\nSanitized knowledge records]
    Q[QuantumStateObjects\nBounded runtime]
    F[QSO-FABRIC\nExperiment coordination]

    G -->|approved manifest, read only| Q
    G -->|same approved identity, read only| F
    S -->|bounded canonical records| Q
    Q -->|validated QSO state and evidence| F

    Q -. no genome write-back .-> G
    F -. no genome write-back .-> G
```

## Repository layers

```mermaid
flowchart TB
    A[Source contracts]
    B[Schemas and reference bindings]
    C[Strict parsing and invariant validation]
    D[Canonical serialization and scoped digests]
    E[Compatibility manifest]
    F[Exact-head evidence bundle]
    G[Human approval]
    H[Downstream read-only replay]

    A --> B --> C --> D --> E --> F --> G --> H
```

## Candidate lifecycle

```mermaid
stateDiagram-v2
    [*] --> Proposed
    Proposed --> Candidate: bounded artifacts submitted
    Candidate --> Candidate: findings repaired on approved path
    Candidate --> FrozenReview: mergeable head frozen
    FrozenReview --> Verified: exact-head suite and evidence pass
    Verified --> Accepted: explicit review approval
    Accepted --> Released: versioned manifest and evidence published
    Released --> Superseded: later approved version

    Candidate --> Rejected: scope, integrity, or evidence failure
    FrozenReview --> Candidate: approved repair creates a new head
    Verified --> Candidate: evidence invalidated by head change
    Released --> RolledBack: release defect or consumer mismatch
```

## Validation sequence

```mermaid
sequenceDiagram
    participant Author
    participant Repo as QSO-GENOMES
    participant Validator
    participant Reviewer
    participant Consumer

    Author->>Repo: propose declarative artifacts
    Repo->>Validator: strict parse and schema checks
    Validator->>Validator: references, invariants, migration, hostile inputs
    Validator->>Validator: canonical bytes and scoped digests
    Validator-->>Repo: deterministic reports tied to exact head
    Repo->>Reviewer: immutable candidate head and evidence
    Reviewer-->>Repo: accept, reject, or request bounded repair
    Repo->>Consumer: approved versioned manifest only after acceptance
    Consumer->>Consumer: revalidate complete set read only
    Consumer-->>Reviewer: downstream replay evidence
```

## Fail-closed decision tree

```mermaid
flowchart TD
    A[Load declared compatibility manifest]
    B{Manifest identity and source head approved?}
    C{All required artifacts present and unique?}
    D{Strict parse, schema, and references pass?}
    E{Immutable, supervisory, migration, and forbidden rules pass?}
    F{Canonical bytes and digest scopes reproduce?}
    G{Exact-head evidence and downstream replay complete?}
    H[Accept exact versioned set]
    X[Reject complete set and preserve evidence]

    A --> B
    B -- no --> X
    B -- yes --> C
    C -- no --> X
    C -- yes --> D
    D -- no --> X
    D -- yes --> E
    E -- no --> X
    E -- yes --> F
    F -- no --> X
    F -- yes --> G
    G -- no --> X
    G -- yes --> H
```

## Authority separation

```mermaid
flowchart TB
    H[Human repository and release authority]
    V[Independent validator]
    G[Declarative genome]
    R[External runtime controller]
    Q[Bounded QSO state]
    P[Proposed mutable change]

    H -->|approves exact artifact set| G
    V -->|reports evidence, no release authority| H
    G -->|read-only immutable contract| R
    R -->|instantiates bounded state| Q
    Q -->|may propose, cannot commit| P
    P -->|external review required| H

    Q -. cannot edit immutable contract .-> G
    R -. cannot silently weaken upstream rules .-> G
```

## Reconciliation and evidence preservation

```mermaid
flowchart LR
    P[Existing canonical pull request]
    M[Current main]
    R[Provenance-preserving reconciliation]
    F[Frozen mergeable review head]
    T[Complete exact-head replay]
    D[Review-thread disposition]
    A[Approval decision]

    P --> R
    M --> R
    R --> F --> T --> D --> A

    R -->|record old base, old head, conflicts, retained and excluded paths| E[Reconciliation record]
    E --> T
```

## Release artifact bundle

```mermaid
flowchart TB
    M[Versioned compatibility manifest]
    S[Schemas and source contracts]
    X[Positive, negative, boundary, and migration fixtures]
    L[Exact-head logs and reports]
    P[Provenance and checksums]
    C[Downstream consumer reports]
    R[Rollback and supersession record]
    B[Release evidence bundle]

    M --> B
    S --> B
    X --> B
    L --> B
    P --> B
    C --> B
    R --> B
```

<!-- QSO-CONSENT-CAPACITY-LOCK-v1 -->
