# QSO-GENOMES

Canonical, reviewable genome definitions for bounded Quantum State Objects.

A genome is a declarative configuration, not executable code. It defines identity, purpose, learning tendencies, immutable ethics, resource limits, communication limits, freeze behavior, and the narrow conditions under which goals may evolve.

## Design principles

- Genomes are data only and must never contain executable instructions.
- Immutable ethics and safety boundaries cannot be modified by the QSO that consumes them.
- Goal evolution is bounded, auditable, reversible, and subordinate to immutable constraints.
- External knowledge is accepted only through QSO-SEEKER canonical records.
- Every state transition produces provenance, a checksum, and a freeze-point decision.
- A QSO may propose changes to mutable preferences, but only an external controller may commit them.
- No genome grants shell access, arbitrary code execution, credential access, unrestricted networking, package installation, or self-replication.

## Initial genomes

- Atlas — structure, mathematics, algorithms, compression, cross-domain mapping.
- Nova — verification, anomaly detection, security, testing, contradiction analysis.
- Orion — architecture, interfaces, protocols, systems composition.
- Lyra — language, ontology, epistemology, etymology, documentation, human context.

## Consumption model

The future `QuantumStateObjects` runtime will load a genome, verify its schema and digest, instantiate a bounded QSO, and keep immutable fields outside the QSO's writable state. Any proposed mutation is recorded separately and evaluated at freeze points.
