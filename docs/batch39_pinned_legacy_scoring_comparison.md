# Batch 39 — Pinned legacy scorer vs current research scorer

Scope: read-only comparison of historical `rebuild_v2/scanner.py` and `rebuild_v2/history.py` at commit `b0f7565998a6b50d6747bebf396e924fd8ebbf11`, against `simple_scanner/scan.py` and `history.py` on the isolated repair branch. No execution, data reads, production access, code changes or new tests.

## Provenance

Historical scorer: `rebuild_v2/scanner.py`, commit `b0f7565998a6b50d6747bebf396e924fd8ebbf11`, Git blob SHA `f423b0f3f98161dddcea52faaabdbdc9688b4de6`. Historical ledger implementation: `rebuild_v2/history.py`, same commit, Git blob SHA `3fe2e0dd071622a7dab17e682f05913cf1f44236`. These hashes identify **source blobs**, not market-data archives or a historical SQLite export.

## Eligibility and scoring

Legacy `eligible_crypto_pair`: excludes a broad set of fiat/stable bases. `scan` requires online status, quote `ZUSD` or `USD`, and pair key not ending in `.d`. Ticker lookup tries pair key then altname. Current scanner requires online status and `wsname` ending `/USD`, with a different excluded-base set, and direct ticker key lookup. Universe mismatch must be measured, not silently normalized.

Legacy `rank(t)` requires last, open, bid positive and ask>=bid; uses ticker 24h volume and trade count. `move24_pct = 100*(last/open-1)`; `spread_bps=10000*(ask-bid)/bid`; raw score is
`min(48,max(0,move)*12)+min(22,trades/120)+min(15,volume*last/250000)+max(0,15-2*spread_bps)`, rounded to 2 decimals. `eligible_watch` requires score>=35, 0.5<=move<=12 and spread<=40. Current scanner requires 0.25<=move<=12, spread<=45, notional>=100000 and uses `min(45,move*7)+min(25,notional/150000)+max(0,30-spread/2)`, rounded to 1 decimal.

Legacy `scan` applies `historical_signal_adjustments()` and `pair_signal_adjustment(pair)` to each eligible watch score, then sorts descending by score and returns up to 20. The final -10<=move<=15 check is redundant after `eligible_watch` but does not alter that code's effective universe. Historical calibration depends on prior 4h outcomes; reconstructing rankings requires the ledger **as it existed before each scan**, including WATCH and NOT_SELECTED observations and outcomes. Current scanner diversifies 12+8+6+6 preselected candidates, validates fresh completed five-minute OHLC, computes 15m movement and volume acceleration, and returns top 12 by early-signal score. It does not apply historical calibration.

## Confirmation and freshness

Legacy double-confirms only the first five watches, with REST Depth+Trades twice separated by ~2 seconds, requiring recent trades age 0–120 seconds, valid book and spread<=100 bps; confirmation does not authorize entry and does not change watchlist ranking. Current scanner requires >=13 completed 5m candles and most recent completed candle age<=900 seconds; rejects missing/stale/invalid OHLC and then ranks validated candidates. Legacy raw ranking does not impose an explicit ticker timestamp freshness check; current ticker response is not individually timestamped either.

## Offline reproducibility

**Can reproduce from pinned code and synthetic/approved historical inputs:** eligibility predicate, raw score, score rounding, tie behavior given stable insertion order, calibration functions from reconstructed prior ledger, selection budgets and double-confirmation logic. No fixture code needs adding.

**Cannot claim genuine historical parity yet:** actual historical Kraken AssetPairs/Ticker (including 24h trades `t[1]`, volume `v[1]`, bid, ask, last, open, altname and quote), original ordering and missing-ticker failures; prior-as-of-time historical outcome ledger and calibration; Depth/Trades and timestamps for legacy confirmation; 5m OHLC close/volume and freshness for current challenger; immutable run outputs, selected/unselected labels and source versions; genuine outcome observation coverage. Legacy `runs.payload` **may** retain watchlists, market_quotes and calibration diagnostics, but its actual records have not been verified and the reported market_quotes omit trade count and open price.

## Minimal next step

Before requesting any new infrastructure, inspect existing **historical source code** for data-capture and historical-export workflows to determine whether immutable as-of-time ticker/OHLC snapshots were ever persisted. If no existing source captured them, document the replay ceiling and seek separately authorized archival evidence; never backfill with modern Kraken prices or infer old trade counts from score. Compare on equal candidate universes and time-aligned outcomes only when verified data exists.

**Release remains BLOCKED:** independent live backup, genuine historical replay, real production-vs-legacy scoring parity, authenticated GitHub delivery, live rollback and scheduled reliability. No merge, deployment, production access, history deletion, model promotion or release-gate weakening.
