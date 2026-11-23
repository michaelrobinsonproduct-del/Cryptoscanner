# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T11:11:53.641464+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45162597703
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1e02b50ed9fe6c60d42d94bad731347623279ccb (atomic ledger/results publication)
**Ledger generation:** 1422 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 153.94 | 90.056 | 89.123 | +7.32% | +0.44% | 0.87x | 5.8 | 2026-11-23T11:11:45.165844+00:00 | Not calibrated | STRONG 75/100 | HIGH 62/100 | Watch | WATCH |
| 2 | ALGO/USD | 0.08179 | 82.868 | 76.138 | +8.43% | +1.31% | 1.02x | 6.1 | 2026-11-23T11:11:45.165844+00:00 | Not calibrated | STRONG 76/100 | HIGH 67/100 | Watch | WATCH |
| 3 | JUP/USD | 0.23974 | 70.080 | 76.784 | +6.76% | -0.67% | 0.66x | 6.7 | 2026-11-23T11:11:45.165844+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 4 | SUI/USD | 0.6689 | 65.626 | 68.343 | +2.01% | -0.25% | 0.86x | 1.5 | 2026-11-23T11:11:45.165844+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 5 | HYPE/USD | 63.99 | 65.288 | 63.761 | +1.47% | +0.03% | 1.14x | 3.1 | 2026-11-23T11:11:45.165844+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 6 | SOL/USD | 72.1 | 65.086 | 68.875 | +2.08% | -0.41% | 0.83x | 1.4 | 2026-11-23T11:11:45.165844+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 7 | XRP/USD | 0.93795 | 64.080 | 62.536 | +1.12% | -0.14% | 1.23x | 0.6 | 2026-11-23T11:11:45.165844+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0555105 | 63.549 | 49.182 | +0.41% | -0.13% | 4.04x | 0.0 | 2026-11-23T11:11:45.165844+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 9 | Q/USD | 0.028097 | 60.600 | 64.019 | +11.35% | +0.49% | 0.41x | 24.6 | 2026-11-23T11:11:45.165844+00:00 | Not calibrated | MODERATE 50/100 | EXTREME 94/100 | Do nothing | WATCH |
| 10 | KAS/USD | 0.02714 | 59.749 | 64.901 | +5.15% | +0.18% | 0.39x | 11.1 | 2026-11-23T11:11:45.165844+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 11 | TRX/USD | 0.307546 | 59.596 | 42.748 | +0.78% | +0.37% | 2.56x | 0.2 | 2026-11-23T11:11:45.165844+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XMR/USD | 502.54 | 53.023 | 62.940 | +1.79% | -0.23% | 0.12x | 9.2 | 2026-11-23T11:11:45.165844+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 89.123 | 153.94 | +0.44% | 0.87x |
| 2 | JUP/USD | 76.784 | 0.23974 | -0.67% | 0.66x |
| 3 | ALGO/USD | 76.138 | 0.08179 | +1.31% | 1.02x |
| 4 | SOL/USD | 68.875 | 72.1 | -0.41% | 0.83x |
| 5 | SUI/USD | 68.343 | 0.6689 | -0.25% | 0.86x |
| 6 | KAS/USD | 64.901 | 0.02714 | +0.18% | 0.39x |
| 7 | Q/USD | 64.019 | 0.028097 | +0.49% | 0.41x |
| 8 | HYPE/USD | 63.761 | 63.99 | +0.03% | 1.14x |
| 9 | XMR/USD | 62.940 | 502.54 | -0.23% | 0.12x |
| 10 | XRP/USD | 62.536 | 0.93795 | -0.14% | 1.23x |
| 11 | XDG/USD | 49.182 | 0.0555105 | -0.13% | 4.04x |
| 12 | TRX/USD | 42.748 | 0.307546 | +0.37% | 2.56x |

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

- Persisted scans: 1422; predictions: 11831; observations: 861101.
- Matured sampled outcomes across 1/6/24/48h: 19581; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45162597703 · **Generation:** 1422 · **Legacy run:** 45162597703
**Main quote time:** 2026-11-23T11:11:53.641464+00:00 · **Legacy report time:** 2026-11-23T11:12:43.812824+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 153.94 | 90.06 | +0.44% | 0.87x | STRONG 75/100 | HIGH 62/100 | Watch |
| 2 | ALGO/USD ⭐ | 0.08179 | 82.87 | +1.31% | 1.02x | STRONG 86/100 | HIGH 67/100 | Watch |
| 3 | JUP/USD | 0.23974 | 70.08 | -0.67% | 0.66x | WEAK 40/100 | VERY_HIGH 81/100 | Watch |
| 4 | SUI/USD | 0.6689 | 65.63 | -0.25% | 0.86x | WEAK 38/100 | HIGH 68/100 | Watch |
| 5 | HYPE/USD | 63.99 | 65.29 | +0.03% | 1.14x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 6 | SOL/USD | 72.1 | 65.09 | -0.41% | 0.83x | WEAK 38/100 | HIGH 68/100 | Watch |
| 7 | XRP/USD | 0.93795 | 64.08 | -0.14% | 1.23x | WEAK 42/100 | HIGH 68/100 | Watch |
| 8 | XDG/USD | 0.0555105 | 63.55 | -0.13% | 4.04x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 9 | Q/USD | 0.028097 | 60.60 | +0.49% | 0.41x | MODERATE 50/100 | EXTREME 94/100 | Do nothing |
| 10 | KAS/USD | 0.02714 | 59.75 | +0.18% | 0.39x | MODERATE 45/100 | VERY_HIGH 81/100 | Watch |
| 11 | TRX/USD | 0.307546 | 59.60 | +0.37% | 2.56x | STRONG 85/100 | HIGH 55/100 | Watch |
| 12 | XMR/USD | 502.54 | 53.02 | -0.23% | 0.12x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD ⭐ | 0.08179 | 81.73 | +1.31% | 1.02x | 3183 | STRONG 86/100 | HIGH 67/100 | Watch |
| 2 | XLM/USD | 0.12909 | 63.23 | +0.15% | 1.01x | 12114 | MODERATE 57/100 | HIGH 62/100 | Watch |

**Same-run overlap:** ALGO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
