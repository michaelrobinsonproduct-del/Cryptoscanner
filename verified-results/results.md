# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T12:41:50.796160+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45176393934
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** b728ae4f076321d56d1e26318ec7469ea6f9d767 (atomic ledger/results publication)
**Ledger generation:** 1431 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ALGO/USD | 0.08296 | 86.183 | 77.065 | +9.98% | +0.95% | 1.43x | 7.2 | 2026-11-23T12:41:42.685564+00:00 | Not calibrated | STRONG 88/100 | HIGH 60/100 | Watch | WATCH |
| 2 | QNT/USD | 157.48 | 83.823 | 83.371 | +9.79% | +0.74% | 0.67x | 19.7 | 2026-11-23T12:41:42.685564+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | UAI/USD | 0.0316 | 73.619 | 71.073 | +6.87% | -0.09% | 1.30x | 9.5 | 2026-11-23T12:41:42.685564+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | XRP/USD | 0.93733 | 73.307 | 61.908 | +1.06% | -0.15% | 2.21x | 1.0 | 2026-11-23T12:41:42.685564+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 5 | CC/USD | 0.07639 | 73.082 | 62.049 | +4.26% | +0.31% | 1.95x | 5.2 | 2026-11-23T12:41:42.685564+00:00 | Not calibrated | STRONG 82/100 | HIGH 60/100 | Consider small entry | WATCH |
| 6 | SOL/USD | 72.08 | 70.613 | 68.677 | +2.05% | -0.22% | 1.30x | 1.4 | 2026-11-23T12:41:42.685564+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6686 | 68.653 | 68.023 | +1.97% | -0.19% | 1.16x | 1.5 | 2026-11-23T12:41:42.685564+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 8 | LTC/USD | 40.84 | 66.636 | 52.491 | +1.69% | -0.17% | 2.89x | 2.4 | 2026-11-23T12:41:42.685564+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 9 | XLM/USD | 0.128149 | 63.228 | 55.884 | +0.49% | -0.18% | 1.83x | 0.9 | 2026-11-23T12:41:42.685564+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 10 | XMR/USD | 502.46 | 63.019 | 65.216 | +1.77% | -0.11% | 0.83x | 4.4 | 2026-11-23T12:41:42.685564+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 11 | HYPE/USD | 63.54 | 56.795 | 59.542 | +0.76% | -0.17% | 0.81x | 1.6 | 2026-11-23T12:41:42.685564+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | KAS/USD | 0.02717 | 55.532 | 61.822 | +5.27% | -0.37% | 0.55x | 18.4 | 2026-11-23T12:41:42.685564+00:00 | Not calibrated | WEAK 28/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 83.371 | 157.48 | +0.74% | 0.67x |
| 2 | ALGO/USD | 77.065 | 0.08296 | +0.95% | 1.43x |
| 3 | UAI/USD | 71.073 | 0.0316 | -0.09% | 1.30x |
| 4 | SOL/USD | 68.677 | 72.08 | -0.22% | 1.30x |
| 5 | SUI/USD | 68.023 | 0.6686 | -0.19% | 1.16x |
| 6 | XMR/USD | 65.216 | 502.46 | -0.11% | 0.83x |
| 7 | CC/USD | 62.049 | 0.07639 | +0.31% | 1.95x |
| 8 | XRP/USD | 61.908 | 0.93733 | -0.15% | 2.21x |
| 9 | KAS/USD | 61.822 | 0.02717 | -0.37% | 0.55x |
| 10 | HYPE/USD | 59.542 | 63.54 | -0.17% | 0.81x |
| 11 | XLM/USD | 55.884 | 0.128149 | -0.18% | 1.83x |
| 12 | LTC/USD | 52.491 | 40.84 | -0.17% | 2.89x |

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

- Persisted scans: 1431; predictions: 11939; observations: 866582.
- Matured sampled outcomes across 1/6/24/48h: 19989; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45176393934 · **Generation:** 1431 · **Legacy run:** 45176393934
**Main quote time:** 2026-11-23T12:41:50.796160+00:00 · **Legacy report time:** 2026-11-23T12:42:40.840804+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD ⭐ | 0.08296 | 86.18 | +0.95% | 1.43x | STRONG 98/100 | HIGH 60/100 | Watch |
| 2 | QNT/USD | 157.48 | 83.82 | +0.74% | 0.67x | MODERATE 67/100 | VERY_HIGH 76/100 | Watch |
| 3 | UAI/USD | 0.0316 | 73.62 | -0.09% | 1.30x | MODERATE 57/100 | VERY_HIGH 73/100 | Watch |
| 4 | XRP/USD | 0.93733 | 73.31 | -0.15% | 2.21x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 5 | CC/USD ⭐ | 0.07639 | 73.08 | +0.31% | 1.95x | STRONG 92/100 | HIGH 60/100 | Consider small entry |
| 6 | SOL/USD | 72.08 | 70.61 | -0.22% | 1.30x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 7 | SUI/USD | 0.6686 | 68.65 | -0.19% | 1.16x | WEAK 44/100 | HIGH 68/100 | Watch |
| 8 | LTC/USD | 40.84 | 66.64 | -0.17% | 2.89x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 9 | XLM/USD | 0.128149 | 63.23 | -0.18% | 1.83x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 10 | XMR/USD | 502.46 | 63.02 | -0.11% | 0.83x | WEAK 37/100 | HIGH 68/100 | Watch |
| 11 | HYPE/USD | 63.54 | 56.80 | -0.17% | 0.81x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 12 | KAS/USD | 0.02717 | 55.53 | -0.37% | 0.55x | WEAK 28/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.07639 | 84.78 | +0.31% | 1.95x | 3971 | STRONG 97/100 | HIGH 60/100 | Consider small entry |
| 2 | ALGO/USD ⭐ | 0.08314 | 78.02 | +0.95% | 1.43x | 4102 | STRONG 89/100 | HIGH 66/100 | Watch |

**Same-run overlap:** ALGO/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
