# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T23:31:08.306050+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44962023262
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 2354d34d9820af25400b154b14876263bdca4505 (atomic ledger/results publication)
**Ledger generation:** 1201 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 490.61 | 111.652 | 95.213 | +7.52% | +0.29% | 2.70x | 9.6 | 2026-11-21T23:31:00.040380+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | UNI/USD | 4.7342 | 96.688 | 94.805 | +5.98% | +0.30% | 1.04x | 4.0 | 2026-11-21T23:31:00.040380+00:00 | Not calibrated | STRONG 83/100 | HIGH 62/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.0445 | 94.115 | 80.770 | +5.40% | -0.25% | 2.46x | 9.0 | 2026-11-21T23:31:00.040380+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ETH/USD | 1679.99 | 90.821 | 81.197 | +3.75% | -0.02% | 1.97x | 0.1 | 2026-11-21T23:31:00.040380+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XRP/USD | 0.9314 | 84.374 | 72.264 | +2.50% | +0.23% | 2.10x | 0.4 | 2026-11-21T23:31:00.040380+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | XLM/USD | 0.128863 | 79.302 | 64.107 | +1.31% | +0.04% | 2.83x | 0.1 | 2026-11-21T23:31:00.040380+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 7 | PEARL/USD | 1.961 | 77.086 | 76.161 | +7.26% | -0.11% | 1.15x | 23.5 | 2026-11-21T23:31:00.040380+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 8 | XDG/USD | 0.055075 | 75.538 | 65.309 | +1.47% | +0.04% | 2.01x | 0.0 | 2026-11-21T23:31:00.040380+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 9 | HYPE/USD | 61.26 | 74.978 | 58.669 | +0.64% | +0.26% | 12.54x | 1.6 | 2026-11-21T23:31:00.040380+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 10 | ZEC/USD | 779.22 | 74.279 | 73.913 | +2.81% | -0.26% | 1.17x | 1.5 | 2026-11-21T23:31:00.040380+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 11 | SOL/USD | 70.15 | 73.436 | 68.958 | +2.10% | -0.01% | 1.45x | 1.4 | 2026-11-21T23:31:00.040380+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 12 | QNT/USD | 143.23 | 70.025 | 75.454 | +3.22% | +0.01% | 0.45x | 4.2 | 2026-11-21T23:31:00.040380+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 95.213 | 490.61 | +0.29% | 2.70x |
| 2 | UNI/USD | 94.805 | 4.7342 | +0.30% | 1.04x |
| 3 | ETH/USD | 81.197 | 1679.99 | -0.02% | 1.97x |
| 4 | NIGHT/USD | 80.770 | 0.0445 | -0.25% | 2.46x |
| 5 | PEARL/USD | 76.161 | 1.961 | -0.11% | 1.15x |
| 6 | QNT/USD | 75.454 | 143.23 | +0.01% | 0.45x |
| 7 | ZEC/USD | 73.913 | 779.22 | -0.26% | 1.17x |
| 8 | XRP/USD | 72.264 | 0.9314 | +0.23% | 2.10x |
| 9 | SOL/USD | 68.958 | 70.15 | -0.01% | 1.45x |
| 10 | XDG/USD | 65.309 | 0.055075 | +0.04% | 2.01x |
| 11 | XLM/USD | 64.107 | 0.128863 | +0.04% | 2.83x |
| 12 | HYPE/USD | 58.669 | 61.26 | +0.26% | 12.54x |

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

- Persisted scans: 1201; predictions: 9721; observations: 726567.
- Matured sampled outcomes across 1/6/24/48h: 13074; gap abstentions: 21641. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44962023262 · **Generation:** 1201 · **Legacy run:** 44962023262
**Main quote time:** 2026-11-21T23:31:08.306050+00:00 · **Legacy report time:** 2026-11-21T23:31:56.316155+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 490.61 | 111.65 | +0.29% | 2.70x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UNI/USD ⭐ | 4.7342 | 96.69 | +0.30% | 1.04x | STRONG 93/100 | HIGH 62/100 | Watch |
| 3 | NIGHT/USD | 0.0445 | 94.11 | -0.25% | 2.46x | STRONG 77/100 | HIGH 61/100 | Watch |
| 4 | ETH/USD | 1679.99 | 90.82 | -0.02% | 1.97x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 5 | XRP/USD ⭐ | 0.9314 | 84.37 | +0.23% | 2.10x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | XLM/USD | 0.128863 | 79.30 | +0.04% | 2.83x | STRONG 85/100 | HIGH 55/100 | Watch |
| 7 | PEARL/USD | 1.961 | 77.09 | -0.11% | 1.15x | WEAK 39/100 | VERY_HIGH 80/100 | Watch |
| 8 | XDG/USD | 0.055075 | 75.54 | +0.04% | 2.01x | STRONG 83/100 | HIGH 55/100 | Watch |
| 9 | HYPE/USD | 61.26 | 74.98 | +0.26% | 12.54x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 10 | ZEC/USD | 779.22 | 74.28 | -0.26% | 1.17x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 11 | SOL/USD | 70.15 | 73.44 | -0.01% | 1.45x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 12 | QNT/USD | 143.23 | 70.03 | +0.01% | 0.45x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 490.61 | 95.03 | +0.29% | 2.70x | 11849 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UNI/USD ⭐ | 4.7342 | 93.43 | +0.30% | 1.04x | 10588 | STRONG 92/100 | HIGH 62/100 | Watch |
| 3 | XRP/USD ⭐ | 0.9316 | 87.08 | +0.23% | 2.10x | 45402 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | ZBCN/USD | 0.001743 | 87.05 | +2.55% | 8.77x | 3027 | STRONG 89/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** XMR/USD, UNI/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
