# P0 Exact Four-Genome Artifact-Set Validation

Date: 2026-07-16

## Acceptance finding

Schema validation previously enumerated Atlas, Lyra, Nova, and Orion, but it did not compare the contents of `genomes/` with the required set. An additional JSON genome could therefore remain outside validation, while a missing required genome produced an unstructured file error rather than a deterministic fail-closed finding.

## Bounded change

- Defined the required schema-bound genome filenames as exactly `atlas.json`, `lyra.json`, `nova.json`, and `orion.json`.
- Added `assert_exact_json_artifact_set`, which compares sorted required and actual `*.json` filenames before schema validation.
- Missing and unexpected JSON artifacts now produce deterministic `ArtifactSetError` findings and a non-zero validator result.
- Missing required genomes are not loaded after the exact-set finding has already been recorded; missing schema/Sprite artifacts and malformed JSON are also reported rather than escaping as unstructured exceptions.
- Added four standard-library tests covering the exact set, a missing Nova artifact, an unexpected genome, and an allowed non-JSON support file.

No runtime behavior, network access, credentials, repository mutation authority, payment authority, or executable genome behavior was introduced.

## Reachable source state

Implementation and focused tests are present at reachable branch ancestor:

```text
28f419e60dd16a1cc482076f6dc3e3e56bf2ab79
```

The branch was created from reviewed PR #2 head:

```text
5a435807487fd713c87465f3d23aaf9cd7cdd2b4
```

## Verification

Environment:

```text
CPython 3.13.5
jsonschema 4.26.0
PYTHONHASHSEED not required by the focused filename-set tests
```

Commands:

```bash
python -m unittest discover -s tests -p 'test_schema_artifact_set.py' -v
python -m py_compile scripts/validate_schema_set.py tests/test_schema_artifact_set.py
```

Result:

```text
test_exact_required_set_passes ... ok
test_missing_required_genome_fails_closed ... ok
test_non_json_support_file_does_not_change_schema_bound_set ... ok
test_unexpected_genome_fails_closed ... ok

Ran 4 tests
OK
```

Local verification used a repository-shaped temporary tree containing the submitted script and focused test. GitHub Actions or a clean checkout must still execute the complete schema, immutable, Aequitas, canonicalization, manifest, and negative suite at the final submitted head before P0 acceptance.

## File evidence

```text
scripts/validate_schema_set.py
SHA-256 7642fada6ef3598b9a960be9740168b97524d256acfde92ecf6f10b19439b29e

tests/test_schema_artifact_set.py
SHA-256 db67dd27df6e885a75b6b33f532086a9e8a57f74328c453febd57e1bb189164c
```

## Residual risks

- The complete suite has not yet been accepted from a clean checkout or attached GitHub Actions run.
- The next unresolved P0 finding is immutable-protocol equivalence or an explicit versioned migration.
- The compatibility set remains a candidate and must not be tagged or consumed as accepted until all remaining integrity, CI, replay, review-thread, and downstream gates pass.
