# P0 Deterministic Contract Manifest Validation

## Result

`PASS` for the bounded Builder item: generate a deterministic contract manifest with stable paths, schema versions, canonical byte counts, per-artifact SHA-256 hashes, and one compatibility-set digest.

P0 is ready for review, not release. A clean-checkout or GitHub CI replay remains required before the candidate can be accepted.

## Claimed item

```text
Generate a deterministic contract manifest with paths, schema versions, and canonical hashes.
```

## Source and implementation

- Repository: `aevespers2/QSO-GENOMES`
- Branch: `builder/p0-four-genome-validation-20260716`
- Reachable submitted source state: `9de3db6a33308346d09b7004e6702e997dce9ba8`
- Provenance record: `reports/submitted-state-provenance.md`
- Runtime: CPython `3.13.5`

The submitted source state contains the generator, candidate manifest, tests, and all nine referenced artifacts. Exact artifact identity is additionally bound by the Git blob and canonical SHA-256 values retained below and in the candidate manifest.

## Canonicalization profile

`qso-canonical-json-v1` is implemented by `scripts/generate_contract_manifest.py`:

- parse JSON as UTF-8;
- reject duplicate object keys;
- reject non-finite numbers;
- sort object keys lexicographically by Unicode code point;
- preserve array order;
- remove insignificant whitespace;
- emit UTF-8 with one trailing LF;
- hash the resulting bytes with SHA-256.

The manifest is data only. It does not import repository code, execute artifact content, grant network or credential access, or permit genome mutation.

## Compatibility set

Compatibility-set identifier:

```text
qso-genomes-four-object-v1
```

Set digest:

```text
4ed083cb204a77d1f1878aea8dbf9c61f996541c9b4de83c812bb461530d3eac
```

| Path | Kind | Version | Canonical bytes | SHA-256 |
|---|---|---:|---:|---|
| `contracts/aequitas-review-binding.json` | contract | 1 | 1909 | `f5673c24159098312a7c173048d4b6abf2f13cbb91530b863d484f91655d1843` |
| `contracts/immutable-baseline.json` | contract | 1 | 1549 | `a7950e02a087fc8f1ff87ece00604ddb7f0e063e0d3a4656958147dcfef87ec6` |
| `genomes/atlas.json` | genome | 1 | 2903 | `6ad49dc872a50fe7f909062aaa805cec10477d34a73002475a34e47548a40a4c` |
| `genomes/lyra.json` | genome | 1 | 2982 | `1a9c59fdb9081af1c5e22787dd32b772242d6e7f9f0bbd44fe9cfabe5c821d4c` |
| `genomes/nova.json` | genome | 1 | 2854 | `d7363b36b00f9ea763f17dd4f2d4ab743fe2ff7b3891faaac937726afb9206a1` |
| `genomes/orion.json` | genome | 1 | 2905 | `ca64c19a20b45fbb8858ef11a1acddf42d478e6f37b75b1de90abee1180a5203` |
| `schema/qso-genome.schema.json` | schema | 1 | 4619 | `a2cb601d6d284f411903c972ae5e3574ca8faf6db28848e43cb91a697dbcb54b` |
| `schema/qso-sprite.schema.json` | schema | 1 | 2775 | `16ca71249869c46e0e184c14b98bb0eada17d34774a361b38aba6efaddba12ba` |
| `sprites/aequitas.json` | sprite | 1 | 1327 | `32752ebfa1ff1e9d60d9a94cd505bfcbc3a27724991e48a238e5261af9ac3d2a` |

## Verification commands

```bash
python3 -m unittest discover -s tests -v
python3 scripts/generate_contract_manifest.py --check
sha256sum \
  scripts/generate_contract_manifest.py \
  manifests/qso-genomes-compatibility-v1.json \
  tests/test_contract_manifest.py
```

Observed result:

```text
Ran 16 tests in 0.013s
OK
PASS: 9 artifacts; set_sha256=4ed083cb204a77d1f1878aea8dbf9c61f996541c9b4de83c812bb461530d3eac
```

The six new manifest tests verify completeness, sorted unique paths, canonical byte counts, per-artifact hashes, formatting independence, duplicate-key rejection, repeatable generation, committed-manifest equality, and the final set digest. The ten earlier immutable-contract and Aequitas-binding tests also passed in the same run.

New-file raw SHA-256 evidence:

```text
d72919cbd0bd53a5e524c3635c684a392139df6d2b7f600c05c65533bbf960dd  scripts/generate_contract_manifest.py
0a16cffcfc04b59bffc5fe5e1158e7c2e4118162fd9f48f4b4cedcb5719d42c4  manifests/qso-genomes-compatibility-v1.json
c3f067272dc268d9851b27ff7f51cca3259b7de0125af870f7546078e920672d  tests/test_contract_manifest.py
```

## Verification limitation

Direct GitHub cloning was unavailable in the execution runner because DNS resolution for `github.com` failed. The test run used a repository-shaped local tree populated from the branch artifacts fetched through the GitHub connector. No GitHub Actions workflow or commit-status check is attached to the branch head, so clean-checkout or CI verification remains an explicit acceptance gate. The separate review finding about whether `set_sha256` covers artifact bytes only or all identity-bearing manifest metadata also remains open.
