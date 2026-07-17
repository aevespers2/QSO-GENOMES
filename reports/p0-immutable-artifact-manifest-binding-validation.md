# P0 Immutable Protocol and Migration Manifest Binding Validation

## Scope

This bounded Builder task addresses the highest-priority unresolved PR #2 finding: bind `protocols/immutable-ethics-v1.json` and `contracts/immutable-ethics-migration-v1.json` into the candidate compatibility-set identity.

No runtime behavior, execution authority, network access, credentials, repository-write authority, payment capability, or publication status was added.

## Reviewed state

- Canonical PR #2 submitted head used as the branch base: `2d42c960cefb70fdaada969e75debf50fb06f36c`
- Implementation and focused-test head: `74c7d714a14123f52903178e805a614f2ead1bf1`
- Branch: `builder/bind-immutable-artifacts-v1`
- Branch comparison at implementation head: three commits ahead, zero behind the reviewed base

## Changes

- Added `contracts/immutable-ethics-migration-v1.json` to `ARTIFACT_SPECS` as contract `QSO-GENOME-IMMUTABLE-ETHICS-MIGRATION-v1`, version 1.
- Added `protocols/immutable-ethics-v1.json` to `ARTIFACT_SPECS` as protocol `QSO-IMMUTABLE-ETHICS-v1`, version 1.
- Regenerated the candidate manifest from nine to eleven artifacts.
- Added a focused test requiring both paths and exact IDs, requiring the migration's authoritative protocol digest to match the protocol descriptor, and requiring the migration descriptor hash to match its canonical bytes.

## Canonical evidence

| Artifact | Git blob | Canonical bytes | QSO Canonical JSON v1 SHA-256 |
|---|---|---:|---|
| `protocols/immutable-ethics-v1.json` | `0c5b1a5021fd90eaf9934a2856585ec3bd0e5d7f` | 1,898 | `ecbab42031461161e91e511ce5f1ba19f1d2d75d81a8351a32f185b181c206af` |
| `contracts/immutable-ethics-migration-v1.json` | `b6583d27a015ed6075af5f8ab9c584accce62a5e` | 1,773 | `d56994e90dd9d57a65db62b558d4acbd99b8b28ac8b1e124ed48257a9e29fb30` |
| Updated manifest | `89041015e054d30ff127393869d862c4c9e42a8b` | rendered JSON | candidate set digest below |

The migration's `to_protocol.canonical_sha256` equals the protocol's canonical digest. The eleven-artifact path/hash payload produces candidate set digest:

`6d9b0ca8c6766fbb63b4613df5b2baee455f1e63c848d6f75e56726efbc57cac`

## Verification

Environment: CPython 3.13.5, standard library only.

Commands/equivalent checks executed:

```text
python -m py_compile scripts/generate_contract_manifest.py tests/test_contract_manifest.py
```

Result: exit code 0.

A focused deterministic replay also:

1. parsed the committed manifest, protocol, and migration with duplicate-key and non-finite-number rejection;
2. asserted eleven sorted, unique artifact paths;
3. recomputed canonical byte counts and SHA-256 values for the protocol and migration;
4. asserted the migration's authoritative protocol digest equals the protocol descriptor;
5. recomputed the complete current path/hash set payload and obtained `6d9b0ca8c6766fbb63b4613df5b2baee455f1e63c848d6f75e56726efbc57cac`.

Result: PASS.

## Residual gates

This is candidate Builder evidence, not independent acceptance. A complete repository test replay from a clean checkout remains blocked in this runner because DNS resolution for `github.com` failed. Source-identity derivation, local-ethics conflict rejection, duplicate migration-path rejection, duplicate Aequitas surface rejection, digest-scope semantics, dependency declaration, exact-head CI, review-thread disposition, downstream replay, and publication approval remain open.
