# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T01:40:42.735512+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45527203803
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c90ea0f70ae730c2bb5c5849930ae65e8ae2149c (atomic ledger/results publication)
**Ledger generation:** 1652 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.32063 | 56.426 | 45.036 | +2.02% | +0.24% | 2.02x | 7.2 | 2026-11-25T01:40:38.360464+00:00 | Not calibrated | STRONG 83/100 | HIGH 60/100 | Watch | WATCH |
| 2 | GWEI/USD | 0.010554 | 40.624 | 29.992 | +2.42% | +2.13% | 1.00x | 35.3 | 2026-11-25T01:40:38.360464+00:00 | Not calibrated | WEAK 35/100 | EXTREME 86/100 | Do nothing | WATCH |
| 3 | SYRUP/USD | 0.07095 | 38.603 | 36.735 | +1.84% | +0.84% | 0.77x | 15.5 | 2026-11-25T01:40:38.360464+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 4 | SKY/USD | 0.04137 | 29.365 | 35.757 | +0.95% | +0.00% | 0.36x | 9.7 | 2026-11-25T01:40:38.360464+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 5 | PEARL/USD | 2.1589 | 19.920 | 35.365 | +0.88% | -1.81% | 0.36x | 19.0 | 2026-11-25T01:40:38.360464+00:00 | Not calibrated | WEAK 10/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 45.036 | 0.32063 | +0.24% | 2.02x |
| 2 | SYRUP/USD | 36.735 | 0.07095 | +0.84% | 0.77x |
| 3 | SKY/USD | 35.757 | 0.04137 | +0.00% | 0.36x |
| 4 | PEARL/USD | 35.365 | 2.1589 | -1.81% | 0.36x |
| 5 | GWEI/USD | 29.992 | 0.010554 | +2.13% | 1.00x |

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

- Persisted scans: 1652; predictions: 14110; observations: 1001159.
- Matured sampled outcomes across 1/6/24/48h: 29484; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45527203803 · **Generation:** 1652 · **Legacy run:** 45527203803
**Main quote time:** 2026-11-25T01:40:42.735512+00:00 · **Legacy report time:** 2026-11-25T01:41:29.333686+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.32063 | 56.43 | +0.24% | 2.02x | STRONG 93/100 | HIGH 60/100 | Consider small entry |
| 2 | GWEI/USD | 0.010554 | 40.62 | +2.13% | 1.00x | WEAK 35/100 | EXTREME 86/100 | Do nothing |
| 3 | SYRUP/USD | 0.07095 | 38.60 | +0.84% | 0.77x | WEAK 44/100 | VERY_HIGH 80/100 | Watch |
| 4 | SKY/USD | 0.04137 | 29.37 | +0.00% | 0.36x | WEAK 35/100 | VERY_HIGH 75/100 | Watch |
| 5 | PEARL/USD | 2.1589 | 19.92 | -1.81% | 0.36x | WEAK 10/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.32063 | 60.00 | +0.24% | 2.02x | 6497 | STRONG 95/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** DRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
