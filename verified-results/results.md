# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T16:42:07.608054+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46035462716
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8f33a6483be8aecac130cb327ab6aa6d69b98def (atomic ledger/results publication)
**Ledger generation:** 2033 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 754.07 | 122.082 | 96.684 | +10.62% | +2.08% | 2.95x | 6.6 | 2026-11-27T16:42:00.749471+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | HYPE/USD | 64.62 | 89.826 | 80.455 | +3.86% | +0.37% | 1.75x | 3.1 | 2026-11-27T16:42:00.749471+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | UNI/USD | 4.7741 | 86.609 | 71.011 | +2.67% | +0.12% | 3.29x | 0.2 | 2026-11-27T16:42:00.749471+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SENT/USD | 0.022559 | 76.561 | 60.207 | +4.54% | +0.27% | 11.63x | 4.4 | 2026-11-27T16:42:00.749471+00:00 | Not calibrated | STRONG 93/100 | HIGH 67/100 | Consider small entry | WATCH |
| 5 | SPACE/USD | 0.004161 | 71.935 | 70.905 | +7.46% | +0.53% | 0.84x | 9.6 | 2026-11-27T16:42:00.749471+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.04956 | 71.643 | 67.031 | +2.25% | +1.48% | 0.72x | 6.1 | 2026-11-27T16:42:00.749471+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | VVV/USD | 26.999 | 71.433 | 67.583 | +3.12% | +1.03% | 0.87x | 10.0 | 2026-11-27T16:42:00.749471+00:00 | Not calibrated | MODERATE 61/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XDG/USD | 0.057611 | 64.091 | 70.345 | +2.19% | -0.16% | 0.45x | 0.0 | 2026-11-27T16:42:00.749471+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | PAXG/USD | 3614.28 | 63.862 | 54.275 | +1.62% | +0.12% | 1.90x | 1.9 | 2026-11-27T16:42:00.749471+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 10 | XAUT/USD | 3617.1 | 63.511 | 48.220 | +1.61% | +0.06% | 2.70x | 0.3 | 2026-11-27T16:42:00.749471+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 11 | SOL/USD | 72.14 | 62.763 | 66.148 | +1.69% | +0.31% | 0.51x | 1.4 | 2026-11-27T16:42:00.749471+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | SUI/USD | 0.6719 | 54.025 | 58.660 | +0.63% | +0.13% | 0.47x | 1.5 | 2026-11-27T16:42:00.749471+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 96.684 | 754.07 | +2.08% | 2.95x |
| 2 | HYPE/USD | 80.455 | 64.62 | +0.37% | 1.75x |
| 3 | UNI/USD | 71.011 | 4.7741 | +0.12% | 3.29x |
| 4 | SPACE/USD | 70.905 | 0.004161 | +0.53% | 0.84x |
| 5 | XDG/USD | 70.345 | 0.057611 | -0.16% | 0.45x |
| 6 | VVV/USD | 67.583 | 26.999 | +1.03% | 0.87x |
| 7 | NIGHT/USD | 67.031 | 0.04956 | +1.48% | 0.72x |
| 8 | SOL/USD | 66.148 | 72.14 | +0.31% | 0.51x |
| 9 | SENT/USD | 60.207 | 0.022559 | +0.27% | 11.63x |
| 10 | SUI/USD | 58.660 | 0.6719 | +0.13% | 0.47x |
| 11 | PAXG/USD | 54.275 | 3614.28 | +0.12% | 1.90x |
| 12 | XAUT/USD | 48.220 | 3617.1 | +0.06% | 2.70x |

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

- Persisted scans: 2033; predictions: 18098; observations: 1231074.
- Matured sampled outcomes across 1/6/24/48h: 40517; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 151 (sampled only; not a success-rate estimate).
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

**Writer:** 46035462716 · **Generation:** 2033 · **Legacy run:** 46035462716
**Main quote time:** 2026-11-27T16:42:07.608054+00:00 · **Legacy report time:** 2026-11-27T16:42:51.247183+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 754.07 | 122.08 | +2.08% | 2.95x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HYPE/USD ⭐ | 64.62 | 89.83 | +0.37% | 1.75x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | UNI/USD ⭐ | 4.7741 | 86.61 | +0.12% | 3.29x | STRONG 98/100 | HIGH 55/100 | Watch |
| 4 | SENT/USD ⭐ | 0.022559 | 76.56 | +0.27% | 11.63x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 5 | SPACE/USD | 0.004161 | 71.94 | +0.53% | 0.84x | MODERATE 66/100 | VERY_HIGH 74/100 | Watch |
| 6 | NIGHT/USD | 0.04956 | 71.64 | +1.48% | 0.72x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 7 | VVV/USD | 26.999 | 71.43 | +1.03% | 0.87x | MODERATE 61/100 | HIGH 68/100 | Watch |
| 8 | XDG/USD | 0.057611 | 64.09 | -0.16% | 0.45x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 9 | PAXG/USD ⭐ | 3614.28 | 63.86 | +0.12% | 1.90x | STRONG 77/100 | HIGH 55/100 | Watch |
| 10 | XAUT/USD | 3617.1 | 63.51 | +0.06% | 2.70x | STRONG 77/100 | HIGH 55/100 | Watch |
| 11 | SOL/USD | 72.14 | 62.76 | +0.31% | 0.51x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 12 | SUI/USD | 0.6719 | 54.03 | +0.13% | 0.47x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 754.41 | 99.02 | +2.08% | 2.95x | 38587 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HYPE/USD ⭐ | 64.65 | 96.80 | +0.37% | 1.75x | 19848 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | UNI/USD ⭐ | 4.7741 | 83.30 | +0.12% | 3.29x | 10350 | STRONG 97/100 | HIGH 55/100 | Watch |
| 4 | SENT/USD ⭐ | 0.022559 | 82.69 | +0.27% | 11.63x | 3354 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 5 | PAXG/USD ⭐ | 3615.17 | 66.01 | +0.12% | 1.90x | 4388 | STRONG 78/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD, HYPE/USD, UNI/USD, SENT/USD, PAXG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
