# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T20:22:11.949590+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45258206071
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1b9c0c674994c039a5b5e6eda1928085bb16a203 (atomic ledger/results publication)
**Ledger generation:** 1477 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ALGO/USD | 0.0832 | 93.151 | 92.858 | +10.30% | +1.16% | 0.45x | 3.6 | 2026-11-23T20:22:03.767090+00:00 | Not calibrated | STRONG 77/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | QNT/USD | 159.09 | 88.247 | 97.486 | +10.91% | -0.29% | 0.22x | 5.0 | 2026-11-23T20:22:03.767090+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | UNI/USD | 4.8781 | 88.025 | 79.472 | +4.21% | -0.53% | 2.12x | 4.3 | 2026-11-23T20:22:03.767090+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 4 | INJ/USD | 6.504 | 79.302 | 81.206 | +4.43% | +0.26% | 0.68x | 6.1 | 2026-11-23T20:22:03.767090+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | XDG/USD | 0.0568329 | 77.325 | 74.298 | +2.80% | +0.17% | 1.22x | 0.6 | 2026-11-23T20:22:03.767090+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 6 | LTC/USD | 41.49 | 75.026 | 76.977 | +3.31% | +0.05% | 0.78x | 2.4 | 2026-11-23T20:22:03.767090+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 7 | SOL/USD | 73.08 | 74.485 | 78.597 | +3.47% | +0.05% | 0.56x | 1.4 | 2026-11-23T20:22:03.767090+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | CC/USD | 0.07777 | 72.206 | 77.640 | +6.14% | +0.26% | 0.33x | 3.9 | 2026-11-23T20:22:03.767090+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | XLM/USD | 0.130869 | 70.728 | 72.116 | +2.62% | +0.10% | 0.81x | 2.4 | 2026-11-23T20:22:03.767090+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6773 | 69.154 | 76.583 | +3.29% | -0.26% | 0.39x | 3.0 | 2026-11-23T20:22:03.767090+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XAUT/USD | 3626.8 | 59.387 | 44.759 | +1.53% | -0.07% | 3.76x | 0.3 | 2026-11-23T20:22:03.767090+00:00 | Not calibrated | MODERATE 60/100 | HIGH 66/100 | Watch | WATCH |
| 12 | XRP/USD | 0.94274 | 58.609 | 65.887 | +1.64% | -0.02% | 0.28x | 1.2 | 2026-11-23T20:22:03.767090+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 97.486 | 159.09 | -0.29% | 0.22x |
| 2 | ALGO/USD | 92.858 | 0.0832 | +1.16% | 0.45x |
| 3 | INJ/USD | 81.206 | 6.504 | +0.26% | 0.68x |
| 4 | UNI/USD | 79.472 | 4.8781 | -0.53% | 2.12x |
| 5 | SOL/USD | 78.597 | 73.08 | +0.05% | 0.56x |
| 6 | CC/USD | 77.640 | 0.07777 | +0.26% | 0.33x |
| 7 | LTC/USD | 76.977 | 41.49 | +0.05% | 0.78x |
| 8 | SUI/USD | 76.583 | 0.6773 | -0.26% | 0.39x |
| 9 | XDG/USD | 74.298 | 0.0568329 | +0.17% | 1.22x |
| 10 | XLM/USD | 72.116 | 0.130869 | +0.10% | 0.81x |
| 11 | XRP/USD | 65.887 | 0.94274 | -0.02% | 0.28x |
| 12 | XAUT/USD | 44.759 | 3626.8 | -0.07% | 3.76x |

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

- Persisted scans: 1477; predictions: 12491; observations: 894595.
- Matured sampled outcomes across 1/6/24/48h: 22240; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45258206071 · **Generation:** 1477 · **Legacy run:** 45258206071
**Main quote time:** 2026-11-23T20:22:11.949590+00:00 · **Legacy report time:** 2026-11-23T20:23:09.792354+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD | 0.0832 | 93.15 | +1.16% | 0.45x | STRONG 77/100 | VERY_HIGH 70/100 | Watch |
| 2 | QNT/USD | 159.09 | 88.25 | -0.29% | 0.22x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |
| 3 | UNI/USD | 4.8781 | 88.03 | -0.53% | 2.12x | STRONG 74/100 | HIGH 61/100 | Watch |
| 4 | INJ/USD | 6.504 | 79.30 | +0.26% | 0.68x | STRONG 70/100 | VERY_HIGH 70/100 | Watch |
| 5 | XDG/USD ⭐ | 0.0568329 | 77.32 | +0.17% | 1.22x | STRONG 74/100 | HIGH 62/100 | Watch |
| 6 | LTC/USD | 41.49 | 75.03 | +0.05% | 0.78x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 7 | SOL/USD | 73.08 | 74.49 | +0.05% | 0.56x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 8 | CC/USD | 0.07777 | 72.21 | +0.26% | 0.33x | MODERATE 66/100 | VERY_HIGH 75/100 | Watch |
| 9 | XLM/USD | 0.130869 | 70.73 | +0.10% | 0.81x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 10 | SUI/USD | 0.6773 | 69.15 | -0.26% | 0.39x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 11 | XAUT/USD | 3626.8 | 59.39 | -0.07% | 3.76x | MODERATE 60/100 | HIGH 66/100 | Watch |
| 12 | XRP/USD | 0.94274 | 58.61 | -0.02% | 0.28x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XDG/USD ⭐ | 0.0568616 | 83.16 | +0.17% | 1.22x | 9831 | STRONG 77/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XDG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
