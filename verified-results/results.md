# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T02:01:32.229717+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45097618724
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 84bd1f0b862c5167eeb848dd7c80cf2b80ab625d (atomic ledger/results publication)
**Ledger generation:** 1365 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.38281 | 56.039 | 64.866 | +3.78% | -0.93% | 0.58x | 13.6 | 2026-11-23T02:01:25.954719+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 2 | CC/USD | 0.074 | 49.715 | 39.755 | +1.00% | +0.05% | 1.97x | 5.4 | 2026-11-23T02:01:25.954719+00:00 | Not calibrated | MODERATE 60/100 | HIGH 60/100 | Watch | WATCH |
| 3 | PAXG/USD | 3590.84 | 38.874 | 47.174 | +0.52% | -0.32% | 0.33x | 2.0 | 2026-11-23T02:01:25.954719+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | XAUT/USD | 3588.6 | 31.067 | 36.006 | +0.46% | -0.29% | 0.65x | 0.3 | 2026-11-23T02:01:25.954719+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 5 | PEARL/USD | 2.0742 | 26.954 | 35.525 | +0.96% | -1.40% | 0.84x | 25.1 | 2026-11-23T02:01:25.954719+00:00 | Not calibrated | WEAK 8/100 | VERY_HIGH 84/100 | Do nothing | WATCH |
| 6 | ICNT/USD | 0.3564 | 23.693 | 31.550 | +1.19% | +0.11% | 0.16x | 19.6 | 2026-11-23T02:01:25.954719+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 64.866 | 0.38281 | -0.93% | 0.58x |
| 2 | PAXG/USD | 47.174 | 3590.84 | -0.32% | 0.33x |
| 3 | CC/USD | 39.755 | 0.074 | +0.05% | 1.97x |
| 4 | XAUT/USD | 36.006 | 3588.6 | -0.29% | 0.65x |
| 5 | PEARL/USD | 35.525 | 2.0742 | -1.40% | 0.84x |
| 6 | ICNT/USD | 31.550 | 0.3564 | +0.11% | 0.16x |

The baseline ordering is over this same confirmed WATCH pool, not an independent full-market baseline scan.
The separate legacy-inspired scanner publishes its own WATCH signals in a later, read-only GitHub artifact linked by this paper run ID.

**30%+ in 48h probability:** NOT CALIBRATED. The separate signal-confidence index (0–100) expresses current setup strength, NOT odds of a gain. Risk varies by spread, momentum and volume; every candidate remains speculative. The action is a research consideration, not an executed or authorized trade. A more substantial entry requires independently qualified held-out calibration.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 1365; predictions: 11202; observations: 826391.
- Matured sampled outcomes across 1/6/24/48h: 17827; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 79 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45097618724 · **Generation:** 1365 · **Legacy run:** 45097618724
**Main quote time:** 2026-11-23T02:01:32.229717+00:00 · **Legacy report time:** 2026-11-23T02:02:40.067996+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.38281 | 56.04 | -0.93% | 0.58x | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing |
| 2 | CC/USD ⭐ | 0.074 | 49.72 | +0.05% | 1.97x | STRONG 70/100 | HIGH 60/100 | Watch |
| 3 | PAXG/USD | 3590.84 | 38.87 | -0.32% | 0.33x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | XAUT/USD | 3588.6 | 31.07 | -0.29% | 0.65x | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing |
| 5 | PEARL/USD | 2.0742 | 26.95 | -1.40% | 0.84x | WEAK 8/100 | VERY_HIGH 84/100 | Do nothing |
| 6 | ICNT/USD | 0.3564 | 23.69 | +0.11% | 0.16x | WEAK 27/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.07406 | 54.60 | +0.05% | 1.97x | 3726 | STRONG 72/100 | HIGH 60/100 | Watch |

**Same-run overlap:** CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
