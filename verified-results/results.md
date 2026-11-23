# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T07:11:32.084914+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45129067475
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2951c776e7f33ff97038ab01f28d79385ab59729 (atomic ledger/results publication)
**Ledger generation:** 1397 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05034 | 80.656 | 62.858 | +2.38% | +0.86% | 2.35x | 9.9 | 2026-11-23T07:11:24.995178+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | SUI/USD | 0.6659 | 71.633 | 65.138 | +1.56% | +0.05% | 1.63x | 1.5 | 2026-11-23T07:11:24.995178+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 3 | PAXG/USD | 3617.42 | 68.814 | 53.083 | +1.27% | +0.15% | 3.60x | 0.9 | 2026-11-23T07:11:24.995178+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 4 | JUP/USD | 0.23862 | 65.439 | 72.653 | +6.26% | -0.29% | 0.42x | 11.3 | 2026-11-23T07:11:24.995178+00:00 | Not calibrated | WEAK 33/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | NEAR/USD | 3.0155 | 64.285 | 62.769 | +1.13% | +0.06% | 1.12x | 0.3 | 2026-11-23T07:11:24.995178+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 6 | BLESS/USD | 0.017933 | 64.031 | 63.650 | +11.43% | +0.77% | 0.65x | 40.3 | 2026-11-23T07:11:24.995178+00:00 | Not calibrated | MODERATE 47/100 | EXTREME 92/100 | Do nothing | WATCH |
| 7 | SOL/USD | 72.11 | 63.213 | 68.974 | +2.10% | +0.21% | 0.32x | 1.4 | 2026-11-23T07:11:24.995178+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | CC/USD | 0.0763 | 62.981 | 62.282 | +4.14% | -0.04% | 1.09x | 3.9 | 2026-11-23T07:11:24.995178+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 9 | DOT/USD | 0.6739 | 61.474 | 46.251 | +1.98% | +0.04% | 8.14x | 1.5 | 2026-11-23T07:11:24.995178+00:00 | Not calibrated | STRONG 76/100 | HIGH 60/100 | Watch | WATCH |
| 10 | XLM/USD | 0.128619 | 54.909 | 60.494 | +0.86% | +0.04% | 0.42x | 0.1 | 2026-11-23T07:11:24.995178+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XRP/USD | 0.94007 | 54.730 | 64.190 | +1.35% | -0.02% | 0.06x | 0.5 | 2026-11-23T07:11:24.995178+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | XBT/USD | 61412.4 | 52.192 | 57.765 | +0.40% | +0.00% | 0.44x | 0.0 | 2026-11-23T07:11:24.995178+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | JUP/USD | 72.653 | 0.23862 | -0.29% | 0.42x |
| 2 | SOL/USD | 68.974 | 72.11 | +0.21% | 0.32x |
| 3 | SUI/USD | 65.138 | 0.6659 | +0.05% | 1.63x |
| 4 | XRP/USD | 64.190 | 0.94007 | -0.02% | 0.06x |
| 5 | BLESS/USD | 63.650 | 0.017933 | +0.77% | 0.65x |
| 6 | NIGHT/USD | 62.858 | 0.05034 | +0.86% | 2.35x |
| 7 | NEAR/USD | 62.769 | 3.0155 | +0.06% | 1.12x |
| 8 | CC/USD | 62.282 | 0.0763 | -0.04% | 1.09x |
| 9 | XLM/USD | 60.494 | 0.128619 | +0.04% | 0.42x |
| 10 | XBT/USD | 57.765 | 61412.4 | +0.00% | 0.44x |
| 11 | PAXG/USD | 53.083 | 3617.42 | +0.15% | 3.60x |
| 12 | DOT/USD | 46.251 | 0.6739 | +0.04% | 8.14x |

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

- Persisted scans: 1397; predictions: 11531; observations: 845877.
- Matured sampled outcomes across 1/6/24/48h: 18746; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 123 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45129067475 · **Generation:** 1397 · **Legacy run:** 45129067475
**Main quote time:** 2026-11-23T07:11:32.084914+00:00 · **Legacy report time:** 2026-11-23T07:12:38.350002+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.05034 | 80.66 | +0.86% | 2.35x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SUI/USD | 0.6659 | 71.63 | +0.05% | 1.63x | STRONG 71/100 | HIGH 55/100 | Watch |
| 3 | PAXG/USD ⭐ | 3617.42 | 68.81 | +0.15% | 3.60x | STRONG 89/100 | HIGH 55/100 | Watch |
| 4 | JUP/USD | 0.23862 | 65.44 | -0.29% | 0.42x | WEAK 33/100 | EXTREME 87/100 | Do nothing |
| 5 | NEAR/USD | 3.0155 | 64.28 | +0.06% | 1.12x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 6 | BLESS/USD | 0.017933 | 64.03 | +0.77% | 0.65x | MODERATE 47/100 | EXTREME 92/100 | Do nothing |
| 7 | SOL/USD | 72.11 | 63.21 | +0.21% | 0.32x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 8 | CC/USD | 0.0763 | 62.98 | -0.04% | 1.09x | WEAK 41/100 | VERY_HIGH 73/100 | Watch |
| 9 | DOT/USD | 0.6739 | 61.47 | +0.04% | 8.14x | STRONG 76/100 | HIGH 60/100 | Watch |
| 10 | XLM/USD | 0.128619 | 54.91 | +0.04% | 0.42x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 11 | XRP/USD | 0.94007 | 54.73 | -0.02% | 0.06x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | XBT/USD | 61412.4 | 52.19 | +0.00% | 0.44x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD | 2.1302 | 73.96 | +0.09% | 1.16x | 7080 | MODERATE 57/100 | HIGH 68/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.05029 | 70.00 | +0.86% | 2.35x | 11153 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | PAXG/USD ⭐ | 3618.36 | 69.33 | +0.15% | 3.60x | 6995 | STRONG 90/100 | HIGH 55/100 | Watch |
| 4 | KAS/USD | 0.0266 | 68.99 | +0.49% | 31.49x | 2496 | STRONG 84/100 | HIGH 66/100 | Watch |

**Same-run overlap:** NIGHT/USD, PAXG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
