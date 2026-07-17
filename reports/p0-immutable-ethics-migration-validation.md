# P0 Immutable-Ethics Migration Validation

## Scope

This report records the bounded Builder task that resolves the PR #2 immutable-policy finding by adding an explicit, versioned migration from genome-local ethics text to the complete approved `QSO-IMMUTABLE-ETHICS-v1` protocol.

The migration does not self-approve a release. It keeps the protocol external to genome-writable state, makes the protocol authoritative, treats genome-local ethics as additive specialization only, and requires fail-closed rejection on missing, mismatched, or conflicting protocol data.

## Submitted artifacts

- Migration contract: `contracts/immutable-ethics-migration-v1.json`
  - Git blob: `b6583d27a015ed6075af5f8ab9c584accce62a5e`
  - QSO Canonical JSON v1 SHA-256: `d56994e90dd9d57a65db62b558d4acbd99b8b28ac8b1e124ed48257a9e29fb30`
- Focused tests: `tests/test_immutable_ethics_migration.py`
  - Git blob: `1a97f0f83b4302861b9a542e10e86c7a1a878d10`
- Authoritative protocol: `protocols/immutable-ethics-v1.json`
  - Git blob: `0c5b1a5021fd90eaf9934a2856585ec3bd0e5d7f`
  - QSO Canonical JSON v1 SHA-256: `ecbab42031461161e91e511ce5f1ba19f1d2d75d81a8351a32f185b181c206af`

Reachable implementation/test ancestor: `257839316082faf2a3ab115a65fb1550b74ecc06`.

## Migration guarantees

The candidate migration binds all four required genome paths to the exact protocol path, identifier, immutable status, canonicalization profile, canonical digest, twelve principles, five-step decision order, conflict rule, and amendment rule. Consumers must validate the binding before genome use, retain every protocol component verbatim, reject local conflicts, reject missing or mismatched protocol artifacts, require human review, and issue both a new protocol identifier and a new migration version for any change.

The migration remains `candidate` with approval state `not_accepted`. Clean replay and downstream consumer enforcement remain acceptance gates.

## Verification

Environment:

```text
CPython 3.13.5
Linux x86_64, glibc 2.41
standard library only
```

Command:

```bash
python3 -m unittest -v tests/test_immutable_ethics_migration.py
```

Result:

```text
test_current_migration_binds_full_protocol ... ok
test_missing_genome_reference_fails_closed ... ok
test_protocol_identity_mutation_fails_closed ... ok
test_protocol_mutation_fails_digest_binding ... ok
test_weakened_consumer_requirement_fails_closed ... ok

Ran 5 tests in 0.001s
OK
```

The focused replay used the exact committed migration and immutable protocol content with the four branch-derived genome identifiers and immutable-ethics projections in a repository-shaped tree. It verified deterministic canonical hashing and fail-closed behavior for protocol mutation, protocol-ID mutation, a missing Atlas reference, and a weakened human-review requirement.

## Residual gates

- Run the focused test and complete suite from a clean checkout at the final reviewed head.
- Add this migration artifact to the final compatibility-manifest identity once digest semantics are resolved.
- Validate the migration read-only in `QuantumStateObjects` and `QSO-FABRIC` after publication approval.
- Resolve or formally disposition the applicable PR review finding against the final candidate head.
