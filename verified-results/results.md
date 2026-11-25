# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T21:05:53.152707+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45700946579
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a329f8545088af798b064b7a5392677b92dea491 (atomic ledger/results publication)
**Ledger generation:** 1767 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LTC/USD | 42.57 | 92.347 | 83.299 | +4.21% | +0.54% | 1.63x | 2.3 | 2026-11-25T21:05:46.203378+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | SUI/USD | 0.6657 | 92.031 | 73.173 | +2.81% | +0.77% | 2.53x | 3.0 | 2026-11-25T21:05:46.203378+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | HYPE/USD | 61.91 | 89.701 | 78.044 | +3.41% | +0.96% | 1.68x | 1.6 | 2026-11-25T21:05:46.203378+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | LINK/USD | 9.11923 | 87.701 | 68.627 | +3.14% | +0.81% | 4.10x | 3.6 | 2026-11-25T21:05:46.203378+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | ADA/USD | 0.147648 | 87.119 | 68.229 | +2.28% | +0.78% | 5.55x | 5.5 | 2026-11-25T21:05:46.203378+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | XMR/USD | 521.72 | 82.828 | 67.243 | +2.38% | +0.12% | 5.80x | 8.8 | 2026-11-25T21:05:46.203378+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 7 | NEAR/USD | 3.0133 | 82.078 | 83.931 | +4.47% | +0.97% | 0.33x | 4.7 | 2026-11-25T21:05:46.203378+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | SOL/USD | 70.54 | 80.451 | 63.745 | +1.35% | +0.34% | 2.92x | 1.4 | 2026-11-25T21:05:46.203378+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | XLM/USD | 0.128735 | 75.901 | 70.087 | +3.77% | +0.73% | 1.22x | 0.8 | 2026-11-25T21:05:46.203378+00:00 | Not calibrated | STRONG 73/100 | HIGH 62/100 | Watch | WATCH |
| 10 | XRP/USD | 0.94716 | 75.549 | 72.479 | +2.55% | +1.02% | 0.80x | 0.7 | 2026-11-25T21:05:46.203378+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 11 | ZEC/USD | 761.86 | 75.292 | 74.856 | +3.11% | +1.04% | 0.53x | 3.8 | 2026-11-25T21:05:46.203378+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | PAXG/USD | 3563.71 | 73.417 | 58.807 | +0.62% | -0.08% | 2.55x | 1.0 | 2026-11-25T21:05:46.203378+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 83.931 | 3.0133 | +0.97% | 0.33x |
| 2 | LTC/USD | 83.299 | 42.57 | +0.54% | 1.63x |
| 3 | HYPE/USD | 78.044 | 61.91 | +0.96% | 1.68x |
| 4 | ZEC/USD | 74.856 | 761.86 | +1.04% | 0.53x |
| 5 | SUI/USD | 73.173 | 0.6657 | +0.77% | 2.53x |
| 6 | XRP/USD | 72.479 | 0.94716 | +1.02% | 0.80x |
| 7 | XLM/USD | 70.087 | 0.128735 | +0.73% | 1.22x |
| 8 | LINK/USD | 68.627 | 9.11923 | +0.81% | 4.10x |
| 9 | ADA/USD | 68.229 | 0.147648 | +0.78% | 5.55x |
| 10 | XMR/USD | 67.243 | 521.72 | +0.12% | 5.80x |
| 11 | SOL/USD | 63.745 | 70.54 | +0.34% | 2.92x |
| 12 | PAXG/USD | 58.807 | 3563.71 | -0.08% | 2.55x |

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

- Persisted scans: 1767; predictions: 14948; observations: 1071147.
- Matured sampled outcomes across 1/6/24/48h: 32690; gap abstentions: 23066. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45700946579 · **Generation:** 1767 · **Legacy run:** 45700946579
**Main quote time:** 2026-11-25T21:05:53.152707+00:00 · **Legacy report time:** 2026-11-25T21:07:01.207246+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD ⭐ | 42.57 | 92.35 | +0.54% | 1.63x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SUI/USD ⭐ | 0.6657 | 92.03 | +0.77% | 2.53x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | HYPE/USD ⭐ | 61.91 | 89.70 | +0.96% | 1.68x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | LINK/USD ⭐ | 9.11923 | 87.70 | +0.81% | 4.10x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | ADA/USD ⭐ | 0.147648 | 87.12 | +0.78% | 5.55x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | XMR/USD ⭐ | 521.72 | 82.83 | +0.12% | 5.80x | STRONG 96/100 | HIGH 55/100 | Watch |
| 7 | NEAR/USD | 3.0133 | 82.08 | +0.97% | 0.33x | STRONG 71/100 | VERY_HIGH 70/100 | Watch |
| 8 | SOL/USD | 70.54 | 80.45 | +0.34% | 2.92x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 9 | XLM/USD ⭐ | 0.128735 | 75.90 | +0.73% | 1.22x | STRONG 83/100 | HIGH 62/100 | Watch |
| 10 | XRP/USD | 0.94716 | 75.55 | +1.02% | 0.80x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 11 | ZEC/USD | 761.86 | 75.29 | +1.04% | 0.53x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 12 | PAXG/USD | 3563.71 | 73.42 | -0.08% | 2.55x | MODERATE 67/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD ⭐ | 42.52 | 99.46 | +0.54% | 1.63x | 13547 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HYPE/USD ⭐ | 61.95 | 92.86 | +0.96% | 1.68x | 22435 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | VVV/USD | 27.995 | 92.67 | +2.28% | 1.20x | 13195 | STRONG 76/100 | HIGH 68/100 | Watch |
| 4 | SUI/USD ⭐ | 0.6651 | 90.05 | +0.77% | 2.53x | 7633 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | DRV/USD | 0.3572 | 87.93 | +2.58% | 2.09x | 12153 | STRONG 89/100 | HIGH 67/100 | Consider small entry |
| 6 | XLM/USD ⭐ | 0.128735 | 86.15 | +0.73% | 1.22x | 8195 | STRONG 88/100 | HIGH 62/100 | Watch |
| 7 | LINK/USD ⭐ | 9.10819 | 84.85 | +0.81% | 4.10x | 7813 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | HBAR/USD | 0.05208 | 81.52 | +0.62% | 1.78x | 5974 | STRONG 86/100 | HIGH 60/100 | Consider small entry |
| 9 | XMR/USD ⭐ | 521.72 | 80.45 | +0.12% | 5.80x | 8345 | STRONG 95/100 | HIGH 55/100 | Watch |
| 10 | ADA/USD ⭐ | 0.147537 | 80.39 | +0.78% | 5.55x | 10061 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** LTC/USD, SUI/USD, HYPE/USD, LINK/USD, ADA/USD, XMR/USD, XLM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
