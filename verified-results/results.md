# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T01:21:18.887002+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45921918410
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** babbc8f280fe76cdd2642b756f51aed44beebdb9 (atomic ledger/results publication)
**Ledger generation:** 1939 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 705.25 | 96.477 | 77.664 | +3.46% | +0.76% | 3.14x | 3.1 | 2026-11-27T01:21:10.398144+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | LTC/USD | 44.13 | 75.562 | 60.108 | +0.89% | +0.09% | 3.16x | 2.3 | 2026-11-27T01:21:10.398144+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 3 | LINK/USD | 9.34313 | 73.452 | 59.245 | +0.81% | -0.16% | 4.16x | 2.8 | 2026-11-27T01:21:10.398144+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XBT/USD | 60687.5 | 63.307 | 57.184 | +0.31% | +0.02% | 1.60x | 0.0 | 2026-11-27T01:21:10.398144+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 5 | ETH/USD | 1699.28 | 61.759 | 59.782 | +0.69% | -0.07% | 1.23x | 0.1 | 2026-11-27T01:21:10.398144+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 6 | SUI/USD | 0.6724 | 60.401 | 52.825 | +0.70% | +0.34% | 1.59x | 1.5 | 2026-11-27T01:21:10.398144+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 7 | HYPE/USD | 62.85 | 57.264 | 61.292 | +1.01% | -0.16% | 0.68x | 1.6 | 2026-11-27T01:21:10.398144+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | AVAX/USD | 6.637 | 56.795 | 40.965 | +0.64% | +0.17% | 10.01x | 3.0 | 2026-11-27T01:21:10.398144+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 9 | NEAR/USD | 3.0715 | 55.111 | 58.631 | +0.77% | -0.27% | 0.78x | 3.6 | 2026-11-27T01:21:10.398144+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 10 | XMR/USD | 464.9 | 54.179 | 61.771 | +1.74% | -0.38% | 0.43x | 10.8 | 2026-11-27T01:21:10.398144+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 11 | XRP/USD | 0.94652 | 53.896 | 57.746 | +0.40% | +0.13% | 0.55x | 0.1 | 2026-11-27T01:21:10.398144+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | SOL/USD | 71.36 | 53.216 | 58.444 | +0.59% | +0.13% | 0.41x | 1.4 | 2026-11-27T01:21:10.398144+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 77.664 | 705.25 | +0.76% | 3.14x |
| 2 | XMR/USD | 61.771 | 464.9 | -0.38% | 0.43x |
| 3 | HYPE/USD | 61.292 | 62.85 | -0.16% | 0.68x |
| 4 | LTC/USD | 60.108 | 44.13 | +0.09% | 3.16x |
| 5 | ETH/USD | 59.782 | 1699.28 | -0.07% | 1.23x |
| 6 | LINK/USD | 59.245 | 9.34313 | -0.16% | 4.16x |
| 7 | NEAR/USD | 58.631 | 3.0715 | -0.27% | 0.78x |
| 8 | SOL/USD | 58.444 | 71.36 | +0.13% | 0.41x |
| 9 | XRP/USD | 57.746 | 0.94652 | +0.13% | 0.55x |
| 10 | XBT/USD | 57.184 | 60687.5 | +0.02% | 1.60x |
| 11 | SUI/USD | 52.825 | 0.6724 | +0.34% | 1.59x |
| 12 | AVAX/USD | 40.965 | 6.637 | +0.17% | 10.01x |

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

- Persisted scans: 1939; predictions: 16970; observations: 1174424.
- Matured sampled outcomes across 1/6/24/48h: 37206; gap abstentions: 25425. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45921918410 · **Generation:** 1939 · **Legacy run:** 45921918410
**Main quote time:** 2026-11-27T01:21:18.887002+00:00 · **Legacy report time:** 2026-11-27T01:22:01.289574+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 705.25 | 96.48 | +0.76% | 3.14x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | LTC/USD ⭐ | 44.13 | 75.56 | +0.09% | 3.16x | STRONG 93/100 | HIGH 55/100 | Watch |
| 3 | LINK/USD | 9.34313 | 73.45 | -0.16% | 4.16x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 4 | XBT/USD | 60687.5 | 63.31 | +0.02% | 1.60x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 5 | ETH/USD | 1699.28 | 61.76 | -0.07% | 1.23x | WEAK 41/100 | HIGH 68/100 | Watch |
| 6 | SUI/USD ⭐ | 0.6724 | 60.40 | +0.34% | 1.59x | STRONG 85/100 | HIGH 55/100 | Consider small entry |
| 7 | HYPE/USD | 62.85 | 57.26 | -0.16% | 0.68x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | AVAX/USD ⭐ | 6.637 | 56.80 | +0.17% | 10.01x | STRONG 83/100 | HIGH 55/100 | Watch |
| 9 | NEAR/USD | 3.0715 | 55.11 | -0.27% | 0.78x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 10 | XMR/USD | 464.9 | 54.18 | -0.38% | 0.43x | WEAK 27/100 | VERY_HIGH 82/100 | Do nothing |
| 11 | XRP/USD | 0.94652 | 53.90 | +0.13% | 0.55x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 12 | SOL/USD | 71.36 | 53.22 | +0.13% | 0.41x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 704.93 | 91.90 | +0.76% | 3.14x | 33595 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | LTC/USD ⭐ | 44.15 | 66.99 | +0.09% | 3.16x | 14408 | STRONG 88/100 | HIGH 55/100 | Watch |
| 3 | SUI/USD ⭐ | 0.6724 | 56.83 | +0.34% | 1.59x | 4386 | STRONG 83/100 | HIGH 55/100 | Consider small entry |
| 4 | AVAX/USD ⭐ | 6.637 | 51.67 | +0.17% | 10.01x | 2249 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD, LTC/USD, SUI/USD, AVAX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
