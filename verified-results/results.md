# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T20:01:10.285802+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44943849966
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** aafdaf81c0a3af86f003865097aa6f94c38ebc46 (atomic ledger/results publication)
**Ledger generation:** 1179 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 485.4 | 98.008 | 92.745 | +6.38% | +0.35% | 1.35x | 13.8 | 2026-11-21T20:01:02.371260+00:00 | Not calibrated | STRONG 89/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ZEC/USD | 788.94 | 93.738 | 81.505 | +4.09% | +0.03% | 2.21x | 4.3 | 2026-11-21T20:01:02.371260+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Watch | WATCH |
| 3 | XRP/USD | 0.93418 | 89.400 | 73.924 | +2.80% | +0.10% | 2.70x | 1.4 | 2026-11-21T20:01:02.371260+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ETH/USD | 1681.8 | 82.187 | 81.979 | +3.86% | -0.07% | 1.06x | 0.1 | 2026-11-21T20:01:02.371260+00:00 | Not calibrated | MODERATE 51/100 | HIGH 68/100 | Watch | WATCH |
| 5 | UNI/USD | 4.6778 | 81.769 | 86.183 | +4.71% | +0.05% | 0.53x | 3.6 | 2026-11-21T20:01:02.371260+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.0451 | 80.775 | 87.800 | +6.82% | -0.20% | 0.40x | 11.1 | 2026-11-21T20:01:02.371260+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 7 | PEARL/USD | 1.964 | 77.367 | 81.930 | +7.42% | -0.19% | 0.64x | 17.8 | 2026-11-21T20:01:02.371260+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 8 | SOL/USD | 70.34 | 71.441 | 70.895 | +2.37% | -0.20% | 1.15x | 1.4 | 2026-11-21T20:01:02.371260+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 9 | XBT/USD | 60187.5 | 70.408 | 71.432 | +2.35% | -0.06% | 0.93x | 0.0 | 2026-11-21T20:01:02.371260+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 10 | PAXG/USD | 3554.84 | 66.915 | 53.718 | +0.66% | +0.07% | 2.29x | 0.9 | 2026-11-21T20:01:02.371260+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 11 | XLM/USD | 0.12925 | 66.713 | 65.657 | +1.61% | +0.14% | 1.03x | 1.2 | 2026-11-21T20:01:02.371260+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 12 | QNT/USD | 141.4 | 66.481 | 67.964 | +1.90% | -0.13% | 0.92x | 0.7 | 2026-11-21T20:01:02.371260+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 92.745 | 485.4 | +0.35% | 1.35x |
| 2 | NIGHT/USD | 87.800 | 0.0451 | -0.20% | 0.40x |
| 3 | UNI/USD | 86.183 | 4.6778 | +0.05% | 0.53x |
| 4 | ETH/USD | 81.979 | 1681.8 | -0.07% | 1.06x |
| 5 | PEARL/USD | 81.930 | 1.964 | -0.19% | 0.64x |
| 6 | ZEC/USD | 81.505 | 788.94 | +0.03% | 2.21x |
| 7 | XRP/USD | 73.924 | 0.93418 | +0.10% | 2.70x |
| 8 | XBT/USD | 71.432 | 60187.5 | -0.06% | 0.93x |
| 9 | SOL/USD | 70.895 | 70.34 | -0.20% | 1.15x |
| 10 | QNT/USD | 67.964 | 141.4 | -0.13% | 0.92x |
| 11 | XLM/USD | 65.657 | 0.12925 | +0.14% | 1.03x |
| 12 | PAXG/USD | 53.718 | 3554.84 | +0.07% | 2.29x |

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

- Persisted scans: 1179; predictions: 9457; observations: 713191.
- Matured sampled outcomes across 1/6/24/48h: 12556; gap abstentions: 21268. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44943849966 · **Generation:** 1179 · **Legacy run:** 44943849966
**Main quote time:** 2026-11-21T20:01:10.285802+00:00 · **Legacy report time:** 2026-11-21T20:02:15.819207+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 485.4 | 98.01 | +0.35% | 1.35x | STRONG 99/100 | HIGH 61/100 | Watch |
| 2 | ZEC/USD | 788.94 | 93.74 | +0.03% | 2.21x | STRONG 92/100 | HIGH 55/100 | Watch |
| 3 | XRP/USD ⭐ | 0.93418 | 89.40 | +0.10% | 2.70x | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | ETH/USD | 1681.8 | 82.19 | -0.07% | 1.06x | MODERATE 51/100 | HIGH 68/100 | Watch |
| 5 | UNI/USD | 4.6778 | 81.77 | +0.05% | 0.53x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 6 | NIGHT/USD | 0.0451 | 80.78 | -0.20% | 0.40x | WEAK 40/100 | VERY_HIGH 82/100 | Watch |
| 7 | PEARL/USD | 1.964 | 77.37 | -0.19% | 0.64x | WEAK 39/100 | VERY_HIGH 82/100 | Watch |
| 8 | SOL/USD | 70.34 | 71.44 | -0.20% | 1.15x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 9 | XBT/USD | 60187.5 | 70.41 | -0.06% | 0.93x | WEAK 40/100 | HIGH 68/100 | Watch |
| 10 | PAXG/USD | 3554.84 | 66.91 | +0.07% | 2.29x | STRONG 78/100 | HIGH 55/100 | Watch |
| 11 | XLM/USD ⭐ | 0.12925 | 66.71 | +0.14% | 1.03x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 12 | QNT/USD | 141.4 | 66.48 | -0.13% | 0.92x | WEAK 38/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.93412 | 92.43 | +0.10% | 2.70x | 54600 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | XMR/USD ⭐ | 485.3 | 87.63 | +0.35% | 1.35x | 12480 | STRONG 99/100 | HIGH 55/100 | Watch |
| 3 | XLM/USD ⭐ | 0.129362 | 71.87 | +0.14% | 1.03x | 15215 | STRONG 71/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XMR/USD, XRP/USD, XLM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
