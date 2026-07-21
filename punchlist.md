# QSO-GENOMES Punch List

This list converts the current compatibility, identity, format, authority, and gluing obstructions into bounded review work. A checked item means documentation or candidate evidence exists; it does not mean the item is accepted, released, or downstream-authoritative.

## P0 — Candidate inventory and review order

- [ ] Reconfirm exact base, head, mergeability, checks, artifacts, and unresolved review threads for PRs #2, #12, #13, #14, and #15.
- [ ] Record which focused repairs from PR #13 were superseded by merged PRs #16 and #18.
- [ ] Approve one merge, reconciliation, and supersession order without force-rewriting reviewed history.
- [ ] Preserve all rejected, retired, and superseded heads as provenance.
- [ ] Freeze one immutable compatibility-set head before acceptance replay.

## P0 — Identity and authority disposition

- [ ] Approve or revise ADR-0003 separating declarative identity and policy from operational authority.
- [ ] Decide the active treatment of Aequitas, Socrates, Jacob Thomas Redmond, historical aliases, declarative role records, human authority, and operational service principals.
- [ ] Define alias purpose, retirement, negative resolution, provenance visibility, and downstream cache invalidation.
- [ ] Prove a genome or Sprite cannot issue credentials, capabilities, approvals, repository writes, releases, deployments, or canonical state.
- [ ] Record migration, correction, revocation, supersession, and rollback evidence.

## P1 — Compatibility-set integrity

- [ ] Reconcile PR #2 with current `main` and approved identity disposition while preserving the existing review path.
- [ ] Enforce the exact Atlas/Nova/Orion/Lyra artifact set and explicitly approved supervisory artifacts only.
- [ ] Define artifact-byte and complete-manifest digest scopes with domain separation.
- [ ] Pin canonicalization profile, duplicate-key rejection, strict UTF-8, non-finite-number rejection, unknown-field behavior, and numeric limits.
- [ ] Bind schema versions, immutable policy identity and contents, migrations, lineage, references, source-derived identity, and compatibility state.
- [ ] Resolve or formally disposition every material review finding against the frozen head.

## P2 — Generic format and QSIO boundary

- [ ] Designate the owner of the generic QSO envelope, registry, serialization family, canonicalization interface, and package namespace.
- [ ] Limit QSO-GENOMES ownership to genome-specific profiles and declarative semantics.
- [ ] Review PR #14 against the approved owner and package boundary.
- [ ] Add golden vectors for JSON/other approved encodings, round trips, domain-separated hashes, unknown versions, protected fields, and tampering.
- [ ] Reject adapter-specific fields that are absent from the genome contract.

## P3 — Pairwise gluing fixtures

- [ ] `genome-runtime-profile/v0`: QuantumStateObjects accepts the exact approved set and rejects missing, stale, mutated, duplicate, conflicting, or unsupported artifacts.
- [ ] `genome-fabric-profile/v0`: QSO-FABRIC consumes the same identity and policy without redefining genome or mutation authority.
- [ ] `genome-qsio-adapter/v0`: the approved kernel or format owner and QSO-GENOMES produce byte-stable compatible records.
- [ ] `genome-authority-admission/v0`: Repository `1` or a successor distinguishes local validity from operational admission, activation, expiry, revocation, and recovery.
- [ ] `genome-public-projection/v0`: QSO-STUDIO and AionUi expose only approved projections with provenance, redaction, correction, and revocation state.

## P4 — Triple-overlap witnesses

- [ ] Genome → runtime → Fabric.
- [ ] Genome → Repository `1` → runtime.
- [ ] Genome → QSIO/kernel → runtime.
- [ ] Identity migration → alias resolver → downstream cache.
- [ ] Immutable policy → freeze/revocation → recovery.
- [ ] Public projection → interface → correction.

Each witness must include positive, negative, stale, replay, unsupported-version, wrong-identity, partial-failure, correction, revocation, and rollback cases where applicable.

## P5 — Security, privacy, and recovery

- [ ] Classify public projections, protected commitments, private evidence, stable identifiers, and correlatable metadata.
- [ ] Define retention, deletion, correction, publication, and cache invalidation policy.
- [ ] Assign signing-key, capability, privacy, incident, emergency-stop, recovery, and publication owners.
- [ ] Prove emergency stop does not depend on the component being stopped.
- [ ] Prove recovery restores a consistent manifest, capability state, runtime state, Fabric state, interface state, and evidence chain with no automatic unlock.

## P6 — Release evidence

- [ ] Run complete conformance from a clean checkout at the exact frozen head on supported environments.
- [ ] Retain commands, versions, logs, reports, artifacts, checksums, source archive, SBOM or dependency record, review dispositions, and rollback instructions.
- [ ] Validate identical read-only downstream results in QuantumStateObjects and QSO-FABRIC.
- [ ] Record Repository `1` or successor admission evidence without treating it as a genome-issued capability.
- [ ] Obtain explicit approval before tag, manifest publication, Pages publication, package publication, or downstream compatibility claims.

## Quality invariants

- [ ] Genomes, Sprites, manifests, policies, and migrations remain declarative data only.
- [ ] No network, credential, repository-write, repair-PR, payment, deployment, infrastructure, or self-replication authority enters an accepted genome set.
- [ ] Candidate, implemented, validated, accepted, published, released, deployed, superseded, and revoked remain distinct states.
- [ ] Unknown or conflicting identity, policy, version, digest, capability, or correction state fails closed.
- [ ] Every claim is tied to an immutable commit and reproducible evidence.

<!-- QSO-CONSENT-CAPACITY-LOCK-v1 -->
