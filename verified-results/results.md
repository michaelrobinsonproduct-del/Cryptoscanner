# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T14:40:59.191306+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44915064717
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 2193df8b26df4c55c5136eae2cd64ee4616cf428 (atomic ledger/results publication)
**Ledger generation:** 1146 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | USELESS/USD | 0.0821 | 95.287 | 80.851 | +10.20% | -0.02% | 2.46x | 11.0 | 2026-11-21T14:40:52.561149+00:00 | Not calibrated | STRONG 73/100 | HIGH 67/100 | Watch | WATCH |
| 2 | ETH/USD | 1685.62 | 84.725 | 83.630 | +4.09% | -0.43% | 1.32x | 0.1 | 2026-11-21T14:40:52.561149+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 3 | UNI/USD | 4.6973 | 81.820 | 88.929 | +5.15% | -0.39% | 0.48x | 4.3 | 2026-11-21T14:40:52.561149+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | ZEC/USD | 792.28 | 77.666 | 84.913 | +4.53% | -0.50% | 0.52x | 3.7 | 2026-11-21T14:40:52.561149+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | XMR/USD | 471.21 | 75.802 | 72.478 | +3.27% | -0.31% | 1.49x | 10.8 | 2026-11-21T14:40:52.561149+00:00 | Not calibrated | MODERATE 53/100 | HIGH 67/100 | Watch | WATCH |
| 6 | TAO/USD | 187.587 | 70.899 | 77.479 | +3.92% | -0.01% | 0.35x | 9.9 | 2026-11-21T14:40:52.561149+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | SOL/USD | 70.29 | 68.634 | 70.385 | +2.30% | -0.52% | 1.09x | 1.4 | 2026-11-21T14:40:52.561149+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 8 | AVAX/USD | 6.622 | 67.286 | 65.972 | +1.78% | -0.12% | 1.19x | 3.0 | 2026-11-21T14:40:52.561149+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 9 | XLM/USD | 0.128467 | 64.903 | 60.683 | +1.00% | -0.17% | 1.51x | 2.6 | 2026-11-21T14:40:52.561149+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 10 | XBT/USD | 60203.9 | 64.282 | 71.627 | +2.38% | -0.19% | 0.36x | 0.0 | 2026-11-21T14:40:52.561149+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0551684 | 61.843 | 66.441 | +1.65% | -0.16% | 0.62x | 0.2 | 2026-11-21T14:40:52.561149+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | XRP/USD | 0.92655 | 60.016 | 68.635 | +1.96% | -0.45% | 0.36x | 0.2 | 2026-11-21T14:40:52.561149+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UNI/USD | 88.929 | 4.6973 | -0.39% | 0.48x |
| 2 | ZEC/USD | 84.913 | 792.28 | -0.50% | 0.52x |
| 3 | ETH/USD | 83.630 | 1685.62 | -0.43% | 1.32x |
| 4 | USELESS/USD | 80.851 | 0.0821 | -0.02% | 2.46x |
| 5 | TAO/USD | 77.479 | 187.587 | -0.01% | 0.35x |
| 6 | XMR/USD | 72.478 | 471.21 | -0.31% | 1.49x |
| 7 | XBT/USD | 71.627 | 60203.9 | -0.19% | 0.36x |
| 8 | SOL/USD | 70.385 | 70.29 | -0.52% | 1.09x |
| 9 | XRP/USD | 68.635 | 0.92655 | -0.45% | 0.36x |
| 10 | XDG/USD | 66.441 | 0.0551684 | -0.16% | 0.62x |
| 11 | AVAX/USD | 65.972 | 6.622 | -0.12% | 1.19x |
| 12 | XLM/USD | 60.683 | 0.128467 | -0.17% | 1.51x |

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

- Persisted scans: 1146; predictions: 9061; observations: 693127.
- Matured sampled outcomes across 1/6/24/48h: 11910; gap abstentions: 20545. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44915064717 · **Generation:** 1146 · **Legacy run:** 44915064717
**Main quote time:** 2026-11-21T14:40:59.191306+00:00 · **Legacy report time:** 2026-11-21T14:42:03.217698+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | USELESS/USD | 0.0821 | 95.29 | -0.02% | 2.46x | STRONG 73/100 | HIGH 67/100 | Watch |
| 2 | ETH/USD | 1685.62 | 84.72 | -0.43% | 1.32x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 3 | UNI/USD | 4.6973 | 81.82 | -0.39% | 0.48x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 4 | ZEC/USD | 792.28 | 77.67 | -0.50% | 0.52x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 5 | XMR/USD | 471.21 | 75.80 | -0.31% | 1.49x | MODERATE 53/100 | HIGH 67/100 | Watch |
| 6 | TAO/USD | 187.587 | 70.90 | -0.01% | 0.35x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 7 | SOL/USD | 70.29 | 68.63 | -0.52% | 1.09x | WEAK 44/100 | HIGH 68/100 | Watch |
| 8 | AVAX/USD | 6.622 | 67.29 | -0.12% | 1.19x | WEAK 44/100 | HIGH 68/100 | Watch |
| 9 | XLM/USD | 0.128467 | 64.90 | -0.17% | 1.51x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 10 | XBT/USD | 60203.9 | 64.28 | -0.19% | 0.36x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 11 | XDG/USD | 0.0551684 | 61.84 | -0.16% | 0.62x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 12 | XRP/USD | 0.92655 | 60.02 | -0.45% | 0.36x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 23.443 | 91.98 | +1.37% | 1.72x | 15320 | STRONG 86/100 | HIGH 61/100 | Consider small entry |
| 2 | SHX/USD | 0.003513 | 81.38 | +1.12% | 2.73x | 3002 | STRONG 91/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
