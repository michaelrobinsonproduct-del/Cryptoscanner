# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T13:11:45.242996+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45181129520
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a0e3987e50cfeaa805a272b64a95d3123cacef79 (atomic ledger/results publication)
**Ledger generation:** 1434 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 157.93 | 97.578 | 83.158 | +10.10% | +0.12% | 2.38x | 19.7 | 2026-11-23T13:11:36.872644+00:00 | Not calibrated | STRONG 89/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SUI/USD | 0.6685 | 82.018 | 67.168 | +1.95% | -0.03% | 2.50x | 3.0 | 2026-11-23T13:11:36.872644+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 3 | SOL/USD | 72.41 | 81.437 | 71.951 | +2.52% | +0.14% | 1.88x | 1.4 | 2026-11-23T13:11:36.872644+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 4 | PEARL/USD | 2.227 | 80.883 | 80.116 | +8.40% | -2.85% | 10.97x | 18.9 | 2026-11-23T13:11:36.872644+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 71/100 | Do nothing | WATCH |
| 5 | ALGO/USD | 0.08421 | 75.765 | 76.138 | +11.64% | +1.36% | 0.28x | 9.5 | 2026-11-23T13:11:36.872644+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 6 | XRP/USD | 0.94128 | 61.057 | 65.316 | +1.48% | +0.07% | 0.54x | 0.1 | 2026-11-23T13:11:36.872644+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | CC/USD | 0.07667 | 60.190 | 64.091 | +4.64% | +0.38% | 0.42x | 6.5 | 2026-11-23T13:11:36.872644+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | HYPE/USD | 63.96 | 60.093 | 64.209 | +1.43% | +0.30% | 0.44x | 1.6 | 2026-11-23T13:11:36.872644+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | TRX/USD | 0.307017 | 57.525 | 42.266 | +0.60% | +0.05% | 3.43x | 1.1 | 2026-11-23T13:11:36.872644+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 10 | XAUT/USD | 3608 | 56.103 | 40.243 | +1.00% | +0.17% | 15.01x | 0.6 | 2026-11-23T13:11:36.872644+00:00 | Not calibrated | STRONG 73/100 | HIGH 60/100 | Watch | WATCH |
| 11 | UAI/USD | 0.0317 | 54.653 | 64.799 | +7.20% | -0.41% | 0.19x | 22.0 | 2026-11-23T13:11:36.872644+00:00 | Not calibrated | WEAK 22/100 | EXTREME 100/100 | Do nothing | WATCH |
| 12 | XLM/USD | 0.128674 | 54.064 | 57.761 | +0.90% | +0.26% | 0.50x | 0.1 | 2026-11-23T13:11:36.872644+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 83.158 | 157.93 | +0.12% | 2.38x |
| 2 | PEARL/USD | 80.116 | 2.227 | -2.85% | 10.97x |
| 3 | ALGO/USD | 76.138 | 0.08421 | +1.36% | 0.28x |
| 4 | SOL/USD | 71.951 | 72.41 | +0.14% | 1.88x |
| 5 | SUI/USD | 67.168 | 0.6685 | -0.03% | 2.50x |
| 6 | XRP/USD | 65.316 | 0.94128 | +0.07% | 0.54x |
| 7 | UAI/USD | 64.799 | 0.0317 | -0.41% | 0.19x |
| 8 | HYPE/USD | 64.209 | 63.96 | +0.30% | 0.44x |
| 9 | CC/USD | 64.091 | 0.07667 | +0.38% | 0.42x |
| 10 | XLM/USD | 57.761 | 0.128674 | +0.26% | 0.50x |
| 11 | TRX/USD | 42.266 | 0.307017 | +0.05% | 3.43x |
| 12 | XAUT/USD | 40.243 | 3608 | +0.17% | 15.01x |

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

- Persisted scans: 1434; predictions: 11975; observations: 868409.
- Matured sampled outcomes across 1/6/24/48h: 20143; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45181129520 · **Generation:** 1434 · **Legacy run:** 45181129520
**Main quote time:** 2026-11-23T13:11:45.242996+00:00 · **Legacy report time:** 2026-11-23T13:12:40.878139+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 157.93 | 97.58 | +0.12% | 2.38x | STRONG 99/100 | HIGH 61/100 | Watch |
| 2 | SUI/USD | 0.6685 | 82.02 | -0.03% | 2.50x | STRONG 71/100 | HIGH 61/100 | Watch |
| 3 | SOL/USD ⭐ | 72.41 | 81.44 | +0.14% | 1.88x | STRONG 86/100 | HIGH 55/100 | Watch |
| 4 | PEARL/USD | 2.227 | 80.88 | -2.85% | 10.97x | MODERATE 65/100 | VERY_HIGH 71/100 | Do nothing |
| 5 | ALGO/USD | 0.08421 | 75.76 | +1.36% | 0.28x | MODERATE 68/100 | VERY_HIGH 75/100 | Watch |
| 6 | XRP/USD | 0.94128 | 61.06 | +0.07% | 0.54x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 7 | CC/USD | 0.07667 | 60.19 | +0.38% | 0.42x | MODERATE 60/100 | VERY_HIGH 75/100 | Watch |
| 8 | HYPE/USD | 63.96 | 60.09 | +0.30% | 0.44x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 9 | TRX/USD | 0.307017 | 57.52 | +0.05% | 3.43x | STRONG 74/100 | HIGH 55/100 | Watch |
| 10 | XAUT/USD | 3608 | 56.10 | +0.17% | 15.01x | STRONG 73/100 | HIGH 60/100 | Watch |
| 11 | UAI/USD | 0.0317 | 54.65 | -0.41% | 0.19x | WEAK 22/100 | EXTREME 100/100 | Do nothing |
| 12 | XLM/USD | 0.128674 | 54.06 | +0.26% | 0.50x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 157.87 | 86.69 | +0.12% | 2.38x | 6227 | STRONG 93/100 | HIGH 61/100 | Watch |
| 2 | SOL/USD ⭐ | 72.38 | 82.90 | +0.14% | 1.88x | 29270 | STRONG 86/100 | HIGH 55/100 | Watch |

**Same-run overlap:** QNT/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
