# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T12:01:51.970434+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45994920131
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** fe29b1df62c61c0aab87b50686c6a20cce0bf903 (atomic ledger/results publication)
**Ledger generation:** 2005 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 65.77 | 102.976 | 94.179 | +5.71% | +0.05% | 1.86x | 1.5 | 2026-11-27T12:01:44.257563+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 2 | ZEC/USD | 752.6 | 90.149 | 97.807 | +10.41% | -0.04% | 0.25x | 4.4 | 2026-11-27T12:01:44.257563+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | ADA/USD | 0.152921 | 87.233 | 71.621 | +3.00% | +0.12% | 2.70x | 3.4 | 2026-11-27T12:01:44.257563+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.628e-06 | 76.471 | 72.806 | +4.31% | +0.33% | 1.20x | 2.8 | 2026-11-27T12:01:44.257563+00:00 | Not calibrated | STRONG 73/100 | HIGH 62/100 | Watch | WATCH |
| 5 | PAXG/USD | 3656.82 | 75.595 | 60.560 | +2.81% | +0.01% | 2.64x | 1.2 | 2026-11-27T12:01:44.257563+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XRP/USD | 0.97347 | 74.867 | 77.502 | +3.26% | -0.10% | 0.79x | 0.6 | 2026-11-27T12:01:44.257563+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0587573 | 71.851 | 75.493 | +4.23% | -0.02% | 0.65x | 2.1 | 2026-11-27T12:01:44.257563+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | XBT/USD | 61519.3 | 71.028 | 66.809 | +1.69% | -0.04% | 1.44x | 0.0 | 2026-11-27T12:01:44.257563+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 9 | UNI/USD | 4.8971 | 70.947 | 79.924 | +5.31% | -0.20% | 0.20x | 4.3 | 2026-11-27T12:01:44.257563+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6875 | 67.796 | 75.030 | +2.97% | -0.10% | 0.33x | 1.5 | 2026-11-27T12:01:44.257563+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | ETH/USD | 1719.33 | 67.143 | 68.098 | +1.88% | -0.17% | 0.99x | 0.1 | 2026-11-27T12:01:44.257563+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 12 | LINK/USD | 9.51527 | 66.369 | 71.560 | +2.66% | -0.15% | 0.56x | 4.2 | 2026-11-27T12:01:44.257563+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.807 | 752.6 | -0.04% | 0.25x |
| 2 | HYPE/USD | 94.179 | 65.77 | +0.05% | 1.86x |
| 3 | UNI/USD | 79.924 | 4.8971 | -0.20% | 0.20x |
| 4 | XRP/USD | 77.502 | 0.97347 | -0.10% | 0.79x |
| 5 | XDG/USD | 75.493 | 0.0587573 | -0.02% | 0.65x |
| 6 | SUI/USD | 75.030 | 0.6875 | -0.10% | 0.33x |
| 7 | PEPE/USD | 72.806 | 3.628e-06 | +0.33% | 1.20x |
| 8 | ADA/USD | 71.621 | 0.152921 | +0.12% | 2.70x |
| 9 | LINK/USD | 71.560 | 9.51527 | -0.15% | 0.56x |
| 10 | ETH/USD | 68.098 | 1719.33 | -0.17% | 0.99x |
| 11 | XBT/USD | 66.809 | 61519.3 | -0.04% | 1.44x |
| 12 | PAXG/USD | 60.560 | 3656.82 | +0.01% | 2.64x |

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

- Persisted scans: 2005; predictions: 17762; observations: 1214164.
- Matured sampled outcomes across 1/6/24/48h: 39497; gap abstentions: 25819. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45994920131 · **Generation:** 2005 · **Legacy run:** 45994920131
**Main quote time:** 2026-11-27T12:01:51.970434+00:00 · **Legacy report time:** 2026-11-27T12:02:34.470253+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 65.77 | 102.98 | +0.05% | 1.86x | STRONG 85/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD | 752.6 | 90.15 | -0.04% | 0.25x | MODERATE 50/100 | VERY_HIGH 76/100 | Watch |
| 3 | ADA/USD ⭐ | 0.152921 | 87.23 | +0.12% | 2.70x | STRONG 99/100 | HIGH 55/100 | Watch |
| 4 | PEPE/USD ⭐ | 3.628e-06 | 76.47 | +0.33% | 1.20x | STRONG 83/100 | HIGH 62/100 | Watch |
| 5 | PAXG/USD | 3656.82 | 75.59 | +0.01% | 2.64x | STRONG 83/100 | HIGH 55/100 | Watch |
| 6 | XRP/USD | 0.97347 | 74.87 | -0.10% | 0.79x | WEAK 42/100 | HIGH 68/100 | Watch |
| 7 | XDG/USD | 0.0587573 | 71.85 | -0.02% | 0.65x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 8 | XBT/USD | 61519.3 | 71.03 | -0.04% | 1.44x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 9 | UNI/USD | 4.8971 | 70.95 | -0.20% | 0.20x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 10 | SUI/USD | 0.6875 | 67.80 | -0.10% | 0.33x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 11 | ETH/USD | 1719.33 | 67.14 | -0.17% | 0.99x | WEAK 39/100 | HIGH 68/100 | Watch |
| 12 | LINK/USD | 9.51527 | 66.37 | -0.15% | 0.56x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD ⭐ | 3.628e-06 | 89.69 | +0.33% | 1.20x | 5770 | STRONG 90/100 | HIGH 62/100 | Watch |
| 2 | ADA/USD ⭐ | 0.153103 | 89.45 | +0.12% | 2.70x | 9436 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | PUMP/USD | 0.002684 | 89.19 | +0.19% | 38.82x | 3975 | STRONG 90/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ADA/USD, PEPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
