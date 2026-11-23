# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T11:01:06.555969+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45161009677
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 9b6631628fdd7b1c03f6dd7467f41d4a28234ffd (atomic ledger/results publication)
**Ledger generation:** 1420 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 152.43 | 90.296 | 87.844 | +6.27% | +0.07% | 1.21x | 5.9 | 2026-11-23T11:00:58.853815+00:00 | Not calibrated | STRONG 70/100 | HIGH 62/100 | Watch | WATCH |
| 2 | ALGO/USD | 0.08099 | 75.109 | 75.921 | +7.37% | -0.12% | 0.98x | 6.2 | 2026-11-23T11:00:58.853815+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | XRP/USD | 0.93856 | 74.772 | 63.103 | +1.19% | -0.04% | 2.19x | 0.4 | 2026-11-23T11:00:58.853815+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 4 | JUP/USD | 0.24102 | 74.311 | 74.354 | +7.33% | +0.02% | 0.99x | 11.6 | 2026-11-23T11:00:58.853815+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | SOL/USD | 72.26 | 70.365 | 70.463 | +2.31% | +0.08% | 0.95x | 1.4 | 2026-11-23T11:00:58.853815+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 6 | CC/USD | 0.07607 | 68.722 | 59.055 | +3.82% | +0.28% | 1.83x | 5.3 | 2026-11-23T11:00:58.853815+00:00 | Not calibrated | STRONG 79/100 | HIGH 60/100 | Watch | WATCH |
| 7 | HYPE/USD | 64.28 | 66.461 | 67.765 | +1.93% | +0.33% | 0.71x | 1.6 | 2026-11-23T11:00:58.853815+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | SUI/USD | 0.669 | 65.304 | 67.704 | +2.03% | +0.06% | 0.73x | 3.0 | 2026-11-23T11:00:58.853815+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XMR/USD | 502.57 | 64.882 | 64.376 | +1.79% | -0.06% | 1.08x | 6.4 | 2026-11-23T11:00:58.853815+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0555029 | 64.428 | 48.951 | +0.40% | +0.10% | 4.15x | 0.3 | 2026-11-23T11:00:58.853815+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 11 | XLM/USD | 0.12889 | 64.316 | 60.017 | +1.07% | +0.15% | 1.35x | 2.9 | 2026-11-23T11:00:58.853815+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 12 | KAS/USD | 0.02717 | 57.807 | 60.154 | +5.27% | -0.70% | 1.11x | 22.1 | 2026-11-23T11:00:58.853815+00:00 | Not calibrated | WEAK 29/100 | EXTREME 85/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 87.844 | 152.43 | +0.07% | 1.21x |
| 2 | ALGO/USD | 75.921 | 0.08099 | -0.12% | 0.98x |
| 3 | JUP/USD | 74.354 | 0.24102 | +0.02% | 0.99x |
| 4 | SOL/USD | 70.463 | 72.26 | +0.08% | 0.95x |
| 5 | HYPE/USD | 67.765 | 64.28 | +0.33% | 0.71x |
| 6 | SUI/USD | 67.704 | 0.669 | +0.06% | 0.73x |
| 7 | XMR/USD | 64.376 | 502.57 | -0.06% | 1.08x |
| 8 | XRP/USD | 63.103 | 0.93856 | -0.04% | 2.19x |
| 9 | KAS/USD | 60.154 | 0.02717 | -0.70% | 1.11x |
| 10 | XLM/USD | 60.017 | 0.12889 | +0.15% | 1.35x |
| 11 | CC/USD | 59.055 | 0.07607 | +0.28% | 1.83x |
| 12 | XDG/USD | 48.951 | 0.0555029 | +0.10% | 4.15x |

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

- Persisted scans: 1420; predictions: 11807; observations: 859883.
- Matured sampled outcomes across 1/6/24/48h: 19538; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45161009677 · **Generation:** 1420 · **Legacy run:** 45161009677
**Main quote time:** 2026-11-23T11:01:06.555969+00:00 · **Legacy report time:** 2026-11-23T11:01:50.443775+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 152.43 | 90.30 | +0.07% | 1.21x | STRONG 80/100 | HIGH 62/100 | Watch |
| 2 | ALGO/USD | 0.08099 | 75.11 | -0.12% | 0.98x | WEAK 43/100 | VERY_HIGH 73/100 | Watch |
| 3 | XRP/USD | 0.93856 | 74.77 | -0.04% | 2.19x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 4 | JUP/USD | 0.24102 | 74.31 | +0.02% | 0.99x | MODERATE 52/100 | VERY_HIGH 73/100 | Watch |
| 5 | SOL/USD | 72.26 | 70.36 | +0.08% | 0.95x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 6 | CC/USD ⭐ | 0.07607 | 68.72 | +0.28% | 1.83x | STRONG 89/100 | HIGH 60/100 | Consider small entry |
| 7 | HYPE/USD | 64.28 | 66.46 | +0.33% | 0.71x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 8 | SUI/USD | 0.669 | 65.30 | +0.06% | 0.73x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 9 | XMR/USD | 502.57 | 64.88 | -0.06% | 1.08x | WEAK 42/100 | HIGH 68/100 | Watch |
| 10 | XDG/USD | 0.0555029 | 64.43 | +0.10% | 4.15x | STRONG 77/100 | HIGH 55/100 | Watch |
| 11 | XLM/USD | 0.12889 | 64.32 | +0.15% | 1.35x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 12 | KAS/USD | 0.02717 | 57.81 | -0.70% | 1.11x | WEAK 29/100 | EXTREME 85/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.07607 | 82.07 | +0.28% | 1.83x | 4055 | STRONG 96/100 | HIGH 60/100 | Consider small entry |
| 2 | QNT/USD ⭐ | 152.22 | 81.20 | +0.07% | 1.21x | 5338 | STRONG 76/100 | HIGH 62/100 | Watch |

**Same-run overlap:** QNT/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
