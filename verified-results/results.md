# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T09:01:45.646432+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45969978061
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** dd0768a479a749c94d06978a831a8e3294535849 (atomic ledger/results publication)
**Ledger generation:** 1986 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 752.13 | 96.153 | 96.012 | +10.34% | +0.65% | 0.69x | 8.0 | 2026-11-27T09:01:39.830256+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | HYPE/USD | 65.7 | 88.952 | 93.390 | +5.59% | +0.00% | 0.56x | 1.5 | 2026-11-27T09:01:39.830256+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | VVV/USD | 27.086 | 78.301 | 72.880 | +3.45% | +0.37% | 1.36x | 8.1 | 2026-11-27T09:01:39.830256+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ENA/USD | 0.1069 | 78.058 | 76.743 | +6.47% | +0.85% | 0.71x | 9.3 | 2026-11-27T09:01:39.830256+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 5 | PAXG/USD | 3663.91 | 75.887 | 60.403 | +3.01% | +0.10% | 3.53x | 1.5 | 2026-11-27T09:01:39.830256+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 6 | UNI/USD | 4.8724 | 74.722 | 74.891 | +4.78% | -0.16% | 1.06x | 5.9 | 2026-11-27T09:01:39.830256+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 7 | XRP/USD | 0.97599 | 73.844 | 78.708 | +3.53% | -0.51% | 0.77x | 1.9 | 2026-11-27T09:01:39.830256+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 8 | SOL/USD | 73.43 | 73.129 | 78.889 | +3.51% | +0.16% | 0.34x | 1.4 | 2026-11-27T09:01:39.830256+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | LINK/USD | 9.62384 | 72.721 | 79.946 | +3.83% | +0.23% | 0.16x | 3.8 | 2026-11-27T09:01:39.830256+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | ETH/USD | 1729.64 | 70.456 | 72.375 | +2.49% | +0.00% | 0.81x | 0.1 | 2026-11-27T09:01:39.830256+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 11 | W/USD | 0.00954 | 69.677 | 73.569 | +8.29% | -0.31% | 0.77x | 10.5 | 2026-11-27T09:01:39.830256+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 12 | XDG/USD | 0.058201 | 67.010 | 69.515 | +3.24% | +0.11% | 0.69x | 0.8 | 2026-11-27T09:01:39.830256+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 96.012 | 752.13 | +0.65% | 0.69x |
| 2 | HYPE/USD | 93.390 | 65.7 | +0.00% | 0.56x |
| 3 | LINK/USD | 79.946 | 9.62384 | +0.23% | 0.16x |
| 4 | SOL/USD | 78.889 | 73.43 | +0.16% | 0.34x |
| 5 | XRP/USD | 78.708 | 0.97599 | -0.51% | 0.77x |
| 6 | ENA/USD | 76.743 | 0.1069 | +0.85% | 0.71x |
| 7 | UNI/USD | 74.891 | 4.8724 | -0.16% | 1.06x |
| 8 | W/USD | 73.569 | 0.00954 | -0.31% | 0.77x |
| 9 | VVV/USD | 72.880 | 27.086 | +0.37% | 1.36x |
| 10 | ETH/USD | 72.375 | 1729.64 | +0.00% | 0.81x |
| 11 | XDG/USD | 69.515 | 0.058201 | +0.11% | 0.69x |
| 12 | PAXG/USD | 60.403 | 3663.91 | +0.10% | 3.53x |

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

- Persisted scans: 1986; predictions: 17534; observations: 1202711.
- Matured sampled outcomes across 1/6/24/48h: 38837; gap abstentions: 25706. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45969978061 · **Generation:** 1986 · **Legacy run:** 45969978061
**Main quote time:** 2026-11-27T09:01:45.646432+00:00 · **Legacy report time:** 2026-11-27T09:02:22.941467+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 752.13 | 96.15 | +0.65% | 0.69x | STRONG 78/100 | VERY_HIGH 70/100 | Watch |
| 2 | HYPE/USD | 65.7 | 88.95 | +0.00% | 0.56x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 3 | VVV/USD ⭐ | 27.086 | 78.30 | +0.37% | 1.36x | STRONG 94/100 | HIGH 55/100 | Watch |
| 4 | ENA/USD | 0.1069 | 78.06 | +0.85% | 0.71x | MODERATE 69/100 | VERY_HIGH 75/100 | Watch |
| 5 | PAXG/USD | 3663.91 | 75.89 | +0.10% | 3.53x | STRONG 83/100 | HIGH 55/100 | Watch |
| 6 | UNI/USD | 4.8724 | 74.72 | -0.16% | 1.06x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 7 | XRP/USD | 0.97599 | 73.84 | -0.51% | 0.77x | WEAK 42/100 | HIGH 68/100 | Watch |
| 8 | SOL/USD | 73.43 | 73.13 | +0.16% | 0.34x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 9 | LINK/USD | 9.62384 | 72.72 | +0.23% | 0.16x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 10 | ETH/USD | 1729.64 | 70.46 | +0.00% | 0.81x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 11 | W/USD | 0.00954 | 69.68 | -0.31% | 0.77x | WEAK 35/100 | VERY_HIGH 79/100 | Watch |
| 12 | XDG/USD | 0.058201 | 67.01 | +0.11% | 0.69x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 27.071 | 79.86 | +0.37% | 1.36x | 9847 | STRONG 95/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
