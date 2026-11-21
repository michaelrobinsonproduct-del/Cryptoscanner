# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T23:41:13.885788+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44962865971
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 78eb10109cc9b895e5aac95e3675da779c0f4ccf (atomic ledger/results publication)
**Ledger generation:** 1203 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 490.03 | 111.891 | 98.062 | +7.39% | -0.20% | 2.48x | 3.9 | 2026-11-21T23:41:07.591993+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ZEC/USD | 778.31 | 89.505 | 72.300 | +2.69% | +0.44% | 2.51x | 3.1 | 2026-11-21T23:41:07.591993+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | UNI/USD | 4.7262 | 86.301 | 92.992 | +5.80% | -0.07% | 0.37x | 4.2 | 2026-11-21T23:41:07.591993+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04428 | 84.610 | 75.889 | +4.88% | -0.40% | 2.07x | 11.3 | 2026-11-21T23:41:07.591993+00:00 | Not calibrated | MODERATE 67/100 | HIGH 67/100 | Watch | WATCH |
| 5 | ETH/USD | 1681.05 | 83.278 | 81.655 | +3.81% | +0.13% | 1.10x | 0.1 | 2026-11-21T23:41:07.591993+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 6 | XRP/USD | 0.93256 | 81.288 | 73.319 | +2.62% | +0.36% | 1.62x | 0.1 | 2026-11-21T23:41:07.591993+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | XDG/USD | 0.0551459 | 80.320 | 66.114 | +1.60% | +0.29% | 2.27x | 0.2 | 2026-11-21T23:41:07.591993+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | PEARL/USD | 1.9502 | 76.454 | 80.375 | +6.67% | -0.28% | 0.75x | 14.9 | 2026-11-21T23:41:07.591993+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 9 | HYPE/USD | 61.21 | 74.403 | 58.093 | +0.56% | +0.26% | 5.42x | 1.6 | 2026-11-21T23:41:07.591993+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 10 | SOL/USD | 70.25 | 74.342 | 69.977 | +2.24% | +0.27% | 1.30x | 1.4 | 2026-11-21T23:41:07.591993+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 11 | QNT/USD | 143.63 | 72.953 | 76.781 | +3.51% | +0.43% | 0.40x | 5.6 | 2026-11-21T23:41:07.591993+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XLM/USD | 0.128949 | 69.683 | 64.581 | +1.37% | +0.26% | 1.38x | 0.1 | 2026-11-21T23:41:07.591993+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 98.062 | 490.03 | -0.20% | 2.48x |
| 2 | UNI/USD | 92.992 | 4.7262 | -0.07% | 0.37x |
| 3 | ETH/USD | 81.655 | 1681.05 | +0.13% | 1.10x |
| 4 | PEARL/USD | 80.375 | 1.9502 | -0.28% | 0.75x |
| 5 | QNT/USD | 76.781 | 143.63 | +0.43% | 0.40x |
| 6 | NIGHT/USD | 75.889 | 0.04428 | -0.40% | 2.07x |
| 7 | XRP/USD | 73.319 | 0.93256 | +0.36% | 1.62x |
| 8 | ZEC/USD | 72.300 | 778.31 | +0.44% | 2.51x |
| 9 | SOL/USD | 69.977 | 70.25 | +0.27% | 1.30x |
| 10 | XDG/USD | 66.114 | 0.0551459 | +0.29% | 2.27x |
| 11 | XLM/USD | 64.581 | 0.128949 | +0.26% | 1.38x |
| 12 | HYPE/USD | 58.093 | 61.21 | +0.26% | 5.42x |

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

- Persisted scans: 1203; predictions: 9745; observations: 727783.
- Matured sampled outcomes across 1/6/24/48h: 13111; gap abstentions: 21652. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44962865971 · **Generation:** 1203 · **Legacy run:** 44962865971
**Main quote time:** 2026-11-21T23:41:13.885788+00:00 · **Legacy report time:** 2026-11-21T23:42:18.398358+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 490.03 | 111.89 | -0.20% | 2.48x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | ZEC/USD ⭐ | 778.31 | 89.51 | +0.44% | 2.51x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | UNI/USD | 4.7262 | 86.30 | -0.07% | 0.37x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 4 | NIGHT/USD | 0.04428 | 84.61 | -0.40% | 2.07x | MODERATE 67/100 | HIGH 67/100 | Watch |
| 5 | ETH/USD ⭐ | 1681.05 | 83.28 | +0.13% | 1.10x | STRONG 77/100 | HIGH 62/100 | Watch |
| 6 | XRP/USD ⭐ | 0.93256 | 81.29 | +0.36% | 1.62x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 7 | XDG/USD ⭐ | 0.0551459 | 80.32 | +0.29% | 2.27x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | PEARL/USD | 1.9502 | 76.45 | -0.28% | 0.75x | WEAK 38/100 | VERY_HIGH 82/100 | Watch |
| 9 | HYPE/USD | 61.21 | 74.40 | +0.26% | 5.42x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 10 | SOL/USD ⭐ | 70.25 | 74.34 | +0.27% | 1.30x | STRONG 92/100 | HIGH 55/100 | Watch |
| 11 | QNT/USD | 143.63 | 72.95 | +0.43% | 0.40x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 12 | XLM/USD | 0.128949 | 69.68 | +0.26% | 1.38x | STRONG 80/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD ⭐ | 1680.68 | 98.13 | +0.13% | 1.10x | 65549 | STRONG 84/100 | HIGH 62/100 | Watch |
| 2 | XRP/USD ⭐ | 0.93299 | 87.40 | +0.36% | 1.62x | 45000 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 3 | ZEC/USD ⭐ | 778.85 | 81.48 | +0.44% | 2.51x | 39677 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SOL/USD ⭐ | 70.25 | 78.07 | +0.27% | 1.30x | 46502 | STRONG 94/100 | HIGH 55/100 | Watch |
| 5 | XDG/USD ⭐ | 0.0551411 | 76.94 | +0.29% | 2.27x | 14030 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ZEC/USD, ETH/USD, XRP/USD, XDG/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
