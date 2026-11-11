# Batch 38 — Repository historical implementation and artifact provenance review

Read-only investigation. No executable changes, CI claim, production access or history-branch data reads.

## Verified code provenance

- **Legacy-era historical implementation:** `rebuild_v2/history.py` at commit `b0f7565998a6b50d6747bebf396e924fd8ebbf11`, GitHub blob SHA `3fe2e0dd071622a7dab17e682f05913cf1f44236`. The file defines `runs(id,created_at,health,payload)`, `observations(run_id,pair,price,score,status)`, and `outcomes(run_id,pair,horizon_hours,return_pct,evaluated_at)`. It stores entire scan payload JSON in `runs.payload`, and marks `WATCH` vs `NOT_SELECTED` observations. This is a **promising source of original watchlists and non-selected population**, conditional on finding genuine immutable data. It is not proof of legacy score implementation parity or actual persisted rows.
- **Historical workflow:** commit `1dc5833f589123fc5144373bde7bb65a67094562` added an isolated scheduled Kraken research workflow that restored `simple-history:history.sqlite3`, checked SQLite integrity and appended snapshots. The commit's workflow diff establishes intended storage mechanics, **not** the branch's current existence, independent backup, completeness or hashes. It checked out `simplified-scanner-recovery-20261011`; the `simple_scanner/scan.py` path at this commit was unavailable (404), so that specific scorer is not pinned by this check.
- **Legacy workflow status:** commit `703d34f8230c78206f644228cf9405e3af2d5688` removed the five-minute schedule from `.github/workflows/kraken-reliability-watch.yml`; it does not provide a historical score or market-data artifact.
- **Present research scorer:** `simple_scanner/scan.py` on the repair branch implements Kraken ticker screening, OHLC validation, diversified candidate selection and early-signal score; source content is available, but production equivalence and the legacy scorer are unverified.

## Workflow artifacts and repository search

- GitHub Actions runs #127 (`39881070967`) and #120 (`39880831388`) each returned **zero attached artifacts**.
- Repository code searches for `legacy_score` and `OHLC` returned no matches in the default-branch index. These are limited searches, **not** an exhaustive audit of all historical branches.
- Commit search returned historical compatibility commits, including `b0f7565`; direct inspection confirmed a genuine older `rebuild_v2/history.py` blob. No historical raw ticker/OHLC file or verified dataset checksum was obtained.

## Parity readiness

| Requirement | Finding |
|---|---|
| Pinned legacy-era history schema and storage logic | **AVAILABLE as code** at `b0f7565` |
| Legacy run payloads / original watchlists | **POTENTIALLY AVAILABLE** in `runs.payload`, but no actual data read or verified |
| Non-selected population | **POTENTIALLY AVAILABLE** in `observations.status`, no actual data verified |
| Exact pinned legacy scoring algorithm | **NOT VERIFIED**; `rebuild_v2/history.py` does not define scanner scoring |
| Raw point-in-time Kraken ticker/OHLC | **NOT VERIFIED** |
| Independently verified immutable history, manifest and SHA-256 | **NOT VERIFIED** |
| Genuine historical replay and production-vs-legacy parity | **BLOCKED** |

## Shortest safe next action

Search repository **code only** for the historical `rebuild_v2` scanner entrypoint and its scoring formula, and compare that code with the pinned current scanner without executing scans. Then, **only with explicit separate authorization**, inventory the historical data branch or export to see whether `runs.payload` contains full watchlists and point-in-time inputs. Verify SHA-256 and provenance before any offline replay. Never treat Git blob SHA as an exported SQLite SHA-256.

**Release remains BLOCKED**: independent backup, actual history replay, real scoring parity, authenticated delivery, live rollback and scheduled reliability. No merge, deployment, production access, history deletion, model promotion or release-gate weakening.
