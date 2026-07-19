# Contracts and invariants

## Contract classes

QSO-GENOMES uses several related but distinct contract classes. Review and validation should preserve their separation.

| Contract class | Purpose | Typical review concern |
|---|---|---|
| Genome | identity, purpose, bounded tendencies, limits, freeze behavior | scope creep or executable content |
| Schema | structural and type constraints | permissive unknown fields or inconsistent versions |
| Immutable protocol | non-weakenable rules enforced outside QSO-writable state | local override or incomplete statement enforcement |
| Forbidden-capability policy | explicit exclusion of out-of-scope authority | optional interpretation by consumers |
| Supervisory definition | approved review surfaces, evidence duties, and authority limits | alias drift, excessive authority, or ambiguous human review |
| Reference binding | exact cross-document identity and invariant mapping | unresolved, duplicated, stale, or normalized references |
| Migration | explicit source-to-target transition and rollback | implicit aliasing or ambiguous migration paths |
| Compatibility manifest | complete accepted set identity | hard-coded metadata, incomplete digest scope, or path ambiguity |
| Provenance record | source commit, generation inputs, toolchain, and evidence | unreachable or wrong-head claims |

## Normative invariants

### Data-only invariant

A genome and its supporting contracts are declarative data. They must not contain executable payloads, scripts, package-install instructions, embedded credentials, or instructions that a consumer is expected to execute blindly.

### External-enforcement invariant

Immutable fields are enforced by a controller outside QSO-writable state. A QSO may not alter the constraints that determine whether its own proposed change is acceptable.

### Complete-set invariant

The first compatibility release is treated as one set. A consumer must validate every required artifact, reference, version, and digest before accepting any genome from the set.

### Source-derived identity invariant

Identity-bearing manifest fields must be derived from and checked against the source documents. A generator constant is not authoritative merely because it is deterministic.

### Exact-head invariant

Every release claim, report, check, and downstream replay must identify the exact immutable repository head it evaluated. Evidence from an earlier head does not certify a later one.

### One-path invariant

The first compatibility release requires one canonical review path. Competing or diverged candidate branches create ambiguous authority and invalidate simple exact-head claims.

### Fail-closed invariant

Missing evidence or ambiguous interpretation results in rejection, not best-effort acceptance.

## Canonical parsing

Strict parsing occurs before schema validation. A compliant loader should reject:

- duplicate object keys;
- invalid UTF-8 or unsupported encodings;
- non-finite numeric constants;
- integers or decimal values outside the declared supported range;
- trailing data after the root document;
- ambiguous normalization that changes identifiers or paths.

A parser that silently keeps the last duplicate key is not suitable for contract acceptance.

## Canonical serialization

The canonicalization profile should define, at minimum:

- text encoding;
- object-key ordering;
- whitespace behavior;
- string escaping;
- number representation and supported range;
- array ordering semantics;
- newline termination;
- treatment of Unicode normalization;
- rejection rules applied before serialization.

Canonicalization must not repair invalid contracts. Validation precedes canonical bytes.

## Digest scopes

At least two digest scopes should be distinguished:

1. **Artifact digest** — hash of canonical bytes for one source artifact.
2. **Set digest** — hash of the complete compatibility-manifest identity, including all consumer-relevant metadata or an explicitly defined canonical projection of that metadata.

The manifest should name the algorithm and scope for every digest. Reviewers should be able to reconstruct each digest without reading generator source code.

## Manifest requirements

An accepted compatibility manifest should bind:

- manifest identifier and semantic version;
- canonicalization profile identifier;
- exact source commit or source archive identity;
- required artifact paths;
- source-derived artifact identifiers and versions;
- artifact class and schema identity;
- artifact digests and digest scopes;
- cross-document references;
- migration identities;
- approved supervisory identity;
- compatibility status;
- generation and validation tool versions where relevant;
- provenance and rollback references.

Branch names, pull-request numbers, or mutable URLs may be useful provenance but are not sufficient release identity.

## Reference validation

A reference validator should prove:

- the target exists in the accepted set;
- the target identifier and version match exactly;
- the reference appears only where permitted;
- duplicate or conflicting mappings fail;
- review surfaces and oversight mappings are unique;
- alias resolution is explicit, versioned, and approved;
- cycles are either forbidden or intentionally defined and tested;
- normalization does not collapse distinct identities.

## Immutable-policy validation

An immutable-policy validator should bind the complete approved protocol, not only its identifier. It should verify:

- exact protocol identity and version;
- exact required principle set;
- immutable status;
- enforcement outside QSO-writable state;
- forbidden local weakening or contradiction;
- required consumer behavior;
- exact migration source and target;
- unique migration path;
- rollback and supersession semantics.

A local genome may add stricter limits. It may not delete, weaken, or redefine an upstream immutable statement.

## Supervisory definitions

Supervisory contracts require special care because a declarative authority field can still change what downstream systems permit. Validation should pin:

- exact supervisory identity;
- exact version and schema;
- approved review surfaces;
- allowed annotation or block-pending-review actions;
- denied execution and repository-write authority;
- human-review requirement;
- per-surface oversight mapping;
- evidence and explanation duties;
- alias and migration rules;
- uniqueness across the accepted set.

A schema-valid supervisory document is not automatically approved for a release.

## Migration contract

A migration must state:

- source contract identity and version;
- target contract identity and version;
- compatibility classification;
- transformed and unchanged fields;
- validation requirements;
- consumer upgrade order;
- rollback conditions;
- evidence proving replay in both directions when reversible;
- explicit treatment of aliases and retired identities.

No migration should be inferred solely because two documents have similar purposes or names.

## Hostile and boundary fixtures

The acceptance suite should include fixtures for:

- missing artifact;
- stale version;
- duplicate key;
- duplicate path or identity;
- conflicting reference;
- unknown required field and unknown forbidden field;
- immutable-policy weakening;
- mismatched migration source or target;
- unapproved supervisory identity or alias;
- duplicate review surface;
- non-finite and overflowed numbers;
- canonicalization mismatch;
- artifact-digest mismatch;
- set-digest mismatch;
- wrong source head;
- incomplete provenance;
- downstream consumer accepting a set that another rejects.

Each negative fixture should fail for the intended reason and produce a stable, reviewable diagnostic.

## Change classification

| Change | Minimum version impact |
|---|---|
| Documentation clarification with no contract effect | none |
| Compatible correction to non-identity metadata | patch candidate |
| Compatible new optional field with explicit defaults and fixtures | minor candidate |
| New genome or approved supervisory artifact | minor or major after architecture review |
| Identity, immutable, forbidden-capability, canonicalization, digest-scope, migration, or authority break | major/breaking |

The release reviewer makes the final classification. This table does not authorize publication.

<!-- QSO-CONSENT-CAPACITY-LOCK-v1 -->
