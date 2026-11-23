# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T05:21:37.981121+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45117058069
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 722f4f372241c3a18fbf778c11c7c69eae2e6ff8 (atomic ledger/results publication)
**Ledger generation:** 1386 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | JUP/USD | 0.235 | 84.807 | 64.481 | +4.64% | +1.07% | 3.20x | 3.8 | 2026-11-23T05:21:31.205120+00:00 | Not calibrated | STRONG 97/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | BLESS/USD | 0.017858 | 70.377 | 64.535 | +10.97% | +0.08% | 1.54x | 38.6 | 2026-11-23T05:21:31.205120+00:00 | Not calibrated | MODERATE 55/100 | HIGH 67/100 | Watch | WATCH |
| 3 | AI/USD | 0.01604 | 65.017 | 66.711 | +9.71% | +0.95% | 0.36x | 18.7 | 2026-11-23T05:21:31.205120+00:00 | Not calibrated | MODERATE 58/100 | EXTREME 88/100 | Do nothing | WATCH |
| 4 | SOL/USD | 71.47 | 61.428 | 62.626 | +1.19% | +0.18% | 0.79x | 1.4 | 2026-11-23T05:21:31.205120+00:00 | Not calibrated | MODERATE 51/100 | HIGH 62/100 | Watch | WATCH |
| 5 | SUI/USD | 0.66 | 61.326 | 58.834 | +0.66% | +0.15% | 1.17x | 1.5 | 2026-11-23T05:21:31.205120+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0554598 | 60.502 | 48.279 | +0.32% | +0.08% | 2.18x | 1.2 | 2026-11-23T05:21:31.205120+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 7 | XMR/USD | 501.29 | 59.522 | 63.754 | +1.54% | +0.15% | 0.50x | 4.0 | 2026-11-23T05:21:31.205120+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | CC/USD | 0.07555 | 59.229 | 55.579 | +3.11% | +0.07% | 1.33x | 2.6 | 2026-11-23T05:21:31.205120+00:00 | Not calibrated | MODERATE 65/100 | HIGH 60/100 | Watch | WATCH |
| 9 | NEAR/USD | 3.0122 | 56.973 | 59.509 | +1.02% | +0.54% | 0.48x | 5.3 | 2026-11-23T05:21:31.205120+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XRP/USD | 0.93389 | 56.363 | 59.310 | +0.68% | +0.17% | 0.62x | 1.0 | 2026-11-23T05:21:31.205120+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ETH/USD | 1728.37 | 54.617 | 57.720 | +0.39% | +0.08% | 0.65x | 0.1 | 2026-11-23T05:21:31.205120+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | PAXG/USD | 3600.32 | 51.499 | 49.584 | +0.79% | +0.13% | 1.12x | 0.6 | 2026-11-23T05:21:31.205120+00:00 | Not calibrated | MODERATE 51/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | AI/USD | 66.711 | 0.01604 | +0.95% | 0.36x |
| 2 | BLESS/USD | 64.535 | 0.017858 | +0.08% | 1.54x |
| 3 | JUP/USD | 64.481 | 0.235 | +1.07% | 3.20x |
| 4 | XMR/USD | 63.754 | 501.29 | +0.15% | 0.50x |
| 5 | SOL/USD | 62.626 | 71.47 | +0.18% | 0.79x |
| 6 | NEAR/USD | 59.509 | 3.0122 | +0.54% | 0.48x |
| 7 | XRP/USD | 59.310 | 0.93389 | +0.17% | 0.62x |
| 8 | SUI/USD | 58.834 | 0.66 | +0.15% | 1.17x |
| 9 | ETH/USD | 57.720 | 1728.37 | +0.08% | 0.65x |
| 10 | CC/USD | 55.579 | 0.07555 | +0.07% | 1.33x |
| 11 | PAXG/USD | 49.584 | 3600.32 | +0.13% | 1.12x |
| 12 | XDG/USD | 48.279 | 0.0554598 | +0.08% | 2.18x |

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

- Persisted scans: 1386; predictions: 11399; observations: 839178.
- Matured sampled outcomes across 1/6/24/48h: 18453; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 107 (sampled only; not a success-rate estimate).
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

**Writer:** 45117058069 · **Generation:** 1386 · **Legacy run:** 45117058069
**Main quote time:** 2026-11-23T05:21:37.981121+00:00 · **Legacy report time:** 2026-11-23T05:22:38.247744+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | JUP/USD ⭐ | 0.235 | 84.81 | +1.07% | 3.20x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | BLESS/USD ⭐ | 0.017858 | 70.38 | +0.08% | 1.54x | MODERATE 65/100 | HIGH 67/100 | Watch |
| 3 | AI/USD | 0.01604 | 65.02 | +0.95% | 0.36x | MODERATE 58/100 | EXTREME 88/100 | Do nothing |
| 4 | SOL/USD | 71.47 | 61.43 | +0.18% | 0.79x | MODERATE 51/100 | HIGH 62/100 | Watch |
| 5 | SUI/USD ⭐ | 0.66 | 61.33 | +0.15% | 1.17x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 6 | XDG/USD | 0.0554598 | 60.50 | +0.08% | 2.18x | STRONG 75/100 | HIGH 55/100 | Watch |
| 7 | XMR/USD | 501.29 | 59.52 | +0.15% | 0.50x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 8 | CC/USD ⭐ | 0.07555 | 59.23 | +0.07% | 1.33x | STRONG 75/100 | HIGH 60/100 | Watch |
| 9 | NEAR/USD | 3.0122 | 56.97 | +0.54% | 0.48x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 10 | XRP/USD | 0.93389 | 56.36 | +0.17% | 0.62x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 11 | ETH/USD | 1728.37 | 54.62 | +0.08% | 0.65x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 12 | PAXG/USD | 3600.32 | 51.50 | +0.13% | 1.12x | MODERATE 51/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | JUP/USD ⭐ | 0.23588 | 83.55 | +1.07% | 3.20x | 2920 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | BLESS/USD ⭐ | 0.017858 | 77.73 | +0.08% | 1.54x | 5729 | STRONG 74/100 | HIGH 67/100 | Watch |
| 3 | CC/USD ⭐ | 0.07555 | 71.00 | +0.07% | 1.33x | 4102 | STRONG 80/100 | HIGH 60/100 | Watch |
| 4 | SUI/USD ⭐ | 0.6619 | 58.45 | +0.15% | 1.17x | 6274 | MODERATE 64/100 | HIGH 62/100 | Watch |

**Same-run overlap:** JUP/USD, BLESS/USD, SUI/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
