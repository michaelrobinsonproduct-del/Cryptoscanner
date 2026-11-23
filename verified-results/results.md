# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T06:11:31.177705+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45122251259
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** bc2510cee02f96ade5ee7a5933170ddf0fb1330c (atomic ledger/results publication)
**Ledger generation:** 1391 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SOL/USD | 71.83 | 78.918 | 66.197 | +1.70% | +0.31% | 2.12x | 1.4 | 2026-11-23T06:11:25.333812+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XMR/USD | 500.54 | 75.770 | 61.786 | +1.38% | -0.20% | 4.05x | 5.8 | 2026-11-23T06:11:25.333812+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XBT/USD | 61619.9 | 75.250 | 60.139 | +0.74% | +0.19% | 2.42x | 0.0 | 2026-11-23T06:11:25.333812+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 4 | XLM/USD | 0.12806 | 71.651 | 56.613 | +0.42% | +0.24% | 2.38x | 0.9 | 2026-11-23T06:11:25.333812+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | JUP/USD | 0.24079 | 69.740 | 73.439 | +7.22% | +0.29% | 0.49x | 11.6 | 2026-11-23T06:11:25.333812+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 6 | PAXG/USD | 3610.93 | 67.025 | 51.637 | +1.08% | +0.08% | 3.83x | 1.2 | 2026-11-23T06:11:25.333812+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6661 | 65.168 | 65.350 | +1.59% | +0.36% | 0.80x | 1.5 | 2026-11-23T06:11:25.333812+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 8 | ALGO/USD | 0.07874 | 65.167 | 59.886 | +4.39% | +1.29% | 0.89x | 7.6 | 2026-11-23T06:11:25.333812+00:00 | Not calibrated | MODERATE 63/100 | HIGH 67/100 | Watch | WATCH |
| 9 | LTC/USD | 40.77 | 63.955 | 52.495 | +1.52% | +0.37% | 1.96x | 2.5 | 2026-11-23T06:11:25.333812+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 10 | XRP/USD | 0.94137 | 62.928 | 65.331 | +1.49% | +0.54% | 0.49x | 0.2 | 2026-11-23T06:11:25.333812+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | NEAR/USD | 3.007 | 59.005 | 59.941 | +0.85% | -0.48% | 1.15x | 2.0 | 2026-11-23T06:11:25.333812+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 12 | NIGHT/USD | 0.05015 | 58.443 | 59.836 | +1.99% | +0.04% | 0.84x | 10.0 | 2026-11-23T06:11:25.333812+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | JUP/USD | 73.439 | 0.24079 | +0.29% | 0.49x |
| 2 | SOL/USD | 66.197 | 71.83 | +0.31% | 2.12x |
| 3 | SUI/USD | 65.350 | 0.6661 | +0.36% | 0.80x |
| 4 | XRP/USD | 65.331 | 0.94137 | +0.54% | 0.49x |
| 5 | XMR/USD | 61.786 | 500.54 | -0.20% | 4.05x |
| 6 | XBT/USD | 60.139 | 61619.9 | +0.19% | 2.42x |
| 7 | NEAR/USD | 59.941 | 3.007 | -0.48% | 1.15x |
| 8 | ALGO/USD | 59.886 | 0.07874 | +1.29% | 0.89x |
| 9 | NIGHT/USD | 59.836 | 0.05015 | +0.04% | 0.84x |
| 10 | XLM/USD | 56.613 | 0.12806 | +0.24% | 2.38x |
| 11 | LTC/USD | 52.495 | 40.77 | +0.37% | 1.96x |
| 12 | PAXG/USD | 51.637 | 3610.93 | +0.08% | 3.83x |

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

- Persisted scans: 1391; predictions: 11459; observations: 842223.
- Matured sampled outcomes across 1/6/24/48h: 18604; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 120 (sampled only; not a success-rate estimate).
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

**Writer:** 45122251259 · **Generation:** 1391 · **Legacy run:** 45122251259
**Main quote time:** 2026-11-23T06:11:31.177705+00:00 · **Legacy report time:** 2026-11-23T06:12:18.479308+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD ⭐ | 71.83 | 78.92 | +0.31% | 2.12x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD | 500.54 | 75.77 | -0.20% | 4.05x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 3 | XBT/USD ⭐ | 61619.9 | 75.25 | +0.19% | 2.42x | STRONG 93/100 | HIGH 55/100 | Watch |
| 4 | XLM/USD | 0.12806 | 71.65 | +0.24% | 2.38x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 5 | JUP/USD | 0.24079 | 69.74 | +0.29% | 0.49x | MODERATE 60/100 | VERY_HIGH 81/100 | Watch |
| 6 | PAXG/USD | 3610.93 | 67.03 | +0.08% | 3.83x | STRONG 79/100 | HIGH 55/100 | Watch |
| 7 | SUI/USD | 0.6661 | 65.17 | +0.36% | 0.80x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 8 | ALGO/USD | 0.07874 | 65.17 | +1.29% | 0.89x | MODERATE 63/100 | HIGH 67/100 | Watch |
| 9 | LTC/USD ⭐ | 40.77 | 63.96 | +0.37% | 1.96x | STRONG 87/100 | HIGH 55/100 | Consider small entry |
| 10 | XRP/USD | 0.94137 | 62.93 | +0.54% | 0.49x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 11 | NEAR/USD | 3.007 | 59.01 | -0.48% | 1.15x | WEAK 40/100 | HIGH 68/100 | Watch |
| 12 | NIGHT/USD | 0.05015 | 58.44 | +0.04% | 0.84x | MODERATE 49/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD ⭐ | 71.86 | 75.51 | +0.31% | 2.12x | 29988 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | CC/USD | 0.07596 | 74.48 | +0.22% | 1.04x | 4154 | STRONG 72/100 | HIGH 67/100 | Watch |
| 3 | XBT/USD ⭐ | 61641.6 | 67.45 | +0.19% | 2.42x | 134775 | STRONG 89/100 | HIGH 55/100 | Watch |
| 4 | LTC/USD ⭐ | 40.77 | 63.13 | +0.37% | 1.96x | 9195 | STRONG 87/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** SOL/USD, XBT/USD, LTC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
