# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T02:40:40.316709+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44662363279
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 740db7ac10db6be8f49b83c6e58196ac53f50a29 (atomic ledger/results publication)
**Ledger generation:** 909 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 2s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 5.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04499 | 34.612 | 42.261 | +0.51% | -0.99% | 0.73x | 4.4 | 2026-11-20T02:40:38.548526+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 2 | BLUR/USD | 0.00671 | 32.783 | 26.038 | +0.30% | +0.60% | 1.37x | 14.9 | 2026-11-20T02:40:38.548526+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | ACU/USD | 0.1103 | 22.148 | 28.102 | +0.27% | +0.00% | 0.40x | 9.1 | 2026-11-20T02:40:38.548526+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 4 | CAP/USD | 0.097195 | 21.898 | 28.820 | +0.60% | -0.17% | 0.39x | 19.2 | 2026-11-20T02:40:38.548526+00:00 | Not calibrated | WEAK 11/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 42.261 | 0.04499 | -0.99% | 0.73x |
| 2 | CAP/USD | 28.820 | 0.097195 | -0.17% | 0.39x |
| 3 | ACU/USD | 28.102 | 0.1103 | +0.00% | 0.40x |
| 4 | BLUR/USD | 26.038 | 0.00671 | +0.60% | 1.37x |

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

- Persisted scans: 909; predictions: 7884; observations: 549252.
- Matured sampled outcomes across 1/6/24/48h: 8860; gap abstentions: 16390. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 1; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44662363279 · **Generation:** 909 · **Legacy run:** 44662363279
**Main quote time:** 2026-11-20T02:40:40.316709+00:00 · **Legacy report time:** 2026-11-20T02:41:27.748556+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04499 | 34.61 | -0.99% | 0.73x | WEAK 22/100 | VERY_HIGH 76/100 | Do nothing |
| 2 | BLUR/USD ⭐ | 0.00671 | 32.78 | +0.60% | 1.37x | MODERATE 66/100 | VERY_HIGH 73/100 | Watch |
| 3 | ACU/USD | 0.1103 | 22.15 | +0.00% | 0.40x | WEAK 31/100 | VERY_HIGH 82/100 | Do nothing |
| 4 | CAP/USD | 0.097195 | 21.90 | -0.17% | 0.39x | WEAK 11/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BLUR/USD ⭐ | 0.00671 | 13.99 | +0.60% | 1.37x | 753 | MODERATE 52/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** BLUR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
