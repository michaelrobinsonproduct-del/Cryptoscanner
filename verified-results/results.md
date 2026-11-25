# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T12:32:33.384625+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45614257220
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 51f240fec2547bc47c2cb368e79448fc61849815 (atomic ledger/results publication)
**Ledger generation:** 1718 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.00991 | 75.440 | 70.744 | +4.65% | +1.12% | 0.91x | 20.2 | 2026-11-25T12:32:28.591944+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | CT/USD | 0.1308 | 68.285 | 48.312 | +3.56% | +0.99% | 6.37x | 15.3 | 2026-11-25T12:32:28.591944+00:00 | Not calibrated | STRONG 84/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | VVV/USD | 25.061 | 68.222 | 69.720 | +2.13% | +0.48% | 0.61x | 0.4 | 2026-11-25T12:32:28.591944+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | INX/USD | 0.003947 | 28.273 | 37.889 | +3.03% | -1.99% | 1.03x | 28.0 | 2026-11-25T12:32:28.591944+00:00 | Not calibrated | WEAK 14/100 | EXTREME 96/100 | Do nothing | WATCH |
| 5 | CAP/USD | 0.092739 | 27.488 | 31.165 | +0.35% | +0.40% | 0.43x | 6.0 | 2026-11-25T12:32:28.591944+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 70.744 | 0.00991 | +1.12% | 0.91x |
| 2 | VVV/USD | 69.720 | 25.061 | +0.48% | 0.61x |
| 3 | CT/USD | 48.312 | 0.1308 | +0.99% | 6.37x |
| 4 | INX/USD | 37.889 | 0.003947 | -1.99% | 1.03x |
| 5 | CAP/USD | 31.165 | 0.092739 | +0.40% | 0.43x |

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

- Persisted scans: 1718; predictions: 14508; observations: 1041329.
- Matured sampled outcomes across 1/6/24/48h: 31717; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45614257220 · **Generation:** 1718 · **Legacy run:** 45614257220
**Main quote time:** 2026-11-25T12:32:33.384625+00:00 · **Legacy report time:** 2026-11-25T12:33:35.755633+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.00991 | 75.44 | +1.12% | 0.91x | MODERATE 58/100 | VERY_HIGH 74/100 | Watch |
| 2 | CT/USD ⭐ | 0.1308 | 68.28 | +0.99% | 6.37x | STRONG 94/100 | VERY_HIGH 73/100 | Watch |
| 3 | VVV/USD | 25.061 | 68.22 | +0.48% | 0.61x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 4 | INX/USD | 0.003947 | 28.27 | -1.99% | 1.03x | WEAK 14/100 | EXTREME 96/100 | Do nothing |
| 5 | CAP/USD | 0.092739 | 27.49 | +0.40% | 0.43x | WEAK 44/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BABY/USD | 0.00882 | 77.02 | +1.48% | 1.41x | 3021 | STRONG 79/100 | VERY_HIGH 73/100 | Watch |
| 2 | CT/USD ⭐ | 0.1304 | 62.78 | +0.99% | 6.37x | 1468 | STRONG 86/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** CT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
