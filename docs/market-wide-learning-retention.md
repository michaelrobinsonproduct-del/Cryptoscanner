# Market-wide learning durable recovery handoff

**Scope:** isolated Kraken spot paper research. No production ranking change, canonical ledger writer, trading, or new paid infrastructure.

The compact strict seed is equivalent to the original historical training fit;
it is NOT a substitute for the complete historical cohorts for other horizons.
Preserve both. The published canonical scanner result is not modified by this
process. The independent learning receipt reports scope, model version, source
counts and exact writer generation separately.

## Staged evidence

The PR-only backup job stages source cohorts from immutable completed runs
44220694310 (Q2), 44220694272 (Q3), 44227877790 (retained November),
44244545891 (compact seed), and a verified recent learning and historical
trade checkpoint from 44244937090. Each cohort's pinned digest is checked.
The seed tar is extracted and checked against the pinned manifest; the
partitioned state is restored and checked against its original digest.
The historical trade manifest and raw cursor receipts are validated by replay.
The manifest covers every file to detect corruption in durable storage.

The staged ZIP is an Actions artifact, **not yet durable**. It expires under
the repo's artifact retention policy. The original raw exchange archives
are not inside this bundle; the reconstructed full cohorts and their source
hashes are. Missing historical windows and unqualified source authentication
are still explicit.

## Publication and restore

Do not publish without owner approval. GitHub release assets in this public
repository are public. Inspect the staged contents; no credentials, account
data, or private information should be included. Use a dedicated research
release, separate from scanner deployment, with no overwrite of existing
assets. Upload the seed tar and checksummed backup, then independently
download the assets and verify the manifest hashes before considering them
durable. Set repository variable MARKET_WIDE_SEED_RELEASE_TAG to the approved
tag only after that verification. The compact seed loader also verifies the
pinned internal manifest and original-source receipts.

Main's independent learning job requires explicit one-time bootstrap after an
approved merge; subsequent jobs refuse a missing checkpoint rather than
falling back to an older snapshot. The first main bootstrap is a pinned PR
research checkpoint, not a production scan or promoted model. If main state
is unavailable, restore a verified backup at or after the last accepted
generation, and document the exact recovery source. Never use first-bootstrap
as a reset. The latest main checkpoint still needs a durable recurring
publication/readback mechanism before artifact expiry. No such remote write
is enabled by this rehearsal.

## Activation gate

Before production integration: all exact-head gates pass; backup and
readback verified; main-specific continuity and explicit bootstrap approved;
independent learning receipt consumed read-only by delivery; no change to
production scoring; preserve shadow-only status until paired live evidence
qualifies. Present unavailable outcomes as unavailable, not zero losses.
