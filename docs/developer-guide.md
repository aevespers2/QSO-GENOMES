# Developer guide

## Contribution posture

QSO-GENOMES is a contract repository. A small data change can alter downstream authority, compatibility, or safety behavior even when no executable source file changes. Treat every contract edit as an interface change and every release claim as an evidence claim.

## Prerequisites

- Git 2.40 or newer.
- Python 3.11 or newer for repository validation scripts and documentation tooling.
- An isolated virtual environment.
- No production credentials or service tokens are required for documentation or contract review.

## Clone and isolate

```bash
git clone https://github.com/aevespers2/QSO-GENOMES.git
cd QSO-GENOMES
python -m venv .venv
source .venv/bin/activate   # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

Do not run repository scripts from a privileged account or from an environment containing unrelated credentials.

## Build the documentation

```bash
python -m pip install -r requirements-docs.txt
mkdocs build --strict
mkdocs serve
```

The strict build should complete without broken navigation or unresolved internal links. A successful documentation build proves only that the site renders; it does not validate a genome contract or release.

## Repository-wide policy check

Current `main` contains a repository-wide consent-capacity validator. Run it after documentation or policy-sensitive changes:

```bash
python scripts/validate_consent_lock.py
```

The generated report is local evidence. It does not replace review or authorize merge.

## Before editing a contract

Read, in order:

1. [`taskchain.md`](https://github.com/aevespers2/QSO-GENOMES/blob/main/taskchain.md)
2. [`release.md`](https://github.com/aevespers2/QSO-GENOMES/blob/main/release.md)
3. [`changelog.md`](https://github.com/aevespers2/QSO-GENOMES/blob/main/changelog.md)
4. [Architecture](architecture.md)
5. [Contracts and invariants](contracts-and-invariants.md)
6. relevant ADRs, schemas, migrations, fixtures, and open review findings

Confirm whether the intended change belongs on the active compatibility-review path, a separate future proposal, or documentation only. Do not move scope between those paths implicitly.

## Change workflow

### 1. Classify the change

Record whether the change affects:

- documentation only;
- schema shape;
- identity or versioning;
- immutable policy;
- forbidden capabilities;
- canonicalization or digest scope;
- supervisory authority;
- reference binding;
- migration semantics;
- manifest membership;
- validator behavior;
- release or downstream evidence.

### 2. State the non-goals

List what the change does not authorize. For example: no runtime behavior, no network access, no credentials, no repository write authority, no deployment, and no release promotion.

### 3. Preserve the canonical path

The current release plan requires one canonical review path for the first compatibility set. Do not open a competing release candidate or move accepted-looking artifacts into another branch without an explicit reconciliation decision.

### 4. Update contracts and fixtures together

A contract change should normally include:

- source artifact change;
- schema or invariant update when required;
- positive fixture;
- negative and boundary fixtures;
- migration and rollback impact;
- canonical bytes and digest expectation;
- documentation update;
- task-chain, release, or changelog update when lifecycle meaning changes.

### 5. Validate from a clean checkout

Evidence should be reproducible from the exact submitted commit. Record:

- commit SHA;
- operating system and architecture;
- Python and dependency versions;
- commands executed;
- fixture and schema versions;
- canonicalization profile;
- artifact and set digests;
- logs and report checksums;
- known limitations.

### 6. Request bounded review

The pull request should make it easy to answer:

- What contract changed?
- Why is the change required now?
- Which invariant families are affected?
- What new authority, if any, could a consumer infer?
- What fixtures prove acceptance and rejection behavior?
- What is the versioning impact?
- How is the change rolled back or superseded?
- Does it alter the current release path or only a future proposal?

## Documentation-only changes

A documentation pull request should not silently modify schemas, generators, validation behavior, policies, dependencies used by runtime code, or release status. It may add documentation build dependencies and validation limited to documentation, provided those additions are clearly isolated.

Use precise status language:

- **exists** does not mean **implemented**;
- **implemented** does not mean **verified**;
- **verified** does not mean **accepted**;
- **accepted** does not mean **released**;
- **released** does not mean **deployed**.

## Contract-review checklist

- [ ] The change is on the correct branch and review path.
- [ ] Scope and non-goals are explicit.
- [ ] Identity and version changes are declared.
- [ ] Unknown-field and duplicate behavior is defined.
- [ ] Immutable and forbidden-capability rules cannot be weakened.
- [ ] References resolve exactly and uniquely.
- [ ] Canonicalization and digest scopes are reproducible.
- [ ] Positive, negative, boundary, and migration fixtures are updated.
- [ ] Evidence is tied to the exact submitted head.
- [ ] Downstream impact is documented.
- [ ] Rollback or supersession is defined.
- [ ] `taskchain.md`, `release.md`, and `changelog.md` remain consistent.
- [ ] No release or deployment state is overstated.

## Pull-request evidence template

```text
Exact head:
Change class:
Contracts affected:
Non-goals:
Validation commands:
Tool and dependency versions:
Positive fixtures:
Negative/boundary fixtures:
Canonicalization profile:
Artifact digests:
Set digest and scope:
Review findings resolved:
Downstream replay:
Rollback/supersession:
Residual risks:
```

## Debugging validation failures

1. Reproduce from a clean checkout at the exact failing head.
2. Confirm the expected schema and canonicalization profile.
3. Inspect strict-parsing failures before schema diagnostics.
4. Verify source-derived identifiers and versions before checking manifest hashes.
5. Check duplicate paths, identities, references, review surfaces, and migration routes.
6. Confirm immutable-policy identity and complete contents.
7. Recompute artifact and set digests with their declared scopes.
8. Preserve the failing input and diagnostic as a regression fixture.
9. Avoid changing expected output merely to make the test pass; explain the contract decision.

## Branch and history safety

Do not force-push over a reviewed compatibility head, discard review threads, or rewrite provenance without explicit approval. When reconciliation is required, preserve old base and head identifiers, conflict decisions, retained and excluded paths, the resulting head, and renewed validation evidence.

<!-- QSO-CONSENT-CAPACITY-LOCK-v1 -->
