# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T19:21:45.115862+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45247746971
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2c4cdb182d0fc8963f401d9aa9011a39c117a1ad (atomic ledger/results publication)
**Ledger generation:** 1471 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ALGO/USD | 0.08306 | 100.183 | 92.353 | +10.12% | -1.43% | 3.88x | 1.2 | 2026-11-23T19:21:38.905260+00:00 | Not calibrated | STRONG 80/100 | HIGH 65/100 | Do nothing | WATCH |
| 2 | UNI/USD | 4.9118 | 97.194 | 84.186 | +4.93% | -0.40% | 3.05x | 4.5 | 2026-11-23T19:21:38.905260+00:00 | Not calibrated | STRONG 79/100 | HIGH 61/100 | Watch | WATCH |
| 3 | INJ/USD | 6.623 | 96.907 | 93.672 | +6.34% | -0.30% | 1.47x | 7.6 | 2026-11-23T19:21:38.905260+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 4 | CC/USD | 0.07865 | 95.054 | 78.459 | +7.34% | +0.32% | 2.80x | 6.4 | 2026-11-23T19:21:38.905260+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 5 | XMR/USD | 508.91 | 88.375 | 76.060 | +3.08% | -0.54% | 3.15x | 1.0 | 2026-11-23T19:21:38.905260+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SOL/USD | 73.36 | 82.636 | 81.375 | +3.87% | -0.30% | 1.28x | 1.4 | 2026-11-23T19:21:38.905260+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 7 | PAXG/USD | 3645 | 81.244 | 66.031 | +2.04% | +0.04% | 3.45x | 0.0 | 2026-11-23T19:21:38.905260+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 8 | LTC/USD | 41.78 | 79.362 | 80.842 | +4.03% | -0.21% | 0.96x | 4.8 | 2026-11-23T19:21:38.905260+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 9 | ADA/USD | 0.149562 | 79.149 | 77.267 | +3.43% | -0.54% | 1.46x | 3.5 | 2026-11-23T19:21:38.905260+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6855 | 77.529 | 85.354 | +4.54% | -0.04% | 0.24x | 2.9 | 2026-11-23T19:21:38.905260+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XBT/USD | 61600 | 71.213 | 59.911 | +0.70% | -0.08% | 2.17x | 0.0 | 2026-11-23T19:21:38.905260+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 12 | XRP/USD | 0.95206 | 69.918 | 73.190 | +2.64% | -0.17% | 0.76x | 0.6 | 2026-11-23T19:21:38.905260+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 93.672 | 6.623 | -0.30% | 1.47x |
| 2 | ALGO/USD | 92.353 | 0.08306 | -1.43% | 3.88x |
| 3 | SUI/USD | 85.354 | 0.6855 | -0.04% | 0.24x |
| 4 | UNI/USD | 84.186 | 4.9118 | -0.40% | 3.05x |
| 5 | SOL/USD | 81.375 | 73.36 | -0.30% | 1.28x |
| 6 | LTC/USD | 80.842 | 41.78 | -0.21% | 0.96x |
| 7 | CC/USD | 78.459 | 0.07865 | +0.32% | 2.80x |
| 8 | ADA/USD | 77.267 | 0.149562 | -0.54% | 1.46x |
| 9 | XMR/USD | 76.060 | 508.91 | -0.54% | 3.15x |
| 10 | XRP/USD | 73.190 | 0.95206 | -0.17% | 0.76x |
| 11 | PAXG/USD | 66.031 | 3645 | +0.04% | 3.45x |
| 12 | XBT/USD | 59.911 | 61600 | -0.08% | 2.17x |

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

- Persisted scans: 1471; predictions: 12419; observations: 890941.
- Matured sampled outcomes across 1/6/24/48h: 21952; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45247746971 · **Generation:** 1471 · **Legacy run:** 45247746971
**Main quote time:** 2026-11-23T19:21:45.115862+00:00 · **Legacy report time:** 2026-11-23T19:22:52.953493+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD | 0.08306 | 100.18 | -1.43% | 3.88x | STRONG 80/100 | HIGH 65/100 | Do nothing |
| 2 | UNI/USD | 4.9118 | 97.19 | -0.40% | 3.05x | STRONG 79/100 | HIGH 61/100 | Watch |
| 3 | INJ/USD | 6.623 | 96.91 | -0.30% | 1.47x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 4 | CC/USD | 0.07865 | 95.05 | +0.32% | 2.80x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 5 | XMR/USD | 508.91 | 88.38 | -0.54% | 3.15x | STRONG 74/100 | HIGH 61/100 | Watch |
| 6 | SOL/USD | 73.36 | 82.64 | -0.30% | 1.28x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 7 | PAXG/USD | 3645 | 81.24 | +0.04% | 3.45x | STRONG 86/100 | HIGH 55/100 | Watch |
| 8 | LTC/USD | 41.78 | 79.36 | -0.21% | 0.96x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 9 | ADA/USD | 0.149562 | 79.15 | -0.54% | 1.46x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 10 | SUI/USD | 0.6855 | 77.53 | -0.04% | 0.24x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 11 | XBT/USD | 61600 | 71.21 | -0.08% | 2.17x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 12 | XRP/USD | 0.95206 | 69.92 | -0.17% | 0.76x | WEAK 40/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
