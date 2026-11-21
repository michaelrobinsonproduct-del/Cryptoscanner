# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T18:00:58.449092+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44933023682
**Source SHA:** 7ac7b40f8385b7b363a3015feba153e001ac4fc4
**Previous ledger commit:** b83ef2bfd06ce5e69f752bf338367b35b5edade9 (atomic ledger/results publication)
**Ledger generation:** 1167 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.7116 | 90.822 | 92.024 | +5.47% | -0.26% | 1.01x | 2.5 | 2026-11-21T18:00:51.865143+00:00 | Not calibrated | MODERATE 55/100 | HIGH 68/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04578 | 90.120 | 91.344 | +8.43% | +0.51% | 0.62x | 2.2 | 2026-11-21T18:00:51.865143+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | QNT/USD | 142.74 | 87.582 | 72.276 | +2.87% | +0.58% | 2.24x | 5.6 | 2026-11-21T18:00:51.865143+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | PEARL/USD | 1.9634 | 86.314 | 91.165 | +7.39% | -3.97% | 3.32x | 0.5 | 2026-11-21T18:00:51.865143+00:00 | Not calibrated | STRONG 73/100 | HIGH 65/100 | Do nothing | WATCH |
| 5 | ETH/USD | 1680.27 | 79.824 | 81.318 | +3.76% | +0.06% | 0.82x | 0.1 | 2026-11-21T18:00:51.865143+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 6 | XMR/USD | 479.05 | 77.249 | 85.219 | +4.99% | -0.55% | 0.48x | 9.4 | 2026-11-21T18:00:51.865143+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | ZEC/USD | 785.95 | 75.759 | 80.516 | +3.70% | +0.30% | 0.38x | 0.8 | 2026-11-21T18:00:51.865143+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XRP/USD | 0.93229 | 75.353 | 72.628 | +2.59% | -0.10% | 1.32x | 1.1 | 2026-11-21T18:00:51.865143+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 9 | LINK/USD | 8.56834 | 72.279 | 57.463 | +0.45% | -0.04% | 2.76x | 1.4 | 2026-11-21T18:00:51.865143+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 10 | SOL/USD | 70.56 | 72.094 | 73.139 | +2.69% | -0.13% | 0.96x | 1.4 | 2026-11-21T18:00:51.865143+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0550628 | 69.462 | 64.961 | +1.45% | -0.20% | 1.55x | 0.4 | 2026-11-21T18:00:51.865143+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 12 | BEAM/USD | 0.003495 | 67.886 | 69.722 | +6.62% | +0.40% | 0.61x | 14.4 | 2026-11-21T18:00:51.865143+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UNI/USD | 92.024 | 4.7116 | -0.26% | 1.01x |
| 2 | NIGHT/USD | 91.344 | 0.04578 | +0.51% | 0.62x |
| 3 | PEARL/USD | 91.165 | 1.9634 | -3.97% | 3.32x |
| 4 | XMR/USD | 85.219 | 479.05 | -0.55% | 0.48x |
| 5 | ETH/USD | 81.318 | 1680.27 | +0.06% | 0.82x |
| 6 | ZEC/USD | 80.516 | 785.95 | +0.30% | 0.38x |
| 7 | SOL/USD | 73.139 | 70.56 | -0.13% | 0.96x |
| 8 | XRP/USD | 72.628 | 0.93229 | -0.10% | 1.32x |
| 9 | QNT/USD | 72.276 | 142.74 | +0.58% | 2.24x |
| 10 | BEAM/USD | 69.722 | 0.003495 | +0.40% | 0.61x |
| 11 | XDG/USD | 64.961 | 0.0550628 | -0.20% | 1.55x |
| 12 | LINK/USD | 57.463 | 8.56834 | -0.04% | 2.76x |

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

- Persisted scans: 1167; predictions: 9313; observations: 705895.
- Matured sampled outcomes across 1/6/24/48h: 12273; gap abstentions: 21018. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44933023682 · **Generation:** 1167 · **Legacy run:** 44933023682
**Main quote time:** 2026-11-21T18:00:58.449092+00:00 · **Legacy report time:** 2026-11-21T18:02:02.449816+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD | 4.7116 | 90.82 | -0.26% | 1.01x | MODERATE 55/100 | HIGH 68/100 | Watch |
| 2 | NIGHT/USD | 0.04578 | 90.12 | +0.51% | 0.62x | STRONG 75/100 | VERY_HIGH 70/100 | Watch |
| 3 | QNT/USD ⭐ | 142.74 | 87.58 | +0.58% | 2.24x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | PEARL/USD | 1.9634 | 86.31 | -3.97% | 3.32x | STRONG 73/100 | HIGH 65/100 | Do nothing |
| 5 | ETH/USD | 1680.27 | 79.82 | +0.06% | 0.82x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 6 | XMR/USD | 479.05 | 77.25 | -0.55% | 0.48x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 7 | ZEC/USD | 785.95 | 75.76 | +0.30% | 0.38x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 8 | XRP/USD | 0.93229 | 75.35 | -0.10% | 1.32x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 9 | LINK/USD | 8.56834 | 72.28 | -0.04% | 2.76x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 10 | SOL/USD | 70.56 | 72.09 | -0.13% | 0.96x | WEAK 41/100 | HIGH 68/100 | Watch |
| 11 | XDG/USD | 0.0550628 | 69.46 | -0.20% | 1.55x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 12 | BEAM/USD | 0.003495 | 67.89 | +0.40% | 0.61x | MODERATE 59/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 143.25 | 89.15 | +0.58% | 2.24x | 11219 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SHX/USD | 0.003528 | 77.54 | +0.60% | 1.26x | 2741 | STRONG 74/100 | HIGH 60/100 | Watch |

**Same-run overlap:** QNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
