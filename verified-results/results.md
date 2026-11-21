# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T21:41:05.937583+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44952675416
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 16fe2470c768c8fb19f6c81a78d09acded19c56b (atomic ledger/results publication)
**Ledger generation:** 1189 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.7204 | 108.055 | 92.557 | +5.67% | +0.10% | 3.09x | 4.2 | 2026-11-21T21:40:57.142513+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | XMR/USD | 490.63 | 104.159 | 96.333 | +7.53% | +0.17% | 1.70x | 7.3 | 2026-11-21T21:40:57.142513+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ZEC/USD | 791.08 | 97.601 | 83.993 | +4.38% | -0.28% | 3.85x | 3.3 | 2026-11-21T21:40:57.142513+00:00 | Not calibrated | STRONG 79/100 | HIGH 61/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04515 | 88.061 | 89.632 | +6.94% | +0.79% | 0.45x | 8.9 | 2026-11-21T21:40:57.142513+00:00 | Not calibrated | STRONG 74/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | ETH/USD | 1683.18 | 80.681 | 82.576 | +3.94% | -0.00% | 0.81x | 0.1 | 2026-11-21T21:40:57.142513+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 6 | PEARL/USD | 2.0021 | 80.466 | 89.109 | +9.51% | -0.56% | 0.41x | 0.5 | 2026-11-21T21:40:57.142513+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | SOL/USD | 70.34 | 72.234 | 70.895 | +2.37% | -0.11% | 1.19x | 1.4 | 2026-11-21T21:40:57.142513+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XBT/USD | 60308.3 | 70.298 | 72.870 | +2.55% | -0.05% | 0.77x | 0.0 | 2026-11-21T21:40:57.142513+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 9 | XRP/USD | 0.92796 | 61.475 | 69.559 | +2.12% | -0.20% | 0.29x | 0.5 | 2026-11-21T21:40:57.142513+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | TAO/USD | 185.4055 | 61.353 | 70.490 | +2.71% | -0.07% | 0.12x | 7.0 | 2026-11-21T21:40:57.142513+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | QNT/USD | 142.07 | 60.444 | 68.882 | +2.39% | +0.00% | 0.16x | 5.6 | 2026-11-21T21:40:57.142513+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0550909 | 58.071 | 65.387 | +1.50% | -0.14% | 0.34x | 0.3 | 2026-11-21T21:40:57.142513+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 96.333 | 490.63 | +0.17% | 1.70x |
| 2 | UNI/USD | 92.557 | 4.7204 | +0.10% | 3.09x |
| 3 | NIGHT/USD | 89.632 | 0.04515 | +0.79% | 0.45x |
| 4 | PEARL/USD | 89.109 | 2.0021 | -0.56% | 0.41x |
| 5 | ZEC/USD | 83.993 | 791.08 | -0.28% | 3.85x |
| 6 | ETH/USD | 82.576 | 1683.18 | -0.00% | 0.81x |
| 7 | XBT/USD | 72.870 | 60308.3 | -0.05% | 0.77x |
| 8 | SOL/USD | 70.895 | 70.34 | -0.11% | 1.19x |
| 9 | TAO/USD | 70.490 | 185.4055 | -0.07% | 0.12x |
| 10 | XRP/USD | 69.559 | 0.92796 | -0.20% | 0.29x |
| 11 | QNT/USD | 68.882 | 142.07 | +0.00% | 0.16x |
| 12 | XDG/USD | 65.387 | 0.0550909 | -0.14% | 0.34x |

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

- Persisted scans: 1189; predictions: 9577; observations: 719271.
- Matured sampled outcomes across 1/6/24/48h: 12796; gap abstentions: 21478. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44952675416 · **Generation:** 1189 · **Legacy run:** 44952675416
**Main quote time:** 2026-11-21T21:41:05.937583+00:00 · **Legacy report time:** 2026-11-21T21:41:58.666268+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.7204 | 108.06 | +0.10% | 3.09x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | XMR/USD ⭐ | 490.63 | 104.16 | +0.17% | 1.70x | STRONG 95/100 | HIGH 55/100 | Watch |
| 3 | ZEC/USD | 791.08 | 97.60 | -0.28% | 3.85x | STRONG 79/100 | HIGH 61/100 | Watch |
| 4 | NIGHT/USD | 0.04515 | 88.06 | +0.79% | 0.45x | STRONG 74/100 | VERY_HIGH 70/100 | Watch |
| 5 | ETH/USD | 1683.18 | 80.68 | -0.00% | 0.81x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 6 | PEARL/USD | 2.0021 | 80.47 | -0.56% | 0.41x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 7 | SOL/USD | 70.34 | 72.23 | -0.11% | 1.19x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 8 | XBT/USD | 60308.3 | 70.30 | -0.05% | 0.77x | WEAK 40/100 | HIGH 68/100 | Watch |
| 9 | XRP/USD | 0.92796 | 61.48 | -0.20% | 0.29x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 10 | TAO/USD | 185.4055 | 61.35 | -0.07% | 0.12x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 11 | QNT/USD | 142.07 | 60.44 | +0.00% | 0.16x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 12 | XDG/USD | 0.0550909 | 58.07 | -0.14% | 0.34x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.7204 | 95.15 | +0.10% | 3.09x | 11024 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | XMR/USD ⭐ | 491.54 | 88.30 | +0.17% | 1.70x | 12039 | STRONG 89/100 | HIGH 55/100 | Watch |

**Same-run overlap:** UNI/USD, XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
