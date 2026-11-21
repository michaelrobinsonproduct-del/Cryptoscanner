# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T14:20:53.613913+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44913337750
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 22fa90759c084231f2b43e2a1f48be68e2026acc (atomic ledger/results publication)
**Ledger generation:** 1144 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.833 | 91.185 | 96.730 | +10.10% | -1.35% | 1.12x | 6.5 | 2026-11-21T14:20:46.885434+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 2 | UNI/USD | 4.695 | 82.241 | 88.459 | +5.10% | -0.31% | 0.53x | 4.5 | 2026-11-21T14:20:46.885434+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | ETH/USD | 1688.12 | 74.606 | 84.711 | +4.25% | -1.03% | 0.50x | 0.1 | 2026-11-21T14:20:46.885434+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 4 | XMR/USD | 471.62 | 72.133 | 76.397 | +3.36% | -0.43% | 0.79x | 4.2 | 2026-11-21T14:20:46.885434+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 5 | ZEC/USD | 788.73 | 70.201 | 81.754 | +4.07% | -1.44% | 0.57x | 3.4 | 2026-11-21T14:20:46.885434+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 6 | SOL/USD | 70.43 | 69.020 | 71.103 | +2.50% | -0.42% | 1.00x | 2.8 | 2026-11-21T14:20:46.885434+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 7 | XRP/USD | 0.92711 | 66.113 | 68.581 | +2.02% | -0.27% | 0.89x | 1.2 | 2026-11-21T14:20:46.885434+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XBT/USD | 60161.1 | 63.564 | 70.253 | +2.30% | -0.60% | 0.63x | 1.7 | 2026-11-21T14:20:46.885434+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | USELESS/USD | 0.0805 | 63.412 | 75.087 | +8.05% | -0.73% | 0.20x | 21.1 | 2026-11-21T14:20:46.885434+00:00 | Not calibrated | WEAK 27/100 | EXTREME 88/100 | Do nothing | WATCH |
| 10 | TAO/USD | 186.4723 | 63.115 | 73.639 | +3.30% | -0.77% | 0.33x | 9.0 | 2026-11-21T14:20:46.885434+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | BNB/USD | 545.19 | 59.534 | 57.393 | +1.03% | -0.63% | 1.53x | 2.0 | 2026-11-21T14:20:46.885434+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 12 | NEAR/USD | 2.9009 | 56.913 | 66.400 | +2.05% | -0.41% | 0.25x | 5.9 | 2026-11-21T14:20:46.885434+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 96.730 | 22.833 | -1.35% | 1.12x |
| 2 | UNI/USD | 88.459 | 4.695 | -0.31% | 0.53x |
| 3 | ETH/USD | 84.711 | 1688.12 | -1.03% | 0.50x |
| 4 | ZEC/USD | 81.754 | 788.73 | -1.44% | 0.57x |
| 5 | XMR/USD | 76.397 | 471.62 | -0.43% | 0.79x |
| 6 | USELESS/USD | 75.087 | 0.0805 | -0.73% | 0.20x |
| 7 | TAO/USD | 73.639 | 186.4723 | -0.77% | 0.33x |
| 8 | SOL/USD | 71.103 | 70.43 | -0.42% | 1.00x |
| 9 | XBT/USD | 70.253 | 60161.1 | -0.60% | 0.63x |
| 10 | XRP/USD | 68.581 | 0.92711 | -0.27% | 0.89x |
| 11 | NEAR/USD | 66.400 | 2.9009 | -0.41% | 0.25x |
| 12 | BNB/USD | 57.393 | 545.19 | -0.63% | 1.53x |

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

- Persisted scans: 1144; predictions: 9037; observations: 691911.
- Matured sampled outcomes across 1/6/24/48h: 11872; gap abstentions: 20491. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44913337750 · **Generation:** 1144 · **Legacy run:** 44913337750
**Main quote time:** 2026-11-21T14:20:53.613913+00:00 · **Legacy report time:** 2026-11-21T14:22:07.968120+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.833 | 91.19 | -1.35% | 1.12x | MODERATE 56/100 | VERY_HIGH 72/100 | Do nothing |
| 2 | UNI/USD | 4.695 | 82.24 | -0.31% | 0.53x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 3 | ETH/USD | 1688.12 | 74.61 | -1.03% | 0.50x | WEAK 42/100 | VERY_HIGH 80/100 | Watch |
| 4 | XMR/USD | 471.62 | 72.13 | -0.43% | 0.79x | WEAK 41/100 | HIGH 68/100 | Watch |
| 5 | ZEC/USD | 788.73 | 70.20 | -1.44% | 0.57x | WEAK 40/100 | VERY_HIGH 80/100 | Do nothing |
| 6 | SOL/USD | 70.43 | 69.02 | -0.42% | 1.00x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 7 | XRP/USD | 0.92711 | 66.11 | -0.27% | 0.89x | WEAK 38/100 | HIGH 68/100 | Watch |
| 8 | XBT/USD | 60161.1 | 63.56 | -0.60% | 0.63x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 9 | USELESS/USD | 0.0805 | 63.41 | -0.73% | 0.20x | WEAK 27/100 | EXTREME 88/100 | Do nothing |
| 10 | TAO/USD | 186.4723 | 63.12 | -0.77% | 0.33x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 11 | BNB/USD | 545.19 | 59.53 | -0.63% | 1.53x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 12 | NEAR/USD | 2.9009 | 56.91 | -0.41% | 0.25x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD | 0.5243 | 73.38 | +0.19% | 1.19x | 5191 | MODERATE 62/100 | HIGH 67/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
