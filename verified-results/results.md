# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T10:52:06.675010+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45985344577
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 929fff86fd1923e92c6a5d445a74a944c6c01bef (atomic ledger/results publication)
**Ledger generation:** 1997 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 757.66 | 103.679 | 96.962 | +11.15% | +0.37% | 1.49x | 6.1 | 2026-11-27T10:51:57.631911+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | HYPE/USD | 66.12 | 103.127 | 98.120 | +6.27% | +0.53% | 1.23x | 1.5 | 2026-11-27T10:51:57.631911+00:00 | Not calibrated | STRONG 85/100 | HIGH 62/100 | Watch | WATCH |
| 3 | LINK/USD | 9.55359 | 90.200 | 74.160 | +3.08% | +0.21% | 15.55x | 4.8 | 2026-11-27T10:51:57.631911+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | XRP/USD | 0.9786 | 80.975 | 80.393 | +3.80% | -0.11% | 1.11x | 2.5 | 2026-11-27T10:51:57.631911+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 5 | SOL/USD | 73.42 | 78.549 | 78.790 | +3.50% | +0.19% | 0.88x | 1.4 | 2026-11-27T10:51:57.631911+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0585027 | 75.787 | 73.372 | +3.78% | -0.05% | 1.27x | 0.8 | 2026-11-27T10:51:57.631911+00:00 | Not calibrated | MODERATE 48/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ENA/USD | 0.1082 | 74.404 | 77.264 | +7.77% | +0.56% | 0.43x | 9.3 | 2026-11-27T10:51:57.631911+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6909 | 73.941 | 78.598 | +3.47% | +0.10% | 0.48x | 1.4 | 2026-11-27T10:51:57.631911+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | ADA/USD | 0.153 | 71.459 | 73.349 | +3.06% | +0.32% | 0.65x | 0.1 | 2026-11-27T10:51:57.631911+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | LTC/USD | 44.61 | 68.910 | 67.238 | +1.99% | +0.22% | 1.05x | 2.2 | 2026-11-27T10:51:57.631911+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 11 | ETH/USD | 1727.74 | 68.811 | 71.587 | +2.37% | +0.09% | 0.68x | 0.1 | 2026-11-27T10:51:57.631911+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | NEAR/USD | 3.1428 | 65.721 | 73.609 | +3.11% | +0.31% | 0.06x | 6.4 | 2026-11-27T10:51:57.631911+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | HYPE/USD | 98.120 | 66.12 | +0.53% | 1.23x |
| 2 | ZEC/USD | 96.962 | 757.66 | +0.37% | 1.49x |
| 3 | XRP/USD | 80.393 | 0.9786 | -0.11% | 1.11x |
| 4 | SOL/USD | 78.790 | 73.42 | +0.19% | 0.88x |
| 5 | SUI/USD | 78.598 | 0.6909 | +0.10% | 0.48x |
| 6 | ENA/USD | 77.264 | 0.1082 | +0.56% | 0.43x |
| 7 | LINK/USD | 74.160 | 9.55359 | +0.21% | 15.55x |
| 8 | NEAR/USD | 73.609 | 3.1428 | +0.31% | 0.06x |
| 9 | XDG/USD | 73.372 | 0.0585027 | -0.05% | 1.27x |
| 10 | ADA/USD | 73.349 | 0.153 | +0.32% | 0.65x |
| 11 | ETH/USD | 71.587 | 1727.74 | +0.09% | 0.68x |
| 12 | LTC/USD | 67.238 | 44.61 | +0.22% | 1.05x |

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

- Persisted scans: 1997; predictions: 17666; observations: 1209340.
- Matured sampled outcomes across 1/6/24/48h: 39245; gap abstentions: 25785. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45985344577 · **Generation:** 1997 · **Legacy run:** 45985344577
**Main quote time:** 2026-11-27T10:52:06.675010+00:00 · **Legacy report time:** 2026-11-27T10:52:55.160319+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 757.66 | 103.68 | +0.37% | 1.49x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | HYPE/USD ⭐ | 66.12 | 103.13 | +0.53% | 1.23x | STRONG 95/100 | HIGH 62/100 | Watch |
| 3 | LINK/USD ⭐ | 9.55359 | 90.20 | +0.21% | 15.55x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | XRP/USD | 0.9786 | 80.97 | -0.11% | 1.11x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 5 | SOL/USD | 73.42 | 78.55 | +0.19% | 0.88x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 6 | XDG/USD | 0.0585027 | 75.79 | -0.05% | 1.27x | MODERATE 48/100 | HIGH 61/100 | Watch |
| 7 | ENA/USD | 0.1082 | 74.40 | +0.56% | 0.43x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 8 | SUI/USD | 0.6909 | 73.94 | +0.10% | 0.48x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 9 | ADA/USD | 0.153 | 71.46 | +0.32% | 0.65x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 10 | LTC/USD | 44.61 | 68.91 | +0.22% | 1.05x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 11 | ETH/USD | 1727.74 | 68.81 | +0.09% | 0.68x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 12 | NEAR/USD | 3.1428 | 65.72 | +0.31% | 0.06x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 66.12 | 96.49 | +0.53% | 1.23x | 16186 | STRONG 93/100 | HIGH 62/100 | Watch |
| 2 | ZEC/USD ⭐ | 758.07 | 95.15 | +0.37% | 1.49x | 40414 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | LINK/USD ⭐ | 9.55393 | 88.11 | +0.21% | 15.55x | 8174 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | VVV/USD | 27.124 | 87.38 | +0.30% | 7.60x | 9557 | STRONG 94/100 | HIGH 61/100 | Consider small entry |
| 5 | PEPE/USD | 3.629e-06 | 85.55 | +0.14% | 1.72x | 5609 | STRONG 78/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD, HYPE/USD, LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
