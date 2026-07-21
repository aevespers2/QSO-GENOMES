# QSO-GENOMES

Canonical, reviewable genome contracts for bounded Quantum State Objects.

A genome is declarative data, not executable code. It defines identity, purpose, bounded learning tendencies, immutable policy, resource and communication limits, freeze requirements, provenance, lineage, and the narrow conditions under which mutable preferences may be proposed for external review.

> **Release status:** blocked. The first Atlas/Nova/Orion/Lyra compatibility set is not accepted or published. Identity migration, canonical-head reconciliation, generic format ownership, gluing fixtures, downstream replay, and explicit approval remain unresolved. See [`taskchain.md`](taskchain.md) and [`release.md`](release.md) for the authoritative gate state.

## Repository role

QSO-GENOMES is the upstream declarative contract authority for `QuantumStateObjects`, `QSO-FABRIC`, an approved generic QSO format or kernel package, Repository `1` or another approved capability authority, and read-only interfaces. It owns versioned genome artifacts, schemas, immutable-policy and forbidden-capability boundaries, genome-specific canonicalization, compatibility-manifest identity, migrations, fixtures, and release-evidence requirements.

It does not execute QSOs, retrieve network data, hold credentials, issue capabilities, perform payments, deploy services, create canonical operational state, or grant a QSO authority to commit its own contract changes.

## Design principles

- Genomes are data only and must never contain executable instructions.
- Declarative identity and policy are distinct from operational credentials, capabilities, approvals, and canonical state.
- Immutable policy and safety boundaries cannot be modified by the QSO that consumes them.
- Goal and preference evolution is bounded, auditable, reversible, and subordinate to immutable constraints.
- External knowledge is accepted only through approved evidence contracts.
- Every accepted state transition is provenance-bound and evaluated at an externally enforced freeze point.
- A QSO may propose changes to mutable preferences, but only an external human-controlled and capability-governed process may commit them.
- No genome grants shell access, arbitrary code execution, credential access, unrestricted networking, package installation, payment authority, deployment authority, or self-replication.
- Consumers validate the complete approved set read only and fail closed on missing, stale, conflicting, duplicated, mutated, retired, revoked, or unverifiable artifacts.

## Initial bounded set

| Genome | Emphasis |
|---|---|
| Atlas | structure, mathematics, algorithms, compression, and cross-domain mapping |
| Nova | verification, anomaly detection, security, testing, and contradiction analysis |
| Orion | architecture, interfaces, protocols, and systems composition |
| Lyra | language, ontology, epistemology, documentation, and human context |

These summaries are descriptive. The accepted versioned artifacts and manifest, once approved, are authoritative.

## Documentation

The GitHub Pages-ready documentation package includes:

- [Project overview](docs/project-overview.md)
- [Architecture and trust boundaries](docs/architecture.md)
- [Contracts, canonicalization, manifests, and invariants](docs/contracts-and-invariants.md)
- [Portfolio obstruction and gluing analysis](docs/obstruction-and-gluing.md)
- [Architecture and lifecycle diagrams](docs/diagrams.md)
- [Developer onboarding and contract-review workflow](docs/developer-guide.md)
- [Security and governance](docs/security-and-governance.md)
- [Release gates and evidence](docs/release-and-evidence.md)
- [Operations, incident response, and rollback](docs/operations-and-rollback.md)
- [ADR-0001: data-only authority](docs/adr/0001-data-only-authority.md)
- [ADR-0002: canonical review path](docs/adr/0002-canonical-review-path.md)
- [ADR-0003: declarative identity versus operational authority](docs/adr/0003-separate-declarative-identity-from-operational-authority.md)

Build locally with:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-docs.txt
mkdocs build --strict
mkdocs serve
```

A successful documentation build proves only that the site renders. It does not validate or approve a compatibility release, identity migration, capability route, or publication.

## Consumption model

A downstream runtime resolves one approved compatibility manifest, verifies the exact source identity, strictly parses every declared artifact, validates schemas and cross-document invariants, reproduces canonical bytes and domain-separated digests, and rejects the complete set when any required condition cannot be proven. Immutable fields remain outside QSO-writable state, and proposed mutable changes remain separate until external review. Operational use additionally requires any independently approved admission or capability decision; genome validity alone does not authorize execution.

## Contribution rule

Before changing a contract, read [`taskchain.md`](taskchain.md), [`release.md`](release.md), [`punchlist.md`](punchlist.md), [`changelog.md`](changelog.md), the [developer guide](docs/developer-guide.md), and the [gluing analysis](docs/obstruction-and-gluing.md). Keep proposed, implemented, validated, accepted, published, released, deployed, superseded, and revoked states distinct; preserve review provenance; and attach every claim to an exact immutable head.

<!-- QSO-CONSENT-CAPACITY-LOCK-v1 -->
