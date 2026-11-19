# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T06:00:20.513008+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44468927107
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 5fa567224d78e2a070eea804544d0a35ac96bda5 (atomic ledger/results publication)
**Ledger generation:** 771 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 938.86 | 90.885 | 74.432 | +2.95% | +0.29% | 3.21x | 2.4 | 2026-11-19T06:00:14.031416+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 22.68 | 86.474 | 84.651 | +4.66% | +0.29% | 1.04x | 4.9 | 2026-11-19T06:00:14.031416+00:00 | Not calibrated | STRONG 78/100 | HIGH 62/100 | Watch | WATCH |
| 3 | TAO/USD | 195.3126 | 80.793 | 64.090 | +1.75% | +0.34% | 2.95x | 6.3 | 2026-11-19T06:00:14.031416+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | NEAR/USD | 3.3789 | 66.245 | 69.785 | +2.47% | +0.17% | 0.56x | 5.0 | 2026-11-19T06:00:14.031416+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | SOL/USD | 74.59 | 64.270 | 64.324 | +1.43% | +0.11% | 0.94x | 1.3 | 2026-11-19T06:00:14.031416+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |
| 6 | TRX/USD | 0.312188 | 64.176 | 48.210 | +0.94% | +0.19% | 68.33x | 0.0 | 2026-11-19T06:00:14.031416+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 7 | ETH/USD | 1798.55 | 61.433 | 64.355 | +1.34% | +0.02% | 0.70x | 0.1 | 2026-11-19T06:00:14.031416+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | HYPE/USD | 67.97 | 61.021 | 64.937 | +1.63% | +0.28% | 0.47x | 2.9 | 2026-11-19T06:00:14.031416+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XBT/USD | 63295.5 | 54.265 | 58.449 | +0.49% | +0.04% | 0.56x | 0.0 | 2026-11-19T06:00:14.031416+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XRP/USD | 0.9728 | 52.234 | 59.606 | +0.67% | +0.06% | 0.23x | 0.1 | 2026-11-19T06:00:14.031416+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0590881 | 48.469 | 54.073 | +0.65% | +0.07% | 0.40x | 0.0 | 2026-11-19T06:00:14.031416+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | DOT/USD | 0.7205 | 46.712 | 30.808 | +0.25% | +0.18% | 4.71x | 6.9 | 2026-11-19T06:00:14.031416+00:00 | Not calibrated | MODERATE 68/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 84.651 | 22.68 | +0.29% | 1.04x |
| 2 | ZEC/USD | 74.432 | 938.86 | +0.29% | 3.21x |
| 3 | NEAR/USD | 69.785 | 3.3789 | +0.17% | 0.56x |
| 4 | HYPE/USD | 64.937 | 67.97 | +0.28% | 0.47x |
| 5 | ETH/USD | 64.355 | 1798.55 | +0.02% | 0.70x |
| 6 | SOL/USD | 64.324 | 74.59 | +0.11% | 0.94x |
| 7 | TAO/USD | 64.090 | 195.3126 | +0.34% | 2.95x |
| 8 | XRP/USD | 59.606 | 0.9728 | +0.06% | 0.23x |
| 9 | XBT/USD | 58.449 | 63295.5 | +0.04% | 0.56x |
| 10 | XDG/USD | 54.073 | 0.0590881 | +0.07% | 0.40x |
| 11 | TRX/USD | 48.210 | 0.312188 | +0.19% | 68.33x |
| 12 | DOT/USD | 30.808 | 0.7205 | +0.18% | 4.71x |

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

- Persisted scans: 771; predictions: 6396; observations: 466545.
- Matured sampled outcomes across 1/6/24/48h: 6427; gap abstentions: 13803. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44468927107 · **Generation:** 771 · **Legacy run:** 44468927107
**Main quote time:** 2026-11-19T06:00:20.513008+00:00 · **Legacy report time:** 2026-11-19T06:01:00.832354+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 938.86 | 90.88 | +0.29% | 3.21x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 22.68 | 86.47 | +0.29% | 1.04x | STRONG 88/100 | HIGH 62/100 | Watch |
| 3 | TAO/USD | 195.3126 | 80.79 | +0.34% | 2.95x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 4 | NEAR/USD | 3.3789 | 66.25 | +0.17% | 0.56x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 5 | SOL/USD | 74.59 | 64.27 | +0.11% | 0.94x | MODERATE 52/100 | HIGH 62/100 | Watch |
| 6 | TRX/USD | 0.312188 | 64.18 | +0.19% | 68.33x | STRONG 77/100 | HIGH 55/100 | Watch |
| 7 | ETH/USD | 1798.55 | 61.43 | +0.02% | 0.70x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 8 | HYPE/USD | 67.97 | 61.02 | +0.28% | 0.47x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 9 | XBT/USD | 63295.5 | 54.27 | +0.04% | 0.56x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 10 | XRP/USD | 0.9728 | 52.23 | +0.06% | 0.23x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 11 | XDG/USD | 0.0590881 | 48.47 | +0.07% | 0.40x | WEAK 44/100 | VERY_HIGH 70/100 | Watch |
| 12 | DOT/USD | 0.7205 | 46.71 | +0.18% | 4.71x | MODERATE 68/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 940.29 | 90.30 | +0.29% | 3.21x | 22277 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 22.708 | 85.64 | +0.29% | 1.04x | 9698 | STRONG 83/100 | HIGH 68/100 | Watch |
| 3 | AKT/USD | 0.5382 | 71.21 | +0.17% | 1.24x | 3479 | MODERATE 56/100 | VERY_HIGH 80/100 | Watch |

**Same-run overlap:** ZEC/USD, VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
