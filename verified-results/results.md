# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T23:01:52.076499+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45505982451
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 6d6e31940ef535f4b149b9e781123178cf029a21 (atomic ledger/results publication)
**Ledger generation:** 1637 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 508.73 | 82.804 | 84.168 | +4.67% | -0.71% | 1.22x | 7.1 | 2026-11-24T23:01:46.709634+00:00 | Not calibrated | MODERATE 51/100 | HIGH 68/100 | Watch | WATCH |
| 2 | VVV/USD | 24.823 | 68.813 | 63.923 | +1.53% | +0.06% | 1.46x | 3.6 | 2026-11-24T23:01:46.709634+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 3 | GBP/USD | 1.31063 | 68.460 | 58.888 | +0.57% | -0.04% | 1.98x | 0.2 | 2026-11-24T23:01:46.709634+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 4 | LUNA/USD | 4.545e-05 | 58.486 | 52.536 | +4.55% | +0.49% | 1.35x | 22.1 | 2026-11-24T23:01:46.709634+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04872 | 57.369 | 46.442 | +1.18% | -0.10% | 2.14x | 2.1 | 2026-11-24T23:01:46.709634+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 6 | PEPE/USD | 3.48e-06 | 57.151 | 55.728 | +1.69% | -0.63% | 1.46x | 2.9 | 2026-11-24T23:01:46.709634+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |
| 7 | WINGS/USD | 0.002162 | 51.375 | 41.071 | +4.34% | +1.45% | 1.30x | 41.6 | 2026-11-24T23:01:46.709634+00:00 | Not calibrated | MODERATE 56/100 | EXTREME 89/100 | Do nothing | WATCH |
| 8 | ZEUS/USD | 0.00453 | 38.720 | 44.540 | +3.42% | +0.44% | 0.20x | 22.1 | 2026-11-24T23:01:46.709634+00:00 | Not calibrated | WEAK 39/100 | EXTREME 94/100 | Do nothing | WATCH |
| 9 | SKY/USD | 0.04111 | 38.622 | 41.453 | +1.78% | +0.61% | 0.41x | 9.7 | 2026-11-24T23:01:46.709634+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 84.168 | 508.73 | -0.71% | 1.22x |
| 2 | VVV/USD | 63.923 | 24.823 | +0.06% | 1.46x |
| 3 | GBP/USD | 58.888 | 1.31063 | -0.04% | 1.98x |
| 4 | PEPE/USD | 55.728 | 3.48e-06 | -0.63% | 1.46x |
| 5 | LUNA/USD | 52.536 | 4.545e-05 | +0.49% | 1.35x |
| 6 | NIGHT/USD | 46.442 | 0.04872 | -0.10% | 2.14x |
| 7 | ZEUS/USD | 44.540 | 0.00453 | +0.44% | 0.20x |
| 8 | SKY/USD | 41.453 | 0.04111 | +0.61% | 0.41x |
| 9 | WINGS/USD | 41.071 | 0.002162 | +1.45% | 1.30x |

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

- Persisted scans: 1637; predictions: 14020; observations: 992024.
- Matured sampled outcomes across 1/6/24/48h: 28951; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45505982451 · **Generation:** 1637 · **Legacy run:** 45505982451
**Main quote time:** 2026-11-24T23:01:52.076499+00:00 · **Legacy report time:** 2026-11-24T23:02:39.475176+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 508.73 | 82.80 | -0.71% | 1.22x | MODERATE 51/100 | HIGH 68/100 | Watch |
| 2 | VVV/USD ⭐ | 24.823 | 68.81 | +0.06% | 1.46x | STRONG 79/100 | HIGH 55/100 | Watch |
| 3 | GBP/USD | 1.31063 | 68.46 | -0.04% | 1.98x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 4 | LUNA/USD ⭐ | 4.545e-05 | 58.49 | +0.49% | 1.35x | STRONG 74/100 | VERY_HIGH 72/100 | Watch |
| 5 | NIGHT/USD | 0.04872 | 57.37 | -0.10% | 2.14x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 6 | PEPE/USD | 3.48e-06 | 57.15 | -0.63% | 1.46x | MODERATE 49/100 | HIGH 61/100 | Watch |
| 7 | WINGS/USD ⭐ | 0.002162 | 51.37 | +1.45% | 1.30x | MODERATE 66/100 | EXTREME 89/100 | Do nothing |
| 8 | ZEUS/USD | 0.00453 | 38.72 | +0.44% | 0.20x | WEAK 39/100 | EXTREME 94/100 | Do nothing |
| 9 | SKY/USD | 0.04111 | 38.62 | +0.61% | 0.41x | MODERATE 49/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | WINGS/USD ⭐ | 0.002162 | 76.46 | +1.45% | 1.30x | 3825 | STRONG 78/100 | EXTREME 89/100 | Do nothing |
| 2 | LUNA/USD ⭐ | 4.529e-05 | 67.75 | +0.49% | 1.35x | 1905 | STRONG 74/100 | VERY_HIGH 72/100 | Watch |
| 3 | VVV/USD ⭐ | 24.816 | 57.08 | +0.06% | 1.46x | 16987 | STRONG 74/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD, LUNA/USD, WINGS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
