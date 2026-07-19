# Security and governance

## Security objective

QSO-GENOMES should make it difficult for malformed, ambiguous, overpowered, or insufficiently reviewed data to become runtime authority. The primary security boundary is not process isolation inside this repository; it is the combination of declarative-only artifacts, strict interpretation, immutable external enforcement, exact identity, fail-closed consumers, and human-controlled release approval.

## Threat model

### Untrusted contract input

A proposed genome, policy, binding, migration, or manifest may be malformed or intentionally crafted to exploit parser differences, duplicate-key behavior, numeric edge cases, reference normalization, alias handling, or incomplete schema rules.

**Controls:** strict parsing, duplicate rejection, finite numeric domains, explicit unknown-field policy, source-derived identity, cross-document validation, deterministic canonicalization, and hostile fixtures.

### Authority smuggling

A declarative field may grant more power than the repository role permits even when the file contains no executable code. Examples include repository writes, credentials, direct network access, execution, self-modification, hidden policy replacement, or bypass of human review.

**Controls:** forbidden-capability rules, schema restrictions, semantic validation, explicit authority-denial fields, review of supervisory definitions, and downstream fail-closed enforcement.

### Identity substitution

A new supervisory definition, alias, migration, or similarly named artifact may be treated as equivalent to an approved identity without a versioned decision.

**Controls:** exact identifiers and versions, no implicit aliasing, unique reference binding, migration contracts, manifest membership, security review, and rollback.

### Evidence substitution

A report or workflow may pass on one commit while the pull request advances to another, or CI may validate a synthetic merge state rather than the reviewed head.

**Controls:** exact-head checkout and assertion, immutable submitted-head recording, retained logs and checksums, head-stability gate, clean-checkout replay, and rejection of stale evidence.

### Canonicalization ambiguity

Different consumers may parse or serialize the same document differently and compute incompatible hashes.

**Controls:** named canonicalization profile, strict preconditions, reproducible test vectors, artifact and set digest scopes, and independent downstream replay.

### Partial-set acceptance

A consumer may accept one genome despite missing policies, migrations, bindings, or manifest metadata.

**Controls:** complete-set invariant, required manifest membership, all-or-nothing validation, and negative fixtures for missing and conflicting artifacts.

### Governance drift

A separate governance proposal or automation may enter the compatibility release unintentionally, changing authority or moving the review base.

**Controls:** one canonical release path, explicit merge order, scope exclusions, separate versioning, lifecycle synchronization, and approval records.

## Trust zones

| Zone | Trusted for | Not trusted for |
|---|---|---|
| Working branch | drafting and local tests | release identity or final evidence |
| Pull-request candidate | bounded review | acceptance, publication, or deployment |
| Independent validation environment | reproducible technical evidence | product or release approval |
| Accepted immutable head | source of approved artifacts | future versions or downstream deployment state |
| Published evidence bundle | audit and consumer verification | weakening local consumer controls |
| Downstream runtime | enforcing equal or stricter limits | modifying upstream contracts |

## Authority model

### Human repository authority

Humans retain control over repository changes, branch reconciliation, review disposition, approval, release, and rollback. No declarative artifact grants itself authority to change the repository.

### Validator authority

Validators may accept or reject a candidate according to specified rules and produce evidence. They do not approve product scope or release.

### Supervisory contract authority

An approved supervisory definition may describe annotation, review, or block-pending-review behavior within a bounded consumer. It must explicitly deny execution, repository writes, immutable-policy override, and hidden release authority unless a future separately approved architecture says otherwise.

### Runtime authority

A downstream controller enforces the accepted contract. It may impose stricter limits but may not silently weaken or reinterpret upstream immutable rules.

## Required security properties

- Data-only artifacts.
- No embedded secrets or credentials.
- No executable payloads.
- No direct package-install or shell authority.
- No direct external-network authority in a genome.
- No self-commit or self-release authority.
- Immutable constraints enforced outside QSO-writable state.
- Exact identity and version binding.
- Strict parser behavior.
- Complete reference and migration validation.
- Explicit canonicalization and digest scopes.
- Complete-set acceptance.
- Exact-head evidence.
- Human-controlled scope and release approval.

## Review of policy-sensitive changes

Changes to immutable rules, forbidden capabilities, supervisory authority, migrations, aliases, review surfaces, evidence requirements, or release governance require independent security review. The review should identify:

- the authority before and after the change;
- who can trigger or approve the behavior;
- what evidence is required;
- how denial and failure behave;
- whether any consumer can interpret the change more broadly;
- compatibility and migration impact;
- rollback and supersession steps;
- new hostile-input fixtures.

## Supply-chain posture

The release artifact is data, but validation and documentation use tools. Record tool and dependency versions, prefer isolated environments, avoid unnecessary packages, pin release-critical dependencies, verify source archives where practical, and preserve sufficient metadata to reproduce the evidence.

A passing third-party tool is not the final authority. The repository's declared invariants and independently reviewed evidence remain controlling.

## Sensitive-data posture

Genome contracts should not contain personal secrets, account credentials, private keys, precise personal records, raw surveillance data, biometric templates, or unnecessary personal identifiers. Test fixtures should be synthetic and minimized. Evidence bundles should avoid copying sensitive inputs when a checksum, redacted fixture, or bounded diagnostic is sufficient.

## Incident classes

- unexpected authority field or policy weakening;
- identity or alias substitution;
- parser disagreement;
- digest mismatch;
- wrong-head evidence;
- missing provenance;
- unapproved artifact entering a manifest;
- downstream consumers disagreeing on acceptance;
- repository history or review evidence loss;
- published contract requiring urgent rollback.

See [Operations and rollback](operations-and-rollback.md) for response procedures.

## Governance records

Material decisions should be recorded in an ADR, the task chain, release plan, and changelog as appropriate. A decision record should state status, context, chosen option, rejected alternatives, consequences, evidence, migration, and rollback.

## No silent promotion

Documentation, tests, workflows, generated manifests, and reports may improve a candidate. None of them alone promotes a candidate to accepted, released, or deployed. Promotion requires the explicit gate sequence in the release plan.

<!-- QSO-CONSENT-CAPACITY-LOCK-v1 -->
