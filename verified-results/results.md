# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T19:25:53.167369+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45684901132
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 837359abd88f11f7acf0ceb7531546e19c85d652 (atomic ledger/results publication)
**Ledger generation:** 1756 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LTC/USD | 42.53 | 101.278 | 82.613 | +4.11% | +0.73% | 8.87x | 2.4 | 2026-11-25T19:25:44.735596+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XPL/USD | 0.0484 | 89.977 | 71.859 | +10.00% | +0.62% | 2.62x | 20.7 | 2026-11-25T19:25:44.735596+00:00 | Not calibrated | STRONG 90/100 | HIGH 67/100 | Consider small entry | WATCH |
| 3 | XLM/USD | 0.128072 | 84.610 | 65.136 | +3.24% | +0.89% | 3.17x | 3.9 | 2026-11-25T19:25:44.735596+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | XMR/USD | 520.68 | 84.420 | 65.324 | +2.17% | +1.10% | 2.36x | 9.8 | 2026-11-25T19:25:44.735596+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | CC/USD | 0.07804 | 84.181 | 62.480 | +3.98% | +1.68% | 2.33x | 1.3 | 2026-11-25T19:25:44.735596+00:00 | Not calibrated | STRONG 97/100 | HIGH 60/100 | Consider small entry | WATCH |
| 6 | XRP/USD | 0.94093 | 83.421 | 67.702 | +1.88% | +0.78% | 2.18x | 0.9 | 2026-11-25T19:25:44.735596+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | ZEC/USD | 762.93 | 81.349 | 74.828 | +3.25% | +1.51% | 0.90x | 5.9 | 2026-11-25T19:25:44.735596+00:00 | Not calibrated | STRONG 71/100 | HIGH 62/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6648 | 79.284 | 71.448 | +2.67% | +1.14% | 1.21x | 4.5 | 2026-11-25T19:25:44.735596+00:00 | Not calibrated | STRONG 75/100 | HIGH 62/100 | Watch | WATCH |
| 9 | HYPE/USD | 61.83 | 76.661 | 76.298 | +3.27% | +1.61% | 0.23x | 3.2 | 2026-11-25T19:25:44.735596+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XBT/USD | 60098.2 | 74.951 | 59.173 | +0.60% | +0.44% | 2.36x | 0.0 | 2026-11-25T19:25:44.735596+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 11 | SOL/USD | 70.71 | 73.498 | 65.457 | +1.59% | +1.06% | 1.28x | 1.4 | 2026-11-25T19:25:44.735596+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 12 | LINK/USD | 9.09549 | 70.678 | 65.117 | +2.88% | +1.15% | 0.98x | 5.2 | 2026-11-25T19:25:44.735596+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 82.613 | 42.53 | +0.73% | 8.87x |
| 2 | HYPE/USD | 76.298 | 61.83 | +1.61% | 0.23x |
| 3 | ZEC/USD | 74.828 | 762.93 | +1.51% | 0.90x |
| 4 | XPL/USD | 71.859 | 0.0484 | +0.62% | 2.62x |
| 5 | SUI/USD | 71.448 | 0.6648 | +1.14% | 1.21x |
| 6 | XRP/USD | 67.702 | 0.94093 | +0.78% | 2.18x |
| 7 | SOL/USD | 65.457 | 70.71 | +1.06% | 1.28x |
| 8 | XMR/USD | 65.324 | 520.68 | +1.10% | 2.36x |
| 9 | XLM/USD | 65.136 | 0.128072 | +0.89% | 3.17x |
| 10 | LINK/USD | 65.117 | 9.09549 | +1.15% | 0.98x |
| 11 | CC/USD | 62.480 | 0.07804 | +1.68% | 2.33x |
| 12 | XBT/USD | 59.173 | 60098.2 | +0.44% | 2.36x |

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

- Persisted scans: 1756; predictions: 14816; observations: 1064448.
- Matured sampled outcomes across 1/6/24/48h: 32570; gap abstentions: 22820. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45684901132 · **Generation:** 1756 · **Legacy run:** 45684901132
**Main quote time:** 2026-11-25T19:25:53.167369+00:00 · **Legacy report time:** 2026-11-25T19:26:48.763843+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD ⭐ | 42.53 | 101.28 | +0.73% | 8.87x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XPL/USD ⭐ | 0.0484 | 89.98 | +0.62% | 2.62x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 3 | XLM/USD ⭐ | 0.128072 | 84.61 | +0.89% | 3.17x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | XMR/USD | 520.68 | 84.42 | +1.10% | 2.36x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 5 | CC/USD ⭐ | 0.07804 | 84.18 | +1.68% | 2.33x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 6 | XRP/USD ⭐ | 0.94093 | 83.42 | +0.78% | 2.18x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | ZEC/USD | 762.93 | 81.35 | +1.51% | 0.90x | STRONG 71/100 | HIGH 62/100 | Watch |
| 8 | SUI/USD ⭐ | 0.6648 | 79.28 | +1.14% | 1.21x | STRONG 85/100 | HIGH 62/100 | Watch |
| 9 | HYPE/USD | 61.83 | 76.66 | +1.61% | 0.23x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 10 | XBT/USD | 60098.2 | 74.95 | +0.44% | 2.36x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 11 | SOL/USD ⭐ | 70.71 | 73.50 | +1.06% | 1.28x | STRONG 82/100 | HIGH 55/100 | Watch |
| 12 | LINK/USD | 9.09549 | 70.68 | +1.15% | 0.98x | MODERATE 65/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD ⭐ | 42.52 | 100.00 | +0.73% | 8.87x | 13305 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XLM/USD ⭐ | 0.12802 | 88.44 | +0.89% | 3.17x | 8155 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | CC/USD ⭐ | 0.07784 | 87.41 | +1.68% | 2.33x | 5250 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 4 | SUI/USD ⭐ | 0.6644 | 81.57 | +1.14% | 1.21x | 7433 | STRONG 86/100 | HIGH 62/100 | Watch |
| 5 | XRP/USD ⭐ | 0.941 | 80.17 | +0.78% | 2.18x | 38003 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | XPL/USD ⭐ | 0.0486 | 80.03 | +0.62% | 2.62x | 2320 | STRONG 95/100 | HIGH 67/100 | Consider small entry |
| 7 | DRV/USD | 0.35649 | 79.62 | +1.20% | 1.10x | 11505 | STRONG 75/100 | HIGH 62/100 | Watch |
| 8 | SOL/USD ⭐ | 70.64 | 71.37 | +1.06% | 1.28x | 45348 | STRONG 81/100 | HIGH 55/100 | Watch |
| 9 | ASTER/USD | 0.49658 | 71.27 | +0.52% | 1.55x | 3069 | STRONG 81/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** LTC/USD, XPL/USD, XLM/USD, CC/USD, XRP/USD, SUI/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
