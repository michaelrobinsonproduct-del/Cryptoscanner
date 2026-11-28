# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T11:22:37.888844+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46139339346
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** bb1634855bd06c37fecf0edb241682546d7dcf9f (atomic ledger/results publication)
**Ledger generation:** 2147 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05341 | 92.807 | 89.794 | +6.31% | +1.45% | 0.58x | 18.7 | 2026-11-28T11:22:34.775397+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | XMR/USD | 427.52 | 92.654 | 88.987 | +4.97% | +0.35% | 1.19x | 1.6 | 2026-11-28T11:22:34.775397+00:00 | Not calibrated | STRONG 81/100 | HIGH 62/100 | Watch | WATCH |
| 3 | VVV/USD | 26.733 | 73.849 | 64.639 | +3.82% | +0.10% | 1.87x | 12.4 | 2026-11-28T11:22:34.775397+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SENT/USD | 0.024521 | 56.834 | 53.557 | +3.40% | +0.11% | 1.27x | 3.3 | 2026-11-28T11:22:34.775397+00:00 | Not calibrated | MODERATE 53/100 | HIGH 67/100 | Watch | WATCH |
| 5 | SPACE/USD | 0.004419 | 55.729 | 67.426 | +5.77% | -0.70% | 0.18x | 9.0 | 2026-11-28T11:22:34.775397+00:00 | Not calibrated | WEAK 33/100 | EXTREME 88/100 | Do nothing | WATCH |
| 6 | AKE/USD | 0.00112151 | 46.804 | 37.486 | +3.22% | +2.15% | 0.86x | 43.5 | 2026-11-28T11:22:34.775397+00:00 | Not calibrated | WEAK 38/100 | EXTREME 89/100 | Do nothing | WATCH |
| 7 | KAVA/USD | 0.028 | 41.900 | 31.796 | +2.56% | +0.36% | 1.83x | 35.8 | 2026-11-28T11:22:34.775397+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 8 | CC/USD | 0.07436 | 29.126 | 32.587 | +0.28% | -0.38% | 0.84x | 6.7 | 2026-11-28T11:22:34.775397+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 73/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 89.794 | 0.05341 | +1.45% | 0.58x |
| 2 | XMR/USD | 88.987 | 427.52 | +0.35% | 1.19x |
| 3 | SPACE/USD | 67.426 | 0.004419 | -0.70% | 0.18x |
| 4 | VVV/USD | 64.639 | 26.733 | +0.10% | 1.87x |
| 5 | SENT/USD | 53.557 | 0.024521 | +0.11% | 1.27x |
| 6 | AKE/USD | 37.486 | 0.00112151 | +2.15% | 0.86x |
| 7 | CC/USD | 32.587 | 0.07436 | -0.38% | 0.84x |
| 8 | KAVA/USD | 31.796 | 0.028 | +0.36% | 1.83x |

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

- Persisted scans: 2147; predictions: 19155; observations: 1300128.
- Matured sampled outcomes across 1/6/24/48h: 45586; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46139339346 · **Generation:** 2147 · **Legacy run:** 46139339346
**Main quote time:** 2026-11-28T11:22:37.888844+00:00 · **Legacy report time:** 2026-11-28T11:23:23.676420+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.05341 | 92.81 | +1.45% | 0.58x | STRONG 71/100 | VERY_HIGH 76/100 | Watch |
| 2 | XMR/USD ⭐ | 427.52 | 92.65 | +0.35% | 1.19x | STRONG 91/100 | HIGH 62/100 | Watch |
| 3 | VVV/USD ⭐ | 26.733 | 73.85 | +0.10% | 1.87x | STRONG 77/100 | HIGH 61/100 | Watch |
| 4 | SENT/USD ⭐ | 0.024521 | 56.83 | +0.11% | 1.27x | MODERATE 63/100 | HIGH 67/100 | Watch |
| 5 | SPACE/USD | 0.004419 | 55.73 | -0.70% | 0.18x | WEAK 33/100 | EXTREME 88/100 | Do nothing |
| 6 | AKE/USD | 0.00112151 | 46.80 | +2.15% | 0.86x | WEAK 38/100 | EXTREME 89/100 | Do nothing |
| 7 | KAVA/USD ⭐ | 0.028 | 41.90 | +0.36% | 1.83x | MODERATE 61/100 | VERY_HIGH 72/100 | Watch |
| 8 | CC/USD | 0.07436 | 29.13 | -0.38% | 0.84x | WEAK 20/100 | VERY_HIGH 73/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 427.86 | 86.81 | +0.35% | 1.19x | 16580 | STRONG 83/100 | HIGH 68/100 | Watch |
| 2 | VVV/USD ⭐ | 26.763 | 81.48 | +0.10% | 1.87x | 7724 | STRONG 86/100 | HIGH 55/100 | Watch |
| 3 | SENT/USD ⭐ | 0.024564 | 80.63 | +0.11% | 1.27x | 5635 | STRONG 75/100 | HIGH 67/100 | Watch |
| 4 | KAVA/USD ⭐ | 0.028 | 54.05 | +0.36% | 1.83x | 2139 | MODERATE 67/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** XMR/USD, VVV/USD, SENT/USD, KAVA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
