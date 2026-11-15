# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-15T14:08:48.558144+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43722700598
**Source SHA:** 2f30269316c847a4ba711151fcbb5ed3ab468275
**Previous ledger commit:** c8e4531cbaf78e39a4f5fb7ed42614e0e633056f (atomic ledger/results publication)
**Ledger generation:** 432 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 501.78 | 108.676 | 95.213 | +6.72% | -0.31% | 10.93x | 9.6 | 2026-11-15T14:08:41.844962+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XRP/USD | 0.96516 | 99.595 | 94.308 | +5.62% | -0.60% | 1.83x | 0.1 | 2026-11-15T14:08:41.844962+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | AAVE/USD | 106.91 | 97.560 | 87.136 | +6.33% | -0.92% | 3.20x | 5.6 | 2026-11-15T14:08:41.844962+00:00 | Not calibrated | STRONG 79/100 | HIGH 61/100 | Watch | WATCH |
| 4 | UNI/USD | 5.1396 | 90.867 | 90.462 | +5.27% | -0.80% | 1.44x | 2.9 | 2026-11-15T14:08:41.844962+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ADA/USD | 0.154174 | 90.192 | 83.112 | +4.41% | -0.75% | 2.09x | 5.6 | 2026-11-15T14:08:41.844962+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 6 | QNT/USD | 154.78 | 89.658 | 96.445 | +8.00% | -0.88% | 0.76x | 7.1 | 2026-11-15T14:08:41.844962+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 7 | ZEC/USD | 896.66 | 87.421 | 80.344 | +3.80% | -1.58% | 3.13x | 2.5 | 2026-11-15T14:08:41.844962+00:00 | Not calibrated | STRONG 74/100 | HIGH 65/100 | Do nothing | WATCH |
| 8 | HYPE/USD | 67.42 | 83.027 | 88.110 | +4.84% | -0.75% | 0.87x | 1.5 | 2026-11-15T14:08:41.844962+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 9 | LINK/USD | 9.27772 | 80.258 | 83.015 | +4.38% | -0.74% | 1.09x | 5.3 | 2026-11-15T14:08:41.844962+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 10 | TAO/USD | 191.4534 | 78.680 | 79.181 | +4.12% | -0.85% | 1.37x | 9.3 | 2026-11-15T14:08:41.844962+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 11 | SUI/USD | 0.7247 | 73.326 | 78.390 | +3.44% | -0.93% | 0.96x | 1.4 | 2026-11-15T14:08:41.844962+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 12 | PAXG/USD | 3820.72 | 70.565 | 55.616 | +0.58% | -0.01% | 12.04x | 0.4 | 2026-11-15T14:08:41.844962+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 96.445 | 154.78 | -0.88% | 0.76x |
| 2 | XMR/USD | 95.213 | 501.78 | -0.31% | 10.93x |
| 3 | XRP/USD | 94.308 | 0.96516 | -0.60% | 1.83x |
| 4 | UNI/USD | 90.462 | 5.1396 | -0.80% | 1.44x |
| 5 | HYPE/USD | 88.110 | 67.42 | -0.75% | 0.87x |
| 6 | AAVE/USD | 87.136 | 106.91 | -0.92% | 3.20x |
| 7 | ADA/USD | 83.112 | 0.154174 | -0.75% | 2.09x |
| 8 | LINK/USD | 83.015 | 9.27772 | -0.74% | 1.09x |
| 9 | ZEC/USD | 80.344 | 896.66 | -1.58% | 3.13x |
| 10 | TAO/USD | 79.181 | 191.4534 | -0.85% | 1.37x |
| 11 | SUI/USD | 78.390 | 0.7247 | -0.93% | 0.96x |
| 12 | PAXG/USD | 55.616 | 3820.72 | -0.01% | 12.04x |

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

- Persisted scans: 432; predictions: 3700; observations: 260139.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 11014. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 43722700598 · **Generation:** 432 · **Legacy run:** 43722700598
**Main quote time:** 2026-11-15T14:08:48.558144+00:00 · **Legacy report time:** 2026-11-15T14:09:00.699594+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 501.78 | 108.68 | -0.31% | 10.93x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | XRP/USD | 0.96516 | 99.59 | -0.60% | 1.83x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | AAVE/USD | 106.91 | 97.56 | -0.92% | 3.20x | STRONG 79/100 | HIGH 61/100 | Watch |
| 4 | UNI/USD | 5.1396 | 90.87 | -0.80% | 1.44x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 5 | ADA/USD | 0.154174 | 90.19 | -0.75% | 2.09x | STRONG 75/100 | HIGH 61/100 | Watch |
| 6 | QNT/USD | 154.78 | 89.66 | -0.88% | 0.76x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 7 | ZEC/USD | 896.66 | 87.42 | -1.58% | 3.13x | STRONG 74/100 | HIGH 65/100 | Do nothing |
| 8 | HYPE/USD | 67.42 | 83.03 | -0.75% | 0.87x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 9 | LINK/USD | 9.27772 | 80.26 | -0.74% | 1.09x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 10 | TAO/USD | 191.4534 | 78.68 | -0.85% | 1.37x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 11 | SUI/USD | 0.7247 | 73.33 | -0.93% | 0.96x | WEAK 42/100 | HIGH 68/100 | Watch |
| 12 | PAXG/USD | 3820.72 | 70.57 | -0.01% | 12.04x | MODERATE 65/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
