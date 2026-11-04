# Owner E — bounded retained Kraken hindsight-entry candidates (2026-11-02 UTC)

**Purpose:** progress beyond a generic data-readiness inventory without mislabeling historical OHLC as a tradable, authenticated first-entry dataset. All work is isolated on draft PR #125; no model/scoring/writer/cron/ledger/trading/production changes.

## Source and reproducibility

- Reused actual GitHub Actions [run 41154739332](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41154739332), retained OHLC artifact **13024232238** (expires **2026-11-30 01:19 UTC**). Downloaded and rehashed outer ZIP SHA256 **f69a0d1a8611ed10259f4884f4427c5e131c39d82c556dbe1602d1b7aa298b59**, and inner `reusable_ohlc_evidence.zip` SHA256 **704513836ee4b35680fde0ff93a3bb3e8ed6e39469a7183afd89b1ddb01a52a2**, matching previously independently verified values. Original 9GB archive was not rehashed this run.
- Ran bounded `research.retained_first_entry_candidates` against the actual inner ZIP after member SHA, manifest, geometry, row, chronology and source identity checks from `research.kraken_archive_readiness.inspect_retained`. **48 markets / 341,233 retained rows**; no network or source regeneration.
- Entry price is **close of a five-minute candle**; hindsight target is **highest high of the next full 1/6/24/48h candles**, excluding the entry candle. Never cross a missing candle interval. Decimal threshold comparisons at +20% and +30%. This is a *possible historical price path*, not evidence an order could execute.
- A secondary fixed-phase cohort starts only after 12 prior contiguous candles and strides by the full outcome horizon to avoid overlapping future windows *within a market*. Phase sensitivity, correlated markets, survivorship, fees, spread, slippage and selection bias remain; **not statistically independent or held-out validation**.

## Actual retained data — descriptive candidates, NOT verified positive/negative labels

| Horizon | Full contiguous entry windows | Hindsight +30% entry windows (overlapping) | Fixed non-overlap cohort entries | Cohort hindsight +30% | Cohort hindsight below +30% |
|---|---:|---:|---:|---:|---:|
| 1h | 54,007 | 330 | 3,583 | 11 | 3,572 |
| 6h | 22,721 | 224 | 368 | 5 | 363 |
| 24h | 11,150 | 85 | 45 | 1 | 44 |
| 48h | 9,129 | 1 | 17 | 0 | 17 |

The full candidate-window totals conserve exactly with the prior independent archive-readiness auditor. The +30% counts are **potential hindsight windows, not distinct surges**. In particular, the single 48h overlapping +30% window does not enter the fixed cohort. The cohort is sparse at 24h/48h; it cannot support model claims. The 1h +30% count is **330 with exact Decimal comparisons**, not a float-rounded count.

**Authenticated first-entry episodes: still unquantifiable (0 certifiable from these artifacts), not zero actual movers.** Historical first-observed-at, complete authenticated trade paths, source-bound order/quote chronology and point-in-time spread/depth are absent. No claimed predictive lift, trained rule, production promotion or forward execution result.

## Next executable source requirement

1. Verify full Kraken trade-archive digest and full trade-bucket coverage on the exact selected 48-market cohort; preserve event sequence for same-timestamp trade ties.
2. Acquire or reconstruct verifiable historical *first-observed* quote timestamps and entry-time bid/ask/spread/depth/volume. If unavailable for historical dates, explicitly classify historical OHLC as research-only and begin collecting these features live for prospective validation instead of fabricating them.
3. Only then build independent first-eligible-entry positive/negative episodes, purged chronological held-out evaluation and shadow challenger comparison. Do not alter scoring before measured out-of-sample benefit.

Run: `python -m research.retained_first_entry_candidates --retained-zip reusable_ohlc_evidence.zip --output candidate_report.json`.
