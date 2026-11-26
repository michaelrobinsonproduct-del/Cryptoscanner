# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T00:06:01.314917+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45726073365
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** ef607d528ba81c910cfcad9d2fcd39c66189e272 (atomic ledger/results publication)
**Ledger generation:** 1785 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 21.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 772.67 | 75.151 | 54.456 | +0.32% | +1.14% | 3.82x | 5.6 | 2026-11-26T00:05:54.303923+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | AKT/USD | 0.478 | 38.208 | 27.507 | +1.04% | +0.53% | 1.80x | 25.1 | 2026-11-26T00:05:54.303923+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | ME/USD | 0.0371 | 18.927 | 21.125 | +0.54% | +0.27% | 0.65x | 27.0 | 2026-11-26T00:05:54.303923+00:00 | Not calibrated | WEAK 29/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 54.456 | 772.67 | +1.14% | 3.82x |
| 2 | AKT/USD | 27.507 | 0.478 | +0.53% | 1.80x |
| 3 | ME/USD | 21.125 | 0.0371 | +0.27% | 0.65x |

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

- Persisted scans: 1785; predictions: 15155; observations: 1082109.
- Matured sampled outcomes across 1/6/24/48h: 32961; gap abstentions: 23455. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 18; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45726073365 · **Generation:** 1785 · **Legacy run:** 45726073365
**Main quote time:** 2026-11-26T00:06:01.314917+00:00 · **Legacy report time:** 2026-11-26T00:07:04.537172+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 772.67 | 75.15 | +1.14% | 3.82x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | AKT/USD ⭐ | 0.478 | 38.21 | +0.53% | 1.80x | MODERATE 64/100 | VERY_HIGH 72/100 | Watch |
| 3 | ME/USD | 0.0371 | 18.93 | +0.27% | 0.65x | WEAK 29/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD | 42.79 | 56.48 | +0.49% | 2.36x | 14029 | STRONG 83/100 | HIGH 55/100 | Watch |
| 2 | AKT/USD ⭐ | 0.4839 | 55.98 | +0.53% | 1.80x | 3656 | MODERATE 68/100 | VERY_HIGH 72/100 | Watch |
| 3 | ZEC/USD ⭐ | 772.65 | 55.57 | +1.14% | 3.82x | 43742 | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 4 | TAO/USD | 182 | 53.43 | +0.40% | 2.40x | 9037 | STRONG 82/100 | HIGH 55/100 | Watch |
| 5 | NEAR/USD | 3.0616 | 47.93 | +0.77% | 1.19x | 17629 | MODERATE 59/100 | HIGH 62/100 | Watch |
| 6 | XLM/USD | 0.128149 | 46.74 | +0.30% | 1.81x | 8341 | MODERATE 68/100 | HIGH 55/100 | Watch |
| 7 | PEPE/USD | 3.492e-06 | 45.27 | +0.58% | 1.25x | 6749 | MODERATE 58/100 | HIGH 62/100 | Watch |

**Same-run overlap:** ZEC/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
