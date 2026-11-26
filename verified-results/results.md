# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T07:26:03.109115+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45775088029
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 3350ab02126c2007460ad6405109d192c3a4d188 (atomic ledger/results publication)
**Ledger generation:** 1830 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 147.81 | 75.037 | 61.588 | +2.08% | -0.31% | 16.33x | 6.1 | 2026-11-26T07:25:56.794824+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SUI/USD | 0.6691 | 74.069 | 57.194 | +0.42% | +0.38% | 4.65x | 1.5 | 2026-11-26T07:25:56.794824+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | XRP/USD | 0.95192 | 69.875 | 66.428 | +1.64% | +0.31% | 1.19x | 0.1 | 2026-11-26T07:25:56.794824+00:00 | Not calibrated | STRONG 70/100 | HIGH 62/100 | Watch | WATCH |
| 4 | LTC/USD | 43.41 | 65.238 | 65.321 | +1.64% | +0.32% | 0.83x | 2.3 | 2026-11-26T07:25:56.794824+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 5 | SYRUP/USD | 0.07077 | 65.100 | 70.038 | +6.79% | -0.03% | 0.52x | 14.2 | 2026-11-26T07:25:56.794824+00:00 | Not calibrated | WEAK 33/100 | EXTREME 87/100 | Do nothing | WATCH |
| 6 | ADA/USD | 0.147744 | 64.642 | 63.058 | +1.35% | +0.01% | 1.15x | 2.8 | 2026-11-26T07:25:56.794824+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 7 | XLM/USD | 0.128435 | 62.660 | 46.106 | +0.48% | +0.31% | 2.77x | 3.5 | 2026-11-26T07:25:56.794824+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 8 | INJ/USD | 6.101 | 62.242 | 57.974 | +2.47% | -0.10% | 1.48x | 3.3 | 2026-11-26T07:25:56.794824+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 9 | ZRO/USD | 1.07 | 61.214 | 67.036 | +4.49% | +0.56% | 0.14x | 9.4 | 2026-11-26T07:25:56.794824+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SKY/USD | 0.04382 | 57.042 | 62.617 | +4.63% | +0.34% | 0.27x | 6.8 | 2026-11-26T07:25:56.794824+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 11 | SOL/USD | 70.99 | 55.724 | 60.262 | +0.85% | +0.37% | 0.36x | 1.4 | 2026-11-26T07:25:56.794824+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | HBAR/USD | 0.05331 | 54.784 | 51.469 | +2.32% | +0.47% | 1.10x | 3.8 | 2026-11-26T07:25:56.794824+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SYRUP/USD | 70.038 | 0.07077 | -0.03% | 0.52x |
| 2 | ZRO/USD | 67.036 | 1.07 | +0.56% | 0.14x |
| 3 | XRP/USD | 66.428 | 0.95192 | +0.31% | 1.19x |
| 4 | LTC/USD | 65.321 | 43.41 | +0.32% | 0.83x |
| 5 | ADA/USD | 63.058 | 0.147744 | +0.01% | 1.15x |
| 6 | SKY/USD | 62.617 | 0.04382 | +0.34% | 0.27x |
| 7 | QNT/USD | 61.588 | 147.81 | -0.31% | 16.33x |
| 8 | SOL/USD | 60.262 | 70.99 | +0.37% | 0.36x |
| 9 | INJ/USD | 57.974 | 6.101 | -0.10% | 1.48x |
| 10 | SUI/USD | 57.194 | 0.6691 | +0.38% | 4.65x |
| 11 | HBAR/USD | 51.469 | 0.05331 | +0.47% | 1.10x |
| 12 | XLM/USD | 46.106 | 0.128435 | +0.31% | 2.77x |

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

- Persisted scans: 1830; predictions: 15695; observations: 1109514.
- Matured sampled outcomes across 1/6/24/48h: 34022; gap abstentions: 24203. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45775088029 · **Generation:** 1830 · **Legacy run:** 45775088029
**Main quote time:** 2026-11-26T07:26:03.109115+00:00 · **Legacy report time:** 2026-11-26T07:27:08.910359+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 147.81 | 75.04 | -0.31% | 16.33x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 2 | SUI/USD | 0.6691 | 74.07 | +0.38% | 4.65x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 3 | XRP/USD ⭐ | 0.95192 | 69.88 | +0.31% | 1.19x | STRONG 80/100 | HIGH 62/100 | Watch |
| 4 | LTC/USD | 43.41 | 65.24 | +0.32% | 0.83x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 5 | SYRUP/USD | 0.07077 | 65.10 | -0.03% | 0.52x | WEAK 33/100 | EXTREME 87/100 | Do nothing |
| 6 | ADA/USD | 0.147744 | 64.64 | +0.01% | 1.15x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 7 | XLM/USD | 0.128435 | 62.66 | +0.31% | 2.77x | STRONG 86/100 | HIGH 55/100 | Watch |
| 8 | INJ/USD | 6.101 | 62.24 | -0.10% | 1.48x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 9 | ZRO/USD | 1.07 | 61.21 | +0.56% | 0.14x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 10 | SKY/USD | 0.04382 | 57.04 | +0.34% | 0.27x | MODERATE 59/100 | VERY_HIGH 75/100 | Watch |
| 11 | SOL/USD | 70.99 | 55.72 | +0.37% | 0.36x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 12 | HBAR/USD ⭐ | 0.05331 | 54.78 | +0.47% | 1.10x | STRONG 72/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.95053 | 71.38 | +0.31% | 1.19x | 42566 | STRONG 81/100 | HIGH 62/100 | Watch |
| 2 | W/USD | 0.00862 | 63.00 | +0.35% | 1.78x | 1368 | STRONG 71/100 | HIGH 66/100 | Watch |
| 3 | HBAR/USD ⭐ | 0.05321 | 61.10 | +0.47% | 1.10x | 6326 | STRONG 76/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XRP/USD, HBAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
