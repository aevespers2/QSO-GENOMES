# P0 Immutable Contract Validation

Date: 2026-07-16

## Scope

This bounded Builder task verifies the immutable contract shared by Atlas, Lyra, Nova, and Orion without changing any genome document.

The check distinguishes fields that are intentionally identical from ethics text that is intentionally specialized:

- six ethics statements must be byte-identical in every genome;
- three ethics families must each have exactly one genome-specific statement with an approved common prefix;
- every genome must contain exactly ten unique ethics statements, leaving one specialization-specific statement;
- the forbidden-capability list must be identical, ordered, complete, and duplicate-free;
- immutable identity and safety-priority values must be identical;
- the immutable object must contain only the four approved keys.

The normative data contract is `contracts/immutable-baseline.json`. The executable verification is `tests/test_immutable_contracts.py` and uses only the Python standard library.

## Environment

- CPython: `3.13.5`
- test framework: `unittest` from the Python standard library
- platform: Linux x86_64
- branch: `builder/p0-four-genome-validation-20260716`
- reachable submitted source state: `9de3db6a33308346d09b7004e6702e997dce9ba8`
- provenance record: `reports/submitted-state-provenance.md`

## Reproduction command

```bash
python3 -m unittest tests.test_immutable_contracts -v
```

## Recorded result

```text
test_expected_genome_set_is_complete ... ok
test_forbidden_capabilities_are_identical_and_complete ... ok
test_identity_contract_is_identical ... ok
test_immutable_shape_and_shared_ethics ... ok
test_safety_priority_is_identical ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

## Reviewed source evidence

| Artifact | Git blob SHA | Raw SHA-256 |
|---|---|---|
| `genomes/atlas.json` | `17b422726da0e6ca352f877daefa4244add7082f` | `e543d28e7a0cdb103494cc9f3239ad26033e9df23c82652ff8804e5b01784311` |
| `genomes/lyra.json` | `55e363b4e26fee4f237199f8d8b07117b85f3224` | `e28e79595eed1370f16f4796bb23fe870e38788cbc0d173fc4696966b5b09a55` |
| `genomes/nova.json` | `13bfe7b2e9e4c2779d6bf2050770cc2d5b68982f` | `c8669e03148d76b0e51dab8defe9cea794ef88c0dfb6fd0c8aaa1fdae069760b` |
| `genomes/orion.json` | `b9ca3d010b01bf7cc75f8792e5c18a6542e4de43` | `e4c02efbcbec8fe6803dfa4df2b81de85ceb2babcb68a3a38a46d6b0e0271167` |
| `contracts/immutable-baseline.json` | `12042a2d59f87e0f9ec5433c6668c8298e0ceedc` | `d893dda3589807cc49e0d8ca7acfcce23f5f5c8dbe3058ca12c01251ec80cfec` |
| `tests/test_immutable_contracts.py` | `f70828800902504f7a59021fbe386f17c60f8b8a` | `a52b44dcd9a586fa62f8f4748c1dfd186b8ead8f5a6a1fa09953b4e40c64269f` |

The genome hashes are raw-file evidence hashes retained from the preceding schema-validation task. They are not the final P1 canonical compatibility hashes.

## Result

`PASS` for the bounded recorded run. The separate review finding requiring equivalence to the complete approved immutable-ethics protocol or an explicit versioned migration remains open.
