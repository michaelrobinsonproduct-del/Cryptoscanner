# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T17:01:11.182554+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45863770023
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 34ad1d0c701390f41725c15151e65dbe5f44daf0 (atomic ledger/results publication)
**Ledger generation:** 1888 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 594; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 150.45 | 86.507 | 69.537 | +3.90% | +0.39% | 3.53x | 4.6 | 2026-11-26T17:01:04.467254+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | INJ/USD | 6.18 | 82.712 | 66.007 | +3.80% | +0.34% | 2.94x | 4.8 | 2026-11-26T17:01:04.467254+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | SKY/USD | 0.04565 | 72.716 | 75.272 | +9.00% | -0.13% | 0.81x | 8.8 | 2026-11-26T17:01:04.467254+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | 2Z/USD | 0.01755 | 70.469 | 72.466 | +6.23% | -0.40% | 1.00x | 5.7 | 2026-11-26T17:01:04.467254+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | LTC/USD | 43.52 | 69.560 | 67.127 | +1.90% | -0.11% | 1.30x | 2.3 | 2026-11-26T17:01:04.467254+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 6 | WIF/USD | 0.1365 | 67.762 | 69.079 | +7.23% | +0.44% | 0.65x | 14.7 | 2026-11-26T17:01:04.467254+00:00 | Not calibrated | MODERATE 59/100 | EXTREME 88/100 | Do nothing | WATCH |
| 7 | ADA/USD | 0.148846 | 62.424 | 68.260 | +2.11% | +0.23% | 0.30x | 3.0 | 2026-11-26T17:01:04.467254+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XRP/USD | 0.95113 | 62.028 | 65.574 | +1.56% | -0.04% | 0.67x | 0.6 | 2026-11-26T17:01:04.467254+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | STBL/USD | 0.020364 | 59.280 | 66.912 | +7.83% | -0.04% | 0.26x | 18.2 | 2026-11-26T17:01:04.467254+00:00 | Not calibrated | WEAK 30/100 | EXTREME 94/100 | Do nothing | WATCH |
| 10 | SOL/USD | 71.03 | 58.158 | 60.660 | +0.91% | -0.04% | 0.77x | 1.4 | 2026-11-26T17:01:04.467254+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 11 | XBT/USD | 60538.8 | 54.351 | 56.965 | +0.28% | -0.04% | 0.76x | 0.0 | 2026-11-26T17:01:04.467254+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | XDG/USD | 0.0567076 | 50.542 | 55.181 | +1.34% | +0.07% | 0.50x | 0.0 | 2026-11-26T17:01:04.467254+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 75.272 | 0.04565 | -0.13% | 0.81x |
| 2 | 2Z/USD | 72.466 | 0.01755 | -0.40% | 1.00x |
| 3 | QNT/USD | 69.537 | 150.45 | +0.39% | 3.53x |
| 4 | WIF/USD | 69.079 | 0.1365 | +0.44% | 0.65x |
| 5 | ADA/USD | 68.260 | 0.148846 | +0.23% | 0.30x |
| 6 | LTC/USD | 67.127 | 43.52 | -0.11% | 1.30x |
| 7 | STBL/USD | 66.912 | 0.020364 | -0.04% | 0.26x |
| 8 | INJ/USD | 66.007 | 6.18 | +0.34% | 2.94x |
| 9 | XRP/USD | 65.574 | 0.95113 | -0.04% | 0.67x |
| 10 | SOL/USD | 60.660 | 71.03 | -0.04% | 0.77x |
| 11 | XBT/USD | 56.965 | 60538.8 | -0.04% | 0.76x |
| 12 | XDG/USD | 55.181 | 0.0567076 | +0.07% | 0.50x |

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

- Persisted scans: 1888; predictions: 16391; observations: 1143892.
- Matured sampled outcomes across 1/6/24/48h: 35414; gap abstentions: 25081. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45863770023 · **Generation:** 1888 · **Legacy run:** 45863770023
**Main quote time:** 2026-11-26T17:01:11.182554+00:00 · **Legacy report time:** 2026-11-26T17:02:01.719256+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 150.45 | 86.51 | +0.39% | 3.53x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | INJ/USD ⭐ | 6.18 | 82.71 | +0.34% | 2.94x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SKY/USD | 0.04565 | 72.72 | -0.13% | 0.81x | WEAK 41/100 | VERY_HIGH 73/100 | Watch |
| 4 | 2Z/USD | 0.01755 | 70.47 | -0.40% | 1.00x | WEAK 40/100 | VERY_HIGH 73/100 | Watch |
| 5 | LTC/USD | 43.52 | 69.56 | -0.11% | 1.30x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 6 | WIF/USD | 0.1365 | 67.76 | +0.44% | 0.65x | MODERATE 59/100 | EXTREME 88/100 | Do nothing |
| 7 | ADA/USD | 0.148846 | 62.42 | +0.23% | 0.30x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 8 | XRP/USD | 0.95113 | 62.03 | -0.04% | 0.67x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 9 | STBL/USD | 0.020364 | 59.28 | -0.04% | 0.26x | WEAK 30/100 | EXTREME 94/100 | Do nothing |
| 10 | SOL/USD | 71.03 | 58.16 | -0.04% | 0.77x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 11 | XBT/USD | 60538.8 | 54.35 | -0.04% | 0.76x | WEAK 32/100 | HIGH 68/100 | Do nothing |
| 12 | XDG/USD | 0.0567076 | 50.54 | +0.07% | 0.50x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 150.67 | 87.92 | +0.39% | 3.53x | 7641 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | INJ/USD ⭐ | 6.173 | 87.34 | +0.34% | 2.94x | 6418 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | AKT/USD | 0.4962 | 75.80 | +0.51% | 1.64x | 2807 | STRONG 78/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** QNT/USD, INJ/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
