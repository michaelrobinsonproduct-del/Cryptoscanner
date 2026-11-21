# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T13:50:54.594884+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44910785062
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 10d694c72293db8b826997f9bde2c29f73908520 (atomic ledger/results publication)
**Ledger generation:** 1141 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ETH/USD | 1703.61 | 111.797 | 90.028 | +5.21% | +1.35% | 3.73x | 2.8 | 2026-11-21T13:50:48.574928+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 795.47 | 109.850 | 89.627 | +4.96% | +1.89% | 2.08x | 0.1 | 2026-11-21T13:50:48.574928+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | UNI/USD | 4.7289 | 104.047 | 91.560 | +5.86% | +1.24% | 1.63x | 8.9 | 2026-11-21T13:50:48.574928+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | TAO/USD | 187.9092 | 102.147 | 80.471 | +4.10% | +1.34% | 3.42x | 6.5 | 2026-11-21T13:50:48.574928+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | USELESS/USD | 0.08016 | 101.276 | 73.670 | +7.60% | +2.52% | 10.86x | 23.7 | 2026-11-21T13:50:48.574928+00:00 | Not calibrated | STRONG 95/100 | HIGH 67/100 | Consider small entry | WATCH |
| 6 | XBT/USD | 60573.7 | 97.909 | 76.029 | +3.01% | +1.38% | 3.07x | 0.0 | 2026-11-21T13:50:48.574928+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | SOL/USD | 70.68 | 96.034 | 74.362 | +2.87% | +1.33% | 4.08x | 1.4 | 2026-11-21T13:50:48.574928+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | XRP/USD | 0.9299 | 93.109 | 70.624 | +2.33% | +1.50% | 9.53x | 1.4 | 2026-11-21T13:50:48.574928+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | AVAX/USD | 6.654 | 89.142 | 68.671 | +2.27% | +1.09% | 3.87x | 4.5 | 2026-11-21T13:50:48.574928+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 10 | NEAR/USD | 2.9094 | 88.574 | 70.222 | +2.35% | +1.93% | 1.87x | 2.4 | 2026-11-21T13:50:48.574928+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Consider small entry | WATCH |
| 11 | LINK/USD | 8.65007 | 84.182 | 64.871 | +1.41% | +0.86% | 9.65x | 0.0 | 2026-11-21T13:50:48.574928+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 12 | TRX/USD | 0.305879 | 83.070 | 64.504 | +1.45% | +0.71% | 6.65x | 1.3 | 2026-11-21T13:50:48.574928+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UNI/USD | 91.560 | 4.7289 | +1.24% | 1.63x |
| 2 | ETH/USD | 90.028 | 1703.61 | +1.35% | 3.73x |
| 3 | ZEC/USD | 89.627 | 795.47 | +1.89% | 2.08x |
| 4 | TAO/USD | 80.471 | 187.9092 | +1.34% | 3.42x |
| 5 | XBT/USD | 76.029 | 60573.7 | +1.38% | 3.07x |
| 6 | SOL/USD | 74.362 | 70.68 | +1.33% | 4.08x |
| 7 | USELESS/USD | 73.670 | 0.08016 | +2.52% | 10.86x |
| 8 | XRP/USD | 70.624 | 0.9299 | +1.50% | 9.53x |
| 9 | NEAR/USD | 70.222 | 2.9094 | +1.93% | 1.87x |
| 10 | AVAX/USD | 68.671 | 6.654 | +1.09% | 3.87x |
| 11 | LINK/USD | 64.871 | 8.65007 | +0.86% | 9.65x |
| 12 | TRX/USD | 64.504 | 0.305879 | +0.71% | 6.65x |

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

- Persisted scans: 1141; predictions: 9001; observations: 690087.
- Matured sampled outcomes across 1/6/24/48h: 11807; gap abstentions: 20420. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44910785062 · **Generation:** 1141 · **Legacy run:** 44910785062
**Main quote time:** 2026-11-21T13:50:54.594884+00:00 · **Legacy report time:** 2026-11-21T13:51:58.909959+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD ⭐ | 1703.61 | 111.80 | +1.35% | 3.73x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 795.47 | 109.85 | +1.89% | 2.08x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | UNI/USD ⭐ | 4.7289 | 104.05 | +1.24% | 1.63x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | TAO/USD ⭐ | 187.9092 | 102.15 | +1.34% | 3.42x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | USELESS/USD ⭐ | 0.08016 | 101.28 | +2.52% | 10.86x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 6 | XBT/USD ⭐ | 60573.7 | 97.91 | +1.38% | 3.07x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | SOL/USD ⭐ | 70.68 | 96.03 | +1.33% | 4.08x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | XRP/USD ⭐ | 0.9299 | 93.11 | +1.50% | 9.53x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | AVAX/USD | 6.654 | 89.14 | +1.09% | 3.87x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 10 | NEAR/USD ⭐ | 2.9094 | 88.57 | +1.93% | 1.87x | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 11 | LINK/USD | 8.65007 | 84.18 | +0.86% | 9.65x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 12 | TRX/USD | 0.305879 | 83.07 | +0.71% | 6.65x | STRONG 97/100 | HIGH 55/100 | Consider small entry |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD ⭐ | 1704.01 | 100.00 | +1.35% | 3.73x | 101387 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | TAO/USD ⭐ | 188.2526 | 100.00 | +1.34% | 3.42x | 16497 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SOL/USD ⭐ | 70.79 | 97.50 | +1.33% | 4.08x | 58081 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | XBT/USD ⭐ | 60641 | 95.86 | +1.38% | 3.07x | 278246 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | ZEC/USD ⭐ | 798.08 | 95.68 | +1.89% | 2.08x | 57160 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | VVV/USD | 23.162 | 95.68 | +2.89% | 1.67x | 15010 | STRONG 88/100 | HIGH 61/100 | Consider small entry |
| 7 | UNI/USD ⭐ | 4.7241 | 93.53 | +1.24% | 1.63x | 13380 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | USELESS/USD ⭐ | 0.08016 | 91.86 | +2.52% | 10.86x | 5065 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 9 | XRP/USD ⭐ | 0.93103 | 91.39 | +1.50% | 9.53x | 68749 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 10 | AAVE/USD | 101.15 | 86.87 | +0.60% | 3.97x | 8514 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 11 | NEAR/USD ⭐ | 2.9118 | 82.20 | +1.93% | 1.87x | 29459 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 12 | XMR/USD | 472.02 | 80.56 | +0.32% | 1.30x | 12325 | STRONG 80/100 | HIGH 61/100 | Watch |

**Same-run overlap:** ETH/USD, ZEC/USD, UNI/USD, TAO/USD, USELESS/USD, XBT/USD, SOL/USD, XRP/USD, NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
