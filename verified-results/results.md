# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T02:41:20.172322+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45314000908
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 82c7ebd711f2b3548f12249f62057d4770d9d04b (atomic ledger/results publication)
**Ledger generation:** 1514 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01242 | 101.856 | 79.545 | +7.81% | +3.33% | 1.56x | 8.0 | 2026-11-24T02:41:13.921591+00:00 | Not calibrated | STRONG 95/100 | HIGH 65/100 | Consider small entry | WATCH |
| 2 | NIGHT/USD | 0.04866 | 68.102 | 54.130 | +1.06% | -0.21% | 9.91x | 6.2 | 2026-11-24T02:41:13.921591+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XLM/USD | 0.130809 | 62.536 | 59.350 | +0.63% | +0.12% | 1.26x | 0.1 | 2026-11-24T02:41:13.921591+00:00 | Not calibrated | MODERATE 56/100 | HIGH 55/100 | Watch | WATCH |
| 4 | XRP/USD | 0.94533 | 61.228 | 59.373 | +0.63% | -0.17% | 1.27x | 0.1 | 2026-11-24T02:41:13.921591+00:00 | Not calibrated | WEAK 41/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ADA/USD | 0.148839 | 56.973 | 54.596 | +0.26% | -0.11% | 1.29x | 4.5 | 2026-11-24T02:41:13.921591+00:00 | Not calibrated | WEAK 38/100 | HIGH 61/100 | Watch | WATCH |
| 6 | LINK/USD | 9.03092 | 55.584 | 54.406 | +0.29% | -0.09% | 1.16x | 5.2 | 2026-11-24T02:41:13.921591+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 7 | PEPE/USD | 3.459e-06 | 49.724 | 53.345 | +1.08% | +0.35% | 0.46x | 5.8 | 2026-11-24T02:41:13.921591+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XAUT/USD | 3636.3 | 48.119 | 36.329 | +0.47% | -0.08% | 2.22x | 0.6 | 2026-11-24T02:41:13.921591+00:00 | Not calibrated | MODERATE 54/100 | HIGH 66/100 | Watch | WATCH |
| 9 | XDG/USD | 0.0564897 | 47.161 | 56.675 | +0.33% | -0.23% | 0.16x | 1.2 | 2026-11-24T02:41:13.921591+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | LIGHTER/USD | 2.437 | 45.922 | 30.238 | +0.45% | +1.29% | 1.92x | 16.4 | 2026-11-24T02:41:13.921591+00:00 | Not calibrated | MODERATE 63/100 | HIGH 66/100 | Watch | WATCH |
| 11 | CC/USD | 0.07953 | 43.781 | 42.520 | +1.23% | -0.09% | 1.17x | 5.0 | 2026-11-24T02:41:13.921591+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 12 | AI/USD | 0.01586 | 43.483 | 56.918 | +4.14% | -1.86% | 0.58x | 6.4 | 2026-11-24T02:41:13.921591+00:00 | Not calibrated | WEAK 27/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 79.545 | 0.01242 | +3.33% | 1.56x |
| 2 | XRP/USD | 59.373 | 0.94533 | -0.17% | 1.27x |
| 3 | XLM/USD | 59.350 | 0.130809 | +0.12% | 1.26x |
| 4 | AI/USD | 56.918 | 0.01586 | -1.86% | 0.58x |
| 5 | XDG/USD | 56.675 | 0.0564897 | -0.23% | 0.16x |
| 6 | ADA/USD | 54.596 | 0.148839 | -0.11% | 1.29x |
| 7 | LINK/USD | 54.406 | 9.03092 | -0.09% | 1.16x |
| 8 | NIGHT/USD | 54.130 | 0.04866 | -0.21% | 9.91x |
| 9 | PEPE/USD | 53.345 | 3.459e-06 | +0.35% | 0.46x |
| 10 | CC/USD | 42.520 | 0.07953 | -0.09% | 1.17x |
| 11 | XAUT/USD | 36.329 | 3636.3 | -0.08% | 2.22x |
| 12 | LIGHTER/USD | 30.238 | 2.437 | +1.29% | 1.92x |

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

- Persisted scans: 1514; predictions: 12925; observations: 917127.
- Matured sampled outcomes across 1/6/24/48h: 23915; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 135 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45314000908 · **Generation:** 1514 · **Legacy run:** 45314000908
**Main quote time:** 2026-11-24T02:41:20.172322+00:00 · **Legacy report time:** 2026-11-24T02:42:10.143537+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01242 | 101.86 | +3.33% | 1.56x | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 2 | NIGHT/USD | 0.04866 | 68.10 | -0.21% | 9.91x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 3 | XLM/USD ⭐ | 0.130809 | 62.54 | +0.12% | 1.26x | MODERATE 66/100 | HIGH 55/100 | Watch |
| 4 | XRP/USD | 0.94533 | 61.23 | -0.17% | 1.27x | WEAK 41/100 | HIGH 61/100 | Watch |
| 5 | ADA/USD | 0.148839 | 56.97 | -0.11% | 1.29x | WEAK 38/100 | HIGH 61/100 | Watch |
| 6 | LINK/USD | 9.03092 | 55.58 | -0.09% | 1.16x | WEAK 38/100 | HIGH 68/100 | Watch |
| 7 | PEPE/USD | 3.459e-06 | 49.72 | +0.35% | 0.46x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 8 | XAUT/USD | 3636.3 | 48.12 | -0.08% | 2.22x | MODERATE 54/100 | HIGH 66/100 | Watch |
| 9 | XDG/USD | 0.0564897 | 47.16 | -0.23% | 0.16x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | LIGHTER/USD | 2.437 | 45.92 | +1.29% | 1.92x | MODERATE 63/100 | HIGH 66/100 | Watch |
| 11 | CC/USD | 0.07953 | 43.78 | -0.09% | 1.17x | WEAK 32/100 | VERY_HIGH 73/100 | Do nothing |
| 12 | AI/USD | 0.01586 | 43.48 | -1.86% | 0.58x | WEAK 27/100 | EXTREME 92/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01234 | 85.37 | +3.33% | 1.56x | 7262 | STRONG 93/100 | VERY_HIGH 71/100 | Watch |
| 2 | XLM/USD ⭐ | 0.130751 | 50.73 | +0.12% | 1.26x | 18272 | MODERATE 60/100 | HIGH 55/100 | Watch |
| 3 | BAT/USD | 0.07842 | 46.22 | +0.37% | 1.62x | 2952 | MODERATE 58/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** MON/USD, XLM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
