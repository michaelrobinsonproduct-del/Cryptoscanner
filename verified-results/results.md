# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T12:50:41.902095+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44905812141
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 83bb52d910197993095b8eafc1de778d93c9904d (atomic ledger/results publication)
**Ledger generation:** 1135 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.548 | 101.039 | 95.781 | +8.72% | +0.76% | 1.15x | 8.4 | 2026-11-21T12:50:34.909509+00:00 | Not calibrated | STRONG 85/100 | HIGH 62/100 | Watch | WATCH |
| 2 | ETH/USD | 1660.05 | 88.669 | 72.577 | +2.52% | +0.22% | 3.35x | 0.1 | 2026-11-21T12:50:34.909509+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | XMR/USD | 469.93 | 85.183 | 72.947 | +2.99% | -0.55% | 2.64x | 6.0 | 2026-11-21T12:50:34.909509+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 4 | USELESS/USD | 0.07736 | 71.178 | 60.985 | +3.84% | -0.17% | 2.10x | 11.7 | 2026-11-21T12:50:34.909509+00:00 | Not calibrated | MODERATE 61/100 | HIGH 67/100 | Watch | WATCH |
| 5 | ZEC/USD | 768.16 | 70.407 | 61.338 | +1.35% | +0.27% | 1.77x | 6.3 | 2026-11-21T12:50:34.909509+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | SOL/USD | 69.02 | 63.970 | 57.434 | +0.45% | +0.01% | 1.65x | 1.4 | 2026-11-21T12:50:34.909509+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 7 | TRX/USD | 0.302654 | 63.495 | 57.125 | +0.38% | +0.03% | 1.62x | 1.1 | 2026-11-21T12:50:34.909509+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 8 | ZAMA/USD | 0.05849 | 59.250 | 45.188 | +2.60% | -0.19% | 19.98x | 8.6 | 2026-11-21T12:50:34.909509+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 9 | SENT/USD | 0.021046 | 56.326 | 43.499 | +2.19% | +0.18% | 2.19x | 5.7 | 2026-11-21T12:50:34.909509+00:00 | Not calibrated | STRONG 73/100 | HIGH 67/100 | Watch | WATCH |
| 10 | TAO/USD | 182.2083 | 55.587 | 57.859 | +0.94% | +0.32% | 0.61x | 7.5 | 2026-11-21T12:50:34.909509+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | AKT/USD | 0.5087 | 54.907 | 31.271 | +0.95% | +1.73% | 45.55x | 17.7 | 2026-11-21T12:50:34.909509+00:00 | Not calibrated | STRONG 77/100 | HIGH 66/100 | Watch | WATCH |
| 12 | AAVE/USD | 99.15 | 53.147 | 51.543 | +1.29% | -0.69% | 1.50x | 7.1 | 2026-11-21T12:50:34.909509+00:00 | Not calibrated | MODERATE 47/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 95.781 | 22.548 | +0.76% | 1.15x |
| 2 | XMR/USD | 72.947 | 469.93 | -0.55% | 2.64x |
| 3 | ETH/USD | 72.577 | 1660.05 | +0.22% | 3.35x |
| 4 | ZEC/USD | 61.338 | 768.16 | +0.27% | 1.77x |
| 5 | USELESS/USD | 60.985 | 0.07736 | -0.17% | 2.10x |
| 6 | TAO/USD | 57.859 | 182.2083 | +0.32% | 0.61x |
| 7 | SOL/USD | 57.434 | 69.02 | +0.01% | 1.65x |
| 8 | TRX/USD | 57.125 | 0.302654 | +0.03% | 1.62x |
| 9 | AAVE/USD | 51.543 | 99.15 | -0.69% | 1.50x |
| 10 | ZAMA/USD | 45.188 | 0.05849 | -0.19% | 19.98x |
| 11 | SENT/USD | 43.499 | 0.021046 | +0.18% | 2.19x |
| 12 | AKT/USD | 31.271 | 0.5087 | +1.73% | 45.55x |

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

- Persisted scans: 1135; predictions: 8931; observations: 686439.
- Matured sampled outcomes across 1/6/24/48h: 11725; gap abstentions: 20381. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44905812141 · **Generation:** 1135 · **Legacy run:** 44905812141
**Main quote time:** 2026-11-21T12:50:41.902095+00:00 · **Legacy report time:** 2026-11-21T12:51:22.551897+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.548 | 101.04 | +0.76% | 1.15x | STRONG 95/100 | HIGH 62/100 | Watch |
| 2 | ETH/USD ⭐ | 1660.05 | 88.67 | +0.22% | 3.35x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XMR/USD | 469.93 | 85.18 | -0.55% | 2.64x | STRONG 73/100 | HIGH 61/100 | Watch |
| 4 | USELESS/USD | 0.07736 | 71.18 | -0.17% | 2.10x | MODERATE 61/100 | HIGH 67/100 | Watch |
| 5 | ZEC/USD ⭐ | 768.16 | 70.41 | +0.27% | 1.77x | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 6 | SOL/USD | 69.02 | 63.97 | +0.01% | 1.65x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 7 | TRX/USD | 0.302654 | 63.50 | +0.03% | 1.62x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 8 | ZAMA/USD | 0.05849 | 59.25 | -0.19% | 19.98x | MODERATE 60/100 | VERY_HIGH 73/100 | Watch |
| 9 | SENT/USD | 0.021046 | 56.33 | +0.18% | 2.19x | STRONG 73/100 | HIGH 67/100 | Watch |
| 10 | TAO/USD | 182.2083 | 55.59 | +0.32% | 0.61x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 11 | AKT/USD | 0.5087 | 54.91 | +1.73% | 45.55x | STRONG 77/100 | HIGH 66/100 | Watch |
| 12 | AAVE/USD | 99.15 | 53.15 | -0.69% | 1.50x | MODERATE 47/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD ⭐ | 1660.77 | 91.25 | +0.22% | 3.35x | 99906 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 22.543 | 87.86 | +0.76% | 1.15x | 14402 | STRONG 84/100 | HIGH 68/100 | Watch |
| 3 | ZEC/USD ⭐ | 766.68 | 61.96 | +0.27% | 1.77x | 57253 | STRONG 86/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** VVV/USD, ETH/USD, ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
