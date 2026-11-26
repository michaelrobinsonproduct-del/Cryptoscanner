# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T12:51:25.688732+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45823276375
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 868d40ce3181f8e5c67e63c0c0aa2f2cd2b05d43 (atomic ledger/results publication)
**Ledger generation:** 1863 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 588; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 150.46 | 93.566 | 72.853 | +3.91% | +1.14% | 7.29x | 7.3 | 2026-11-26T12:51:17.098361+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | LTC/USD | 43.53 | 84.482 | 67.291 | +1.92% | +0.44% | 4.42x | 2.3 | 2026-11-26T12:51:17.098361+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | SYRUP/USD | 0.07232 | 72.517 | 68.976 | +9.13% | -0.43% | 1.57x | 16.6 | 2026-11-26T12:51:17.098361+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | TAO/USD | 184.5049 | 70.936 | 63.958 | +1.60% | +0.44% | 1.48x | 4.5 | 2026-11-26T12:51:17.098361+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 5 | ADA/USD | 0.148995 | 68.605 | 68.775 | +2.21% | +0.40% | 0.78x | 3.4 | 2026-11-26T12:51:17.098361+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 6 | XBT/USD | 60800 | 67.096 | 59.994 | +0.71% | +0.33% | 1.55x | 0.0 | 2026-11-26T12:51:17.098361+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 7 | XRP/USD | 0.94972 | 62.773 | 64.783 | +1.41% | +0.07% | 0.76x | 0.1 | 2026-11-26T12:51:17.098361+00:00 | Not calibrated | MODERATE 51/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0567581 | 61.738 | 61.040 | +1.43% | +0.22% | 0.96x | 0.0 | 2026-11-26T12:51:17.098361+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 9 | NEAR/USD | 3.0914 | 61.688 | 62.584 | +1.36% | +0.63% | 0.60x | 3.9 | 2026-11-26T12:51:17.098361+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | LINK/USD | 9.22697 | 60.631 | 67.951 | +2.02% | +0.31% | 0.11x | 2.3 | 2026-11-26T12:51:17.098361+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | INJ/USD | 6.195 | 58.865 | 68.461 | +4.05% | -0.15% | 0.11x | 6.5 | 2026-11-26T12:51:17.098361+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | SUI/USD | 0.6681 | 56.168 | 56.143 | +0.27% | +0.13% | 0.94x | 1.5 | 2026-11-26T12:51:17.098361+00:00 | Not calibrated | MODERATE 48/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 72.853 | 150.46 | +1.14% | 7.29x |
| 2 | SYRUP/USD | 68.976 | 0.07232 | -0.43% | 1.57x |
| 3 | ADA/USD | 68.775 | 0.148995 | +0.40% | 0.78x |
| 4 | INJ/USD | 68.461 | 6.195 | -0.15% | 0.11x |
| 5 | LINK/USD | 67.951 | 9.22697 | +0.31% | 0.11x |
| 6 | LTC/USD | 67.291 | 43.53 | +0.44% | 4.42x |
| 7 | XRP/USD | 64.783 | 0.94972 | +0.07% | 0.76x |
| 8 | TAO/USD | 63.958 | 184.5049 | +0.44% | 1.48x |
| 9 | NEAR/USD | 62.584 | 3.0914 | +0.63% | 0.60x |
| 10 | XDG/USD | 61.040 | 0.0567581 | +0.22% | 0.96x |
| 11 | XBT/USD | 59.994 | 60800 | +0.33% | 1.55x |
| 12 | SUI/USD | 56.143 | 0.6681 | +0.13% | 0.94x |

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

- Persisted scans: 1863; predictions: 16091; observations: 1129125.
- Matured sampled outcomes across 1/6/24/48h: 34826; gap abstentions: 24774. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45823276375 · **Generation:** 1863 · **Legacy run:** 45823276375
**Main quote time:** 2026-11-26T12:51:25.688732+00:00 · **Legacy report time:** 2026-11-26T12:52:40.233090+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 150.46 | 93.57 | +1.14% | 7.29x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | LTC/USD ⭐ | 43.53 | 84.48 | +0.44% | 4.42x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SYRUP/USD | 0.07232 | 72.52 | -0.43% | 1.57x | MODERATE 51/100 | VERY_HIGH 72/100 | Watch |
| 4 | TAO/USD | 184.5049 | 70.94 | +0.44% | 1.48x | STRONG 80/100 | HIGH 55/100 | Watch |
| 5 | ADA/USD | 0.148995 | 68.61 | +0.40% | 0.78x | MODERATE 64/100 | HIGH 62/100 | Watch |
| 6 | XBT/USD | 60800 | 67.10 | +0.33% | 1.55x | STRONG 79/100 | HIGH 55/100 | Watch |
| 7 | XRP/USD | 0.94972 | 62.77 | +0.07% | 0.76x | MODERATE 51/100 | HIGH 62/100 | Watch |
| 8 | XDG/USD | 0.0567581 | 61.74 | +0.22% | 0.96x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 9 | NEAR/USD | 3.0914 | 61.69 | +0.63% | 0.60x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 10 | LINK/USD | 9.22697 | 60.63 | +0.31% | 0.11x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 11 | INJ/USD | 6.195 | 58.87 | -0.15% | 0.11x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | SUI/USD | 0.6681 | 56.17 | +0.13% | 0.94x | MODERATE 48/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 150.46 | 96.18 | +1.14% | 7.29x | 9225 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SEI/USD | 0.03732 | 85.25 | +0.56% | 2.84x | 3376 | STRONG 98/100 | HIGH 60/100 | Consider small entry |
| 3 | LTC/USD ⭐ | 43.55 | 80.32 | +0.44% | 4.42x | 15630 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SKY/USD | 0.04721 | 75.94 | +0.85% | 1.18x | 5037 | STRONG 73/100 | HIGH 67/100 | Watch |

**Same-run overlap:** QNT/USD, LTC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
