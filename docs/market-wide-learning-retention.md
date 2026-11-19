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
as a reset. After approval, set MARKET_WIDE_CHECKPOINT_RELEASE_TAG to an explicit existing research release. The same learning workflow's main-only retention job publishes at most one immutable daily checkpoint (including cold history and fitted models), independently downloads it, verifies its bytes and restores its state, then publishes a SHA256 readback receipt. No overwrite or canonical ledger write is performed. The publication job is disabled unless the owner configures this tag. The normal main learning job retains every successful run in Actions artifacts; daily release checkpoints protect against artifact expiration, but can lag the last run. For approved exact main restore, supply market_learning_restore_asset, market_learning_restore_sha256, and market_learning_restore_state_digest on manual dispatch only when main's normal checkpoint is missing. The restore refuses mismatched scopes, archive checksums and state digests; prior research bootstrap never replaces main state.

## Activation gate

Before production integration: all exact-head gates pass; backup and
readback verified; main-specific continuity and explicit bootstrap approved;
independent learning receipt consumed read-only by delivery; no change to
production scoring; preserve shadow-only status until paired live evidence
qualifies. Present unavailable outcomes as unavailable, not zero losses.

Optional ongoing main historical cursor recovery is enabled only by MARKET_WIDE_HISTORICAL_RECOVERY_ENABLED=true after approval. It resumes the pinned PR cursor evidence on the explicit first bootstrap and normally accepts only its own completed main job artifacts. Missing research-only cursor evidence does not stop independently qualified strict training. A missing main recovery checkpoint is not silently reset.

### Activation order (owner-approved only)

1. Publish the verified staged seed and full-cohort backup to an approved research release; independently verify readback. Set the seed and durable checkpoint release tag variables. Leave MARKET_WIDE_LEARNING_ENABLED unset/false.
2. Merge the approved exact head after required CI. Normal writer dispatches continue legacy learning, with the independent job disabled until bootstrap. If ongoing historical cursor recovery is approved, set MARKET_WIDE_HISTORICAL_RECOVERY_ENABLED=true before bootstrap.
3. Dispatch the existing Paper Ledger Learning Read Only workflow on main with market_learning_bootstrap=true once, verifying the pinned current research state and durable readback. Never use a second writer or modify scanner scores.
4. Verify the main-specific learning receipt, model and cursor continuity; then set MARKET_WIDE_LEARNING_ENABLED=true. Later automatic writer dispatches use only main learning ancestors.
5. Delivery remains read-only. Read the newest completed main market-wide learning job receipt; verify its digest, source writer run, source SHA, ledger generation and checksum against verified canonical evidence. If the receipt predates the delivered scan, show the separate learning generation/timestamp and label it as lagging; never imply it contains the newest scan outcomes. Show training/positive counts, market coverage, mature per-version/horizon matched results, explicit unknown counts, and shadow-only status. Do not modify the production result or promote the model based on historical proxy comparison.

### Read-only receipt verification

Use `paper_pov.learning_delivery.verify_learning_delivery` with the exact main learning run, successful market-wide owner job, nonexpired matching continuity artifact metadata, the artifact receipt, its independently verified source writer publication and writer status, and the already verified delivered production publication. Verify the immutable historical publication separately for any lagged receipt. The helper preserves shadow-only status and returns CURRENT or LAGGING with explicit generation lag. A missing/invalid receipt must be reported as learning evidence unavailable, never as a failure of otherwise verified scanner prices. This helper does not authenticate exchange data or promote a model. Do not enable delivery consumption until the main learning bootstrap passes.
