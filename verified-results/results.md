# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T01:40:29.709806+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44655210687
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 5c9c557fd4e3ae07fa6dc697869cf623ec1a4a60 (atomic ledger/results publication)
**Ledger generation:** 899 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 501.61 | 62.529 | 60.113 | +0.83% | -0.24% | 1.36x | 1.4 | 2026-11-20T01:40:25.012014+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XRP/USD | 0.96248 | 60.809 | 57.253 | +0.34% | -0.25% | 1.48x | 0.2 | 2026-11-20T01:40:25.012014+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04507 | 59.077 | 43.077 | +0.69% | +0.20% | 3.28x | 4.4 | 2026-11-20T01:40:25.012014+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 4 | XLM/USD | 0.13345 | 46.775 | 56.254 | +0.57% | -0.46% | 0.28x | 5.4 | 2026-11-20T01:40:25.012014+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | SHX/USD | 0.003595 | 44.518 | 31.179 | +0.25% | +0.00% | 2.33x | 2.8 | 2026-11-20T01:40:25.012014+00:00 | Not calibrated | MODERATE 67/100 | HIGH 67/100 | Watch | WATCH |
| 6 | CAP/USD | 0.09747 | 31.716 | 37.709 | +0.88% | +0.19% | 0.30x | 6.1 | 2026-11-20T01:40:25.012014+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 7 | ICNT/USD | 0.428 | 21.706 | 31.326 | +0.45% | -0.84% | 0.46x | 18.7 | 2026-11-20T01:40:25.012014+00:00 | Not calibrated | WEAK 11/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 60.113 | 501.61 | -0.24% | 1.36x |
| 2 | XRP/USD | 57.253 | 0.96248 | -0.25% | 1.48x |
| 3 | XLM/USD | 56.254 | 0.13345 | -0.46% | 0.28x |
| 4 | NIGHT/USD | 43.077 | 0.04507 | +0.20% | 3.28x |
| 5 | CAP/USD | 37.709 | 0.09747 | +0.19% | 0.30x |
| 6 | ICNT/USD | 31.326 | 0.428 | -0.84% | 0.46x |
| 7 | SHX/USD | 31.179 | 0.003595 | +0.00% | 2.33x |

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

- Persisted scans: 899; predictions: 7852; observations: 543222.
- Matured sampled outcomes across 1/6/24/48h: 8650; gap abstentions: 16251. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44655210687 · **Generation:** 899 · **Legacy run:** 44655210687
**Main quote time:** 2026-11-20T01:40:29.709806+00:00 · **Legacy report time:** 2026-11-20T01:41:22.649256+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 501.61 | 62.53 | -0.24% | 1.36x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 2 | XRP/USD | 0.96248 | 60.81 | -0.25% | 1.48x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 3 | NIGHT/USD ⭐ | 0.04507 | 59.08 | +0.20% | 3.28x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 4 | XLM/USD | 0.13345 | 46.77 | -0.46% | 0.28x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | SHX/USD | 0.003595 | 44.52 | +0.00% | 2.33x | MODERATE 67/100 | HIGH 67/100 | Watch |
| 6 | CAP/USD | 0.09747 | 31.72 | +0.19% | 0.30x | WEAK 36/100 | VERY_HIGH 75/100 | Watch |
| 7 | ICNT/USD | 0.428 | 21.71 | -0.84% | 0.46x | WEAK 11/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04507 | 55.73 | +0.20% | 3.28x | 7868 | STRONG 93/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
