# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T00:32:12.234241+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45518489765
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 3312f79f046d3cc271b723acf598f6a8013e2efe (atomic ledger/results publication)
**Ledger generation:** 1646 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AUD/USD | 0.66621 | 55.725 | 46.746 | +0.41% | +0.02% | 1.89x | 1.4 | 2026-11-25T00:32:08.857348+00:00 | Not calibrated | MODERATE 63/100 | HIGH 55/100 | Watch | WATCH |
| 2 | SKY/USD | 0.04182 | 50.628 | 43.436 | +2.05% | +0.95% | 1.25x | 9.6 | 2026-11-25T00:32:08.857348+00:00 | Not calibrated | MODERATE 60/100 | HIGH 67/100 | Watch | WATCH |
| 3 | DRV/USD | 0.31615 | 45.784 | 28.570 | +0.59% | +0.44% | 6.91x | 19.6 | 2026-11-25T00:32:08.857348+00:00 | Not calibrated | STRONG 73/100 | HIGH 66/100 | Watch | WATCH |
| 4 | SYRUP/USD | 0.06986 | 30.823 | 24.228 | +0.27% | +0.46% | 1.43x | 18.6 | 2026-11-25T00:32:08.857348+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 73/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | AUD/USD | 46.746 | 0.66621 | +0.02% | 1.89x |
| 2 | SKY/USD | 43.436 | 0.04182 | +0.95% | 1.25x |
| 3 | DRV/USD | 28.570 | 0.31615 | +0.44% | 6.91x |
| 4 | SYRUP/USD | 24.228 | 0.06986 | +0.46% | 1.43x |

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

- Persisted scans: 1646; predictions: 14075; observations: 997505.
- Matured sampled outcomes across 1/6/24/48h: 29283; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45518489765 · **Generation:** 1646 · **Legacy run:** 45518489765
**Main quote time:** 2026-11-25T00:32:12.234241+00:00 · **Legacy report time:** 2026-11-25T00:33:26.036060+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AUD/USD | 0.66621 | 55.73 | +0.02% | 1.89x | MODERATE 63/100 | HIGH 55/100 | Watch |
| 2 | SKY/USD ⭐ | 0.04182 | 50.63 | +0.95% | 1.25x | STRONG 70/100 | HIGH 67/100 | Watch |
| 3 | DRV/USD | 0.31615 | 45.78 | +0.44% | 6.91x | STRONG 73/100 | HIGH 66/100 | Watch |
| 4 | SYRUP/USD ⭐ | 0.06986 | 30.82 | +0.46% | 1.43x | MODERATE 65/100 | VERY_HIGH 73/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.0419 | 55.76 | +0.95% | 1.25x | 4209 | STRONG 73/100 | HIGH 67/100 | Watch |
| 2 | SYRUP/USD ⭐ | 0.06986 | 29.34 | +0.46% | 1.43x | 3301 | MODERATE 60/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** SKY/USD, SYRUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
