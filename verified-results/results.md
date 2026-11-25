# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T04:19:17.195093+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45545426784
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 5576a0cec77c8746f78a6f69f6e140827cbba5a3 (atomic ledger/results publication)
**Ledger generation:** 1668 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 23.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.00992 | 78.740 | 71.504 | +4.75% | +0.51% | 1.47x | 20.2 | 2026-11-25T04:19:09.454954+00:00 | Not calibrated | STRONG 74/100 | HIGH 67/100 | Watch | WATCH |
| 2 | DRV/USD | 0.33833 | 71.413 | 69.012 | +7.65% | +1.41% | 0.54x | 23.4 | 2026-11-25T04:19:09.454954+00:00 | Not calibrated | MODERATE 56/100 | EXTREME 87/100 | Do nothing | WATCH |
| 3 | PEPE/USD | 3.47e-06 | 57.098 | 41.684 | +0.49% | +0.09% | 2.50x | 11.5 | 2026-11-25T04:19:09.454954+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SKY/USD | 0.04157 | 51.218 | 38.027 | +1.44% | -0.36% | 13.33x | 12.0 | 2026-11-25T04:19:09.454954+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | XMR/USD | 513.66 | 48.502 | 51.720 | +0.80% | -0.02% | 0.69x | 14.2 | 2026-11-25T04:19:09.454954+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 6 | RE/USD | 0.20195 | 38.299 | 25.400 | +0.66% | +1.52% | 1.53x | 19.9 | 2026-11-25T04:19:09.454954+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | SYRUP/USD | 0.07119 | 27.477 | 31.567 | +2.18% | +0.38% | 0.40x | 30.9 | 2026-11-25T04:19:09.454954+00:00 | Not calibrated | WEAK 34/100 | EXTREME 87/100 | Do nothing | WATCH |
| 8 | DOT/USD | 0.6545 | 26.837 | 33.843 | +0.46% | +0.20% | 0.20x | 3.1 | 2026-11-25T04:19:09.454954+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 75/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 71.504 | 0.00992 | +0.51% | 1.47x |
| 2 | DRV/USD | 69.012 | 0.33833 | +1.41% | 0.54x |
| 3 | XMR/USD | 51.720 | 513.66 | -0.02% | 0.69x |
| 4 | PEPE/USD | 41.684 | 3.47e-06 | +0.09% | 2.50x |
| 5 | SKY/USD | 38.027 | 0.04157 | -0.36% | 13.33x |
| 6 | DOT/USD | 33.843 | 0.6545 | +0.20% | 0.20x |
| 7 | SYRUP/USD | 31.567 | 0.07119 | +0.38% | 0.40x |
| 8 | RE/USD | 25.400 | 0.20195 | +1.52% | 1.53x |

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

- Persisted scans: 1668; predictions: 14183; observations: 1010903.
- Matured sampled outcomes across 1/6/24/48h: 29942; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45545426784 · **Generation:** 1668 · **Legacy run:** 45545426784
**Main quote time:** 2026-11-25T04:19:17.195093+00:00 · **Legacy report time:** 2026-11-25T04:20:31.957187+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.00992 | 78.74 | +0.51% | 1.47x | STRONG 84/100 | HIGH 67/100 | Watch |
| 2 | DRV/USD | 0.33833 | 71.41 | +1.41% | 0.54x | MODERATE 56/100 | EXTREME 87/100 | Do nothing |
| 3 | PEPE/USD | 3.47e-06 | 57.10 | +0.09% | 2.50x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 4 | SKY/USD | 0.04157 | 51.22 | -0.36% | 13.33x | MODERATE 51/100 | VERY_HIGH 72/100 | Watch |
| 5 | XMR/USD | 513.66 | 48.50 | -0.02% | 0.69x | WEAK 24/100 | VERY_HIGH 82/100 | Do nothing |
| 6 | RE/USD | 0.20195 | 38.30 | +1.52% | 1.53x | MODERATE 59/100 | VERY_HIGH 73/100 | Watch |
| 7 | SYRUP/USD | 0.07119 | 27.48 | +0.38% | 0.40x | WEAK 34/100 | EXTREME 87/100 | Do nothing |
| 8 | DOT/USD | 0.6545 | 26.84 | +0.20% | 0.20x | WEAK 33/100 | VERY_HIGH 75/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.00993 | 85.24 | +1.23% | 1.12x | 18670 | STRONG 83/100 | HIGH 68/100 | Watch |
| 2 | XAUT/USD | 3543.2 | 40.16 | +0.22% | 9.58x | 1713 | STRONG 75/100 | HIGH 60/100 | Watch |

**Same-run overlap:** MON/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
