# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T18:26:06.876287+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45674845767
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1aece80ce0fbcb7526916f25b83755d17333c668 (atomic ledger/results publication)
**Ledger generation:** 1750 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 26.571 | 91.243 | 94.729 | +8.29% | +0.36% | 0.47x | 10.5 | 2026-11-25T18:25:58.708099+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | DRV/USD | 0.35114 | 85.594 | 81.247 | +11.73% | +1.56% | 0.66x | 6.0 | 2026-11-25T18:25:58.708099+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | XPL/USD | 0.0478 | 72.262 | 71.183 | +8.64% | +0.42% | 0.90x | 21.0 | 2026-11-25T18:25:58.708099+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | HYPE/USD | 60.37 | 68.778 | 56.704 | +0.84% | +0.12% | 2.15x | 8.3 | 2026-11-25T18:25:58.708099+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 5 | LINK/USD | 8.91895 | 65.775 | 49.551 | +0.88% | +0.24% | 6.51x | 3.9 | 2026-11-25T18:25:58.708099+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 6 | LTC/USD | 41.7 | 64.670 | 67.169 | +2.08% | +0.05% | 0.73x | 4.8 | 2026-11-25T18:25:58.708099+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6517 | 60.405 | 58.007 | +0.65% | +0.12% | 1.18x | 3.1 | 2026-11-25T18:25:58.708099+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XMR/USD | 514.41 | 58.887 | 54.605 | +0.94% | +0.42% | 1.22x | 14.0 | 2026-11-25T18:25:58.708099+00:00 | Not calibrated | MODERATE 59/100 | HIGH 68/100 | Watch | WATCH |
| 9 | HBAR/USD | 0.05092 | 55.028 | 42.999 | +1.31% | +0.33% | 2.04x | 3.9 | 2026-11-25T18:25:58.708099+00:00 | Not calibrated | STRONG 83/100 | HIGH 60/100 | Watch | WATCH |
| 10 | ASTER/USD | 0.49225 | 49.739 | 47.317 | +2.38% | -0.05% | 1.27x | 4.1 | 2026-11-25T18:25:58.708099+00:00 | Not calibrated | WEAK 35/100 | HIGH 66/100 | Watch | WATCH |
| 11 | XLM/USD | 0.12583 | 48.686 | 51.007 | +1.43% | +0.12% | 0.71x | 5.0 | 2026-11-25T18:25:58.708099+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | PUMP/USD | 0.002469 | 42.465 | 47.060 | +1.23% | +0.41% | 0.34x | 4.1 | 2026-11-25T18:25:58.708099+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 94.729 | 26.571 | +0.36% | 0.47x |
| 2 | DRV/USD | 81.247 | 0.35114 | +1.56% | 0.66x |
| 3 | XPL/USD | 71.183 | 0.0478 | +0.42% | 0.90x |
| 4 | LTC/USD | 67.169 | 41.7 | +0.05% | 0.73x |
| 5 | SUI/USD | 58.007 | 0.6517 | +0.12% | 1.18x |
| 6 | HYPE/USD | 56.704 | 60.37 | +0.12% | 2.15x |
| 7 | XMR/USD | 54.605 | 514.41 | +0.42% | 1.22x |
| 8 | XLM/USD | 51.007 | 0.12583 | +0.12% | 0.71x |
| 9 | LINK/USD | 49.551 | 8.91895 | +0.24% | 6.51x |
| 10 | ASTER/USD | 47.317 | 0.49225 | -0.05% | 1.27x |
| 11 | PUMP/USD | 47.060 | 0.002469 | +0.41% | 0.34x |
| 12 | HBAR/USD | 42.999 | 0.05092 | +0.33% | 2.04x |

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

- Persisted scans: 1750; predictions: 14744; observations: 1060794.
- Matured sampled outcomes across 1/6/24/48h: 32517; gap abstentions: 22660. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45674845767 · **Generation:** 1750 · **Legacy run:** 45674845767
**Main quote time:** 2026-11-25T18:26:06.876287+00:00 · **Legacy report time:** 2026-11-25T18:27:18.920900+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 26.571 | 91.24 | +0.36% | 0.47x | STRONG 71/100 | VERY_HIGH 76/100 | Watch |
| 2 | DRV/USD | 0.35114 | 85.59 | +1.56% | 0.66x | STRONG 73/100 | VERY_HIGH 70/100 | Watch |
| 3 | XPL/USD | 0.0478 | 72.26 | +0.42% | 0.90x | MODERATE 56/100 | VERY_HIGH 79/100 | Watch |
| 4 | HYPE/USD ⭐ | 60.37 | 68.78 | +0.12% | 2.15x | STRONG 89/100 | HIGH 55/100 | Watch |
| 5 | LINK/USD | 8.91895 | 65.78 | +0.24% | 6.51x | STRONG 88/100 | HIGH 55/100 | Watch |
| 6 | LTC/USD | 41.7 | 64.67 | +0.05% | 0.73x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 7 | SUI/USD ⭐ | 0.6517 | 60.41 | +0.12% | 1.18x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 8 | XMR/USD | 514.41 | 58.89 | +0.42% | 1.22x | MODERATE 59/100 | HIGH 68/100 | Watch |
| 9 | HBAR/USD | 0.05092 | 55.03 | +0.33% | 2.04x | STRONG 83/100 | HIGH 60/100 | Watch |
| 10 | ASTER/USD | 0.49225 | 49.74 | -0.05% | 1.27x | WEAK 35/100 | HIGH 66/100 | Watch |
| 11 | XLM/USD | 0.12583 | 48.69 | +0.12% | 0.71x | WEAK 44/100 | VERY_HIGH 70/100 | Watch |
| 12 | PUMP/USD | 0.002469 | 42.46 | +0.41% | 0.34x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 60.41 | 57.83 | +0.12% | 2.15x | 22116 | STRONG 84/100 | HIGH 55/100 | Watch |
| 2 | SUI/USD ⭐ | 0.6521 | 55.46 | +0.12% | 1.18x | 7027 | MODERATE 63/100 | HIGH 62/100 | Watch |

**Same-run overlap:** HYPE/USD, SUI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
