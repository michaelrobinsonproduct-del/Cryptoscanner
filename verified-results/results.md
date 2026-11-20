# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T03:05:34.642592+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44665202094
**Source SHA:** fc0d0a182774d90ae3acc1755dd1961302ab9d4a
**Previous ledger commit:** d8026e34d28f41390bb3328a992b139861e00fa2 (atomic ledger/results publication)
**Ledger generation:** 912 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PROS/USD | 0.5775 | 78.832 | 70.683 | +7.20% | +1.16% | 1.24x | 10.4 | 2026-11-20T03:05:31.259706+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 2 | SAPIEN/USD | 0.04223 | 39.709 | 51.405 | +5.15% | -5.84% | 2.33x | 30.8 | 2026-11-20T03:05:31.259706+00:00 | Not calibrated | WEAK 40/100 | EXTREME 89/100 | Do nothing | WATCH |
| 3 | NIGHT/USD | 0.04493 | 33.376 | 41.289 | +0.38% | +0.27% | 0.08x | 4.5 | 2026-11-20T03:05:31.259706+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | BLUR/USD | 0.00673 | 26.367 | 20.604 | +0.60% | +0.90% | 1.13x | 29.9 | 2026-11-20T03:05:31.259706+00:00 | Not calibrated | WEAK 38/100 | EXTREME 86/100 | Do nothing | WATCH |
| 5 | ICNT/USD | 0.4287 | 23.293 | 25.573 | +0.61% | +0.26% | 0.64x | 32.8 | 2026-11-20T03:05:31.259706+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PROS/USD | 70.683 | 0.5775 | +1.16% | 1.24x |
| 2 | SAPIEN/USD | 51.405 | 0.04223 | -5.84% | 2.33x |
| 3 | NIGHT/USD | 41.289 | 0.04493 | +0.27% | 0.08x |
| 4 | ICNT/USD | 25.573 | 0.4287 | +0.26% | 0.64x |
| 5 | BLUR/USD | 20.604 | 0.00673 | +0.90% | 1.13x |

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

- Persisted scans: 912; predictions: 7893; observations: 551061.
- Matured sampled outcomes across 1/6/24/48h: 8959; gap abstentions: 16469. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44665202094 · **Generation:** 912 · **Legacy run:** 44665202094
**Main quote time:** 2026-11-20T03:05:34.642592+00:00 · **Legacy report time:** 2026-11-20T03:06:32.083880+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PROS/USD ⭐ | 0.5775 | 78.83 | +1.16% | 1.24x | STRONG 79/100 | VERY_HIGH 80/100 | Watch |
| 2 | SAPIEN/USD | 0.04223 | 39.71 | -5.84% | 2.33x | WEAK 40/100 | EXTREME 89/100 | Do nothing |
| 3 | NIGHT/USD | 0.04493 | 33.38 | +0.27% | 0.08x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 4 | BLUR/USD ⭐ | 0.00673 | 26.37 | +0.90% | 1.13x | MODERATE 48/100 | EXTREME 86/100 | Do nothing |
| 5 | ICNT/USD | 0.4287 | 23.29 | +0.26% | 0.64x | WEAK 32/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PROS/USD ⭐ | 0.5775 | 62.21 | +1.16% | 1.24x | 1112 | MODERATE 66/100 | EXTREME 86/100 | Do nothing |
| 2 | BLUR/USD ⭐ | 0.00673 | 17.54 | +0.90% | 1.13x | 762 | WEAK 44/100 | EXTREME 86/100 | Do nothing |

**Same-run overlap:** PROS/USD, BLUR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
