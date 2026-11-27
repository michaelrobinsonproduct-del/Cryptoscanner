# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T15:42:17.849263+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46026856920
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f948d43ccc48fff9c05b9f888fca1f91f215a101 (atomic ledger/results publication)
**Ledger generation:** 2027 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 741.17 | 102.479 | 98.718 | +8.73% | +1.71% | 0.52x | 2.6 | 2026-11-27T15:42:10.788249+00:00 | Not calibrated | STRONG 80/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | SPACE/USD | 0.004162 | 87.654 | 70.864 | +7.49% | +2.26% | 1.55x | 9.6 | 2026-11-27T15:42:10.788249+00:00 | Not calibrated | STRONG 89/100 | HIGH 67/100 | Consider small entry | WATCH |
| 3 | XDG/USD | 0.057583 | 86.344 | 68.781 | +2.14% | +0.51% | 11.47x | 2.4 | 2026-11-27T15:42:10.788249+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | SOL/USD | 71.94 | 82.013 | 63.477 | +1.41% | +0.71% | 2.50x | 2.8 | 2026-11-27T15:42:10.788249+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | HYPE/USD | 64.52 | 78.895 | 80.101 | +3.70% | +0.84% | 0.46x | 1.5 | 2026-11-27T15:42:10.788249+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XRP/USD | 0.94898 | 71.842 | 59.046 | +0.66% | +0.68% | 1.94x | 1.2 | 2026-11-27T15:42:10.788249+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | UNI/USD | 4.77 | 67.902 | 67.963 | +2.58% | +0.54% | 0.73x | 6.9 | 2026-11-27T15:42:10.788249+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | FET/USD | 0.1274 | 67.511 | 65.897 | +5.81% | +1.43% | 0.45x | 23.6 | 2026-11-27T15:42:10.788249+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 9 | VVV/USD | 26.923 | 67.201 | 60.015 | +2.83% | +2.22% | 0.61x | 22.0 | 2026-11-27T15:42:10.788249+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 10 | LIGHTER/USD | 2.623 | 66.544 | 67.012 | +5.68% | +1.04% | 0.43x | 11.4 | 2026-11-27T15:42:10.788249+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 11 | PAXG/USD | 3613.15 | 65.113 | 52.944 | +1.59% | +0.05% | 2.19x | 2.4 | 2026-11-27T15:42:10.788249+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 12 | SUI/USD | 0.6697 | 60.361 | 56.350 | +0.30% | +0.92% | 0.94x | 1.5 | 2026-11-27T15:42:10.788249+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.718 | 741.17 | +1.71% | 0.52x |
| 2 | HYPE/USD | 80.101 | 64.52 | +0.84% | 0.46x |
| 3 | SPACE/USD | 70.864 | 0.004162 | +2.26% | 1.55x |
| 4 | XDG/USD | 68.781 | 0.057583 | +0.51% | 11.47x |
| 5 | UNI/USD | 67.963 | 4.77 | +0.54% | 0.73x |
| 6 | LIGHTER/USD | 67.012 | 2.623 | +1.04% | 0.43x |
| 7 | FET/USD | 65.897 | 0.1274 | +1.43% | 0.45x |
| 8 | SOL/USD | 63.477 | 71.94 | +0.71% | 2.50x |
| 9 | VVV/USD | 60.015 | 26.923 | +2.22% | 0.61x |
| 10 | XRP/USD | 59.046 | 0.94898 | +0.68% | 1.94x |
| 11 | SUI/USD | 56.350 | 0.6697 | +0.92% | 0.94x |
| 12 | PAXG/USD | 52.944 | 3613.15 | +0.05% | 2.19x |

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

- Persisted scans: 2027; predictions: 18026; observations: 1227444.
- Matured sampled outcomes across 1/6/24/48h: 40301; gap abstentions: 25937. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46026856920 · **Generation:** 2027 · **Legacy run:** 46026856920
**Main quote time:** 2026-11-27T15:42:17.849263+00:00 · **Legacy report time:** 2026-11-27T15:43:11.964513+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 741.17 | 102.48 | +1.71% | 0.52x | STRONG 80/100 | VERY_HIGH 70/100 | Watch |
| 2 | SPACE/USD ⭐ | 0.004162 | 87.65 | +2.26% | 1.55x | STRONG 99/100 | HIGH 67/100 | Consider small entry |
| 3 | XDG/USD ⭐ | 0.057583 | 86.34 | +0.51% | 11.47x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SOL/USD ⭐ | 71.94 | 82.01 | +0.71% | 2.50x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | HYPE/USD | 64.52 | 78.90 | +0.84% | 0.46x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 6 | XRP/USD ⭐ | 0.94898 | 71.84 | +0.68% | 1.94x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 7 | UNI/USD | 4.77 | 67.90 | +0.54% | 0.73x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 8 | FET/USD | 0.1274 | 67.51 | +1.43% | 0.45x | MODERATE 54/100 | VERY_HIGH 82/100 | Watch |
| 9 | VVV/USD | 26.923 | 67.20 | +2.22% | 0.61x | MODERATE 54/100 | VERY_HIGH 82/100 | Watch |
| 10 | LIGHTER/USD | 2.623 | 66.54 | +1.04% | 0.43x | MODERATE 58/100 | VERY_HIGH 81/100 | Watch |
| 11 | PAXG/USD | 3613.15 | 65.11 | +0.05% | 2.19x | STRONG 78/100 | HIGH 55/100 | Watch |
| 12 | SUI/USD | 0.6697 | 60.36 | +0.92% | 0.94x | MODERATE 60/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XDG/USD ⭐ | 0.0576101 | 81.25 | +0.51% | 11.47x | 11203 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SPACE/USD ⭐ | 0.004162 | 77.63 | +2.26% | 1.55x | 2430 | STRONG 94/100 | HIGH 67/100 | Consider small entry |
| 3 | W/USD | 0.00916 | 74.76 | +1.32% | 1.03x | 2486 | MODERATE 62/100 | VERY_HIGH 79/100 | Watch |
| 4 | SOL/USD ⭐ | 71.95 | 74.43 | +0.71% | 2.50x | 41557 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | XRP/USD ⭐ | 0.95038 | 64.14 | +0.68% | 1.94x | 36394 | STRONG 87/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** SPACE/USD, XDG/USD, SOL/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
