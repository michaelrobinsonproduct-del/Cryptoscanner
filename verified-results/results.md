# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T21:51:11.610130+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44953533439
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 9ddae97edb324c614fd6aea54386ef35ff1cd4fb (atomic ledger/results publication)
**Ledger generation:** 1191 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.7265 | 110.962 | 93.936 | +5.80% | +0.45% | 2.48x | 3.4 | 2026-11-21T21:51:03.566559+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 792.11 | 100.539 | 85.324 | +4.51% | +0.04% | 3.43x | 2.5 | 2026-11-21T21:51:03.566559+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 3 | XMR/USD | 492.1 | 92.788 | 96.445 | +7.85% | +0.36% | 0.46x | 7.1 | 2026-11-21T21:51:03.566559+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04504 | 83.584 | 89.468 | +6.68% | +0.22% | 0.30x | 8.9 | 2026-11-21T21:51:03.566559+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | ETH/USD | 1684.47 | 82.218 | 83.133 | +4.02% | +0.10% | 0.86x | 0.1 | 2026-11-21T21:51:03.566559+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 6 | XBT/USD | 60295.4 | 76.630 | 72.716 | +2.53% | +0.02% | 1.38x | 0.0 | 2026-11-21T21:51:03.566559+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 7 | WINGS/USD | 0.001845 | 74.045 | 68.917 | +5.31% | +2.15% | 0.44x | 5.4 | 2026-11-21T21:51:03.566559+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | SOL/USD | 70.29 | 73.418 | 70.385 | +2.30% | -0.03% | 1.32x | 1.4 | 2026-11-21T21:51:03.566559+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 9 | PEARL/USD | 2.0064 | 69.858 | 69.614 | +9.74% | -0.10% | 1.07x | 40.0 | 2026-11-21T21:51:03.566559+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 10 | XRP/USD | 0.92802 | 69.194 | 69.821 | +2.12% | +0.09% | 0.89x | 0.1 | 2026-11-21T21:51:03.566559+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 11 | TAO/USD | 185.8153 | 67.419 | 73.701 | +2.94% | +0.28% | 0.23x | 3.8 | 2026-11-21T21:51:03.566559+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0551124 | 65.812 | 65.719 | +1.54% | +0.06% | 0.98x | 0.2 | 2026-11-21T21:51:03.566559+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 96.445 | 492.1 | +0.36% | 0.46x |
| 2 | UNI/USD | 93.936 | 4.7265 | +0.45% | 2.48x |
| 3 | NIGHT/USD | 89.468 | 0.04504 | +0.22% | 0.30x |
| 4 | ZEC/USD | 85.324 | 792.11 | +0.04% | 3.43x |
| 5 | ETH/USD | 83.133 | 1684.47 | +0.10% | 0.86x |
| 6 | TAO/USD | 73.701 | 185.8153 | +0.28% | 0.23x |
| 7 | XBT/USD | 72.716 | 60295.4 | +0.02% | 1.38x |
| 8 | SOL/USD | 70.385 | 70.29 | -0.03% | 1.32x |
| 9 | XRP/USD | 69.821 | 0.92802 | +0.09% | 0.89x |
| 10 | PEARL/USD | 69.614 | 2.0064 | -0.10% | 1.07x |
| 11 | WINGS/USD | 68.917 | 0.001845 | +2.15% | 0.44x |
| 12 | XDG/USD | 65.719 | 0.0551124 | +0.06% | 0.98x |

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

- Persisted scans: 1191; predictions: 9601; observations: 720487.
- Matured sampled outcomes across 1/6/24/48h: 12820; gap abstentions: 21491. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44953533439 · **Generation:** 1191 · **Legacy run:** 44953533439
**Main quote time:** 2026-11-21T21:51:11.610130+00:00 · **Legacy report time:** 2026-11-21T21:52:15.617313+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.7265 | 110.96 | +0.45% | 2.48x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD | 792.11 | 100.54 | +0.04% | 3.43x | STRONG 95/100 | HIGH 55/100 | Watch |
| 3 | XMR/USD | 492.1 | 92.79 | +0.36% | 0.46x | STRONG 76/100 | VERY_HIGH 70/100 | Watch |
| 4 | NIGHT/USD | 0.04504 | 83.58 | +0.22% | 0.30x | STRONG 72/100 | VERY_HIGH 70/100 | Watch |
| 5 | ETH/USD | 1684.47 | 82.22 | +0.10% | 0.86x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 6 | XBT/USD | 60295.4 | 76.63 | +0.02% | 1.38x | STRONG 73/100 | HIGH 55/100 | Watch |
| 7 | WINGS/USD | 0.001845 | 74.04 | +2.15% | 0.44x | MODERATE 67/100 | VERY_HIGH 75/100 | Watch |
| 8 | SOL/USD | 70.29 | 73.42 | -0.03% | 1.32x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 9 | PEARL/USD | 2.0064 | 69.86 | -0.10% | 1.07x | WEAK 30/100 | VERY_HIGH 80/100 | Do nothing |
| 10 | XRP/USD | 0.92802 | 69.19 | +0.09% | 0.89x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 11 | TAO/USD | 185.8153 | 67.42 | +0.28% | 0.23x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 12 | XDG/USD | 0.0551124 | 65.81 | +0.06% | 0.98x | MODERATE 53/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.7265 | 99.63 | +0.45% | 2.48x | 10836 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** UNI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
