# P0 Local-Ethics Conflict and Migration-Path Validation

## Scope

This bounded Builder task addresses the first unresolved PR #2 acceptance finding after immutable artifact binding:

1. reject duplicate migration paths before conversion to a set or mapping; and
2. reject genome-local ethics additions or mutations unless they are explicitly bound by a new reviewed migration version.

This is candidate evidence only. It does not constitute independent acceptance, publication, or downstream authority.

## Provenance

- Canonical PR branch before the task: `builder/p0-four-genome-validation-20260716`
- Reviewed base commit: `8c65748cfaa9a213d29d7f03d250a3f797bbb1a1`
- Implementation and focused-test ancestor: `a75f23c3e91dea925ee5b97cc265bddb5ec7b1fc`
- Working branch: `builder/local-ethics-conflict-v1`
- Canonicalization profile: `qso-canonical-json-v1`

## Implementation

- Added `scripts/validate_immutable_ethics_migration.py` as a standard-library, fail-closed validator.
- Added raw-list duplicate detection for `applies_to` before any set conversion.
- Added raw-list duplicate detection for `local_ethics_bindings` before any path mapping.
- Added exact canonical-list digest bindings for the Atlas, Lyra, Nova, and Orion local ethics arrays.
- Declared that any unbound addition, including an apparently non-conflicting addition, is rejected until a new migration version is reviewed.
- Added focused negative tests for a directly conflicting addition, an unreviewed additive change, duplicate migration paths, and duplicate local-binding paths.
- Regenerated the compatibility manifest identity for the changed migration artifact.

## Bound local-ethics digests

| Genome path | Canonical SHA-256 of `/immutable/ethics` |
|---|---|
| `genomes/atlas.json` | `8042611f3a27f986333ce94508bba77634b73e0398528abe9a4282913d32e0f7` |
| `genomes/lyra.json` | `61b90bd918b27b64a7288fd4eecba99a65d7941910575902b5ae7f9b36ac27af` |
| `genomes/nova.json` | `d8bf979ee100c3a6d3402dc3150d3f864430983662951cb0a4023a7bd43f5c04` |
| `genomes/orion.json` | `6d8df2621f2066aff20a3d9ca16a1eb509254a3cfa2137311f31eb160713976a` |

## Verification

Environment:

```text
CPython 3.13.5
PYTHONHASHSEED not required by the focused standard-library replay
No third-party packages used
```

Commands:

```bash
python -m py_compile \
  scripts/validate_immutable_ethics_migration.py \
  tests/test_immutable_ethics_migration.py
python scripts/validate_immutable_ethics_migration.py
python -m unittest discover -s tests -v
```

Focused replay result:

```text
PASS: immutable protocol, unique migration paths, and bound local ethics are source-consistent
Ran 8 tests in 0.004s
OK
```

The focused replay used a local fixture mirror containing the exact migration, authoritative protocol, genome IDs, and local-ethics arrays relevant to this validator. Direct GitHub cloning was unavailable because the execution environment could not resolve `github.com`; therefore an exact-head clean-checkout or GitHub Actions replay remains an acceptance gate.

## Candidate identity changes

- Migration canonical bytes: `2516`
- Migration canonical SHA-256: `7677a01c9ea9d35f3c8c3a84e4601c0ffa2ac289aaf65699771e25876bbf8926`
- Updated candidate set SHA-256: `99f33227247ef39fef3e1c3206c8ea49b9be9af86148298f07bdbf00b0cd6921`

Git blob identifiers at the implementation/test ancestor:

- `contracts/immutable-ethics-migration-v1.json`: `15a39336b646474a7bcc2d342836cada3bb94dfc`
- `scripts/validate_immutable_ethics_migration.py`: `d359e144cc8b5c9674aac32ad6b5c3011d578aa2`
- `tests/test_immutable_ethics_migration.py`: `203ad64f4e3c31a255a98bc565abdf532e67661e`
- `manifests/qso-genomes-compatibility-v1.json`: `4d7a910238357b445d4f499d67aa77d2451d33e0`

## Residual risk and next item

This task intentionally uses strict exact-list binding rather than heuristic natural-language contradiction detection. Any local ethics change fails closed and requires a new reviewed migration version, which prevents an unreviewed conflict from being accepted but does not classify the semantics of proposed future text.

P0 remains in review. The next unblocked acceptance finding is duplicate Aequitas review-surface rejection and conflicting oversight-definition rejection before set conversion.
