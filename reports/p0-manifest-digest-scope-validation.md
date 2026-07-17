# P0 Manifest Digest-Scope Validation

Date: 2026-07-17

## Scope

This bounded remediation defines the two SHA-256 meanings used by the compatibility manifest and binds all consumer-relevant manifest metadata into the set identity.

- Each artifact descriptor `sha256` identifies only the artifact's complete `qso-canonical-json-v1` byte encoding.
- `set_sha256` identifies the complete canonical manifest identity.
- The only top-level fields excluded from set identity are lifecycle `status` and recursive `set_sha256`.
- Every current artifact descriptor field (`artifact_id`, `canonical_bytes`, `kind`, `path`, `schema_version`, and `sha256`) is bound.
- New top-level metadata is automatically bound. New artifact-descriptor metadata fails closed until the declared digest semantics are versioned to include it.

No runtime, network, credential, repository-write, payment, or execution authority is added.

## Source and files

- Canonical PR: #2
- Reviewed parent head: `e51a814cd329c55e45a1599b205ef234859e4848`
- Modified generator: `scripts/generate_contract_manifest.py`
- Updated manifest: `manifests/qso-genomes-compatibility-v1.json`
- Updated existing test: `tests/test_contract_manifest.py`
- New focused test: `tests/test_manifest_digest_scope.py`

Candidate set identity after this remediation:

```text
2b59fe7c865409f9112eb3d21bb1954abb7c8195eaa7758da6602fec8410ba6e
```

## Verification

Environment:

```text
Python 3.13.5
```

Commands and results:

```text
python -m py_compile scripts/generate_contract_manifest.py \
  tests/test_contract_manifest.py tests/test_manifest_digest_scope.py
exit 0

python -m unittest discover -s tests -p 'test_manifest_digest_scope.py' -v
Ran 6 tests in 0.019s
OK

committed-manifest replay:
set_sha256_for_manifest(manifest) == manifest['set_sha256']
status candidate -> accepted leaves set_sha256 unchanged
PASS
```

The focused tests prove that:

1. the artifact and set digest scopes are declared in the manifest;
2. lifecycle status is excluded from compatibility identity;
3. mutation of any current artifact descriptor field changes the set digest;
4. newly added top-level consumer metadata changes the set digest;
5. undeclared artifact descriptor metadata fails closed; and
6. mutation of the declared digest semantics fails closed.

File SHA-256 values for the tested candidate files:

```text
2298fd3f20b5dba86a7397e05c71f2b9445f275fd2d35addac982350231cdccb  scripts/generate_contract_manifest.py
205d632b104a1d1271e9ce4bd4e9e8ee5f055c8cf9a969e06da10b36b33b0b3a  tests/test_manifest_digest_scope.py
07bda02003cc8d1832aa9b278d0a048a9dc30769299c4ce923dc3b6378a2a37b  tests/test_contract_manifest.py
a823c1a2f4f3508cb8e79f4fb2903d99f1d90b837b9214317395791527648198  manifests/qso-genomes-compatibility-v1.json
```

## Limitations and next gate

A fresh checkout and the complete repository suite could not be run because direct GitHub cloning failed with DNS resolution for `github.com`. This evidence therefore remains candidate-local focused evidence, not independent acceptance. The candidate lineage already contains a pinned `jsonschema==4.26.0` dependency, a `requirements.txt` cache path, and submitted-head checkout/assertion logic. The next gate is a successful conformance run on the final submitted head, followed by review-thread disposition and independent clean-checkout replay.

## Rollback

Revert the digest-scope remediation commits. Doing so restores the previous path-and-artifact-byte digest, but also restores the ambiguity that omitted identity-bearing manifest metadata from `set_sha256`.
