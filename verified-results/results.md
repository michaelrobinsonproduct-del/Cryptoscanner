# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T07:31:36.066084+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45348396046
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c7a44da1cf81ff6b46618bb3a86195b89eac2339 (atomic ledger/results publication)
**Ledger generation:** 1544 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEPE/USD | 3.559e-06 | 74.760 | 76.017 | +4.00% | +0.25% | 0.75x | 5.6 | 2026-11-24T07:31:29.776764+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | XRP/USD | 0.94292 | 71.317 | 57.259 | +0.38% | -0.19% | 2.57x | 0.7 | 2026-11-24T07:31:29.776764+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 3 | VVV/USD | 25.394 | 69.326 | 79.132 | +3.87% | -0.75% | 0.40x | 5.9 | 2026-11-24T07:31:29.776764+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | XMR/USD | 499.43 | 66.753 | 68.601 | +2.76% | +0.24% | 0.70x | 11.4 | 2026-11-24T07:31:29.776764+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | HYPE/USD | 64.01 | 63.477 | 57.507 | +0.58% | -0.30% | 1.74x | 3.1 | 2026-11-24T07:31:29.776764+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.04949 | 63.245 | 65.889 | +2.78% | -0.34% | 0.91x | 6.1 | 2026-11-24T07:31:29.776764+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 7 | NEAR/USD | 3.0165 | 62.331 | 61.299 | +1.18% | -0.60% | 1.40x | 4.0 | 2026-11-24T07:31:29.776764+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 8 | WLD/USD | 0.2428 | 60.392 | 46.419 | +1.89% | -0.21% | 3.85x | 4.1 | 2026-11-24T07:31:29.776764+00:00 | Not calibrated | MODERATE 60/100 | HIGH 66/100 | Watch | WATCH |
| 9 | LINK/USD | 9.06019 | 57.922 | 57.887 | +0.61% | -0.31% | 1.16x | 2.8 | 2026-11-24T07:31:29.776764+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 10 | LTC/USD | 41.62 | 57.788 | 57.178 | +0.48% | -0.19% | 1.16x | 2.4 | 2026-11-24T07:31:29.776764+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 11 | BAT/USD | 0.08012 | 56.954 | 57.752 | +3.82% | +0.01% | 0.91x | 2.5 | 2026-11-24T07:31:29.776764+00:00 | Not calibrated | MODERATE 48/100 | HIGH 67/100 | Watch | WATCH |
| 12 | TIA/USD | 0.3422 | 54.838 | 43.840 | +1.91% | -0.03% | 2.11x | 2.9 | 2026-11-24T07:31:29.776764+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 79.132 | 25.394 | -0.75% | 0.40x |
| 2 | PEPE/USD | 76.017 | 3.559e-06 | +0.25% | 0.75x |
| 3 | XMR/USD | 68.601 | 499.43 | +0.24% | 0.70x |
| 4 | NIGHT/USD | 65.889 | 0.04949 | -0.34% | 0.91x |
| 5 | NEAR/USD | 61.299 | 3.0165 | -0.60% | 1.40x |
| 6 | LINK/USD | 57.887 | 9.06019 | -0.31% | 1.16x |
| 7 | BAT/USD | 57.752 | 0.08012 | +0.01% | 0.91x |
| 8 | HYPE/USD | 57.507 | 64.01 | -0.30% | 1.74x |
| 9 | XRP/USD | 57.259 | 0.94292 | -0.19% | 2.57x |
| 10 | LTC/USD | 57.178 | 41.62 | -0.19% | 1.16x |
| 11 | WLD/USD | 46.419 | 0.2428 | -0.21% | 3.85x |
| 12 | TIA/USD | 43.840 | 0.3422 | -0.03% | 2.11x |

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

- Persisted scans: 1544; predictions: 13261; observations: 935394.
- Matured sampled outcomes across 1/6/24/48h: 24966; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 139 (sampled only; not a success-rate estimate).
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

**Writer:** 45348396046 · **Generation:** 1544 · **Legacy run:** 45348396046
**Main quote time:** 2026-11-24T07:31:36.066084+00:00 · **Legacy report time:** 2026-11-24T07:32:26.196704+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 3.559e-06 | 74.76 | +0.25% | 0.75x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 2 | XRP/USD | 0.94292 | 71.32 | -0.19% | 2.57x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 3 | VVV/USD | 25.394 | 69.33 | -0.75% | 0.40x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 4 | XMR/USD | 499.43 | 66.75 | +0.24% | 0.70x | MODERATE 58/100 | VERY_HIGH 76/100 | Watch |
| 5 | HYPE/USD | 64.01 | 63.48 | -0.30% | 1.74x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 6 | NIGHT/USD | 0.04949 | 63.25 | -0.34% | 0.91x | WEAK 37/100 | HIGH 68/100 | Watch |
| 7 | NEAR/USD | 3.0165 | 62.33 | -0.60% | 1.40x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 8 | WLD/USD | 0.2428 | 60.39 | -0.21% | 3.85x | MODERATE 60/100 | HIGH 66/100 | Watch |
| 9 | LINK/USD | 9.06019 | 57.92 | -0.31% | 1.16x | WEAK 39/100 | HIGH 68/100 | Watch |
| 10 | LTC/USD | 41.62 | 57.79 | -0.19% | 1.16x | WEAK 39/100 | HIGH 68/100 | Watch |
| 11 | BAT/USD | 0.08012 | 56.95 | +0.01% | 0.91x | MODERATE 48/100 | HIGH 67/100 | Watch |
| 12 | TIA/USD | 0.3422 | 54.84 | -0.03% | 2.11x | MODERATE 57/100 | HIGH 66/100 | Watch |

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
