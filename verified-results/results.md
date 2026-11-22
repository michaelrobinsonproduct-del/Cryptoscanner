# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T14:11:16.196286+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45031279871
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** e5349590509f85e28c660894f5c49940717355bc (atomic ledger/results publication)
**Ledger generation:** 1293 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.606 | 88.516 | 69.577 | +2.84% | +0.79% | 3.37x | 10.5 | 2026-11-22T14:11:08.329918+00:00 | Not calibrated | STRONG 94/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | NEAR/USD | 3.0364 | 85.993 | 89.426 | +5.20% | +0.63% | 0.34x | 4.0 | 2026-11-22T14:11:08.329918+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | TAO/USD | 191.136 | 83.212 | 68.704 | +2.91% | -0.10% | 2.91x | 3.3 | 2026-11-22T14:11:08.329918+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04894 | 83.195 | 85.082 | +10.52% | -0.67% | 1.15x | 12.3 | 2026-11-22T14:11:08.329918+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 5 | LINK/USD | 8.7944 | 77.795 | 60.944 | +2.32% | +0.37% | 3.02x | 2.5 | 2026-11-22T14:11:08.329918+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | HYPE/USD | 62.78 | 77.673 | 71.009 | +2.51% | +0.37% | 1.48x | 3.2 | 2026-11-22T14:11:08.329918+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 7 | ETH/USD | 1704.56 | 77.546 | 64.241 | +1.32% | +0.11% | 2.28x | 0.1 | 2026-11-22T14:11:08.329918+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 8 | MNT/USD | 0.3982 | 67.022 | 73.228 | +7.51% | +0.15% | 0.30x | 5.0 | 2026-11-22T14:11:08.329918+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 9 | ZEC/USD | 794 | 66.203 | 68.169 | +2.03% | +0.15% | 0.73x | 2.1 | 2026-11-22T14:11:08.329918+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6584 | 66.107 | 66.244 | +1.71% | +0.12% | 0.93x | 1.5 | 2026-11-22T14:11:08.329918+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XBT/USD | 60670.3 | 62.401 | 61.753 | +0.97% | +0.02% | 1.05x | 0.0 | 2026-11-22T14:11:08.329918+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 12 | BNB/USD | 555.8 | 47.960 | 47.605 | +1.53% | +0.27% | 0.90x | 1.8 | 2026-11-22T14:11:08.329918+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 89.426 | 3.0364 | +0.63% | 0.34x |
| 2 | NIGHT/USD | 85.082 | 0.04894 | -0.67% | 1.15x |
| 3 | MNT/USD | 73.228 | 0.3982 | +0.15% | 0.30x |
| 4 | HYPE/USD | 71.009 | 62.78 | +0.37% | 1.48x |
| 5 | VVV/USD | 69.577 | 25.606 | +0.79% | 3.37x |
| 6 | TAO/USD | 68.704 | 191.136 | -0.10% | 2.91x |
| 7 | ZEC/USD | 68.169 | 794 | +0.15% | 0.73x |
| 8 | SUI/USD | 66.244 | 0.6584 | +0.12% | 0.93x |
| 9 | ETH/USD | 64.241 | 1704.56 | +0.11% | 2.28x |
| 10 | XBT/USD | 61.753 | 60670.3 | +0.02% | 1.05x |
| 11 | LINK/USD | 60.944 | 8.7944 | +0.37% | 3.02x |
| 12 | BNB/USD | 47.605 | 555.8 | +0.27% | 0.90x |

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

- Persisted scans: 1293; predictions: 10435; observations: 782546.
- Matured sampled outcomes across 1/6/24/48h: 15183; gap abstentions: 22272. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 60 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45031279871 · **Generation:** 1293 · **Legacy run:** 45031279871
**Main quote time:** 2026-11-22T14:11:16.196286+00:00 · **Legacy report time:** 2026-11-22T14:12:09.928677+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.606 | 88.52 | +0.79% | 3.37x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | NEAR/USD | 3.0364 | 85.99 | +0.63% | 0.34x | STRONG 73/100 | VERY_HIGH 70/100 | Watch |
| 3 | TAO/USD | 191.136 | 83.21 | -0.10% | 2.91x | STRONG 72/100 | HIGH 61/100 | Watch |
| 4 | NIGHT/USD | 0.04894 | 83.19 | -0.67% | 1.15x | MODERATE 47/100 | VERY_HIGH 74/100 | Watch |
| 5 | LINK/USD | 8.7944 | 77.80 | +0.37% | 3.02x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 6 | HYPE/USD ⭐ | 62.78 | 77.67 | +0.37% | 1.48x | STRONG 94/100 | HIGH 55/100 | Watch |
| 7 | ETH/USD | 1704.56 | 77.55 | +0.11% | 2.28x | STRONG 84/100 | HIGH 55/100 | Watch |
| 8 | MNT/USD | 0.3982 | 67.02 | +0.15% | 0.30x | MODERATE 54/100 | VERY_HIGH 82/100 | Watch |
| 9 | ZEC/USD | 794 | 66.20 | +0.15% | 0.73x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 10 | SUI/USD | 0.6584 | 66.11 | +0.12% | 0.93x | MODERATE 53/100 | HIGH 62/100 | Watch |
| 11 | XBT/USD | 60670.3 | 62.40 | +0.02% | 1.05x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 12 | BNB/USD | 555.8 | 47.96 | +0.27% | 0.90x | MODERATE 54/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.38308 | 93.78 | +5.21% | 3.04x | 15844 | STRONG 97/100 | VERY_HIGH 71/100 | Watch |
| 2 | VVV/USD ⭐ | 25.606 | 81.39 | +0.79% | 3.37x | 13527 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | HYPE/USD ⭐ | 62.74 | 78.05 | +0.37% | 1.48x | 11710 | STRONG 94/100 | HIGH 55/100 | Watch |
| 4 | ZBCN/USD | 0.001924 | 76.28 | +0.73% | 1.50x | 4682 | STRONG 73/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** VVV/USD, HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
