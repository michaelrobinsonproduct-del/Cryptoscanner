# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T17:12:08.403851+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46039573961
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 38d6c42adf6857a120727b86dfb31689bd52c6a5 (atomic ledger/results publication)
**Ledger generation:** 2036 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 743.82 | 84.144 | 96.368 | +9.12% | -1.35% | 0.45x | 7.3 | 2026-11-27T17:12:00.689574+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 2 | SPACE/USD | 0.004162 | 72.498 | 69.735 | +7.49% | -0.19% | 1.37x | 12.0 | 2026-11-27T17:12:00.689574+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 3 | HYPE/USD | 64.15 | 70.177 | 74.375 | +3.10% | -0.74% | 0.95x | 4.7 | 2026-11-27T17:12:00.689574+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04977 | 69.794 | 67.314 | +2.68% | +0.16% | 1.17x | 12.1 | 2026-11-27T17:12:00.689574+00:00 | Not calibrated | MODERATE 55/100 | HIGH 68/100 | Watch | WATCH |
| 5 | XDG/USD | 0.0576306 | 62.968 | 70.528 | +2.23% | -0.05% | 0.27x | 0.1 | 2026-11-27T17:12:00.689574+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | SOL/USD | 71.91 | 59.465 | 63.876 | +1.37% | -0.47% | 0.79x | 1.4 | 2026-11-27T17:12:00.689574+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 7 | UNI/USD | 4.7627 | 58.651 | 67.354 | +2.42% | -0.44% | 0.35x | 4.2 | 2026-11-27T17:12:00.689574+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | VVV/USD | 26.757 | 58.452 | 62.101 | +2.19% | -0.20% | 0.74x | 4.9 | 2026-11-27T17:12:00.689574+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | SENT/USD | 0.022652 | 56.939 | 65.229 | +4.97% | +0.17% | 0.08x | 0.4 | 2026-11-27T17:12:00.689574+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 10 | MELANIA/USD | 0.0501 | 56.849 | 65.844 | +7.05% | -0.99% | 0.60x | 20.0 | 2026-11-27T17:12:00.689574+00:00 | Not calibrated | WEAK 28/100 | EXTREME 94/100 | Do nothing | WATCH |
| 11 | XRP/USD | 0.94731 | 55.765 | 58.333 | +0.48% | -0.32% | 0.90x | 0.1 | 2026-11-27T17:12:00.689574+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | SUI/USD | 0.6713 | 55.031 | 58.029 | +0.54% | -0.21% | 0.80x | 1.5 | 2026-11-27T17:12:00.689574+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 96.368 | 743.82 | -1.35% | 0.45x |
| 2 | HYPE/USD | 74.375 | 64.15 | -0.74% | 0.95x |
| 3 | XDG/USD | 70.528 | 0.0576306 | -0.05% | 0.27x |
| 4 | SPACE/USD | 69.735 | 0.004162 | -0.19% | 1.37x |
| 5 | UNI/USD | 67.354 | 4.7627 | -0.44% | 0.35x |
| 6 | NIGHT/USD | 67.314 | 0.04977 | +0.16% | 1.17x |
| 7 | MELANIA/USD | 65.844 | 0.0501 | -0.99% | 0.60x |
| 8 | SENT/USD | 65.229 | 0.022652 | +0.17% | 0.08x |
| 9 | SOL/USD | 63.876 | 71.91 | -0.47% | 0.79x |
| 10 | VVV/USD | 62.101 | 26.757 | -0.20% | 0.74x |
| 11 | XRP/USD | 58.333 | 0.94731 | -0.32% | 0.90x |
| 12 | SUI/USD | 58.029 | 0.6713 | -0.21% | 0.80x |

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

- Persisted scans: 2036; predictions: 18134; observations: 1232889.
- Matured sampled outcomes across 1/6/24/48h: 40625; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46039573961 · **Generation:** 2036 · **Legacy run:** 46039573961
**Main quote time:** 2026-11-27T17:12:08.403851+00:00 · **Legacy report time:** 2026-11-27T17:12:46.922555+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 743.82 | 84.14 | -1.35% | 0.45x | MODERATE 47/100 | VERY_HIGH 80/100 | Do nothing |
| 2 | SPACE/USD | 0.004162 | 72.50 | -0.19% | 1.37x | MODERATE 51/100 | VERY_HIGH 79/100 | Watch |
| 3 | HYPE/USD | 64.15 | 70.18 | -0.74% | 0.95x | WEAK 40/100 | HIGH 68/100 | Watch |
| 4 | NIGHT/USD ⭐ | 0.04977 | 69.79 | +0.16% | 1.17x | MODERATE 65/100 | HIGH 68/100 | Watch |
| 5 | XDG/USD | 0.0576306 | 62.97 | -0.05% | 0.27x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 6 | SOL/USD | 71.91 | 59.47 | -0.47% | 0.79x | WEAK 35/100 | HIGH 68/100 | Watch |
| 7 | UNI/USD | 4.7627 | 58.65 | -0.44% | 0.35x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | VVV/USD | 26.757 | 58.45 | -0.20% | 0.74x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | SENT/USD | 0.022652 | 56.94 | +0.17% | 0.08x | MODERATE 48/100 | VERY_HIGH 82/100 | Watch |
| 10 | MELANIA/USD | 0.0501 | 56.85 | -0.99% | 0.60x | WEAK 28/100 | EXTREME 94/100 | Do nothing |
| 11 | XRP/USD | 0.94731 | 55.77 | -0.32% | 0.90x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 12 | SUI/USD | 0.6713 | 55.03 | -0.21% | 0.80x | WEAK 33/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04972 | 79.81 | +0.16% | 1.17x | 16116 | STRONG 75/100 | HIGH 62/100 | Watch |

**Same-run overlap:** NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
