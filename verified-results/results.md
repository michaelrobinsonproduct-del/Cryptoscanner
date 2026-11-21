# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T15:40:46.195943+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44920351287
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 89cb0b349444eac53d602f969487828749d592cd (atomic ledger/results publication)
**Ledger generation:** 1152 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.997 | 103.501 | 95.657 | +10.89% | -0.64% | 2.11x | 8.7 | 2026-11-21T15:40:37.923548+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ZEC/USD | 788.73 | 96.261 | 83.402 | +4.07% | -0.43% | 2.71x | 0.1 | 2026-11-21T15:40:37.923548+00:00 | Not calibrated | STRONG 78/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ETH/USD | 1678.48 | 88.544 | 80.544 | +3.65% | -0.45% | 2.02x | 0.1 | 2026-11-21T15:40:37.923548+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 4 | TAO/USD | 187.521 | 87.737 | 79.088 | +3.88% | -0.44% | 2.09x | 6.2 | 2026-11-21T15:40:37.923548+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 5 | BEAM/USD | 0.003596 | 85.704 | 67.062 | +9.70% | +0.73% | 3.37x | 19.5 | 2026-11-21T15:40:37.923548+00:00 | Not calibrated | STRONG 93/100 | HIGH 66/100 | Consider small entry | WATCH |
| 6 | UNI/USD | 4.7008 | 83.238 | 88.415 | +5.23% | +0.01% | 0.48x | 6.4 | 2026-11-21T15:40:37.923548+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | XBT/USD | 59756.3 | 78.177 | 66.299 | +1.62% | -0.62% | 3.52x | 0.0 | 2026-11-21T15:40:37.923548+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XMR/USD | 474.21 | 76.712 | 78.797 | +3.93% | +0.45% | 0.57x | 7.4 | 2026-11-21T15:40:37.923548+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | NIGHT/USD | 0.04288 | 71.855 | 56.388 | +1.56% | +0.09% | 3.35x | 2.3 | 2026-11-21T15:40:37.923548+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 10 | PAXG/USD | 3543.51 | 71.779 | 56.701 | +0.34% | +0.02% | 2.98x | 1.4 | 2026-11-21T15:40:37.923548+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 11 | XRP/USD | 0.92216 | 71.151 | 64.548 | +1.48% | -0.35% | 1.83x | 1.6 | 2026-11-21T15:40:37.923548+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 12 | SOL/USD | 70.33 | 65.712 | 70.793 | +2.36% | -0.28% | 0.63x | 1.4 | 2026-11-21T15:40:37.923548+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 95.657 | 22.997 | -0.64% | 2.11x |
| 2 | UNI/USD | 88.415 | 4.7008 | +0.01% | 0.48x |
| 3 | ZEC/USD | 83.402 | 788.73 | -0.43% | 2.71x |
| 4 | ETH/USD | 80.544 | 1678.48 | -0.45% | 2.02x |
| 5 | TAO/USD | 79.088 | 187.521 | -0.44% | 2.09x |
| 6 | XMR/USD | 78.797 | 474.21 | +0.45% | 0.57x |
| 7 | SOL/USD | 70.793 | 70.33 | -0.28% | 0.63x |
| 8 | BEAM/USD | 67.062 | 0.003596 | +0.73% | 3.37x |
| 9 | XBT/USD | 66.299 | 59756.3 | -0.62% | 3.52x |
| 10 | XRP/USD | 64.548 | 0.92216 | -0.35% | 1.83x |
| 11 | PAXG/USD | 56.701 | 3543.51 | +0.02% | 2.98x |
| 12 | NIGHT/USD | 56.388 | 0.04288 | +0.09% | 3.35x |

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

- Persisted scans: 1152; predictions: 9133; observations: 696775.
- Matured sampled outcomes across 1/6/24/48h: 12007; gap abstentions: 20684. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44920351287 · **Generation:** 1152 · **Legacy run:** 44920351287
**Main quote time:** 2026-11-21T15:40:46.195943+00:00 · **Legacy report time:** 2026-11-21T15:41:31.658193+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.997 | 103.50 | -0.64% | 2.11x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | ZEC/USD | 788.73 | 96.26 | -0.43% | 2.71x | STRONG 78/100 | HIGH 61/100 | Watch |
| 3 | ETH/USD | 1678.48 | 88.54 | -0.45% | 2.02x | STRONG 74/100 | HIGH 61/100 | Watch |
| 4 | TAO/USD | 187.521 | 87.74 | -0.44% | 2.09x | STRONG 74/100 | HIGH 61/100 | Watch |
| 5 | BEAM/USD | 0.003596 | 85.70 | +0.73% | 3.37x | STRONG 93/100 | HIGH 66/100 | Consider small entry |
| 6 | UNI/USD | 4.7008 | 83.24 | +0.01% | 0.48x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 7 | XBT/USD | 59756.3 | 78.18 | -0.62% | 3.52x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 8 | XMR/USD | 474.21 | 76.71 | +0.45% | 0.57x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 9 | NIGHT/USD | 0.04288 | 71.86 | +0.09% | 3.35x | STRONG 81/100 | HIGH 55/100 | Watch |
| 10 | PAXG/USD | 3543.51 | 71.78 | +0.02% | 2.98x | STRONG 81/100 | HIGH 55/100 | Watch |
| 11 | XRP/USD | 0.92216 | 71.15 | -0.35% | 1.83x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 12 | SOL/USD | 70.33 | 65.71 | -0.28% | 0.63x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD | 0.07665 | 76.00 | +0.13% | 1.35x | 6700 | STRONG 73/100 | HIGH 55/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
