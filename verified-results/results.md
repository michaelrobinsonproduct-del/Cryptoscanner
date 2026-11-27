# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T11:02:24.319524+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45986704632
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e7753458a24b21eb782607fd02b83b71ccc53733 (atomic ledger/results publication)
**Ledger generation:** 1998 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 66.04 | 109.577 | 96.459 | +6.14% | +0.26% | 2.18x | 3.0 | 2026-11-27T11:02:16.636340+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 755.33 | 100.710 | 97.285 | +10.81% | +0.01% | 1.34x | 5.4 | 2026-11-27T11:02:16.636340+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 3 | LINK/USD | 9.55513 | 90.298 | 74.423 | +3.09% | +0.18% | 11.99x | 4.5 | 2026-11-27T11:02:16.636340+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.638e-06 | 88.845 | 73.295 | +4.60% | +0.11% | 3.21x | 5.5 | 2026-11-27T11:02:16.636340+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 5 | XDG/USD | 0.0584291 | 86.722 | 72.807 | +3.64% | -0.22% | 4.51x | 0.0 | 2026-11-27T11:02:16.636340+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XRP/USD | 0.97665 | 78.311 | 79.915 | +3.60% | -0.47% | 1.07x | 0.5 | 2026-11-27T11:02:16.636340+00:00 | Not calibrated | MODERATE 49/100 | HIGH 68/100 | Watch | WATCH |
| 7 | SOL/USD | 73.07 | 76.138 | 75.333 | +3.00% | -0.05% | 1.11x | 1.4 | 2026-11-27T11:02:16.636340+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 8 | VVV/USD | 27.139 | 73.756 | 74.111 | +3.65% | +0.09% | 0.92x | 7.4 | 2026-11-27T11:02:16.636340+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6882 | 71.970 | 75.764 | +3.07% | -0.26% | 0.75x | 1.5 | 2026-11-27T11:02:16.636340+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 10 | ETH/USD | 1722.41 | 66.673 | 69.376 | +2.06% | +0.06% | 0.70x | 0.1 | 2026-11-27T11:02:16.636340+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XBT/USD | 61482.2 | 63.767 | 66.380 | +1.63% | +0.06% | 0.71x | 0.0 | 2026-11-27T11:02:16.636340+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XAUT/USD | 3666.6 | 57.330 | 52.619 | +3.00% | +0.07% | 1.44x | 0.3 | 2026-11-27T11:02:16.636340+00:00 | Not calibrated | MODERATE 64/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.285 | 755.33 | +0.01% | 1.34x |
| 2 | HYPE/USD | 96.459 | 66.04 | +0.26% | 2.18x |
| 3 | XRP/USD | 79.915 | 0.97665 | -0.47% | 1.07x |
| 4 | SUI/USD | 75.764 | 0.6882 | -0.26% | 0.75x |
| 5 | SOL/USD | 75.333 | 73.07 | -0.05% | 1.11x |
| 6 | LINK/USD | 74.423 | 9.55513 | +0.18% | 11.99x |
| 7 | VVV/USD | 74.111 | 27.139 | +0.09% | 0.92x |
| 8 | PEPE/USD | 73.295 | 3.638e-06 | +0.11% | 3.21x |
| 9 | XDG/USD | 72.807 | 0.0584291 | -0.22% | 4.51x |
| 10 | ETH/USD | 69.376 | 1722.41 | +0.06% | 0.70x |
| 11 | XBT/USD | 66.380 | 61482.2 | +0.06% | 0.71x |
| 12 | XAUT/USD | 52.619 | 3666.6 | +0.07% | 1.44x |

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

- Persisted scans: 1998; predictions: 17678; observations: 1209943.
- Matured sampled outcomes across 1/6/24/48h: 39281; gap abstentions: 25789. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45986704632 · **Generation:** 1998 · **Legacy run:** 45986704632
**Main quote time:** 2026-11-27T11:02:24.319524+00:00 · **Legacy report time:** 2026-11-27T11:03:18.458001+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 66.04 | 109.58 | +0.26% | 2.18x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD | 755.33 | 100.71 | +0.01% | 1.34x | STRONG 85/100 | HIGH 55/100 | Watch |
| 3 | LINK/USD ⭐ | 9.55513 | 90.30 | +0.18% | 11.99x | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | PEPE/USD ⭐ | 3.638e-06 | 88.84 | +0.11% | 3.21x | STRONG 99/100 | HIGH 55/100 | Watch |
| 5 | XDG/USD | 0.0584291 | 86.72 | -0.22% | 4.51x | STRONG 73/100 | HIGH 61/100 | Watch |
| 6 | XRP/USD | 0.97665 | 78.31 | -0.47% | 1.07x | MODERATE 49/100 | HIGH 68/100 | Watch |
| 7 | SOL/USD | 73.07 | 76.14 | -0.05% | 1.11x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 8 | VVV/USD | 27.139 | 73.76 | +0.09% | 0.92x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 9 | SUI/USD | 0.6882 | 71.97 | -0.26% | 0.75x | WEAK 41/100 | HIGH 68/100 | Watch |
| 10 | ETH/USD | 1722.41 | 66.67 | +0.06% | 0.70x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 11 | XBT/USD | 61482.2 | 63.77 | +0.06% | 0.71x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 12 | XAUT/USD | 3666.6 | 57.33 | +0.07% | 1.44x | MODERATE 64/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 65.97 | 100.00 | +0.26% | 2.18x | 15989 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | PEPE/USD ⭐ | 3.641e-06 | 96.14 | +0.11% | 3.21x | 5640 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | LINK/USD ⭐ | 9.55493 | 90.71 | +0.18% | 11.99x | 8240 | STRONG 100/100 | HIGH 55/100 | Watch |

**Same-run overlap:** HYPE/USD, LINK/USD, PEPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
