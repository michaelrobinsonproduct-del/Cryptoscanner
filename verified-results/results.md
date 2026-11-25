# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T12:22:22.016977+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45612666226
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 16b1a2386205844a5e4c32ccec8797613e8e3ad3 (atomic ledger/results publication)
**Ledger generation:** 1717 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TREAD/USD | 1.058 | 84.393 | 59.434 | +5.85% | +2.22% | 2.38x | 25.6 | 2026-11-25T12:22:17.479536+00:00 | Not calibrated | STRONG 87/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | MON/USD | 0.00985 | 80.131 | 66.145 | +4.01% | -0.20% | 3.86x | 20.3 | 2026-11-25T12:22:17.479536+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | CT/USD | 0.1307 | 69.233 | 47.694 | +3.48% | +1.31% | 4.86x | 15.3 | 2026-11-25T12:22:17.479536+00:00 | Not calibrated | STRONG 85/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | VVV/USD | 25.16 | 67.492 | 65.188 | +2.53% | +1.28% | 0.59x | 15.1 | 2026-11-25T12:22:17.479536+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | CAP/USD | 0.092779 | 26.841 | 32.458 | +0.39% | +0.43% | 0.23x | 4.1 | 2026-11-25T12:22:17.479536+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 66.145 | 0.00985 | -0.20% | 3.86x |
| 2 | VVV/USD | 65.188 | 25.16 | +1.28% | 0.59x |
| 3 | TREAD/USD | 59.434 | 1.058 | +2.22% | 2.38x |
| 4 | CT/USD | 47.694 | 0.1307 | +1.31% | 4.86x |
| 5 | CAP/USD | 32.458 | 0.092779 | +0.43% | 0.23x |

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

- Persisted scans: 1717; predictions: 14503; observations: 1040721.
- Matured sampled outcomes across 1/6/24/48h: 31685; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45612666226 · **Generation:** 1717 · **Legacy run:** 45612666226
**Main quote time:** 2026-11-25T12:22:22.016977+00:00 · **Legacy report time:** 2026-11-25T12:23:24.458604+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TREAD/USD ⭐ | 1.058 | 84.39 | +2.22% | 2.38x | STRONG 97/100 | VERY_HIGH 79/100 | Watch |
| 2 | MON/USD | 0.00985 | 80.13 | -0.20% | 3.86x | MODERATE 60/100 | VERY_HIGH 73/100 | Watch |
| 3 | CT/USD ⭐ | 0.1307 | 69.23 | +1.31% | 4.86x | STRONG 95/100 | VERY_HIGH 73/100 | Watch |
| 4 | VVV/USD | 25.16 | 67.49 | +1.28% | 0.59x | MODERATE 59/100 | VERY_HIGH 76/100 | Watch |
| 5 | CAP/USD | 0.092779 | 26.84 | +0.43% | 0.23x | WEAK 43/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TREAD/USD ⭐ | 1.0434 | 82.95 | +2.22% | 2.38x | 2768 | STRONG 91/100 | VERY_HIGH 79/100 | Watch |
| 2 | BABY/USD | 0.00892 | 72.72 | +0.57% | 1.02x | 3018 | MODERATE 61/100 | EXTREME 86/100 | Do nothing |
| 3 | CT/USD ⭐ | 0.131 | 69.02 | +1.31% | 4.86x | 1424 | STRONG 95/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** TREAD/USD, CT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
