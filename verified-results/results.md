# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T17:25:18.387747+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44358344147
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** acb3cea4643c93677023a91d90d918423471f331 (atomic ledger/results publication)
**Ledger generation:** 623 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019887 | 92.276 | 73.042 | +6.52% | +0.96% | 2.44x | 6.0 | 2026-11-18T17:25:13.058545+00:00 | Not calibrated | STRONG 100/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | MEGA/USD | 0.05348 | 59.016 | 49.553 | +3.56% | +0.55% | 1.67x | 13.1 | 2026-11-18T17:25:13.058545+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | CC/USD | 0.0833 | 49.669 | 42.548 | +1.42% | +0.98% | 1.22x | 6.0 | 2026-11-18T17:25:13.058545+00:00 | Not calibrated | MODERATE 60/100 | HIGH 67/100 | Watch | WATCH |
| 4 | TRUST/USD | 0.04961 | 48.854 | 52.686 | +5.22% | +0.65% | 0.29x | 32.3 | 2026-11-18T17:25:13.058545+00:00 | Not calibrated | WEAK 44/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | MNT/USD | 0.3859 | 48.808 | 51.562 | +3.38% | +0.03% | 0.71x | 7.8 | 2026-11-18T17:25:13.058545+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 6 | XPL/USD | 0.0468 | 37.648 | 28.703 | +0.86% | +0.86% | 1.46x | 21.4 | 2026-11-18T17:25:13.058545+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | ZAMA/USD | 0.06037 | 28.419 | 30.060 | +0.73% | +0.25% | 0.71x | 13.2 | 2026-11-18T17:25:13.058545+00:00 | Not calibrated | WEAK 39/100 | EXTREME 88/100 | Do nothing | WATCH |
| 8 | AKE/USD | 0.01008725 | 20.586 | 24.275 | +1.03% | +0.18% | 0.54x | 32.9 | 2026-11-18T17:25:13.058545+00:00 | Not calibrated | WEAK 20/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 73.042 | 0.019887 | +0.96% | 2.44x |
| 2 | TRUST/USD | 52.686 | 0.04961 | +0.65% | 0.29x |
| 3 | MNT/USD | 51.562 | 0.3859 | +0.03% | 0.71x |
| 4 | MEGA/USD | 49.553 | 0.05348 | +0.55% | 1.67x |
| 5 | CC/USD | 42.548 | 0.0833 | +0.98% | 1.22x |
| 6 | ZAMA/USD | 30.060 | 0.06037 | +0.25% | 0.71x |
| 7 | XPL/USD | 28.703 | 0.0468 | +0.86% | 1.46x |
| 8 | AKE/USD | 24.275 | 0.01008725 | +0.18% | 0.54x |

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

- Persisted scans: 623; predictions: 5313; observations: 376414.
- Matured sampled outcomes across 1/6/24/48h: 4616; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44358344147 · **Generation:** 623 · **Legacy run:** 44358344147
**Main quote time:** 2026-11-18T17:25:18.387747+00:00 · **Legacy report time:** 2026-11-18T17:25:45.364580+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019887 | 92.28 | +0.96% | 2.44x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | MEGA/USD ⭐ | 0.05348 | 59.02 | +0.55% | 1.67x | STRONG 80/100 | VERY_HIGH 73/100 | Watch |
| 3 | CC/USD ⭐ | 0.0833 | 49.67 | +0.98% | 1.22x | STRONG 70/100 | HIGH 67/100 | Watch |
| 4 | TRUST/USD | 0.04961 | 48.85 | +0.65% | 0.29x | WEAK 44/100 | EXTREME 87/100 | Do nothing |
| 5 | MNT/USD | 0.3859 | 48.81 | +0.03% | 0.71x | WEAK 44/100 | VERY_HIGH 75/100 | Watch |
| 6 | XPL/USD ⭐ | 0.0468 | 37.65 | +0.86% | 1.46x | MODERATE 64/100 | VERY_HIGH 72/100 | Watch |
| 7 | ZAMA/USD | 0.06037 | 28.42 | +0.25% | 0.71x | WEAK 39/100 | EXTREME 88/100 | Do nothing |
| 8 | AKE/USD | 0.01008725 | 20.59 | +0.18% | 0.54x | WEAK 20/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019894 | 81.22 | +0.96% | 2.44x | 5959 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | MEGA/USD ⭐ | 0.05348 | 57.79 | +0.55% | 1.67x | 1202 | STRONG 79/100 | VERY_HIGH 73/100 | Watch |
| 3 | CC/USD ⭐ | 0.0833 | 46.27 | +0.98% | 1.22x | 4946 | MODERATE 68/100 | HIGH 67/100 | Watch |
| 4 | XPL/USD ⭐ | 0.0468 | 28.02 | +0.86% | 1.46x | 1345 | MODERATE 59/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** SENT/USD, MEGA/USD, CC/USD, XPL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
