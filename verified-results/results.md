# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T16:42:26.742048+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45439692328
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c2e92dc6569958a7dd85f05bfcc3373186d4ac63 (atomic ledger/results publication)
**Ledger generation:** 1599 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 2s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | GBP/USD | 1.31089 | 73.554 | 58.798 | +0.59% | -0.05% | 4.39x | 0.6 | 2026-11-24T16:42:24.359104+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XMR/USD | 495.84 | 65.436 | 64.092 | +2.02% | +0.19% | 1.04x | 10.1 | 2026-11-24T16:42:24.359104+00:00 | Not calibrated | MODERATE 53/100 | HIGH 68/100 | Watch | WATCH |
| 3 | VVV/USD | 24.673 | 57.981 | 57.387 | +0.92% | -0.57% | 1.34x | 8.1 | 2026-11-24T16:42:24.359104+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |
| 4 | LUNA/USD | 4.609e-05 | 49.456 | 59.484 | +6.03% | -0.43% | 0.21x | 28.2 | 2026-11-24T16:42:24.359104+00:00 | Not calibrated | WEAK 20/100 | EXTREME 100/100 | Do nothing | WATCH |
| 5 | ICNT/USD | 0.3213 | 42.874 | 52.833 | +3.95% | -0.16% | 0.08x | 15.6 | 2026-11-24T16:42:24.359104+00:00 | Not calibrated | WEAK 21/100 | EXTREME 87/100 | Do nothing | WATCH |
| 6 | 2Z/USD | 0.01602 | 32.342 | 34.820 | +2.36% | +0.25% | 0.63x | 24.9 | 2026-11-24T16:42:24.359104+00:00 | Not calibrated | WEAK 36/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 64.092 | 495.84 | +0.19% | 1.04x |
| 2 | LUNA/USD | 59.484 | 4.609e-05 | -0.43% | 0.21x |
| 3 | GBP/USD | 58.798 | 1.31089 | -0.05% | 4.39x |
| 4 | VVV/USD | 57.387 | 24.673 | -0.57% | 1.34x |
| 5 | ICNT/USD | 52.833 | 0.3213 | -0.16% | 0.08x |
| 6 | 2Z/USD | 34.820 | 0.01602 | +0.25% | 0.63x |

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

- Persisted scans: 1599; predictions: 13749; observations: 968883.
- Matured sampled outcomes across 1/6/24/48h: 27461; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45439692328 · **Generation:** 1599 · **Legacy run:** 45439692328
**Main quote time:** 2026-11-24T16:42:26.742048+00:00 · **Legacy report time:** 2026-11-24T16:43:38.846918+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | GBP/USD | 1.31089 | 73.55 | -0.05% | 4.39x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 2 | XMR/USD ⭐ | 495.84 | 65.44 | +0.19% | 1.04x | MODERATE 63/100 | HIGH 68/100 | Watch |
| 3 | VVV/USD | 24.673 | 57.98 | -0.57% | 1.34x | MODERATE 49/100 | HIGH 61/100 | Watch |
| 4 | LUNA/USD | 4.609e-05 | 49.46 | -0.43% | 0.21x | WEAK 20/100 | EXTREME 100/100 | Do nothing |
| 5 | ICNT/USD | 0.3213 | 42.87 | -0.16% | 0.08x | WEAK 21/100 | EXTREME 87/100 | Do nothing |
| 6 | 2Z/USD | 0.01602 | 32.34 | +0.25% | 0.63x | WEAK 36/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 494.47 | 58.63 | +0.19% | 1.04x | 9434 | MODERATE 64/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
