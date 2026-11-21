# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T13:40:54.222031+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44909953758
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** f0fcf298349871d75b45af0859c2c7c1459d36c8 (atomic ledger/results publication)
**Ledger generation:** 1140 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.7324 | 128.116 | 88.933 | +5.94% | +4.84% | 10.33x | 15.2 | 2026-11-21T13:40:48.291503+00:00 | Not calibrated | STRONG 100/100 | VERY_HIGH 71/100 | Watch | WATCH |
| 2 | ETH/USD | 1699.17 | 112.379 | 86.632 | +4.93% | +2.15% | 4.35x | 5.8 | 2026-11-21T13:40:48.291503+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | VVV/USD | 23.056 | 111.012 | 95.013 | +11.17% | +1.41% | 1.90x | 10.0 | 2026-11-21T13:40:48.291503+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | USELESS/USD | 0.0799 | 106.717 | 72.959 | +7.25% | +3.75% | 8.44x | 25.1 | 2026-11-21T13:40:48.291503+00:00 | Not calibrated | STRONG 95/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 5 | ZEC/USD | 795.46 | 103.769 | 83.831 | +4.95% | +2.40% | 1.79x | 11.7 | 2026-11-21T13:40:48.291503+00:00 | Not calibrated | STRONG 90/100 | HIGH 61/100 | Consider small entry | WATCH |
| 6 | XBT/USD | 60336.7 | 95.776 | 70.215 | +2.60% | +2.11% | 2.85x | 6.0 | 2026-11-21T13:40:48.291503+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | AVAX/USD | 6.648 | 93.289 | 67.268 | +2.18% | +2.20% | 4.19x | 6.0 | 2026-11-21T13:40:48.291503+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | TAO/USD | 186.9297 | 90.731 | 73.959 | +3.56% | +1.55% | 1.90x | 11.9 | 2026-11-21T13:40:48.291503+00:00 | Not calibrated | STRONG 85/100 | HIGH 61/100 | Consider small entry | WATCH |
| 9 | XRP/USD | 0.92352 | 90.555 | 65.379 | +1.63% | +2.04% | 6.32x | 2.1 | 2026-11-21T13:40:48.291503+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 10 | SOL/USD | 70.26 | 89.923 | 67.944 | +2.26% | +1.40% | 4.05x | 5.7 | 2026-11-21T13:40:48.291503+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 11 | XLM/USD | 0.129116 | 88.305 | 64.066 | +1.51% | +1.85% | 3.81x | 2.9 | 2026-11-21T13:40:48.291503+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 12 | XMR/USD | 475.33 | 82.243 | 79.163 | +4.17% | +1.27% | 0.67x | 10.1 | 2026-11-21T13:40:48.291503+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 95.013 | 23.056 | +1.41% | 1.90x |
| 2 | UNI/USD | 88.933 | 4.7324 | +4.84% | 10.33x |
| 3 | ETH/USD | 86.632 | 1699.17 | +2.15% | 4.35x |
| 4 | ZEC/USD | 83.831 | 795.46 | +2.40% | 1.79x |
| 5 | XMR/USD | 79.163 | 475.33 | +1.27% | 0.67x |
| 6 | TAO/USD | 73.959 | 186.9297 | +1.55% | 1.90x |
| 7 | USELESS/USD | 72.959 | 0.0799 | +3.75% | 8.44x |
| 8 | XBT/USD | 70.215 | 60336.7 | +2.11% | 2.85x |
| 9 | SOL/USD | 67.944 | 70.26 | +1.40% | 4.05x |
| 10 | AVAX/USD | 67.268 | 6.648 | +2.20% | 4.19x |
| 11 | XRP/USD | 65.379 | 0.92352 | +2.04% | 6.32x |
| 12 | XLM/USD | 64.066 | 0.129116 | +1.85% | 3.81x |

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

- Persisted scans: 1140; predictions: 8989; observations: 689479.
- Matured sampled outcomes across 1/6/24/48h: 11786; gap abstentions: 20394. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 1; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44909953758 · **Generation:** 1140 · **Legacy run:** 44909953758
**Main quote time:** 2026-11-21T13:40:54.222031+00:00 · **Legacy report time:** 2026-11-21T13:41:59.772780+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.7324 | 128.12 | +4.84% | 10.33x | STRONG 100/100 | VERY_HIGH 71/100 | Watch |
| 2 | ETH/USD ⭐ | 1699.17 | 112.38 | +2.15% | 4.35x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | VVV/USD ⭐ | 23.056 | 111.01 | +1.41% | 1.90x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | USELESS/USD ⭐ | 0.0799 | 106.72 | +3.75% | 8.44x | STRONG 100/100 | VERY_HIGH 77/100 | Watch |
| 5 | ZEC/USD ⭐ | 795.46 | 103.77 | +2.40% | 1.79x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 6 | XBT/USD ⭐ | 60336.7 | 95.78 | +2.11% | 2.85x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | AVAX/USD | 6.648 | 93.29 | +2.20% | 4.19x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | TAO/USD ⭐ | 186.9297 | 90.73 | +1.55% | 1.90x | STRONG 95/100 | HIGH 61/100 | Consider small entry |
| 9 | XRP/USD ⭐ | 0.92352 | 90.56 | +2.04% | 6.32x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 10 | SOL/USD ⭐ | 70.26 | 89.92 | +1.40% | 4.05x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 11 | XLM/USD | 0.129116 | 88.30 | +1.85% | 3.81x | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 12 | XMR/USD | 475.33 | 82.24 | +1.27% | 0.67x | MODERATE 66/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD ⭐ | 1695.85 | 100.00 | +2.15% | 4.35x | 101607 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UNI/USD ⭐ | 4.704 | 100.00 | +4.84% | 10.33x | 13238 | STRONG 100/100 | VERY_HIGH 71/100 | Watch |
| 3 | ZEC/USD ⭐ | 792.26 | 98.01 | +2.40% | 1.79x | 57362 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | VVV/USD ⭐ | 23.132 | 92.81 | +1.41% | 1.90x | 14915 | STRONG 96/100 | HIGH 61/100 | Consider small entry |
| 5 | USELESS/USD ⭐ | 0.07963 | 92.28 | +3.75% | 8.44x | 5114 | STRONG 100/100 | VERY_HIGH 77/100 | Watch |
| 6 | TAO/USD ⭐ | 186.6819 | 86.31 | +1.55% | 1.90x | 16556 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 7 | SOL/USD ⭐ | 70.14 | 83.46 | +1.40% | 4.05x | 58169 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | XBT/USD ⭐ | 60301.4 | 83.04 | +2.11% | 2.85x | 277951 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | XRP/USD ⭐ | 0.92254 | 78.52 | +2.04% | 6.32x | 68864 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 10 | AAVE/USD | 100.8 | 74.52 | +1.51% | 1.61x | 8491 | STRONG 82/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** UNI/USD, ETH/USD, VVV/USD, USELESS/USD, ZEC/USD, XBT/USD, TAO/USD, XRP/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
