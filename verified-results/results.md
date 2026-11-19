# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T13:45:32.027681+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44536472342
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 56f11d581a2945c72ff65272f024bd133fd8b816 (atomic ledger/results publication)
**Ledger generation:** 785 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 593; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.949 | 108.779 | 92.578 | +5.90% | +0.24% | 4.22x | 7.4 | 2026-11-19T13:45:24.184056+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 946 | 86.530 | 79.179 | +3.73% | +0.15% | 1.66x | 3.9 | 2026-11-19T13:45:24.184056+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 3 | NEAR/USD | 3.3947 | 84.249 | 73.740 | +2.95% | -0.43% | 2.27x | 3.8 | 2026-11-19T13:45:24.184056+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ETH/USD | 1804.24 | 82.099 | 66.600 | +1.66% | +0.10% | 2.57x | 0.1 | 2026-11-19T13:45:24.184056+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 5 | TAO/USD | 198.2893 | 74.441 | 76.163 | +3.30% | -0.03% | 0.84x | 3.8 | 2026-11-19T13:45:24.184056+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 6 | AKT/USD | 0.5532 | 72.493 | 72.923 | +6.80% | +0.04% | 0.94x | 7.2 | 2026-11-19T13:45:24.184056+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 7 | PEPE/USD | 3.961e-06 | 68.304 | 75.643 | +5.74% | +0.05% | 0.24x | 10.1 | 2026-11-19T13:45:24.184056+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | XRP/USD | 0.98906 | 65.738 | 71.082 | +2.35% | +0.23% | 0.35x | 0.7 | 2026-11-19T13:45:24.184056+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | LIGHTER/USD | 2.949 | 65.677 | 72.527 | +8.66% | +0.07% | 0.28x | 17.0 | 2026-11-19T13:45:24.184056+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | HYPE/USD | 68.66 | 63.005 | 72.173 | +2.66% | -0.09% | 0.13x | 2.9 | 2026-11-19T13:45:24.184056+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XLM/USD | 0.137937 | 58.557 | 58.760 | +0.54% | +0.01% | 0.98x | 0.1 | 2026-11-19T13:45:24.184056+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XBT/USD | 63653.6 | 56.025 | 62.428 | +1.06% | +0.04% | 0.34x | 0.0 | 2026-11-19T13:45:24.184056+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 92.578 | 22.949 | +0.24% | 4.22x |
| 2 | ZEC/USD | 79.179 | 946 | +0.15% | 1.66x |
| 3 | TAO/USD | 76.163 | 198.2893 | -0.03% | 0.84x |
| 4 | PEPE/USD | 75.643 | 3.961e-06 | +0.05% | 0.24x |
| 5 | NEAR/USD | 73.740 | 3.3947 | -0.43% | 2.27x |
| 6 | AKT/USD | 72.923 | 0.5532 | +0.04% | 0.94x |
| 7 | LIGHTER/USD | 72.527 | 2.949 | +0.07% | 0.28x |
| 8 | HYPE/USD | 72.173 | 68.66 | -0.09% | 0.13x |
| 9 | XRP/USD | 71.082 | 0.98906 | +0.23% | 0.35x |
| 10 | ETH/USD | 66.600 | 1804.24 | +0.10% | 2.57x |
| 11 | XBT/USD | 62.428 | 63653.6 | +0.04% | 0.34x |
| 12 | XLM/USD | 58.760 | 0.137937 | +0.01% | 0.98x |

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

- Persisted scans: 785; predictions: 6564; observations: 474923.
- Matured sampled outcomes across 1/6/24/48h: 6671; gap abstentions: 14994. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44536472342 · **Generation:** 785 · **Legacy run:** 44536472342
**Main quote time:** 2026-11-19T13:45:32.027681+00:00 · **Legacy report time:** 2026-11-19T13:46:25.265459+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.949 | 108.78 | +0.24% | 4.22x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 946 | 86.53 | +0.15% | 1.66x | STRONG 88/100 | HIGH 55/100 | Watch |
| 3 | NEAR/USD | 3.3947 | 84.25 | -0.43% | 2.27x | STRONG 72/100 | HIGH 61/100 | Watch |
| 4 | ETH/USD ⭐ | 1804.24 | 82.10 | +0.10% | 2.57x | STRONG 96/100 | HIGH 55/100 | Watch |
| 5 | TAO/USD | 198.2893 | 74.44 | -0.03% | 0.84x | WEAK 42/100 | HIGH 68/100 | Watch |
| 6 | AKT/USD | 0.5532 | 72.49 | +0.04% | 0.94x | MODERATE 56/100 | VERY_HIGH 74/100 | Watch |
| 7 | PEPE/USD | 3.961e-06 | 68.30 | +0.05% | 0.24x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |
| 8 | XRP/USD | 0.98906 | 65.74 | +0.23% | 0.35x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 9 | LIGHTER/USD | 2.949 | 65.68 | +0.07% | 0.28x | MODERATE 48/100 | VERY_HIGH 81/100 | Watch |
| 10 | HYPE/USD | 68.66 | 63.01 | -0.09% | 0.13x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 11 | XLM/USD | 0.137937 | 58.56 | +0.01% | 0.98x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 12 | XBT/USD | 63653.6 | 56.03 | +0.04% | 0.34x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 23 | 93.72 | +0.24% | 4.22x | 11936 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 945.92 | 92.59 | +0.15% | 1.66x | 21091 | STRONG 91/100 | HIGH 55/100 | Watch |
| 3 | ETH/USD ⭐ | 1804.41 | 78.53 | +0.10% | 2.57x | 56249 | STRONG 94/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD, ZEC/USD, ETH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
