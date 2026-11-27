# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T22:32:40.496448+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46076948955
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2792fe3717b0a01b1a74e7d989c2eff83072ccc9 (atomic ledger/results publication)
**Ledger generation:** 2069 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 728.08 | 104.827 | 99.382 | +6.81% | +0.38% | 1.35x | 1.2 | 2026-11-27T22:32:32.449217+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.05005 | 88.069 | 76.820 | +3.26% | +0.58% | 1.83x | 2.0 | 2026-11-27T22:32:32.449217+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | HYPE/USD | 63.7 | 86.653 | 70.865 | +2.38% | +0.16% | 40.57x | 1.6 | 2026-11-27T22:32:32.449217+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 4 | LIGHTER/USD | 2.624 | 78.135 | 65.796 | +5.72% | -0.08% | 2.27x | 15.2 | 2026-11-27T22:32:32.449217+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | SOL/USD | 71.55 | 75.741 | 60.321 | +0.86% | +0.08% | 2.65x | 1.4 | 2026-11-27T22:32:32.449217+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 6 | UNI/USD | 4.8177 | 74.487 | 75.747 | +3.60% | +0.21% | 0.77x | 2.3 | 2026-11-27T22:32:32.449217+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6702 | 71.877 | 56.129 | +0.37% | +0.15% | 9.23x | 3.0 | 2026-11-27T22:32:32.449217+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 8 | XAUT/USD | 3650.7 | 70.806 | 55.710 | +2.56% | +0.02% | 5.59x | 0.3 | 2026-11-27T22:32:32.449217+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 9 | XDG/USD | 0.0573537 | 70.611 | 66.077 | +1.74% | +0.26% | 1.33x | 2.2 | 2026-11-27T22:32:32.449217+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 10 | TAO/USD | 186.3189 | 70.493 | 62.004 | +1.38% | +0.36% | 1.67x | 5.3 | 2026-11-27T22:32:32.449217+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Consider small entry | WATCH |
| 11 | LTC/USD | 44.34 | 62.879 | 62.247 | +1.37% | +0.36% | 0.88x | 4.5 | 2026-11-27T22:32:32.449217+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 12 | PAXG/USD | 3647.04 | 61.069 | 61.640 | +2.54% | +0.03% | 0.93x | 0.5 | 2026-11-27T22:32:32.449217+00:00 | Not calibrated | MODERATE 51/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 99.382 | 728.08 | +0.38% | 1.35x |
| 2 | NIGHT/USD | 76.820 | 0.05005 | +0.58% | 1.83x |
| 3 | UNI/USD | 75.747 | 4.8177 | +0.21% | 0.77x |
| 4 | HYPE/USD | 70.865 | 63.7 | +0.16% | 40.57x |
| 5 | XDG/USD | 66.077 | 0.0573537 | +0.26% | 1.33x |
| 6 | LIGHTER/USD | 65.796 | 2.624 | -0.08% | 2.27x |
| 7 | LTC/USD | 62.247 | 44.34 | +0.36% | 0.88x |
| 8 | TAO/USD | 62.004 | 186.3189 | +0.36% | 1.67x |
| 9 | PAXG/USD | 61.640 | 3647.04 | +0.03% | 0.93x |
| 10 | SOL/USD | 60.321 | 71.55 | +0.08% | 2.65x |
| 11 | SUI/USD | 56.129 | 0.6702 | +0.15% | 9.23x |
| 12 | XAUT/USD | 55.710 | 3650.7 | +0.02% | 5.59x |

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

- Persisted scans: 2069; predictions: 18530; observations: 1252862.
- Matured sampled outcomes across 1/6/24/48h: 42191; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 154 (sampled only; not a success-rate estimate).
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

**Writer:** 46076948955 · **Generation:** 2069 · **Legacy run:** 46076948955
**Main quote time:** 2026-11-27T22:32:40.496448+00:00 · **Legacy report time:** 2026-11-27T22:33:22.536748+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 728.08 | 104.83 | +0.38% | 1.35x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.05005 | 88.07 | +0.58% | 1.83x | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 3 | HYPE/USD ⭐ | 63.7 | 86.65 | +0.16% | 40.57x | STRONG 98/100 | HIGH 55/100 | Watch |
| 4 | LIGHTER/USD | 2.624 | 78.14 | -0.08% | 2.27x | MODERATE 64/100 | VERY_HIGH 72/100 | Watch |
| 5 | SOL/USD | 71.55 | 75.74 | +0.08% | 2.65x | STRONG 83/100 | HIGH 55/100 | Watch |
| 6 | UNI/USD | 4.8177 | 74.49 | +0.21% | 0.77x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 7 | SUI/USD | 0.6702 | 71.88 | +0.15% | 9.23x | STRONG 81/100 | HIGH 55/100 | Watch |
| 8 | XAUT/USD | 3650.7 | 70.81 | +0.02% | 5.59x | STRONG 80/100 | HIGH 55/100 | Watch |
| 9 | XDG/USD ⭐ | 0.0573537 | 70.61 | +0.26% | 1.33x | STRONG 90/100 | HIGH 55/100 | Watch |
| 10 | TAO/USD | 186.3189 | 70.49 | +0.36% | 1.67x | STRONG 80/100 | HIGH 55/100 | Consider small entry |
| 11 | LTC/USD | 44.34 | 62.88 | +0.36% | 0.88x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 12 | PAXG/USD | 3647.04 | 61.07 | +0.03% | 0.93x | MODERATE 51/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 727.84 | 100.00 | +0.38% | 1.35x | 37865 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.05007 | 92.70 | +0.58% | 1.83x | 19286 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | HYPE/USD ⭐ | 63.67 | 85.29 | +0.16% | 40.57x | 19129 | STRONG 98/100 | HIGH 55/100 | Watch |
| 4 | ENA/USD | 0.1037 | 76.80 | +0.49% | 4.98x | 2813 | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 5 | XDG/USD ⭐ | 0.0573625 | 74.30 | +0.26% | 1.33x | 13313 | STRONG 92/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD, NIGHT/USD, HYPE/USD, XDG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
