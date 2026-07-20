# P0 Four-Genome Schema Validation

Date: 2026-07-20

## Scope

This bounded Builder task adds the declarative Atlas genome and validates the exact Atlas, Nova, Orion, and Lyra artifact set against `schema/qso-genome.schema.json`.

The shared validator also fails closed unless the reviewed sprite directory contains exactly the approved Aequitas and Socrates artifacts and both validate against `schema/qso-sprite.schema.json`.

This report does **not** complete P0. Immutable-ethics equivalence, review-binding references, canonical contract hashes, compatibility-manifest integrity, negative fixtures, reconciliation with `main`, and independent acceptance remain separate gates.

## Environment

- supported CI interpreters: CPython `3.11`, `3.12`, and `3.13`
- dependency declaration: `requirements.txt`
- validator dependency: `jsonschema==4.26.0`
- schema validator: `Draft202012Validator`
- reviewed source state: the Git commit containing this report
- exact submitted commit: retained by the `QSO-GENOMES conformance` workflow in `reports/exact-head.txt` and `reports/event-head.txt`
- provenance record: `reports/submitted-state-provenance.md`

## Reproduction command

From a clean checkout of the reviewed commit:

```bash
python -m pip install --disable-pip-version-check --no-cache-dir -r requirements.txt
python scripts/validate_schema_set.py
```

`validate_schema_set.py` performs all of the following before reporting success:

1. requires exactly `atlas.json`, `lyra.json`, `nova.json`, and `orion.json` under `genomes/`;
2. rejects missing or unexpected genome JSON artifacts;
3. requires exactly `aequitas.json` and `socrates.json` under `sprites/`;
4. rejects missing or unexpected sprite JSON artifacts;
5. rejects duplicate JSON keys and non-finite JSON constants; and
6. validates every required artifact against its Draft 2020-12 schema.

## Expected recorded result

```text
PASS: genomes/atlas.json against schema/qso-genome.schema.json
PASS: genomes/lyra.json against schema/qso-genome.schema.json
PASS: genomes/nova.json against schema/qso-genome.schema.json
PASS: genomes/orion.json against schema/qso-genome.schema.json
PASS: sprites/aequitas.json against schema/qso-sprite.schema.json
PASS: sprites/socrates.json against schema/qso-sprite.schema.json
PASS: 6 schema-bound artifacts validated
```

## Reviewed source hashes

The compatibility manifest and retained CI evidence are the authoritative hash surfaces for the current reviewed head. Historical hashes from earlier branch-local states are intentionally not presented as current evidence.

## Result

The validator now fails closed on anything other than the exact required four-genome and two-sprite set. A successful exact-head conformance run remains required before this candidate can advance.
