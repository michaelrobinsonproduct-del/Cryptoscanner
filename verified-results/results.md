# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T14:10:55.425367+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44912469570
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 482b4dc803451b2987a235bdb630f3d722ae4399 (atomic ledger/results publication)
**Ledger generation:** 1143 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CT/USD | 0.134 | 94.013 | 69.119 | +10.65% | +1.98% | 2.62x | 15.0 | 2026-11-21T14:10:46.588722+00:00 | Not calibrated | STRONG 97/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | ZAMA/USD | 0.06057 | 88.513 | 69.268 | +6.24% | +0.85% | 3.85x | 11.6 | 2026-11-21T14:10:46.588722+00:00 | Not calibrated | STRONG 94/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | VVV/USD | 22.977 | 85.615 | 93.680 | +10.79% | -1.08% | 0.73x | 12.6 | 2026-11-21T14:10:46.588722+00:00 | Not calibrated | WEAK 43/100 | EXTREME 86/100 | Do nothing | WATCH |
| 4 | ETH/USD | 1694.13 | 79.237 | 87.309 | +4.62% | -0.50% | 0.44x | 0.1 | 2026-11-21T14:10:46.588722+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | UNI/USD | 4.6918 | 76.749 | 85.820 | +5.03% | -0.74% | 0.46x | 8.7 | 2026-11-21T14:10:46.588722+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | TAO/USD | 186.8061 | 76.345 | 74.280 | +3.49% | -0.73% | 1.57x | 10.3 | 2026-11-21T14:10:46.588722+00:00 | Not calibrated | MODERATE 53/100 | HIGH 67/100 | Watch | WATCH |
| 7 | XMR/USD | 473.99 | 74.912 | 73.816 | +3.88% | +0.22% | 1.00x | 16.7 | 2026-11-21T14:10:46.588722+00:00 | Not calibrated | MODERATE 62/100 | HIGH 68/100 | Watch | WATCH |
| 8 | LINK/USD | 8.6271 | 70.572 | 61.217 | +1.14% | -0.32% | 2.09x | 3.6 | 2026-11-21T14:10:46.588722+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 9 | QNT/USD | 139.3 | 69.999 | 54.855 | +0.39% | +0.03% | 3.92x | 5.7 | 2026-11-21T14:10:46.588722+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 10 | USELESS/USD | 0.081 | 69.613 | 73.379 | +8.72% | +0.50% | 0.38x | 24.6 | 2026-11-21T14:10:46.588722+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 11 | TRX/USD | 0.305555 | 67.034 | 63.718 | +1.34% | -0.07% | 1.37x | 1.4 | 2026-11-21T14:10:46.588722+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 12 | XRP/USD | 0.92403 | 66.238 | 65.231 | +1.69% | -0.57% | 1.39x | 3.1 | 2026-11-21T14:10:46.588722+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 93.680 | 22.977 | -1.08% | 0.73x |
| 2 | ETH/USD | 87.309 | 1694.13 | -0.50% | 0.44x |
| 3 | UNI/USD | 85.820 | 4.6918 | -0.74% | 0.46x |
| 4 | TAO/USD | 74.280 | 186.8061 | -0.73% | 1.57x |
| 5 | XMR/USD | 73.816 | 473.99 | +0.22% | 1.00x |
| 6 | USELESS/USD | 73.379 | 0.081 | +0.50% | 0.38x |
| 7 | ZAMA/USD | 69.268 | 0.06057 | +0.85% | 3.85x |
| 8 | CT/USD | 69.119 | 0.134 | +1.98% | 2.62x |
| 9 | XRP/USD | 65.231 | 0.92403 | -0.57% | 1.39x |
| 10 | TRX/USD | 63.718 | 0.305555 | -0.07% | 1.37x |
| 11 | LINK/USD | 61.217 | 8.6271 | -0.32% | 2.09x |
| 12 | QNT/USD | 54.855 | 139.3 | +0.03% | 3.92x |

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

- Persisted scans: 1143; predictions: 9025; observations: 691303.
- Matured sampled outcomes across 1/6/24/48h: 11852; gap abstentions: 20476. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 1; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44912469570 · **Generation:** 1143 · **Legacy run:** 44912469570
**Main quote time:** 2026-11-21T14:10:55.425367+00:00 · **Legacy report time:** 2026-11-21T14:11:43.058120+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CT/USD | 0.134 | 94.01 | +1.98% | 2.62x | STRONG 97/100 | VERY_HIGH 73/100 | Watch |
| 2 | ZAMA/USD ⭐ | 0.06057 | 88.51 | +0.85% | 3.85x | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 3 | VVV/USD | 22.977 | 85.61 | -1.08% | 0.73x | WEAK 43/100 | EXTREME 86/100 | Do nothing |
| 4 | ETH/USD | 1694.13 | 79.24 | -0.50% | 0.44x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 5 | UNI/USD | 4.6918 | 76.75 | -0.74% | 0.46x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 6 | TAO/USD | 186.8061 | 76.35 | -0.73% | 1.57x | MODERATE 53/100 | HIGH 67/100 | Watch |
| 7 | XMR/USD | 473.99 | 74.91 | +0.22% | 1.00x | MODERATE 62/100 | HIGH 68/100 | Watch |
| 8 | LINK/USD | 8.6271 | 70.57 | -0.32% | 2.09x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 9 | QNT/USD | 139.3 | 70.00 | +0.03% | 3.92x | STRONG 80/100 | HIGH 55/100 | Watch |
| 10 | USELESS/USD | 0.081 | 69.61 | +0.50% | 0.38x | MODERATE 55/100 | VERY_HIGH 82/100 | Watch |
| 11 | TRX/USD | 0.305555 | 67.03 | -0.07% | 1.37x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 12 | XRP/USD | 0.92403 | 66.24 | -0.57% | 1.39x | MODERATE 53/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZAMA/USD ⭐ | 0.06057 | 81.35 | +0.85% | 3.85x | 2949 | STRONG 100/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** ZAMA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
