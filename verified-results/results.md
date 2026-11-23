# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T01:11:20.189632+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45092935555
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 444351bb3561e846483b472187c24b0afe03bc65 (atomic ledger/results publication)
**Ledger generation:** 1360 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.38756 | 60.876 | 72.171 | +5.07% | -1.56% | 0.65x | 17.3 | 2026-11-23T01:11:15.928988+00:00 | Not calibrated | WEAK 30/100 | EXTREME 86/100 | Do nothing | WATCH |
| 2 | PEARL/USD | 2.0996 | 60.303 | 47.922 | +2.20% | -0.52% | 4.68x | 17.7 | 2026-11-23T01:11:15.928988+00:00 | Not calibrated | MODERATE 55/100 | HIGH 67/100 | Watch | WATCH |
| 3 | PAXG/USD | 3589.06 | 58.364 | 46.152 | +0.47% | +0.59% | 1.93x | 1.8 | 2026-11-23T01:11:15.928988+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 4 | XAUT/USD | 3588.4 | 53.414 | 35.454 | +0.46% | +0.59% | 6.36x | 1.1 | 2026-11-23T01:11:15.928988+00:00 | Not calibrated | STRONG 82/100 | HIGH 60/100 | Watch | WATCH |
| 5 | SPX/USD | 0.2837 | 21.661 | 25.966 | +0.42% | -0.18% | 0.66x | 17.7 | 2026-11-23T01:11:15.928988+00:00 | Not calibrated | WEAK 11/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 72.171 | 0.38756 | -1.56% | 0.65x |
| 2 | PEARL/USD | 47.922 | 2.0996 | -0.52% | 4.68x |
| 3 | PAXG/USD | 46.152 | 3589.06 | +0.59% | 1.93x |
| 4 | XAUT/USD | 35.454 | 3588.4 | +0.59% | 6.36x |
| 5 | SPX/USD | 25.966 | 0.2837 | -0.18% | 0.66x |

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

- Persisted scans: 1360; predictions: 11166; observations: 823346.
- Matured sampled outcomes across 1/6/24/48h: 17607; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 67 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45092935555 · **Generation:** 1360 · **Legacy run:** 45092935555
**Main quote time:** 2026-11-23T01:11:20.189632+00:00 · **Legacy report time:** 2026-11-23T01:12:27.281548+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.38756 | 60.88 | -1.56% | 0.65x | WEAK 30/100 | EXTREME 86/100 | Do nothing |
| 2 | PEARL/USD | 2.0996 | 60.30 | -0.52% | 4.68x | MODERATE 55/100 | HIGH 67/100 | Watch |
| 3 | PAXG/USD ⭐ | 3589.06 | 58.36 | +0.59% | 1.93x | STRONG 84/100 | HIGH 55/100 | Consider small entry |
| 4 | XAUT/USD ⭐ | 3588.4 | 53.41 | +0.59% | 6.36x | STRONG 92/100 | HIGH 60/100 | Consider small entry |
| 5 | SPX/USD | 0.2837 | 21.66 | -0.18% | 0.66x | WEAK 11/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PAXG/USD ⭐ | 3595.58 | 43.84 | +0.59% | 1.93x | 7018 | STRONG 72/100 | HIGH 61/100 | Watch |
| 2 | XAUT/USD ⭐ | 3589 | 42.86 | +0.59% | 6.36x | 1620 | STRONG 86/100 | HIGH 60/100 | Consider small entry |
| 3 | AUD/USD | 0.66448 | 39.36 | +0.40% | 1.32x | 3324 | MODERATE 65/100 | HIGH 55/100 | Watch |

**Same-run overlap:** PAXG/USD, XAUT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
