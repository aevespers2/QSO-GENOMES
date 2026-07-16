# Task Chain

## Repository role
Canonical declarative genomes, immutable ethics, and supervisory Sprite definitions. This repository is an upstream dependency of `QuantumStateObjects` and must not contain executable behavior.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Validate the four genomes, genome schema, immutable ethics, and Aequitas Sprite as one compatibility set | QSOBuilder | — | READY | Atlas, Nova, Orion, and Lyra validate against the current schema; required forbidden capabilities and external-review rules are present; deterministic canonical hashes and exact validation commands are recorded. |
| P1 | Publish a versioned cross-repository genome contract manifest | QSOBuilder | P0 | PROPOSED | One machine-readable manifest identifies schema versions, genome paths, ethics/Sprite references, canonical hashes, and compatibility status for consumption by `QuantumStateObjects`. |
| P2 | Add mutation-proposal and migration fixtures | Builder | P1 | PROPOSED | Fixtures prove immutable fields cannot change, mutable proposals remain external-review-only, and incompatible schema versions fail closed. |
| P3 | Define a declarative payment-policy extension | Architect | P1 and approved settlement boundary | BLOCKED | The extension remains data-only, grants no credentials or transfer authority, separates intent from authorization, and has an approved versioning/migration plan. |

## Cross-repository gate
`QuantumStateObjects` may not claim a verified multi-object run until P0 and P1 are complete.

## Builder Log
Record commit links, validation commands/results, schema hashes, residual risks, and follow-up tasks.
