# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T02:47:59.577801+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45535108334
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 58b1c725600fa2432164bc4728519a7c8128d360 (atomic ledger/results publication)
**Ledger generation:** 1659 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.32879 | 67.000 | 62.493 | +4.62% | -0.15% | 1.52x | 8.8 | 2026-11-25T02:47:55.137202+00:00 | Not calibrated | MODERATE 54/100 | HIGH 66/100 | Watch | WATCH |
| 2 | MON/USD | 0.00957 | 66.191 | 44.465 | +1.06% | +1.60% | 2.37x | 20.9 | 2026-11-25T02:47:55.137202+00:00 | Not calibrated | STRONG 78/100 | HIGH 67/100 | Watch | WATCH |
| 3 | VVV/USD | 24.631 | 51.001 | 53.998 | +0.38% | +0.31% | 0.55x | 7.3 | 2026-11-25T02:47:55.137202+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | BABY/USD | 0.00838 | 44.014 | 36.816 | +1.45% | +0.12% | 1.66x | 11.9 | 2026-11-25T02:47:55.137202+00:00 | Not calibrated | MODERATE 52/100 | HIGH 66/100 | Watch | WATCH |
| 5 | STBL/USD | 0.017951 | 30.689 | 21.252 | +0.62% | +1.44% | 1.22x | 27.8 | 2026-11-25T02:47:55.137202+00:00 | Not calibrated | WEAK 40/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 62.493 | 0.32879 | -0.15% | 1.52x |
| 2 | VVV/USD | 53.998 | 24.631 | +0.31% | 0.55x |
| 3 | MON/USD | 44.465 | 0.00957 | +1.60% | 2.37x |
| 4 | BABY/USD | 36.816 | 0.00838 | +0.12% | 1.66x |
| 5 | STBL/USD | 21.252 | 0.017951 | +1.44% | 1.22x |

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

- Persisted scans: 1659; predictions: 14135; observations: 1005422.
- Matured sampled outcomes across 1/6/24/48h: 29698; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 144 (sampled only; not a success-rate estimate).
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

**Writer:** 45535108334 · **Generation:** 1659 · **Legacy run:** 45535108334
**Main quote time:** 2026-11-25T02:47:59.577801+00:00 · **Legacy report time:** 2026-11-25T02:48:54.641180+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.32879 | 67.00 | -0.15% | 1.52x | MODERATE 54/100 | HIGH 66/100 | Watch |
| 2 | MON/USD | 0.00957 | 66.19 | +1.60% | 2.37x | STRONG 78/100 | HIGH 67/100 | Watch |
| 3 | VVV/USD | 24.631 | 51.00 | +0.31% | 0.55x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 4 | BABY/USD ⭐ | 0.00838 | 44.01 | +0.12% | 1.66x | MODERATE 62/100 | HIGH 66/100 | Watch |
| 5 | STBL/USD ⭐ | 0.017951 | 30.69 | +1.44% | 1.22x | MODERATE 50/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BABY/USD ⭐ | 0.00838 | 44.00 | +0.12% | 1.66x | 4681 | MODERATE 62/100 | HIGH 66/100 | Watch |
| 2 | STBL/USD ⭐ | 0.017951 | 26.36 | +1.44% | 1.22x | 1583 | MODERATE 48/100 | EXTREME 86/100 | Do nothing |

**Same-run overlap:** BABY/USD, STBL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
