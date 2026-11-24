# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T01:22:01.726418+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45304198869
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 5822835a2c334e6f96d0507eb238c1e0dda91b56 (atomic ledger/results publication)
**Ledger generation:** 1506 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XLM/USD | 0.132076 | 77.323 | 65.113 | +1.60% | +0.37% | 2.04x | 2.2 | 2026-11-24T01:21:55.293476+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | HYPE/USD | 64.27 | 73.965 | 61.151 | +0.99% | +0.09% | 2.23x | 1.6 | 2026-11-24T01:21:55.293476+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 3 | VVV/USD | 24.896 | 73.487 | 63.407 | +1.83% | -0.20% | 2.11x | 8.8 | 2026-11-24T01:21:55.293476+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ZEC/USD | 786.73 | 70.007 | 63.686 | +1.50% | +0.59% | 1.34x | 3.6 | 2026-11-24T01:21:55.293476+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.0128 | 69.451 | 60.927 | +1.06% | +0.60% | 1.55x | 3.0 | 2026-11-24T01:21:55.293476+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 6 | ETH/USD | 1718.39 | 64.963 | 58.652 | +0.60% | +0.12% | 1.57x | 1.0 | 2026-11-24T01:21:55.293476+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 7 | HBAR/USD | 0.05299 | 62.439 | 45.162 | +1.03% | +0.46% | 3.21x | 1.9 | 2026-11-24T01:21:55.293476+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 8 | LTC/USD | 41.89 | 62.384 | 61.749 | +1.13% | +0.50% | 0.81x | 2.4 | 2026-11-24T01:21:55.293476+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 9 | XRP/USD | 0.95113 | 61.508 | 63.380 | +1.25% | +0.45% | 0.59x | 0.7 | 2026-11-24T01:21:55.293476+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SOL/USD | 72.5 | 58.408 | 59.857 | +0.79% | +0.11% | 0.80x | 1.4 | 2026-11-24T01:21:55.293476+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XDG/USD | 0.057038 | 58.282 | 63.857 | +1.30% | +0.33% | 0.28x | 0.5 | 2026-11-24T01:21:55.293476+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XBT/USD | 61495.2 | 57.961 | 58.376 | +0.48% | +0.14% | 0.89x | 0.0 | 2026-11-24T01:21:55.293476+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XLM/USD | 65.113 | 0.132076 | +0.37% | 2.04x |
| 2 | XDG/USD | 63.857 | 0.057038 | +0.33% | 0.28x |
| 3 | ZEC/USD | 63.686 | 786.73 | +0.59% | 1.34x |
| 4 | VVV/USD | 63.407 | 24.896 | -0.20% | 2.11x |
| 5 | XRP/USD | 63.380 | 0.95113 | +0.45% | 0.59x |
| 6 | LTC/USD | 61.749 | 41.89 | +0.50% | 0.81x |
| 7 | HYPE/USD | 61.151 | 64.27 | +0.09% | 2.23x |
| 8 | NEAR/USD | 60.927 | 3.0128 | +0.60% | 1.55x |
| 9 | SOL/USD | 59.857 | 72.5 | +0.11% | 0.80x |
| 10 | ETH/USD | 58.652 | 1718.39 | +0.12% | 1.57x |
| 11 | XBT/USD | 58.376 | 61495.2 | +0.14% | 0.89x |
| 12 | HBAR/USD | 45.162 | 0.05299 | +0.46% | 3.21x |

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

- Persisted scans: 1506; predictions: 12829; observations: 912255.
- Matured sampled outcomes across 1/6/24/48h: 23631; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 133 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45304198869 · **Generation:** 1506 · **Legacy run:** 45304198869
**Main quote time:** 2026-11-24T01:22:01.726418+00:00 · **Legacy report time:** 2026-11-24T01:23:12.224475+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD ⭐ | 0.132076 | 77.32 | +0.37% | 2.04x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HYPE/USD ⭐ | 64.27 | 73.96 | +0.09% | 2.23x | STRONG 92/100 | HIGH 55/100 | Watch |
| 3 | VVV/USD | 24.896 | 73.49 | -0.20% | 2.11x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 4 | ZEC/USD ⭐ | 786.73 | 70.01 | +0.59% | 1.34x | STRONG 90/100 | HIGH 55/100 | Watch |
| 5 | NEAR/USD ⭐ | 3.0128 | 69.45 | +0.60% | 1.55x | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 6 | ETH/USD ⭐ | 1718.39 | 64.96 | +0.12% | 1.57x | STRONG 77/100 | HIGH 55/100 | Watch |
| 7 | HBAR/USD | 0.05299 | 62.44 | +0.46% | 3.21x | STRONG 86/100 | HIGH 55/100 | Watch |
| 8 | LTC/USD | 41.89 | 62.38 | +0.50% | 0.81x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 9 | XRP/USD | 0.95113 | 61.51 | +0.45% | 0.59x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 10 | SOL/USD | 72.5 | 58.41 | +0.11% | 0.80x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 11 | XDG/USD | 0.057038 | 58.28 | +0.33% | 0.28x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 12 | XBT/USD | 61495.2 | 57.96 | +0.14% | 0.89x | MODERATE 49/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BLESS/USD | 0.014684 | 86.96 | +3.97% | 2.12x | 5384 | STRONG 83/100 | EXTREME 87/100 | Do nothing |
| 2 | XLM/USD ⭐ | 0.132172 | 72.51 | +0.37% | 2.04x | 18139 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NIGHT/USD | 0.04885 | 70.57 | +0.85% | 2.46x | 12021 | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 4 | HYPE/USD ⭐ | 64.32 | 66.93 | +0.09% | 2.23x | 30180 | STRONG 88/100 | HIGH 55/100 | Watch |
| 5 | ZEC/USD ⭐ | 788.15 | 66.11 | +0.59% | 1.34x | 40177 | STRONG 88/100 | HIGH 55/100 | Watch |
| 6 | AAVE/USD | 99.04 | 65.94 | +0.47% | 1.20x | 6265 | MODERATE 68/100 | HIGH 62/100 | Watch |
| 7 | ETH/USD ⭐ | 1719.13 | 62.20 | +0.12% | 1.57x | 57148 | STRONG 76/100 | HIGH 55/100 | Watch |
| 8 | NEAR/USD ⭐ | 3.0212 | 62.16 | +0.60% | 1.55x | 20633 | STRONG 86/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XLM/USD, HYPE/USD, ZEC/USD, NEAR/USD, ETH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
