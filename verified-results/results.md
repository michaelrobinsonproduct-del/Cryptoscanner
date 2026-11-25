# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T13:32:35.111581+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45624125677
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** ca5fd4e7dea8b60dc7873a77fb909d0047064ca0 (atomic ledger/results publication)
**Ledger generation:** 1724 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.282 | 80.787 | 62.543 | +3.03% | +0.65% | 2.58x | 27.4 | 2026-11-25T13:32:30.562609+00:00 | Not calibrated | STRONG 85/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | MON/USD | 0.0099 | 75.358 | 74.911 | +4.54% | +0.71% | 0.69x | 10.1 | 2026-11-25T13:32:30.562609+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | DRV/USD | 0.33077 | 74.963 | 74.109 | +5.25% | -0.32% | 1.25x | 1.2 | 2026-11-25T13:32:30.562609+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 4 | MOODENG/USD | 0.02712 | 69.558 | 59.057 | +11.47% | +2.62% | 0.74x | 37.1 | 2026-11-25T13:32:30.562609+00:00 | Not calibrated | MODERATE 50/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | CAP/USD | 0.092946 | 43.054 | 26.160 | +0.57% | +0.38% | 3.22x | 19.1 | 2026-11-25T13:32:30.562609+00:00 | Not calibrated | STRONG 72/100 | HIGH 66/100 | Watch | WATCH |
| 6 | INX/USD | 0.003975 | 28.652 | 38.216 | +3.76% | -0.27% | 0.18x | 37.6 | 2026-11-25T13:32:30.562609+00:00 | Not calibrated | WEAK 4/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 74.911 | 0.0099 | +0.71% | 0.69x |
| 2 | DRV/USD | 74.109 | 0.33077 | -0.32% | 1.25x |
| 3 | VVV/USD | 62.543 | 25.282 | +0.65% | 2.58x |
| 4 | MOODENG/USD | 59.057 | 0.02712 | +2.62% | 0.74x |
| 5 | INX/USD | 38.216 | 0.003975 | -0.27% | 0.18x |
| 6 | CAP/USD | 26.160 | 0.092946 | +0.38% | 3.22x |

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

- Persisted scans: 1724; predictions: 14544; observations: 1044977.
- Matured sampled outcomes across 1/6/24/48h: 31921; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45624125677 · **Generation:** 1724 · **Legacy run:** 45624125677
**Main quote time:** 2026-11-25T13:32:35.111581+00:00 · **Legacy report time:** 2026-11-25T13:33:39.854882+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.282 | 80.79 | +0.65% | 2.58x | STRONG 95/100 | HIGH 67/100 | Consider small entry |
| 2 | MON/USD | 0.0099 | 75.36 | +0.71% | 0.69x | MODERATE 63/100 | VERY_HIGH 76/100 | Watch |
| 3 | DRV/USD | 0.33077 | 74.96 | -0.32% | 1.25x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 4 | MOODENG/USD | 0.02712 | 69.56 | +2.62% | 0.74x | MODERATE 50/100 | EXTREME 87/100 | Do nothing |
| 5 | CAP/USD ⭐ | 0.092946 | 43.05 | +0.38% | 3.22x | STRONG 82/100 | HIGH 66/100 | Consider small entry |
| 6 | INX/USD | 0.003975 | 28.65 | -0.27% | 0.18x | WEAK 4/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.012 | 71.44 | +0.65% | 2.58x | 12245 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | CAP/USD ⭐ | 0.092815 | 40.23 | +0.38% | 3.22x | 3597 | STRONG 85/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** VVV/USD, CAP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
