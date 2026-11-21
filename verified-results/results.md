# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T16:40:59.634416+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44925772762
**Source SHA:** 7ac7b40f8385b7b363a3015feba153e001ac4fc4
**Previous ledger commit:** 751db768d0a9f7782b55f5ef9270fe4606f404f4 (atomic ledger/results publication)
**Ledger generation:** 1159 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.7108 | 106.737 | 91.154 | +5.45% | +0.12% | 6.63x | 4.0 | 2026-11-21T16:40:51.344165+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | XMR/USD | 477.56 | 88.585 | 80.613 | +4.66% | -0.03% | 1.81x | 14.0 | 2026-11-21T16:40:51.344165+00:00 | Not calibrated | MODERATE 59/100 | HIGH 67/100 | Watch | WATCH |
| 3 | TAO/USD | 185.6886 | 84.362 | 71.858 | +2.87% | -0.28% | 2.39x | 6.5 | 2026-11-21T16:40:51.344165+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ZEC/USD | 783.22 | 80.126 | 77.994 | +3.34% | -0.35% | 1.39x | 0.8 | 2026-11-21T16:40:51.344165+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ETH/USD | 1679.96 | 79.107 | 80.797 | +3.74% | -0.03% | 0.84x | 0.8 | 2026-11-21T16:40:51.344165+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 6 | XRP/USD | 0.92724 | 71.633 | 68.897 | +2.04% | -0.14% | 1.34x | 0.8 | 2026-11-21T16:40:51.344165+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 7 | SOL/USD | 70.38 | 66.020 | 71.303 | +2.43% | +0.04% | 0.45x | 1.4 | 2026-11-21T16:40:51.344165+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | PAXG/USD | 3542.84 | 64.647 | 56.568 | +0.32% | +0.03% | 1.79x | 0.6 | 2026-11-21T16:40:51.344165+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 9 | USELESS/USD | 0.0819 | 63.160 | 72.435 | +9.93% | -1.44% | 0.79x | 24.4 | 2026-11-21T16:40:51.344165+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 84/100 | Do nothing | WATCH |
| 10 | XDG/USD | 0.0549016 | 62.851 | 62.763 | +1.15% | -0.10% | 1.06x | 0.6 | 2026-11-21T16:40:51.344165+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 11 | XBT/USD | 59878.4 | 62.159 | 67.752 | +1.82% | -0.16% | 0.52x | 0.0 | 2026-11-21T16:40:51.344165+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | BNB/USD | 545.79 | 61.438 | 56.352 | +1.14% | +0.03% | 1.49x | 1.3 | 2026-11-21T16:40:51.344165+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UNI/USD | 91.154 | 4.7108 | +0.12% | 6.63x |
| 2 | ETH/USD | 80.797 | 1679.96 | -0.03% | 0.84x |
| 3 | XMR/USD | 80.613 | 477.56 | -0.03% | 1.81x |
| 4 | ZEC/USD | 77.994 | 783.22 | -0.35% | 1.39x |
| 5 | USELESS/USD | 72.435 | 0.0819 | -1.44% | 0.79x |
| 6 | TAO/USD | 71.858 | 185.6886 | -0.28% | 2.39x |
| 7 | SOL/USD | 71.303 | 70.38 | +0.04% | 0.45x |
| 8 | XRP/USD | 68.897 | 0.92724 | -0.14% | 1.34x |
| 9 | XBT/USD | 67.752 | 59878.4 | -0.16% | 0.52x |
| 10 | XDG/USD | 62.763 | 0.0549016 | -0.10% | 1.06x |
| 11 | PAXG/USD | 56.568 | 3542.84 | +0.03% | 1.79x |
| 12 | BNB/USD | 56.352 | 545.79 | +0.03% | 1.49x |

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

- Persisted scans: 1159; predictions: 9217; observations: 701031.
- Matured sampled outcomes across 1/6/24/48h: 12119; gap abstentions: 20827. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44925772762 · **Generation:** 1159 · **Legacy run:** 44925772762
**Main quote time:** 2026-11-21T16:40:59.634416+00:00 · **Legacy report time:** 2026-11-21T16:41:47.331043+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.7108 | 106.74 | +0.12% | 6.63x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | XMR/USD | 477.56 | 88.58 | -0.03% | 1.81x | MODERATE 59/100 | HIGH 67/100 | Watch |
| 3 | TAO/USD | 185.6886 | 84.36 | -0.28% | 2.39x | STRONG 72/100 | HIGH 61/100 | Watch |
| 4 | ZEC/USD | 783.22 | 80.13 | -0.35% | 1.39x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 5 | ETH/USD | 1679.96 | 79.11 | -0.03% | 0.84x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 6 | XRP/USD | 0.92724 | 71.63 | -0.14% | 1.34x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 7 | SOL/USD | 70.38 | 66.02 | +0.04% | 0.45x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 8 | PAXG/USD | 3542.84 | 64.65 | +0.03% | 1.79x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 9 | USELESS/USD | 0.0819 | 63.16 | -1.44% | 0.79x | WEAK 27/100 | VERY_HIGH 84/100 | Do nothing |
| 10 | XDG/USD | 0.0549016 | 62.85 | -0.10% | 1.06x | WEAK 41/100 | HIGH 68/100 | Watch |
| 11 | XBT/USD | 59878.4 | 62.16 | -0.16% | 0.52x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 12 | BNB/USD | 545.79 | 61.44 | +0.03% | 1.49x | MODERATE 66/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.7108 | 100.00 | +0.12% | 6.63x | 12054 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | PIEVERSE/USD | 3.1233 | 82.63 | +3.60% | 2.44x | 2251 | STRONG 81/100 | EXTREME 92/100 | Do nothing |
| 3 | NIGHT/USD | 0.04345 | 82.46 | +0.98% | 1.66x | 11295 | STRONG 86/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** UNI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
