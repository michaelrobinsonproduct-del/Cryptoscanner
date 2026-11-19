# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T03:35:17.700374+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44452393374
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 784d730cc8dbd1207fb68e5f66018595de295644 (atomic ledger/results publication)
**Ledger generation:** 744 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.022567 | 88.952 | 73.557 | +9.52% | +1.55% | 1.77x | 6.2 | 2026-11-19T03:35:11.058861+00:00 | Not calibrated | STRONG 89/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | NEAR/USD | 3.3675 | 84.820 | 67.209 | +2.13% | +0.97% | 2.27x | 5.3 | 2026-11-19T03:35:11.058861+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | LUNA/USD | 4.811e-05 | 83.187 | 76.722 | +10.50% | +0.25% | 1.52x | 2.1 | 2026-11-19T03:35:11.058861+00:00 | Not calibrated | STRONG 87/100 | HIGH 60/100 | Consider small entry | WATCH |
| 4 | SOL/USD | 73.74 | 64.496 | 55.547 | +0.27% | +0.92% | 1.44x | 2.7 | 2026-11-19T03:35:11.058861+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 5 | ICP/USD | 2.26 | 61.084 | 57.852 | +3.76% | +1.07% | 0.79x | 13.3 | 2026-11-19T03:35:11.058861+00:00 | Not calibrated | MODERATE 56/100 | HIGH 68/100 | Watch | WATCH |
| 6 | VVV/USD | 22.037 | 58.578 | 57.334 | +1.69% | +0.78% | 0.73x | 7.7 | 2026-11-19T03:35:11.058861+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | ETH/USD | 1780.69 | 56.579 | 57.142 | +0.33% | +0.72% | 0.58x | 0.4 | 2026-11-19T03:35:11.058861+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | ONDO/USD | 0.29869 | 55.636 | 33.868 | +0.35% | +1.35% | 12.33x | 6.7 | 2026-11-19T03:35:11.058861+00:00 | Not calibrated | STRONG 83/100 | HIGH 60/100 | Watch | WATCH |
| 9 | CC/USD | 0.08229 | 54.413 | 36.479 | +0.50% | +0.65% | 2.47x | 4.9 | 2026-11-19T03:35:11.058861+00:00 | Not calibrated | STRONG 82/100 | HIGH 60/100 | Watch | WATCH |
| 10 | LTC/USD | 44.28 | 49.897 | 48.348 | +0.61% | +0.80% | 0.76x | 4.5 | 2026-11-19T03:35:11.058861+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 11 | TRX/USD | 0.310147 | 43.153 | 41.875 | +0.28% | +0.11% | 1.07x | 0.8 | 2026-11-19T03:35:11.058861+00:00 | Not calibrated | MODERATE 47/100 | HIGH 62/100 | Watch | WATCH |
| 12 | WLD/USD | 0.2612 | 28.502 | 30.409 | +0.31% | +0.85% | 0.38x | 7.7 | 2026-11-19T03:35:11.058861+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LUNA/USD | 76.722 | 4.811e-05 | +0.25% | 1.52x |
| 2 | SENT/USD | 73.557 | 0.022567 | +1.55% | 1.77x |
| 3 | NEAR/USD | 67.209 | 3.3675 | +0.97% | 2.27x |
| 4 | ICP/USD | 57.852 | 2.26 | +1.07% | 0.79x |
| 5 | VVV/USD | 57.334 | 22.037 | +0.78% | 0.73x |
| 6 | ETH/USD | 57.142 | 1780.69 | +0.72% | 0.58x |
| 7 | SOL/USD | 55.547 | 73.74 | +0.92% | 1.44x |
| 8 | LTC/USD | 48.348 | 44.28 | +0.80% | 0.76x |
| 9 | TRX/USD | 41.875 | 0.310147 | +0.11% | 1.07x |
| 10 | CC/USD | 36.479 | 0.08229 | +0.65% | 2.47x |
| 11 | ONDO/USD | 33.868 | 0.29869 | +1.35% | 12.33x |
| 12 | WLD/USD | 30.409 | 0.2612 | +0.85% | 0.38x |

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

- Persisted scans: 744; predictions: 6075; observations: 450103.
- Matured sampled outcomes across 1/6/24/48h: 6034; gap abstentions: 13551. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44452393374 · **Generation:** 744 · **Legacy run:** 44452393374
**Main quote time:** 2026-11-19T03:35:17.700374+00:00 · **Legacy report time:** 2026-11-19T03:35:55.586862+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.022567 | 88.95 | +1.55% | 1.77x | STRONG 99/100 | HIGH 67/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 3.3675 | 84.82 | +0.97% | 2.27x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | LUNA/USD ⭐ | 4.811e-05 | 83.19 | +0.25% | 1.52x | STRONG 97/100 | HIGH 60/100 | Consider small entry |
| 4 | SOL/USD ⭐ | 73.74 | 64.50 | +0.92% | 1.44x | STRONG 87/100 | HIGH 55/100 | Watch |
| 5 | ICP/USD | 2.26 | 61.08 | +1.07% | 0.79x | MODERATE 56/100 | HIGH 68/100 | Watch |
| 6 | VVV/USD | 22.037 | 58.58 | +0.78% | 0.73x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 7 | ETH/USD | 1780.69 | 56.58 | +0.72% | 0.58x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 8 | ONDO/USD | 0.29869 | 55.64 | +1.35% | 12.33x | STRONG 83/100 | HIGH 60/100 | Watch |
| 9 | CC/USD | 0.08229 | 54.41 | +0.65% | 2.47x | STRONG 82/100 | HIGH 60/100 | Watch |
| 10 | LTC/USD | 44.28 | 49.90 | +0.80% | 0.76x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 11 | TRX/USD | 0.310147 | 43.15 | +0.11% | 1.07x | MODERATE 47/100 | HIGH 62/100 | Watch |
| 12 | WLD/USD | 0.2612 | 28.50 | +0.85% | 0.38x | WEAK 44/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.3685 | 81.14 | +0.97% | 2.27x | 13672 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SENT/USD ⭐ | 0.022496 | 78.70 | +1.55% | 1.77x | 8220 | STRONG 84/100 | VERY_HIGH 79/100 | Watch |
| 3 | LUNA/USD ⭐ | 4.811e-05 | 72.61 | +0.25% | 1.52x | 2414 | STRONG 86/100 | HIGH 66/100 | Consider small entry |
| 4 | SOL/USD ⭐ | 73.7 | 56.40 | +0.92% | 1.44x | 35154 | STRONG 83/100 | HIGH 55/100 | Watch |

**Same-run overlap:** SENT/USD, NEAR/USD, LUNA/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
