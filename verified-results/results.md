# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T11:53:32.474350+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45019201528
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 93046f32dadffc493a8aec896ad65670c9c1c50b (atomic ledger/results publication)
**Ledger generation:** 1279 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04673 | 105.162 | 78.028 | +5.53% | +2.43% | 6.75x | 12.8 | 2026-11-22T11:53:25.062989+00:00 | Not calibrated | STRONG 100/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | CRV/USD | 0.18526 | 80.002 | 67.570 | +3.87% | -0.26% | 2.37x | 9.2 | 2026-11-22T11:53:25.062989+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | TAO/USD | 189.9829 | 74.561 | 66.018 | +2.29% | -0.19% | 1.95x | 5.4 | 2026-11-22T11:53:25.062989+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 4 | PUMP/USD | 0.002484 | 71.436 | 79.632 | +5.97% | -0.12% | 0.24x | 8.0 | 2026-11-22T11:53:25.062989+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | NEAR/USD | 2.9858 | 70.803 | 76.954 | +3.45% | -0.12% | 0.45x | 4.4 | 2026-11-22T11:53:25.062989+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | INJ/USD | 6.222 | 66.527 | 68.855 | +4.17% | -0.69% | 1.11x | 4.8 | 2026-11-22T11:53:25.062989+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 7 | ZEC/USD | 797.58 | 64.129 | 69.700 | +2.49% | -0.44% | 0.66x | 5.5 | 2026-11-22T11:53:25.062989+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | HYPE/USD | 62.6 | 63.775 | 68.948 | +2.22% | +0.24% | 0.36x | 3.2 | 2026-11-22T11:53:25.062989+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XBT/USD | 60962.6 | 59.438 | 65.158 | +1.45% | -0.18% | 0.52x | 0.0 | 2026-11-22T11:53:25.062989+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6591 | 58.635 | 67.003 | +1.82% | -0.21% | 0.27x | 1.5 | 2026-11-22T11:53:25.062989+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | ETH/USD | 1706.96 | 56.364 | 64.420 | +1.47% | -0.15% | 0.27x | 1.7 | 2026-11-22T11:53:25.062989+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | SOL/USD | 70.64 | 52.246 | 58.273 | +0.67% | -0.17% | 0.48x | 2.8 | 2026-11-22T11:53:25.062989+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PUMP/USD | 79.632 | 0.002484 | -0.12% | 0.24x |
| 2 | NIGHT/USD | 78.028 | 0.04673 | +2.43% | 6.75x |
| 3 | NEAR/USD | 76.954 | 2.9858 | -0.12% | 0.45x |
| 4 | ZEC/USD | 69.700 | 797.58 | -0.44% | 0.66x |
| 5 | HYPE/USD | 68.948 | 62.6 | +0.24% | 0.36x |
| 6 | INJ/USD | 68.855 | 6.222 | -0.69% | 1.11x |
| 7 | CRV/USD | 67.570 | 0.18526 | -0.26% | 2.37x |
| 8 | SUI/USD | 67.003 | 0.6591 | -0.21% | 0.27x |
| 9 | TAO/USD | 66.018 | 189.9829 | -0.19% | 1.95x |
| 10 | XBT/USD | 65.158 | 60962.6 | -0.18% | 0.52x |
| 11 | ETH/USD | 64.420 | 1706.96 | -0.15% | 0.27x |
| 12 | SOL/USD | 58.273 | 70.64 | -0.17% | 0.48x |

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

- Persisted scans: 1279; predictions: 10268; observations: 774020.
- Matured sampled outcomes across 1/6/24/48h: 14814; gap abstentions: 22226. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 60 (sampled only; not a success-rate estimate).
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

**Writer:** 45019201528 · **Generation:** 1279 · **Legacy run:** 45019201528
**Main quote time:** 2026-11-22T11:53:32.474350+00:00 · **Legacy report time:** 2026-11-22T11:54:14.218771+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04673 | 105.16 | +2.43% | 6.75x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | CRV/USD | 0.18526 | 80.00 | -0.26% | 2.37x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | TAO/USD | 189.9829 | 74.56 | -0.19% | 1.95x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 4 | PUMP/USD | 0.002484 | 71.44 | -0.12% | 0.24x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 5 | NEAR/USD | 2.9858 | 70.80 | -0.12% | 0.45x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 6 | INJ/USD | 6.222 | 66.53 | -0.69% | 1.11x | WEAK 43/100 | HIGH 68/100 | Watch |
| 7 | ZEC/USD | 797.58 | 64.13 | -0.44% | 0.66x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 8 | HYPE/USD | 62.6 | 63.77 | +0.24% | 0.36x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 9 | XBT/USD | 60962.6 | 59.44 | -0.18% | 0.52x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 10 | SUI/USD | 0.6591 | 58.63 | -0.21% | 0.27x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | ETH/USD | 1706.96 | 56.36 | -0.15% | 0.27x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | SOL/USD | 70.64 | 52.25 | -0.17% | 0.48x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04686 | 94.74 | +2.43% | 6.75x | 9151 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
