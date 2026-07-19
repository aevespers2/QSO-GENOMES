# QSO-GENOMES

Canonical, reviewable genome contracts for bounded Quantum State Objects.

A genome is declarative data, not executable code. It defines identity, purpose, bounded learning tendencies, immutable ethics, resource and communication limits, freeze behavior, provenance requirements, and the narrow conditions under which mutable preferences may be proposed for external review.

> **Release status:** blocked. The first Atlas/Nova/Orion/Lyra compatibility set is not accepted or published. See [`taskchain.md`](taskchain.md) and [`release.md`](release.md) for the authoritative gate state.

## Repository role

QSO-GENOMES is the upstream contract authority for `QuantumStateObjects` and `QSO-FABRIC`. It owns versioned declarative artifacts, schemas, immutable-policy and forbidden-capability boundaries, canonical serialization, compatibility-manifest identity, migrations, fixtures, and release evidence requirements.

It does not execute QSOs, retrieve network data, hold credentials, perform payments, deploy services, or grant a QSO authority to commit its own contract changes.

## Design principles

- Genomes are data only and must never contain executable instructions.
- Immutable ethics and safety boundaries cannot be modified by the QSO that consumes them.
- Goal and preference evolution is bounded, auditable, reversible, and subordinate to immutable constraints.
- External knowledge is accepted only through approved QSO-SEEKER records.
- Every accepted state transition is provenance-bound and evaluated at a freeze point.
- A QSO may propose changes to mutable preferences, but only an external human-controlled process may commit them.
- No genome grants shell access, arbitrary code execution, credential access, unrestricted networking, package installation, payment authority, deployment authority, or self-replication.
- Consumers validate the complete approved set read only and fail closed on missing, stale, conflicting, duplicated, mutated, or unverifiable artifacts.

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
- [Architecture and lifecycle diagrams](docs/diagrams.md)
- [Developer onboarding and contract-review workflow](docs/developer-guide.md)
- [Security and governance](docs/security-and-governance.md)
- [Release gates and evidence](docs/release-and-evidence.md)
- [Operations, incident response, and rollback](docs/operations-and-rollback.md)
- [Architecture decisions](docs/adr/0001-data-only-authority.md)

Build locally with:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-docs.txt
mkdocs build --strict
mkdocs serve
```

A successful documentation build proves only that the site renders. It does not validate or approve a compatibility release.

## Consumption model

A downstream runtime resolves one approved compatibility manifest, verifies the exact source identity, strictly parses every declared artifact, validates schemas and cross-document invariants, reproduces canonical bytes and scoped digests, and rejects the complete set when any required condition cannot be proven. Immutable fields remain outside QSO-writable state, and proposed mutable changes remain separate until external review.

## Contribution rule

Before changing a contract, read [`taskchain.md`](taskchain.md), [`release.md`](release.md), [`changelog.md`](changelog.md), and the [developer guide](docs/developer-guide.md). Keep proposal, candidate, verified, accepted, released, and deployed states distinct, preserve the canonical review path, and attach claims to an exact immutable head.

<!-- QSO-CONSENT-CAPACITY-LOCK-v1 -->
