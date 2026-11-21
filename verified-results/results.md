# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T01:15:28.866097+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44848973668
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 3ddb8014635f558e077704a10186b5390e1e123e (atomic ledger/results publication)
**Ledger generation:** 1053 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LINK/USD | 8.55436 | 70.657 | 55.170 | +0.29% | +0.10% | 3.76x | 3.7 | 2026-11-21T01:15:22.807226+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 2 | ETH/USD | 1624.21 | 69.203 | 57.083 | +0.30% | +0.16% | 2.13x | 0.1 | 2026-11-21T01:15:22.807226+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 3 | VVV/USD | 20.972 | 67.659 | 58.814 | +1.12% | +0.72% | 1.52x | 8.1 | 2026-11-21T01:15:22.807226+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 4 | XBT/USD | 59062.6 | 66.155 | 58.041 | +0.44% | +0.24% | 1.69x | 0.0 | 2026-11-21T01:15:22.807226+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 5 | SOL/USD | 68.96 | 60.168 | 56.822 | +0.36% | +0.12% | 1.28x | 1.5 | 2026-11-21T01:15:22.807226+00:00 | Not calibrated | MODERATE 55/100 | HIGH 55/100 | Watch | WATCH |
| 6 | CC/USD | 0.07491 | 51.798 | 37.198 | +0.48% | -0.08% | 3.63x | 5.3 | 2026-11-21T01:15:22.807226+00:00 | Not calibrated | MODERATE 56/100 | HIGH 66/100 | Watch | WATCH |
| 7 | AVAX/USD | 6.524 | 43.559 | 47.083 | +0.28% | +0.17% | 0.56x | 4.6 | 2026-11-21T01:15:22.807226+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | SKY/USD | 0.04418 | 38.701 | 36.706 | +0.78% | -0.61% | 1.51x | 9.1 | 2026-11-21T01:15:22.807226+00:00 | Not calibrated | WEAK 39/100 | HIGH 66/100 | Watch | WATCH |
| 9 | CAP/USD | 0.09236 | 36.550 | 33.990 | +0.89% | +0.12% | 1.20x | 9.8 | 2026-11-21T01:15:22.807226+00:00 | Not calibrated | WEAK 43/100 | HIGH 67/100 | Watch | WATCH |
| 10 | DCR/USD | 10.147 | 29.034 | 29.689 | +0.42% | +0.22% | 0.83x | 7.9 | 2026-11-21T01:15:22.807226+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 11 | RENDER/USD | 1.277 | 24.468 | 32.681 | +0.31% | -0.08% | 0.22x | 15.6 | 2026-11-21T01:15:22.807226+00:00 | Not calibrated | WEAK 12/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 58.814 | 20.972 | +0.72% | 1.52x |
| 2 | XBT/USD | 58.041 | 59062.6 | +0.24% | 1.69x |
| 3 | ETH/USD | 57.083 | 1624.21 | +0.16% | 2.13x |
| 4 | SOL/USD | 56.822 | 68.96 | +0.12% | 1.28x |
| 5 | LINK/USD | 55.170 | 8.55436 | +0.10% | 3.76x |
| 6 | AVAX/USD | 47.083 | 6.524 | +0.17% | 0.56x |
| 7 | CC/USD | 37.198 | 0.07491 | -0.08% | 3.63x |
| 8 | SKY/USD | 36.706 | 0.04418 | -0.61% | 1.51x |
| 9 | CAP/USD | 33.990 | 0.09236 | +0.12% | 1.20x |
| 10 | RENDER/USD | 32.681 | 1.277 | -0.08% | 0.22x |
| 11 | DCR/USD | 29.689 | 10.147 | +0.22% | 0.83x |

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

- Persisted scans: 1053; predictions: 8439; observations: 636584.
- Matured sampled outcomes across 1/6/24/48h: 10936; gap abstentions: 19146. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44848973668 · **Generation:** 1053 · **Legacy run:** 44848973668
**Main quote time:** 2026-11-21T01:15:28.866097+00:00 · **Legacy report time:** 2026-11-21T01:16:13.566034+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD ⭐ | 8.55436 | 70.66 | +0.10% | 3.76x | STRONG 90/100 | HIGH 55/100 | Watch |
| 2 | ETH/USD ⭐ | 1624.21 | 69.20 | +0.16% | 2.13x | STRONG 90/100 | HIGH 55/100 | Watch |
| 3 | VVV/USD ⭐ | 20.972 | 67.66 | +0.72% | 1.52x | STRONG 89/100 | HIGH 55/100 | Consider small entry |
| 4 | XBT/USD ⭐ | 59062.6 | 66.16 | +0.24% | 1.69x | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 5 | SOL/USD ⭐ | 68.96 | 60.17 | +0.12% | 1.28x | MODERATE 65/100 | HIGH 55/100 | Watch |
| 6 | CC/USD | 0.07491 | 51.80 | -0.08% | 3.63x | MODERATE 56/100 | HIGH 66/100 | Watch |
| 7 | AVAX/USD | 6.524 | 43.56 | +0.17% | 0.56x | WEAK 42/100 | VERY_HIGH 70/100 | Watch |
| 8 | SKY/USD | 0.04418 | 38.70 | -0.61% | 1.51x | WEAK 39/100 | HIGH 66/100 | Watch |
| 9 | CAP/USD | 0.09236 | 36.55 | +0.12% | 1.20x | WEAK 43/100 | HIGH 67/100 | Watch |
| 10 | DCR/USD | 10.147 | 29.03 | +0.22% | 0.83x | MODERATE 45/100 | VERY_HIGH 74/100 | Watch |
| 11 | RENDER/USD | 1.277 | 24.47 | -0.08% | 0.22x | WEAK 12/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XBT/USD ⭐ | 59061 | 60.65 | +0.24% | 1.69x | 230579 | STRONG 85/100 | HIGH 55/100 | Consider small entry |
| 2 | ETH/USD ⭐ | 1623.9 | 60.28 | +0.16% | 2.13x | 86077 | STRONG 85/100 | HIGH 55/100 | Watch |
| 3 | SOL/USD ⭐ | 68.95 | 54.74 | +0.12% | 1.28x | 43654 | MODERATE 62/100 | HIGH 55/100 | Watch |
| 4 | VVV/USD ⭐ | 20.972 | 54.74 | +0.72% | 1.52x | 11527 | STRONG 77/100 | HIGH 61/100 | Consider small entry |
| 5 | LINK/USD ⭐ | 8.55805 | 53.87 | +0.10% | 3.76x | 10978 | STRONG 82/100 | HIGH 55/100 | Watch |
| 6 | QNT/USD | 139.07 | 53.05 | +0.06% | 2.55x | 8710 | STRONG 72/100 | HIGH 55/100 | Watch |
| 7 | PIEVERSE/USD | 3.0397 | 53.03 | +1.24% | 4.32x | 2659 | STRONG 82/100 | HIGH 60/100 | Watch |

**Same-run overlap:** LINK/USD, ETH/USD, VVV/USD, XBT/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
