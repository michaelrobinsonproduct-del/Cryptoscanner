# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T15:31:21.791296+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45038596912
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 247aaa7e4a954e2ae8af02acea010ffd4a510dbe (atomic ledger/results publication)
**Ledger generation:** 1301 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04844 | 98.397 | 89.922 | +9.39% | +0.62% | 1.54x | 4.1 | 2026-11-22T15:31:13.004359+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 25.546 | 81.018 | 67.286 | +2.59% | -0.25% | 4.16x | 11.8 | 2026-11-22T15:31:13.004359+00:00 | Not calibrated | MODERATE 66/100 | HIGH 67/100 | Watch | WATCH |
| 3 | TAO/USD | 190.6366 | 78.465 | 64.184 | +2.64% | -0.14% | 2.57x | 6.6 | 2026-11-22T15:31:13.004359+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 4 | NEAR/USD | 2.9937 | 75.115 | 79.211 | +3.72% | -0.52% | 0.85x | 3.7 | 2026-11-22T15:31:13.004359+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 5 | LINK/USD | 8.79454 | 72.600 | 59.763 | +2.32% | +0.20% | 2.19x | 2.0 | 2026-11-22T15:31:13.004359+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 6 | HYPE/USD | 62.79 | 69.301 | 71.921 | +2.53% | +0.21% | 0.63x | 1.6 | 2026-11-22T15:31:13.004359+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | ETH/USD | 1715.02 | 68.636 | 68.594 | +1.95% | +0.40% | 0.80x | 0.1 | 2026-11-22T15:31:13.004359+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 8 | STBL/USD | 0.017039 | 67.197 | 68.203 | +6.47% | +0.59% | 0.60x | 15.3 | 2026-11-22T15:31:13.004359+00:00 | Not calibrated | MODERATE 59/100 | EXTREME 88/100 | Do nothing | WATCH |
| 9 | SUI/USD | 0.6563 | 63.348 | 63.971 | +1.39% | +0.12% | 0.88x | 1.5 | 2026-11-22T15:31:13.004359+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |
| 10 | ZEC/USD | 793.97 | 62.505 | 67.828 | +2.03% | +0.35% | 0.29x | 2.8 | 2026-11-22T15:31:13.004359+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XBT/USD | 60804.3 | 61.318 | 63.314 | +1.19% | +0.07% | 0.76x | 0.0 | 2026-11-22T15:31:13.004359+00:00 | Not calibrated | MODERATE 51/100 | HIGH 62/100 | Watch | WATCH |
| 12 | ADA/USD | 0.144622 | 58.320 | 42.222 | +0.34% | +0.22% | 3.80x | 3.9 | 2026-11-22T15:31:13.004359+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 89.922 | 0.04844 | +0.62% | 1.54x |
| 2 | NEAR/USD | 79.211 | 2.9937 | -0.52% | 0.85x |
| 3 | HYPE/USD | 71.921 | 62.79 | +0.21% | 0.63x |
| 4 | ETH/USD | 68.594 | 1715.02 | +0.40% | 0.80x |
| 5 | STBL/USD | 68.203 | 0.017039 | +0.59% | 0.60x |
| 6 | ZEC/USD | 67.828 | 793.97 | +0.35% | 0.29x |
| 7 | VVV/USD | 67.286 | 25.546 | -0.25% | 4.16x |
| 8 | TAO/USD | 64.184 | 190.6366 | -0.14% | 2.57x |
| 9 | SUI/USD | 63.971 | 0.6563 | +0.12% | 0.88x |
| 10 | XBT/USD | 63.314 | 60804.3 | +0.07% | 0.76x |
| 11 | LINK/USD | 59.763 | 8.79454 | +0.20% | 2.19x |
| 12 | ADA/USD | 42.222 | 0.144622 | +0.22% | 3.80x |

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

- Persisted scans: 1301; predictions: 10531; observations: 787417.
- Matured sampled outcomes across 1/6/24/48h: 15439; gap abstentions: 22308. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45038596912 · **Generation:** 1301 · **Legacy run:** 45038596912
**Main quote time:** 2026-11-22T15:31:21.791296+00:00 · **Legacy report time:** 2026-11-22T15:32:26.720168+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04844 | 98.40 | +0.62% | 1.54x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD | 25.546 | 81.02 | -0.25% | 4.16x | MODERATE 66/100 | HIGH 67/100 | Watch |
| 3 | TAO/USD | 190.6366 | 78.47 | -0.14% | 2.57x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 4 | NEAR/USD | 2.9937 | 75.11 | -0.52% | 0.85x | WEAK 43/100 | HIGH 68/100 | Watch |
| 5 | LINK/USD ⭐ | 8.79454 | 72.60 | +0.20% | 2.19x | STRONG 91/100 | HIGH 55/100 | Watch |
| 6 | HYPE/USD | 62.79 | 69.30 | +0.21% | 0.63x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 7 | ETH/USD | 1715.02 | 68.64 | +0.40% | 0.80x | MODERATE 64/100 | HIGH 62/100 | Watch |
| 8 | STBL/USD | 0.017039 | 67.20 | +0.59% | 0.60x | MODERATE 59/100 | EXTREME 88/100 | Do nothing |
| 9 | SUI/USD | 0.6563 | 63.35 | +0.12% | 0.88x | MODERATE 52/100 | HIGH 62/100 | Watch |
| 10 | ZEC/USD | 793.97 | 62.50 | +0.35% | 0.29x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 11 | XBT/USD | 60804.3 | 61.32 | +0.07% | 0.76x | MODERATE 51/100 | HIGH 62/100 | Watch |
| 12 | ADA/USD | 0.144622 | 58.32 | +0.22% | 3.80x | STRONG 84/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04836 | 84.18 | +0.62% | 1.54x | 9946 | STRONG 92/100 | HIGH 61/100 | Consider small entry |
| 2 | LINK/USD ⭐ | 8.79378 | 73.45 | +0.20% | 2.19x | 4831 | STRONG 92/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NIGHT/USD, LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
