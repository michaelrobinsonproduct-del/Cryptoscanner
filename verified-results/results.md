# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T16:22:25.718119+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45215215155
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 29802f984bd0ed332883cbc5cff74be767cff7c6 (atomic ledger/results publication)
**Ledger generation:** 1453 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ADA/USD | 0.153818 | 111.875 | 96.227 | +6.37% | +0.13% | 3.66x | 6.8 | 2026-11-23T16:22:17.204898+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | ZEC/USD | 847.41 | 106.356 | 95.964 | +6.26% | +0.69% | 1.70x | 5.7 | 2026-11-23T16:22:17.204898+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | LTC/USD | 42.73 | 97.861 | 96.285 | +6.40% | +0.87% | 0.72x | 7.0 | 2026-11-23T16:22:17.204898+00:00 | Not calibrated | STRONG 79/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | SUI/USD | 0.7127 | 96.720 | 97.895 | +8.69% | +0.68% | 0.54x | 4.2 | 2026-11-23T16:22:17.204898+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | INJ/USD | 6.793 | 95.753 | 93.844 | +9.07% | +1.53% | 0.42x | 7.3 | 2026-11-23T16:22:17.204898+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XRP/USD | 0.98446 | 94.474 | 97.753 | +6.14% | +0.10% | 0.62x | 0.4 | 2026-11-23T16:22:17.204898+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | HYPE/USD | 66.22 | 93.531 | 88.567 | +5.01% | +0.08% | 1.46x | 3.0 | 2026-11-23T16:22:17.204898+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 8 | UNI/USD | 5.048 | 92.752 | 92.840 | +7.84% | +0.17% | 0.91x | 4.9 | 2026-11-23T16:22:17.204898+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 9 | XLM/USD | 0.13425 | 92.609 | 89.961 | +5.27% | +0.57% | 0.98x | 3.9 | 2026-11-23T16:22:17.204898+00:00 | Not calibrated | STRONG 76/100 | HIGH 62/100 | Watch | WATCH |
| 10 | SOL/USD | 75.01 | 91.986 | 97.742 | +6.20% | -0.21% | 0.53x | 1.3 | 2026-11-23T16:22:17.204898+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | NEAR/USD | 3.1381 | 89.879 | 90.124 | +5.25% | +0.89% | 0.53x | 3.2 | 2026-11-23T16:22:17.204898+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0584805 | 89.029 | 93.689 | +5.78% | +0.17% | 0.45x | 3.6 | 2026-11-23T16:22:17.204898+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SUI/USD | 97.895 | 0.7127 | +0.68% | 0.54x |
| 2 | XRP/USD | 97.753 | 0.98446 | +0.10% | 0.62x |
| 3 | SOL/USD | 97.742 | 75.01 | -0.21% | 0.53x |
| 4 | LTC/USD | 96.285 | 42.73 | +0.87% | 0.72x |
| 5 | ADA/USD | 96.227 | 0.153818 | +0.13% | 3.66x |
| 6 | ZEC/USD | 95.964 | 847.41 | +0.69% | 1.70x |
| 7 | INJ/USD | 93.844 | 6.793 | +1.53% | 0.42x |
| 8 | XDG/USD | 93.689 | 0.0584805 | +0.17% | 0.45x |
| 9 | UNI/USD | 92.840 | 5.048 | +0.17% | 0.91x |
| 10 | NEAR/USD | 90.124 | 3.1381 | +0.89% | 0.53x |
| 11 | XLM/USD | 89.961 | 0.13425 | +0.57% | 0.98x |
| 12 | HYPE/USD | 88.567 | 66.22 | +0.08% | 1.46x |

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

- Persisted scans: 1453; predictions: 12203; observations: 879979.
- Matured sampled outcomes across 1/6/24/48h: 21052; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45215215155 · **Generation:** 1453 · **Legacy run:** 45215215155
**Main quote time:** 2026-11-23T16:22:25.718119+00:00 · **Legacy report time:** 2026-11-23T16:23:35.572425+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.153818 | 111.87 | +0.13% | 3.66x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD | 847.41 | 106.36 | +0.69% | 1.70x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 3 | LTC/USD | 42.73 | 97.86 | +0.87% | 0.72x | STRONG 79/100 | VERY_HIGH 70/100 | Watch |
| 4 | SUI/USD | 0.7127 | 96.72 | +0.68% | 0.54x | STRONG 78/100 | VERY_HIGH 70/100 | Watch |
| 5 | INJ/USD | 6.793 | 95.75 | +1.53% | 0.42x | STRONG 78/100 | VERY_HIGH 70/100 | Watch |
| 6 | XRP/USD | 0.98446 | 94.47 | +0.10% | 0.62x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 7 | HYPE/USD ⭐ | 66.22 | 93.53 | +0.08% | 1.46x | STRONG 92/100 | HIGH 55/100 | Watch |
| 8 | UNI/USD | 5.048 | 92.75 | +0.17% | 0.91x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 9 | XLM/USD | 0.13425 | 92.61 | +0.57% | 0.98x | STRONG 76/100 | HIGH 62/100 | Watch |
| 10 | SOL/USD | 75.01 | 91.99 | -0.21% | 0.53x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 11 | NEAR/USD | 3.1381 | 89.88 | +0.89% | 0.53x | STRONG 75/100 | VERY_HIGH 70/100 | Watch |
| 12 | XDG/USD | 0.0584805 | 89.03 | +0.17% | 0.45x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 66.09 | 99.03 | +0.08% | 1.46x | 18740 | STRONG 95/100 | HIGH 55/100 | Watch |
| 2 | ADA/USD ⭐ | 0.154076 | 96.57 | +0.13% | 3.66x | 12059 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | ONDO/USD | 0.30249 | 90.26 | +0.54% | 1.49x | 6767 | STRONG 90/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ADA/USD, HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
