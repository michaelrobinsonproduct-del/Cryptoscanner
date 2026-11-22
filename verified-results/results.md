# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T19:41:18.175734+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45062000330
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** f453d26d59027fb52c2e7deffc325bb001d39717 (atomic ledger/results publication)
**Ledger generation:** 1327 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.37405 | 101.393 | 86.085 | +11.59% | +0.06% | 2.85x | 6.7 | 2026-11-22T19:41:11.577988+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04792 | 97.966 | 85.562 | +8.22% | -0.52% | 2.57x | 14.6 | 2026-11-22T19:41:11.577988+00:00 | Not calibrated | STRONG 74/100 | HIGH 67/100 | Watch | WATCH |
| 3 | PIEVERSE/USD | 3.6257 | 91.937 | 72.064 | +6.54% | +0.97% | 9.69x | 26.8 | 2026-11-22T19:41:11.577988+00:00 | Not calibrated | STRONG 91/100 | HIGH 67/100 | Consider small entry | WATCH |
| 4 | PUMP/USD | 0.002574 | 81.883 | 79.994 | +9.81% | +0.43% | 0.97x | 11.7 | 2026-11-22T19:41:11.577988+00:00 | Not calibrated | MODERATE 66/100 | HIGH 68/100 | Watch | WATCH |
| 5 | VVV/USD | 25.99 | 77.759 | 81.409 | +4.38% | +0.52% | 0.38x | 8.5 | 2026-11-22T19:41:11.577988+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | ETH/USD | 1711.4 | 77.681 | 67.088 | +1.73% | -0.04% | 2.08x | 0.1 | 2026-11-22T19:41:11.577988+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 7 | NEAR/USD | 2.9851 | 75.427 | 76.783 | +3.42% | -0.74% | 1.24x | 4.4 | 2026-11-22T19:41:11.577988+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 8 | PYTH/USD | 0.05167 | 65.836 | 64.759 | +5.73% | -0.63% | 1.42x | 13.6 | 2026-11-22T19:41:11.577988+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 9 | XBT/USD | 60636 | 62.395 | 61.353 | +0.91% | +0.03% | 1.09x | 0.0 | 2026-11-22T19:41:11.577988+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 10 | LINK/USD | 8.7888 | 61.466 | 57.811 | +2.26% | -0.15% | 1.44x | 3.6 | 2026-11-22T19:41:11.577988+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 11 | HYPE/USD | 62.23 | 58.752 | 65.513 | +1.62% | -0.34% | 0.49x | 1.6 | 2026-11-22T19:41:11.577988+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | ZEC/USD | 787.94 | 55.876 | 62.773 | +1.26% | -0.30% | 0.46x | 2.0 | 2026-11-22T19:41:11.577988+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 86.085 | 0.37405 | +0.06% | 2.85x |
| 2 | NIGHT/USD | 85.562 | 0.04792 | -0.52% | 2.57x |
| 3 | VVV/USD | 81.409 | 25.99 | +0.52% | 0.38x |
| 4 | PUMP/USD | 79.994 | 0.002574 | +0.43% | 0.97x |
| 5 | NEAR/USD | 76.783 | 2.9851 | -0.74% | 1.24x |
| 6 | PIEVERSE/USD | 72.064 | 3.6257 | +0.97% | 9.69x |
| 7 | ETH/USD | 67.088 | 1711.4 | -0.04% | 2.08x |
| 8 | HYPE/USD | 65.513 | 62.23 | -0.34% | 0.49x |
| 9 | PYTH/USD | 64.759 | 0.05167 | -0.63% | 1.42x |
| 10 | ZEC/USD | 62.773 | 787.94 | -0.30% | 0.46x |
| 11 | XBT/USD | 61.353 | 60636 | +0.03% | 1.09x |
| 12 | LINK/USD | 57.811 | 8.7888 | -0.15% | 1.44x |

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

- Persisted scans: 1327; predictions: 10843; observations: 803251.
- Matured sampled outcomes across 1/6/24/48h: 16378; gap abstentions: 22343. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
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

**Writer:** 45062000330 · **Generation:** 1327 · **Legacy run:** 45062000330
**Main quote time:** 2026-11-22T19:41:18.175734+00:00 · **Legacy report time:** 2026-11-22T19:42:30.732801+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.37405 | 101.39 | +0.06% | 2.85x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | NIGHT/USD | 0.04792 | 97.97 | -0.52% | 2.57x | STRONG 74/100 | HIGH 67/100 | Watch |
| 3 | PIEVERSE/USD ⭐ | 3.6257 | 91.94 | +0.97% | 9.69x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 4 | PUMP/USD | 0.002574 | 81.88 | +0.43% | 0.97x | MODERATE 66/100 | HIGH 68/100 | Watch |
| 5 | VVV/USD | 25.99 | 77.76 | +0.52% | 0.38x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 6 | ETH/USD | 1711.4 | 77.68 | -0.04% | 2.08x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 7 | NEAR/USD | 2.9851 | 75.43 | -0.74% | 1.24x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 8 | PYTH/USD | 0.05167 | 65.84 | -0.63% | 1.42x | MODERATE 48/100 | VERY_HIGH 79/100 | Watch |
| 9 | XBT/USD | 60636 | 62.40 | +0.03% | 1.09x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 10 | LINK/USD | 8.7888 | 61.47 | -0.15% | 1.44x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 11 | HYPE/USD | 62.23 | 58.75 | -0.34% | 0.49x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | ZEC/USD | 787.94 | 55.88 | -0.30% | 0.46x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD ⭐ | 3.6257 | 87.21 | +0.97% | 9.69x | 5942 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | DRV/USD ⭐ | 0.3748 | 86.25 | +0.06% | 2.85x | 18385 | STRONG 93/100 | HIGH 61/100 | Watch |

**Same-run overlap:** DRV/USD, PIEVERSE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
