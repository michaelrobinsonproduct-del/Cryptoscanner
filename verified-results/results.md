# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T11:22:48.955954+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45989533561
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 80e3de30c4f1c94937cddc7721d5450680bdf50f (atomic ledger/results publication)
**Ledger generation:** 2000 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 757.94 | 106.710 | 97.759 | +11.19% | +0.14% | 1.83x | 4.5 | 2026-11-27T11:22:40.695333+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 2 | SUI/USD | 0.6882 | 90.038 | 75.038 | +3.07% | +0.00% | 5.14x | 2.9 | 2026-11-27T11:22:40.695333+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 3 | HYPE/USD | 66.06 | 88.325 | 96.687 | +6.17% | +0.20% | 0.07x | 3.0 | 2026-11-27T11:22:40.695333+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | XRP/USD | 0.97947 | 79.989 | 81.959 | +3.90% | +0.15% | 0.73x | 0.6 | 2026-11-27T11:22:40.695333+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | SOL/USD | 73.23 | 78.677 | 76.914 | +3.23% | +0.12% | 1.11x | 1.4 | 2026-11-27T11:22:40.695333+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 6 | PEPE/USD | 3.648e-06 | 76.497 | 75.500 | +4.89% | +0.17% | 1.02x | 5.5 | 2026-11-27T11:22:40.695333+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 7 | ETH/USD | 1726.18 | 72.143 | 70.940 | +2.28% | +0.03% | 1.10x | 0.1 | 2026-11-27T11:22:40.695333+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 8 | NIGHT/USD | 0.04952 | 71.480 | 58.669 | +2.17% | -0.44% | 8.56x | 2.0 | 2026-11-27T11:22:40.695333+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 9 | XDG/USD | 0.0586405 | 70.915 | 74.296 | +4.02% | +0.38% | 0.47x | 2.2 | 2026-11-27T11:22:40.695333+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XBT/USD | 61620.3 | 70.298 | 67.978 | +1.86% | +0.14% | 1.16x | 0.0 | 2026-11-27T11:22:40.695333+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 11 | LTC/USD | 44.71 | 70.185 | 68.872 | +2.22% | +0.27% | 1.00x | 2.2 | 2026-11-27T11:22:40.695333+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 12 | VVV/USD | 27.14 | 68.201 | 73.392 | +3.65% | -0.19% | 0.58x | 8.5 | 2026-11-27T11:22:40.695333+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.759 | 757.94 | +0.14% | 1.83x |
| 2 | HYPE/USD | 96.687 | 66.06 | +0.20% | 0.07x |
| 3 | XRP/USD | 81.959 | 0.97947 | +0.15% | 0.73x |
| 4 | SOL/USD | 76.914 | 73.23 | +0.12% | 1.11x |
| 5 | PEPE/USD | 75.500 | 3.648e-06 | +0.17% | 1.02x |
| 6 | SUI/USD | 75.038 | 0.6882 | +0.00% | 5.14x |
| 7 | XDG/USD | 74.296 | 0.0586405 | +0.38% | 0.47x |
| 8 | VVV/USD | 73.392 | 27.14 | -0.19% | 0.58x |
| 9 | ETH/USD | 70.940 | 1726.18 | +0.03% | 1.10x |
| 10 | LTC/USD | 68.872 | 44.71 | +0.27% | 1.00x |
| 11 | XBT/USD | 67.978 | 61620.3 | +0.14% | 1.16x |
| 12 | NIGHT/USD | 58.669 | 0.04952 | -0.44% | 8.56x |

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

- Persisted scans: 2000; predictions: 17702; observations: 1211149.
- Matured sampled outcomes across 1/6/24/48h: 39353; gap abstentions: 25803. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45989533561 · **Generation:** 2000 · **Legacy run:** 45989533561
**Main quote time:** 2026-11-27T11:22:48.955954+00:00 · **Legacy report time:** 2026-11-27T11:23:28.267916+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 757.94 | 106.71 | +0.14% | 1.83x | STRONG 95/100 | HIGH 55/100 | Watch |
| 2 | SUI/USD | 0.6882 | 90.04 | +0.00% | 5.14x | STRONG 90/100 | HIGH 55/100 | Watch |
| 3 | HYPE/USD | 66.06 | 88.32 | +0.20% | 0.07x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 4 | XRP/USD | 0.97947 | 79.99 | +0.15% | 0.73x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 5 | SOL/USD ⭐ | 73.23 | 78.68 | +0.12% | 1.11x | STRONG 74/100 | HIGH 62/100 | Watch |
| 6 | PEPE/USD ⭐ | 3.648e-06 | 76.50 | +0.17% | 1.02x | STRONG 73/100 | HIGH 62/100 | Watch |
| 7 | ETH/USD | 1726.18 | 72.14 | +0.03% | 1.10x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 8 | NIGHT/USD | 0.04952 | 71.48 | -0.44% | 8.56x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 9 | XDG/USD | 0.0586405 | 70.92 | +0.38% | 0.47x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 10 | XBT/USD ⭐ | 61620.3 | 70.30 | +0.14% | 1.16x | STRONG 70/100 | HIGH 62/100 | Watch |
| 11 | LTC/USD | 44.71 | 70.19 | +0.27% | 1.00x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 12 | VVV/USD | 27.14 | 68.20 | -0.19% | 0.58x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 758.98 | 98.45 | +0.14% | 1.83x | 40209 | STRONG 94/100 | HIGH 55/100 | Watch |
| 2 | SOL/USD ⭐ | 73.26 | 89.34 | +0.12% | 1.11x | 33738 | STRONG 80/100 | HIGH 62/100 | Watch |
| 3 | PEPE/USD ⭐ | 3.648e-06 | 88.49 | +0.17% | 1.02x | 5734 | STRONG 79/100 | HIGH 62/100 | Watch |
| 4 | ADA/USD | 0.152897 | 81.25 | +0.29% | 1.74x | 9450 | STRONG 86/100 | HIGH 55/100 | Consider small entry |
| 5 | XBT/USD ⭐ | 61646 | 75.80 | +0.14% | 1.16x | 137263 | STRONG 73/100 | HIGH 62/100 | Watch |

**Same-run overlap:** ZEC/USD, SOL/USD, PEPE/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
