# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T12:12:37.005798+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45611091451
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** dee9c257e95c4810c43ec985f44558c69f4f6d64 (atomic ledger/results publication)
**Ledger generation:** 1716 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.00983 | 78.321 | 64.841 | +3.80% | -0.30% | 2.61x | 20.4 | 2026-11-25T12:12:33.655322+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | BABY/USD | 0.00877 | 70.905 | 69.026 | +6.17% | +0.80% | 0.79x | 11.4 | 2026-11-25T12:12:33.655322+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 3 | VVV/USD | 24.865 | 68.902 | 59.124 | +1.33% | -0.64% | 2.30x | 10.4 | 2026-11-25T12:12:33.655322+00:00 | Not calibrated | MODERATE 59/100 | HIGH 67/100 | Watch | WATCH |
| 4 | TREAD/USD | 1.0208 | 49.970 | 41.783 | +2.13% | -1.36% | 3.34x | 8.7 | 2026-11-25T12:12:33.655322+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 5 | CT/USD | 0.1307 | 49.269 | 43.845 | +3.48% | +1.47% | 0.81x | 23.0 | 2026-11-25T12:12:33.655322+00:00 | Not calibrated | MODERATE 45/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | BABY/USD | 69.026 | 0.00877 | +0.80% | 0.79x |
| 2 | MON/USD | 64.841 | 0.00983 | -0.30% | 2.61x |
| 3 | VVV/USD | 59.124 | 24.865 | -0.64% | 2.30x |
| 4 | CT/USD | 43.845 | 0.1307 | +1.47% | 0.81x |
| 5 | TREAD/USD | 41.783 | 1.0208 | -1.36% | 3.34x |

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

- Persisted scans: 1716; predictions: 14498; observations: 1040113.
- Matured sampled outcomes across 1/6/24/48h: 31652; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45611091451 · **Generation:** 1716 · **Legacy run:** 45611091451
**Main quote time:** 2026-11-25T12:12:37.005798+00:00 · **Legacy report time:** 2026-11-25T12:13:41.309426+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.00983 | 78.32 | -0.30% | 2.61x | MODERATE 59/100 | VERY_HIGH 73/100 | Watch |
| 2 | BABY/USD | 0.00877 | 70.90 | +0.80% | 0.79x | MODERATE 60/100 | VERY_HIGH 80/100 | Watch |
| 3 | VVV/USD | 24.865 | 68.90 | -0.64% | 2.30x | MODERATE 59/100 | HIGH 67/100 | Watch |
| 4 | TREAD/USD | 1.0208 | 49.97 | -1.36% | 3.34x | MODERATE 55/100 | VERY_HIGH 77/100 | Do nothing |
| 5 | CT/USD | 0.1307 | 49.27 | +1.47% | 0.81x | MODERATE 45/100 | EXTREME 86/100 | Do nothing |

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
