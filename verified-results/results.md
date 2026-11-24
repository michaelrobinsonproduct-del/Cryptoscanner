# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T11:21:50.506256+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45383137357
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 159526e91db642c624a7cd75b80590feb948975b (atomic ledger/results publication)
**Ledger generation:** 1567 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.45 | 95.577 | 79.945 | +4.10% | +0.13% | 8.33x | 7.5 | 2026-11-24T11:21:45.736302+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Watch | WATCH |
| 2 | MON/USD | 0.01255 | 84.895 | 82.614 | +8.94% | -0.32% | 1.39x | 8.0 | 2026-11-24T11:21:45.736302+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 3 | GBP/USD | 1.30724 | 72.044 | 57.028 | +0.31% | +0.00% | 3.54x | 0.2 | 2026-11-24T11:21:45.736302+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.455e-06 | 60.672 | 53.504 | +0.96% | -0.26% | 1.85x | 8.7 | 2026-11-24T11:21:45.736302+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XMR/USD | 496.21 | 56.718 | 64.129 | +2.10% | +0.07% | 0.22x | 11.1 | 2026-11-24T11:21:45.736302+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | 2Z/USD | 0.01608 | 47.121 | 46.818 | +2.75% | +0.19% | 0.94x | 6.2 | 2026-11-24T11:21:45.736302+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 7 | BAT/USD | 0.0779 | 45.988 | 30.732 | +0.95% | +0.05% | 3.94x | 16.7 | 2026-11-24T11:21:45.736302+00:00 | Not calibrated | MODERATE 63/100 | HIGH 66/100 | Watch | WATCH |
| 8 | INX/USD | 0.003949 | 33.541 | 29.469 | +1.31% | +0.23% | 1.29x | 22.8 | 2026-11-24T11:21:45.736302+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 9 | DBR/USD | 0.014 | 25.442 | 39.866 | +4.32% | -1.96% | 0.54x | 43.0 | 2026-11-24T11:21:45.736302+00:00 | Not calibrated | WEAK 3/100 | EXTREME 100/100 | Do nothing | WATCH |
| 10 | BABY/USD | 0.00856 | 25.426 | 25.896 | +0.71% | +0.00% | 0.95x | 23.4 | 2026-11-24T11:21:45.736302+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 82.614 | 0.01255 | -0.32% | 1.39x |
| 2 | VVV/USD | 79.945 | 25.45 | +0.13% | 8.33x |
| 3 | XMR/USD | 64.129 | 496.21 | +0.07% | 0.22x |
| 4 | GBP/USD | 57.028 | 1.30724 | +0.00% | 3.54x |
| 5 | PEPE/USD | 53.504 | 3.455e-06 | -0.26% | 1.85x |
| 6 | 2Z/USD | 46.818 | 0.01608 | +0.19% | 0.94x |
| 7 | DBR/USD | 39.866 | 0.014 | -1.96% | 0.54x |
| 8 | BAT/USD | 30.732 | 0.0779 | +0.05% | 3.94x |
| 9 | INX/USD | 29.469 | 0.003949 | +0.23% | 1.29x |
| 10 | BABY/USD | 25.896 | 0.00856 | +0.00% | 0.95x |

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

- Persisted scans: 1567; predictions: 13508; observations: 949401.
- Matured sampled outcomes across 1/6/24/48h: 25991; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45383137357 · **Generation:** 1567 · **Legacy run:** 45383137357
**Main quote time:** 2026-11-24T11:21:50.506256+00:00 · **Legacy report time:** 2026-11-24T11:23:02.900466+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.45 | 95.58 | +0.13% | 8.33x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | MON/USD | 0.01255 | 84.90 | -0.32% | 1.39x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 3 | GBP/USD | 1.30724 | 72.04 | +0.00% | 3.54x | STRONG 81/100 | HIGH 55/100 | Watch |
| 4 | PEPE/USD | 3.455e-06 | 60.67 | -0.26% | 1.85x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 5 | XMR/USD | 496.21 | 56.72 | +0.07% | 0.22x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 6 | 2Z/USD | 0.01608 | 47.12 | +0.19% | 0.94x | WEAK 44/100 | VERY_HIGH 74/100 | Watch |
| 7 | BAT/USD ⭐ | 0.0779 | 45.99 | +0.05% | 3.94x | STRONG 73/100 | HIGH 66/100 | Watch |
| 8 | INX/USD ⭐ | 0.003949 | 33.54 | +0.23% | 1.29x | MODERATE 52/100 | VERY_HIGH 72/100 | Watch |
| 9 | DBR/USD | 0.014 | 25.44 | -1.96% | 0.54x | WEAK 3/100 | EXTREME 100/100 | Do nothing |
| 10 | BABY/USD | 0.00856 | 25.43 | +0.00% | 0.95x | WEAK 23/100 | VERY_HIGH 79/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.442 | 93.38 | +0.13% | 8.33x | 13861 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | BAT/USD ⭐ | 0.07802 | 44.85 | +0.05% | 3.94x | 3831 | MODERATE 67/100 | VERY_HIGH 72/100 | Watch |
| 3 | INX/USD ⭐ | 0.003947 | 39.98 | +0.23% | 1.29x | 4495 | MODERATE 55/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** VVV/USD, BAT/USD, INX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
