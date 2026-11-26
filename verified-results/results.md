# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T19:31:06.560977+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45884025400
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1fc4cdfc53f70ef591aae108826ef7363d343bf2 (atomic ledger/results publication)
**Ledger generation:** 1903 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 597; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LINK/USD | 9.2683 | 84.063 | 68.755 | +2.47% | +0.06% | 2.51x | 4.2 | 2026-11-26T19:30:58.341637+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 2 | INJ/USD | 6.25 | 83.141 | 72.178 | +4.97% | +0.03% | 2.08x | 4.8 | 2026-11-26T19:30:58.341637+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ZRO/USD | 1.107 | 82.017 | 72.399 | +8.11% | -1.08% | 2.81x | 18.1 | 2026-11-26T19:30:58.341637+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | FET/USD | 0.1205 | 80.302 | 70.230 | +11.06% | -0.41% | 2.21x | 16.6 | 2026-11-26T19:30:58.341637+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | XRP/USD | 0.95331 | 78.968 | 67.467 | +1.79% | +0.03% | 2.13x | 0.1 | 2026-11-26T19:30:58.341637+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 6 | ADA/USD | 0.150593 | 75.861 | 77.430 | +3.31% | +0.15% | 0.77x | 1.5 | 2026-11-26T19:30:58.341637+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 7 | WIF/USD | 0.1406 | 74.163 | 73.246 | +10.45% | +0.21% | 0.98x | 7.1 | 2026-11-26T19:30:58.341637+00:00 | Not calibrated | MODERATE 67/100 | HIGH 67/100 | Watch | WATCH |
| 8 | DRV/USD | 0.39072 | 73.422 | 73.537 | +9.20% | -1.93% | 1.95x | 18.2 | 2026-11-26T19:30:58.341637+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 71/100 | Do nothing | WATCH |
| 9 | SKY/USD | 0.04543 | 70.400 | 68.779 | +8.48% | +0.46% | 0.93x | 22.0 | 2026-11-26T19:30:58.341637+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 10 | AKT/USD | 0.5075 | 68.436 | 76.946 | +7.27% | +0.12% | 0.09x | 2.0 | 2026-11-26T19:30:58.341637+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 11 | SOL/USD | 71.34 | 65.781 | 63.747 | +1.35% | +0.08% | 1.16x | 1.4 | 2026-11-26T19:30:58.341637+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XBT/USD | 60555.4 | 62.262 | 57.158 | +0.31% | +0.14% | 1.44x | 0.0 | 2026-11-26T19:30:58.341637+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ADA/USD | 77.430 | 0.150593 | +0.15% | 0.77x |
| 2 | AKT/USD | 76.946 | 0.5075 | +0.12% | 0.09x |
| 3 | DRV/USD | 73.537 | 0.39072 | -1.93% | 1.95x |
| 4 | WIF/USD | 73.246 | 0.1406 | +0.21% | 0.98x |
| 5 | ZRO/USD | 72.399 | 1.107 | -1.08% | 2.81x |
| 6 | INJ/USD | 72.178 | 6.25 | +0.03% | 2.08x |
| 7 | FET/USD | 70.230 | 0.1205 | -0.41% | 2.21x |
| 8 | SKY/USD | 68.779 | 0.04543 | +0.46% | 0.93x |
| 9 | LINK/USD | 68.755 | 9.2683 | +0.06% | 2.51x |
| 10 | XRP/USD | 67.467 | 0.95331 | +0.03% | 2.13x |
| 11 | SOL/USD | 63.747 | 71.34 | +0.08% | 1.16x |
| 12 | XBT/USD | 57.158 | 60555.4 | +0.14% | 1.44x |

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

- Persisted scans: 1903; predictions: 16571; observations: 1152832.
- Matured sampled outcomes across 1/6/24/48h: 35936; gap abstentions: 25189. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45884025400 · **Generation:** 1903 · **Legacy run:** 45884025400
**Main quote time:** 2026-11-26T19:31:06.560977+00:00 · **Legacy report time:** 2026-11-26T19:31:48.098464+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD ⭐ | 9.2683 | 84.06 | +0.06% | 2.51x | STRONG 97/100 | HIGH 55/100 | Watch |
| 2 | INJ/USD | 6.25 | 83.14 | +0.03% | 2.08x | STRONG 87/100 | HIGH 55/100 | Watch |
| 3 | ZRO/USD | 1.107 | 82.02 | -1.08% | 2.81x | MODERATE 66/100 | VERY_HIGH 76/100 | Watch |
| 4 | FET/USD | 0.1205 | 80.30 | -0.41% | 2.21x | MODERATE 65/100 | VERY_HIGH 72/100 | Watch |
| 5 | XRP/USD | 0.95331 | 78.97 | +0.03% | 2.13x | STRONG 84/100 | HIGH 55/100 | Watch |
| 6 | ADA/USD | 0.150593 | 75.86 | +0.15% | 0.77x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 7 | WIF/USD | 0.1406 | 74.16 | +0.21% | 0.98x | MODERATE 67/100 | HIGH 67/100 | Watch |
| 8 | DRV/USD | 0.39072 | 73.42 | -1.93% | 1.95x | MODERATE 52/100 | VERY_HIGH 71/100 | Do nothing |
| 9 | SKY/USD | 0.04543 | 70.40 | +0.46% | 0.93x | MODERATE 55/100 | VERY_HIGH 79/100 | Watch |
| 10 | AKT/USD | 0.5075 | 68.44 | +0.12% | 0.09x | MODERATE 54/100 | VERY_HIGH 75/100 | Watch |
| 11 | SOL/USD | 71.34 | 65.78 | +0.08% | 1.16x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 12 | XBT/USD | 60555.4 | 62.26 | +0.14% | 1.44x | MODERATE 66/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD ⭐ | 9.26434 | 82.99 | +0.06% | 2.51x | 6910 | STRONG 96/100 | HIGH 55/100 | Watch |
| 2 | CRV/USD | 0.17857 | 82.45 | +0.33% | 5.04x | 3902 | STRONG 91/100 | HIGH 66/100 | Consider small entry |
| 3 | LTC/USD | 43.49 | 77.15 | +0.14% | 2.86x | 14438 | STRONG 84/100 | HIGH 55/100 | Watch |

**Same-run overlap:** LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
