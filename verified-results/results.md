# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T20:31:08.163366+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44946547283
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** a68e711ed919795c886c4284abca8498d08d591b (atomic ledger/results publication)
**Ledger generation:** 1182 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.0453 | 102.767 | 88.318 | +7.30% | -0.11% | 2.79x | 11.1 | 2026-11-21T20:30:59.362586+00:00 | Not calibrated | STRONG 75/100 | HIGH 67/100 | Watch | WATCH |
| 2 | XMR/USD | 486.64 | 93.526 | 96.814 | +6.65% | -0.08% | 0.71x | 6.4 | 2026-11-21T20:30:59.362586+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | ZEC/USD | 792.25 | 85.475 | 85.138 | +4.53% | +0.30% | 0.89x | 3.2 | 2026-11-21T20:30:59.362586+00:00 | Not calibrated | STRONG 73/100 | HIGH 62/100 | Watch | WATCH |
| 4 | UNI/USD | 4.6999 | 83.013 | 89.547 | +5.21% | +0.10% | 0.30x | 3.8 | 2026-11-21T20:30:59.362586+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | ETH/USD | 1683.28 | 78.020 | 82.619 | +3.95% | +0.05% | 0.52x | 0.1 | 2026-11-21T20:30:59.362586+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XLM/USD | 0.129539 | 75.031 | 67.094 | +1.84% | +0.16% | 1.71x | 1.5 | 2026-11-21T20:30:59.362586+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SOL/USD | 70.48 | 71.913 | 72.323 | +2.58% | +0.20% | 0.86x | 1.4 | 2026-11-21T20:30:59.362586+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0551398 | 71.085 | 65.736 | +1.59% | +0.12% | 1.48x | 0.8 | 2026-11-21T20:30:59.362586+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 9 | PAXG/USD | 3554.56 | 69.133 | 53.730 | +0.65% | +0.08% | 2.75x | 0.7 | 2026-11-21T20:30:59.362586+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 10 | XBT/USD | 60325.6 | 67.945 | 73.076 | +2.58% | +0.21% | 0.38x | 0.0 | 2026-11-21T20:30:59.362586+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | TAO/USD | 184.8638 | 66.912 | 69.715 | +2.41% | +0.08% | 0.68x | 4.4 | 2026-11-21T20:30:59.362586+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XRP/USD | 0.934 | 65.637 | 74.107 | +2.78% | +0.02% | 0.14x | 0.7 | 2026-11-21T20:30:59.362586+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 96.814 | 486.64 | -0.08% | 0.71x |
| 2 | UNI/USD | 89.547 | 4.6999 | +0.10% | 0.30x |
| 3 | NIGHT/USD | 88.318 | 0.0453 | -0.11% | 2.79x |
| 4 | ZEC/USD | 85.138 | 792.25 | +0.30% | 0.89x |
| 5 | ETH/USD | 82.619 | 1683.28 | +0.05% | 0.52x |
| 6 | XRP/USD | 74.107 | 0.934 | +0.02% | 0.14x |
| 7 | XBT/USD | 73.076 | 60325.6 | +0.21% | 0.38x |
| 8 | SOL/USD | 72.323 | 70.48 | +0.20% | 0.86x |
| 9 | TAO/USD | 69.715 | 184.8638 | +0.08% | 0.68x |
| 10 | XLM/USD | 67.094 | 0.129539 | +0.16% | 1.71x |
| 11 | XDG/USD | 65.736 | 0.0551398 | +0.12% | 1.48x |
| 12 | PAXG/USD | 53.730 | 3554.56 | +0.08% | 2.75x |

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

- Persisted scans: 1182; predictions: 9493; observations: 715015.
- Matured sampled outcomes across 1/6/24/48h: 12628; gap abstentions: 21334. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44946547283 · **Generation:** 1182 · **Legacy run:** 44946547283
**Main quote time:** 2026-11-21T20:31:08.163366+00:00 · **Legacy report time:** 2026-11-21T20:32:12.098267+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.0453 | 102.77 | -0.11% | 2.79x | STRONG 75/100 | HIGH 67/100 | Watch |
| 2 | XMR/USD | 486.64 | 93.53 | -0.08% | 0.71x | MODERATE 52/100 | VERY_HIGH 76/100 | Watch |
| 3 | ZEC/USD | 792.25 | 85.47 | +0.30% | 0.89x | STRONG 73/100 | HIGH 62/100 | Watch |
| 4 | UNI/USD | 4.6999 | 83.01 | +0.10% | 0.30x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 5 | ETH/USD | 1683.28 | 78.02 | +0.05% | 0.52x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 6 | XLM/USD | 0.129539 | 75.03 | +0.16% | 1.71x | STRONG 73/100 | HIGH 55/100 | Watch |
| 7 | SOL/USD | 70.48 | 71.91 | +0.20% | 0.86x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 8 | XDG/USD ⭐ | 0.0551398 | 71.08 | +0.12% | 1.48x | STRONG 81/100 | HIGH 55/100 | Watch |
| 9 | PAXG/USD | 3554.56 | 69.13 | +0.08% | 2.75x | STRONG 80/100 | HIGH 55/100 | Watch |
| 10 | XBT/USD | 60325.6 | 67.94 | +0.21% | 0.38x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 11 | TAO/USD | 184.8638 | 66.91 | +0.08% | 0.68x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 12 | XRP/USD | 0.934 | 65.64 | +0.02% | 0.14x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD | 1.9113 | 87.05 | +1.54% | 1.80x | 12236 | STRONG 79/100 | HIGH 67/100 | Consider small entry |
| 2 | AVAX/USD | 6.624 | 74.60 | +0.18% | 2.28x | 6525 | STRONG 82/100 | HIGH 55/100 | Watch |
| 3 | XDG/USD ⭐ | 0.0551636 | 72.96 | +0.12% | 1.48x | 15366 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XDG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
