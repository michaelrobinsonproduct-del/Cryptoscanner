# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T15:10:53.372100+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44917678607
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** f2fec158fb19eb4cf5fd32bde5133c80ae019ce0 (atomic ledger/results publication)
**Ledger generation:** 1149 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.73 | 93.931 | 94.383 | +5.88% | +0.47% | 0.72x | 3.6 | 2026-11-21T15:10:46.627794+00:00 | Not calibrated | STRONG 77/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | TAO/USD | 188.9528 | 85.415 | 83.532 | +4.68% | +0.94% | 0.72x | 8.4 | 2026-11-21T15:10:46.627794+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | ZEC/USD | 790.33 | 82.450 | 82.732 | +4.28% | -0.19% | 1.07x | 4.4 | 2026-11-21T15:10:46.627794+00:00 | Not calibrated | MODERATE 51/100 | HIGH 68/100 | Watch | WATCH |
| 4 | ETH/USD | 1687.87 | 78.746 | 84.603 | +4.23% | +0.06% | 0.38x | 0.1 | 2026-11-21T15:10:46.627794+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | XMR/USD | 473.37 | 74.989 | 78.561 | +3.74% | -0.31% | 0.80x | 5.3 | 2026-11-21T15:10:46.627794+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 6 | SOL/USD | 70.64 | 72.154 | 73.954 | +2.81% | +0.11% | 0.76x | 1.4 | 2026-11-21T15:10:46.627794+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 7 | USELESS/USD | 0.08185 | 71.911 | 75.146 | +9.87% | -0.33% | 0.84x | 23.2 | 2026-11-21T15:10:46.627794+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 8 | XDG/USD | 0.0554011 | 67.173 | 69.515 | +2.07% | +0.26% | 0.63x | 0.0 | 2026-11-21T15:10:46.627794+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XBT/USD | 60174.9 | 66.773 | 71.282 | +2.33% | -0.11% | 0.60x | 0.0 | 2026-11-21T15:10:46.627794+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XLM/USD | 0.12904 | 65.861 | 64.152 | +1.45% | -0.01% | 1.18x | 1.9 | 2026-11-21T15:10:46.627794+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 11 | XRP/USD | 0.92903 | 65.646 | 70.115 | +2.24% | +0.02% | 0.55x | 1.1 | 2026-11-21T15:10:46.627794+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | AVAX/USD | 6.651 | 64.607 | 68.345 | +2.23% | +0.30% | 0.48x | 4.5 | 2026-11-21T15:10:46.627794+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UNI/USD | 94.383 | 4.73 | +0.47% | 0.72x |
| 2 | ETH/USD | 84.603 | 1687.87 | +0.06% | 0.38x |
| 3 | TAO/USD | 83.532 | 188.9528 | +0.94% | 0.72x |
| 4 | ZEC/USD | 82.732 | 790.33 | -0.19% | 1.07x |
| 5 | XMR/USD | 78.561 | 473.37 | -0.31% | 0.80x |
| 6 | USELESS/USD | 75.146 | 0.08185 | -0.33% | 0.84x |
| 7 | SOL/USD | 73.954 | 70.64 | +0.11% | 0.76x |
| 8 | XBT/USD | 71.282 | 60174.9 | -0.11% | 0.60x |
| 9 | XRP/USD | 70.115 | 0.92903 | +0.02% | 0.55x |
| 10 | XDG/USD | 69.515 | 0.0554011 | +0.26% | 0.63x |
| 11 | AVAX/USD | 68.345 | 6.651 | +0.30% | 0.48x |
| 12 | XLM/USD | 64.152 | 0.12904 | -0.01% | 1.18x |

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

- Persisted scans: 1149; predictions: 9097; observations: 694951.
- Matured sampled outcomes across 1/6/24/48h: 11955; gap abstentions: 20620. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44917678607 · **Generation:** 1149 · **Legacy run:** 44917678607
**Main quote time:** 2026-11-21T15:10:53.372100+00:00 · **Legacy report time:** 2026-11-21T15:11:50.809702+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD | 4.73 | 93.93 | +0.47% | 0.72x | STRONG 77/100 | VERY_HIGH 70/100 | Watch |
| 2 | TAO/USD | 188.9528 | 85.42 | +0.94% | 0.72x | STRONG 73/100 | VERY_HIGH 70/100 | Watch |
| 3 | ZEC/USD | 790.33 | 82.45 | -0.19% | 1.07x | MODERATE 51/100 | HIGH 68/100 | Watch |
| 4 | ETH/USD | 1687.87 | 78.75 | +0.06% | 0.38x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 5 | XMR/USD | 473.37 | 74.99 | -0.31% | 0.80x | WEAK 42/100 | HIGH 68/100 | Watch |
| 6 | SOL/USD | 70.64 | 72.15 | +0.11% | 0.76x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 7 | USELESS/USD | 0.08185 | 71.91 | -0.33% | 0.84x | WEAK 31/100 | VERY_HIGH 80/100 | Do nothing |
| 8 | XDG/USD | 0.0554011 | 67.17 | +0.26% | 0.63x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 9 | XBT/USD | 60174.9 | 66.77 | -0.11% | 0.60x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 10 | XLM/USD | 0.12904 | 65.86 | -0.01% | 1.18x | WEAK 43/100 | HIGH 68/100 | Watch |
| 11 | XRP/USD | 0.92903 | 65.65 | +0.02% | 0.55x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 12 | AVAX/USD | 6.651 | 64.61 | +0.30% | 0.48x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
