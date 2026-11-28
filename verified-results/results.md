# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T13:42:40.632787+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46150701991
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c57b62895e7d0b7e38c810179f24ffea1e55a5bf (atomic ledger/results publication)
**Ledger generation:** 2161 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05424 | 90.055 | 96.313 | +7.96% | -0.37% | 0.56x | 7.4 | 2026-11-28T13:42:37.737751+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | XMR/USD | 431.7 | 83.115 | 81.828 | +6.00% | -0.30% | 1.28x | 30.3 | 2026-11-28T13:42:37.737751+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | SENT/USD | 0.024467 | 63.471 | 50.239 | +3.18% | -0.35% | 3.12x | 7.0 | 2026-11-28T13:42:37.737751+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | VVV/USD | 26.36 | 41.535 | 55.143 | +2.37% | -1.25% | 0.26x | 9.9 | 2026-11-28T13:42:37.737751+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 5 | AKE/USD | 0.00112031 | 39.351 | 36.521 | +3.11% | +1.23% | 0.67x | 41.8 | 2026-11-28T13:42:37.737751+00:00 | Not calibrated | WEAK 35/100 | EXTREME 97/100 | Do nothing | WATCH |
| 6 | SKY/USD | 0.05227 | 38.095 | 37.765 | +0.71% | +1.25% | 0.41x | 11.5 | 2026-11-28T13:42:37.737751+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 96.313 | 0.05424 | -0.37% | 0.56x |
| 2 | XMR/USD | 81.828 | 431.7 | -0.30% | 1.28x |
| 3 | VVV/USD | 55.143 | 26.36 | -1.25% | 0.26x |
| 4 | SENT/USD | 50.239 | 0.024467 | -0.35% | 3.12x |
| 5 | SKY/USD | 37.765 | 0.05227 | +1.25% | 0.41x |
| 6 | AKE/USD | 36.521 | 0.00112031 | +1.23% | 0.67x |

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

- Persisted scans: 2161; predictions: 19236; observations: 1308612.
- Matured sampled outcomes across 1/6/24/48h: 46121; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46150701991 · **Generation:** 2161 · **Legacy run:** 46150701991
**Main quote time:** 2026-11-28T13:42:40.632787+00:00 · **Legacy report time:** 2026-11-28T13:43:21.088294+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.05424 | 90.05 | -0.37% | 0.56x | MODERATE 50/100 | VERY_HIGH 76/100 | Watch |
| 2 | XMR/USD | 431.7 | 83.12 | -0.30% | 1.28x | WEAK 42/100 | VERY_HIGH 73/100 | Watch |
| 3 | SENT/USD | 0.024467 | 63.47 | -0.35% | 3.12x | MODERATE 62/100 | VERY_HIGH 73/100 | Watch |
| 4 | VVV/USD | 26.36 | 41.53 | -1.25% | 0.26x | WEAK 26/100 | VERY_HIGH 80/100 | Do nothing |
| 5 | AKE/USD | 0.00112031 | 39.35 | +1.23% | 0.67x | WEAK 35/100 | EXTREME 97/100 | Do nothing |
| 6 | SKY/USD | 0.05227 | 38.09 | +1.25% | 0.41x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |

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
