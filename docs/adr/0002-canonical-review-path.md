# ADR-0002: Use one canonical review path for the first compatibility release

- **Status:** Accepted release-governance decision for the first alpha candidate.
- **Decision owners:** Architect and human release reviewer.
- **Scope:** Atlas/Nova/Orion/Lyra compatibility-set acceptance.

## Context

The first compatibility set is an upstream dependency for multiple repositories. Diverged or competing candidates make it unclear which artifact paths, identities, hashes, review findings, and workflow results are authoritative. Evidence tied to one head cannot certify another head, and moving the default branch during reconciliation changes the review target.

## Decision

The first compatibility release uses one canonical pull-request path and one immutable final review head.

- Preserve the existing canonical compatibility review and its history.
- Reconcile current `main` without force-rewriting reviewed provenance.
- Keep unrelated governance candidates and unapproved supervisory additions outside the release path.
- Record old base, old head, current default head, conflicts, retained and excluded paths, and resulting head.
- Freeze the mergeable result before final validation.
- Renew exact-head evidence after every approved head change.
- Disposition material review findings against the frozen head.
- Publish only artifacts reproduced from the accepted head.

## Consequences

### Positive

- Review findings, evidence, and approval refer to one state.
- Downstream consumers receive one unambiguous manifest identity.
- Reconciliation preserves historical review context.
- Governance or future-scope proposals cannot enter the compatibility release implicitly.

### Costs

- Reconciliation must precede further acceptance evidence.
- Changes after the freeze require renewed review and replay.
- Separate proposals may wait until the compatibility candidate is stable.
- Conflict and exclusion decisions must be documented in detail.

## Rejected alternatives

### Open a new competing release pull request

Rejected because it would split review history and require a separate authority decision before evidence could be interpreted.

### Merge unrelated governance work first

Rejected for the current sequence because moving `main` changes the reconciliation target and invalidates comparison and exact-head evidence. An alternate sequence requires explicit approval and a complete provenance and rollback record.

### Force-rebase the candidate for a clean history

Rejected because it can discard reviewed commit identity, obscure conflict decisions, and detach review evidence from the content it evaluated.

## Verification

The decision is satisfied when:

- one compatibility pull request remains authoritative;
- reconciliation preserves reviewed history;
- the resulting head is mergeable and frozen;
- scope exclusions are explicit;
- exact-head validation and independent replay pass;
- review findings are mapped to the final head;
- both downstream consumers validate the same approved manifest identity;
- publication uses the accepted source commit.

## Supersession

A future release may adopt a different branching or release model only through a new ADR that preserves exact identity, review provenance, evidence integrity, and downstream migration.

<!-- QSO-CONSENT-CAPACITY-LOCK-v1 -->
