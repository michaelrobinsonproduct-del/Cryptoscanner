# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T03:47:59.243886+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45542055274
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8cfd921f66707d99d2a1fce9cd8abc19c9fb25d0 (atomic ledger/results publication)
**Ledger generation:** 1665 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.33439 | 96.644 | 74.394 | +6.40% | +1.45% | 5.36x | 11.4 | 2026-11-25T03:47:52.580314+00:00 | Not calibrated | STRONG 98/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | MON/USD | 0.00984 | 58.416 | 65.431 | +3.91% | +0.41% | 0.09x | 20.4 | 2026-11-25T03:47:52.580314+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | XMR/USD | 511.64 | 57.112 | 52.507 | +0.40% | +0.44% | 1.24x | 6.8 | 2026-11-25T03:47:52.580314+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 4 | XPL/USD | 0.0447 | 50.911 | 34.790 | +1.59% | +0.22% | 2.80x | 22.4 | 2026-11-25T03:47:52.580314+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | VVV/USD | 24.681 | 47.221 | 55.222 | +0.58% | -0.80% | 0.60x | 7.7 | 2026-11-25T03:47:52.580314+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | SKY/USD | 0.04135 | 37.843 | 35.207 | +0.90% | +0.42% | 1.06x | 9.7 | 2026-11-25T03:47:52.580314+00:00 | Not calibrated | MODERATE 54/100 | HIGH 67/100 | Watch | WATCH |
| 7 | SYRUP/USD | 0.07101 | 28.808 | 34.642 | +1.92% | -0.71% | 0.77x | 21.1 | 2026-11-25T03:47:52.580314+00:00 | Not calibrated | WEAK 9/100 | EXTREME 85/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 74.394 | 0.33439 | +1.45% | 5.36x |
| 2 | MON/USD | 65.431 | 0.00984 | +0.41% | 0.09x |
| 3 | VVV/USD | 55.222 | 24.681 | -0.80% | 0.60x |
| 4 | XMR/USD | 52.507 | 511.64 | +0.44% | 1.24x |
| 5 | SKY/USD | 35.207 | 0.04135 | +0.42% | 1.06x |
| 6 | XPL/USD | 34.790 | 0.0447 | +0.22% | 2.80x |
| 7 | SYRUP/USD | 34.642 | 0.07101 | -0.71% | 0.77x |

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

- Persisted scans: 1665; predictions: 14164; observations: 1009076.
- Matured sampled outcomes across 1/6/24/48h: 29863; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45542055274 · **Generation:** 1665 · **Legacy run:** 45542055274
**Main quote time:** 2026-11-25T03:47:59.243886+00:00 · **Legacy report time:** 2026-11-25T03:49:01.152270+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.33439 | 96.64 | +1.45% | 5.36x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | MON/USD | 0.00984 | 58.42 | +0.41% | 0.09x | MODERATE 49/100 | VERY_HIGH 82/100 | Watch |
| 3 | XMR/USD ⭐ | 511.64 | 57.11 | +0.44% | 1.24x | STRONG 74/100 | HIGH 62/100 | Watch |
| 4 | XPL/USD ⭐ | 0.0447 | 50.91 | +0.22% | 2.80x | STRONG 80/100 | VERY_HIGH 72/100 | Watch |
| 5 | VVV/USD | 24.681 | 47.22 | -0.80% | 0.60x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | SKY/USD ⭐ | 0.04135 | 37.84 | +0.42% | 1.06x | MODERATE 64/100 | HIGH 67/100 | Watch |
| 7 | SYRUP/USD | 0.07101 | 28.81 | -0.71% | 0.77x | WEAK 9/100 | EXTREME 85/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.33372 | 89.15 | +1.45% | 5.36x | 7279 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | XMR/USD ⭐ | 511.31 | 51.69 | +0.44% | 1.24x | 6880 | STRONG 71/100 | HIGH 62/100 | Watch |
| 3 | XPL/USD ⭐ | 0.0446 | 39.44 | +0.22% | 2.80x | 1472 | STRONG 75/100 | VERY_HIGH 72/100 | Watch |
| 4 | SKY/USD ⭐ | 0.04134 | 36.25 | +0.42% | 1.06x | 4317 | MODERATE 63/100 | HIGH 67/100 | Watch |

**Same-run overlap:** DRV/USD, XMR/USD, XPL/USD, SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
