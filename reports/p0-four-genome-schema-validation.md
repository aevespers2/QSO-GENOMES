# P0 Four-Genome Schema Validation

Date: 2026-07-16

## Scope

This bounded Builder task adds the missing declarative Atlas genome and validates Atlas, Nova, Orion, and Lyra against `schema/qso-genome.schema.json`.

This report does **not** complete P0. Immutable-ethics equivalence, Aequitas Sprite references, canonical contract hashes, the compatibility manifest, and negative fixtures remain separate checklist items.

## Environment

- CPython: `3.13.5`
- `jsonschema`: `4.26.0`
- validator: `Draft202012Validator`
- platform used for the recorded run: Linux x86_64
- reachable submitted source state: `9de3db6a33308346d09b7004e6702e997dce9ba8`
- provenance record: `reports/submitted-state-provenance.md`

## Reproduction command

```bash
python3 - <<'PY'
import json
from pathlib import Path
from jsonschema import Draft202012Validator

schema_path = Path("schema/qso-genome.schema.json")
schema = json.loads(schema_path.read_text(encoding="utf-8"))
Draft202012Validator.check_schema(schema)
validator = Draft202012Validator(schema)

for path in sorted(Path("genomes").glob("*.json")):
    instance = json.loads(path.read_text(encoding="utf-8"))
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
    if errors:
        for error in errors:
            print(f"{path}: FAIL: {error.json_path}: {error.message}")
        raise SystemExit(1)
    print(f"{path}: PASS")
PY
```

## Recorded result

```text
genomes/atlas.json: PASS
genomes/lyra.json: PASS
genomes/nova.json: PASS
genomes/orion.json: PASS
```

The schema itself passed `Draft202012Validator.check_schema`.

## Reviewed source hashes

Exact Git blob identifiers at the submitted source state:

| Artifact | Git blob SHA |
|---|---|
| `schema/qso-genome.schema.json` | `b11523d9639550a6d6a529fe916a36ad27d7b319` |
| `genomes/atlas.json` | `17b422726da0e6ca352f877daefa4244add7082f` |
| `genomes/nova.json` | `13bfe7b2e9e4c2779d6bf2050770cc2d5b68982f` |
| `genomes/orion.json` | `b9ca3d010b01bf7cc75f8792e5c18a6542e4de43` |
| `genomes/lyra.json` | `55e363b4e26fee4f237199f8d8b07117b85f3224` |

Raw file SHA-256 values for the four genome documents:

```text
e543d28e7a0cdb103494cc9f3239ad26033e9df23c82652ff8804e5b01784311  genomes/atlas.json
e28e79595eed1370f16f4796bb23fe870e38788cbc0d173fc4696966b5b09a55  genomes/lyra.json
c8669e03148d76b0e51dab8defe9cea794ef88c0dfb6fd0c8aaa1fdae069760b  genomes/nova.json
e4c02efbcbec8fe6803dfa4df2b81de85ceb2babcb68a3a38a46d6b0e0271167  genomes/orion.json
```

These are raw-file evidence hashes, not the final P1 canonical compatibility hashes.

## Result

`PASS` for the bounded recorded run: all four current genome documents validate against the current schema. The separate review finding requiring the reproduction command to assert the exact required four-artifact set remains open.
