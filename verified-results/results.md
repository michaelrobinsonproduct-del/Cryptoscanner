# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T00:31:12.990151+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44966868562
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** cac85602bbb00a8af3617b47cbd3e67f197eec4f (atomic ledger/results publication)
**Ledger generation:** 1208 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.34019 | 66.424 | 45.459 | +1.49% | +2.97% | 1.61x | 24.4 | 2026-11-22T00:31:05.720734+00:00 | Not calibrated | MODERATE 68/100 | HIGH 67/100 | Watch | WATCH |
| 2 | CAP/USD | 0.092428 | 53.136 | 36.309 | +0.52% | +0.37% | 3.33x | 6.2 | 2026-11-22T00:31:05.720734+00:00 | Not calibrated | STRONG 82/100 | HIGH 60/100 | Watch | WATCH |
| 3 | ZBCN/USD | 0.00176 | 46.007 | 28.948 | +1.91% | +1.50% | 1.96x | 34.1 | 2026-11-22T00:31:05.720734+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 72/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 45.459 | 0.34019 | +2.97% | 1.61x |
| 2 | CAP/USD | 36.309 | 0.092428 | +0.37% | 3.33x |
| 3 | ZBCN/USD | 28.948 | 0.00176 | +1.50% | 1.96x |

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

- Persisted scans: 1208; predictions: 9773; observations: 730822.
- Matured sampled outcomes across 1/6/24/48h: 13241; gap abstentions: 21725. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 17; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44966868562 · **Generation:** 1208 · **Legacy run:** 44966868562
**Main quote time:** 2026-11-22T00:31:12.990151+00:00 · **Legacy report time:** 2026-11-22T00:32:07.232824+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.34019 | 66.42 | +2.97% | 1.61x | STRONG 78/100 | HIGH 67/100 | Consider small entry |
| 2 | CAP/USD ⭐ | 0.092428 | 53.14 | +0.37% | 3.33x | STRONG 92/100 | HIGH 60/100 | Consider small entry |
| 3 | ZBCN/USD ⭐ | 0.00176 | 46.01 | +1.50% | 1.96x | MODERATE 68/100 | VERY_HIGH 72/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.33924 | 57.26 | +2.97% | 1.61x | 15580 | STRONG 74/100 | HIGH 67/100 | Watch |
| 2 | NEAR/USD | 2.8907 | 56.16 | +0.48% | 2.95x | 20768 | STRONG 83/100 | HIGH 55/100 | Watch |
| 3 | XLM/USD | 0.129002 | 54.67 | +0.07% | 2.76x | 14134 | STRONG 72/100 | HIGH 55/100 | Watch |
| 4 | ZBCN/USD ⭐ | 0.001756 | 52.04 | +1.50% | 1.96x | 3358 | STRONG 71/100 | VERY_HIGH 72/100 | Watch |
| 5 | VVV/USD | 24.948 | 44.05 | +0.27% | 1.24x | 15649 | MODERATE 57/100 | HIGH 62/100 | Watch |
| 6 | CAP/USD ⭐ | 0.092363 | 42.56 | +0.37% | 3.33x | 7919 | STRONG 86/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** DRV/USD, CAP/USD, ZBCN/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
