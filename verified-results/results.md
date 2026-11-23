# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T14:41:41.995033+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45196569650
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 50d47cd168cb70628e31f36d26b83ac18a135263 (atomic ledger/results publication)
**Ledger generation:** 1443 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INJ/USD | 6.975 | 105.666 | 90.353 | +11.99% | +1.38% | 1.84x | 7.2 | 2026-11-23T14:41:35.329339+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | HYPE/USD | 68.12 | 105.134 | 99.266 | +8.02% | -0.45% | 1.81x | 1.5 | 2026-11-23T14:41:35.329339+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | SOL/USD | 76.93 | 101.337 | 99.350 | +8.92% | -0.13% | 1.26x | 1.3 | 2026-11-23T14:41:35.329339+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 4 | NEAR/USD | 3.2112 | 98.274 | 97.666 | +7.70% | -0.36% | 1.24x | 4.7 | 2026-11-23T14:41:35.329339+00:00 | Not calibrated | MODERATE 59/100 | HIGH 68/100 | Watch | WATCH |
| 5 | XRP/USD | 0.99898 | 98.179 | 97.346 | +7.70% | -1.06% | 1.61x | 5.3 | 2026-11-23T14:41:35.329339+00:00 | Not calibrated | MODERATE 69/100 | HIGH 65/100 | Watch | WATCH |
| 6 | SUI/USD | 0.7194 | 96.841 | 97.914 | +9.71% | -0.28% | 1.03x | 4.2 | 2026-11-23T14:41:35.329339+00:00 | Not calibrated | MODERATE 58/100 | HIGH 68/100 | Watch | WATCH |
| 7 | ZEC/USD | 872.99 | 95.127 | 95.475 | +9.46% | -0.79% | 1.36x | 9.0 | 2026-11-23T14:41:35.329339+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 8 | LINK/USD | 9.38788 | 93.861 | 89.728 | +6.55% | -0.20% | 1.51x | 8.2 | 2026-11-23T14:41:35.329339+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 9 | XLM/USD | 0.13536 | 91.566 | 94.303 | +6.14% | -0.78% | 1.12x | 7.4 | 2026-11-23T14:41:35.329339+00:00 | Not calibrated | MODERATE 56/100 | HIGH 68/100 | Watch | WATCH |
| 10 | ADA/USD | 0.154181 | 90.151 | 95.231 | +6.62% | -0.08% | 0.53x | 9.5 | 2026-11-23T14:41:35.329339+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0592283 | 89.880 | 96.823 | +7.13% | -0.17% | 0.39x | 6.4 | 2026-11-23T14:41:35.329339+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | LTC/USD | 43.06 | 88.880 | 92.097 | +7.22% | +0.07% | 0.64x | 4.6 | 2026-11-23T14:41:35.329339+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SOL/USD | 99.350 | 76.93 | -0.13% | 1.26x |
| 2 | HYPE/USD | 99.266 | 68.12 | -0.45% | 1.81x |
| 3 | SUI/USD | 97.914 | 0.7194 | -0.28% | 1.03x |
| 4 | NEAR/USD | 97.666 | 3.2112 | -0.36% | 1.24x |
| 5 | XRP/USD | 97.346 | 0.99898 | -1.06% | 1.61x |
| 6 | XDG/USD | 96.823 | 0.0592283 | -0.17% | 0.39x |
| 7 | ZEC/USD | 95.475 | 872.99 | -0.79% | 1.36x |
| 8 | ADA/USD | 95.231 | 0.154181 | -0.08% | 0.53x |
| 9 | XLM/USD | 94.303 | 0.13536 | -0.78% | 1.12x |
| 10 | LTC/USD | 92.097 | 43.06 | +0.07% | 0.64x |
| 11 | INJ/USD | 90.353 | 6.975 | +1.38% | 1.84x |
| 12 | LINK/USD | 89.728 | 9.38788 | -0.20% | 1.51x |

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

- Persisted scans: 1443; predictions: 12083; observations: 873889.
- Matured sampled outcomes across 1/6/24/48h: 20572; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45196569650 · **Generation:** 1443 · **Legacy run:** 45196569650
**Main quote time:** 2026-11-23T14:41:41.995033+00:00 · **Legacy report time:** 2026-11-23T14:42:48.592033+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 6.975 | 105.67 | +1.38% | 1.84x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HYPE/USD | 68.12 | 105.13 | -0.45% | 1.81x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | SOL/USD | 76.93 | 101.34 | -0.13% | 1.26x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 4 | NEAR/USD | 3.2112 | 98.27 | -0.36% | 1.24x | MODERATE 59/100 | HIGH 68/100 | Watch |
| 5 | XRP/USD | 0.99898 | 98.18 | -1.06% | 1.61x | MODERATE 69/100 | HIGH 65/100 | Watch |
| 6 | SUI/USD | 0.7194 | 96.84 | -0.28% | 1.03x | MODERATE 58/100 | HIGH 68/100 | Watch |
| 7 | ZEC/USD | 872.99 | 95.13 | -0.79% | 1.36x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 8 | LINK/USD | 9.38788 | 93.86 | -0.20% | 1.51x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 9 | XLM/USD | 0.13536 | 91.57 | -0.78% | 1.12x | MODERATE 56/100 | HIGH 68/100 | Watch |
| 10 | ADA/USD | 0.154181 | 90.15 | -0.08% | 0.53x | MODERATE 50/100 | VERY_HIGH 76/100 | Watch |
| 11 | XDG/USD | 0.0592283 | 89.88 | -0.17% | 0.39x | MODERATE 50/100 | VERY_HIGH 76/100 | Watch |
| 12 | LTC/USD | 43.06 | 88.88 | +0.07% | 0.64x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 6.977 | 92.41 | +1.38% | 1.84x | 6828 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** INJ/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
