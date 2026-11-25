# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T13:42:56.229803+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45625841935
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f3597260b76b9b93d0e2fe84707a706ddc4a804b (atomic ledger/results publication)
**Ledger generation:** 1725 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.33038 | 71.571 | 72.754 | +5.12% | -0.24% | 1.00x | 2.1 | 2026-11-25T13:42:51.864459+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 2 | VVV/USD | 24.979 | 69.531 | 62.766 | +1.80% | -1.65% | 5.31x | 9.6 | 2026-11-25T13:42:51.864459+00:00 | Not calibrated | MODERATE 65/100 | HIGH 65/100 | Do nothing | WATCH |
| 3 | ZEUS/USD | 0.00501 | 62.651 | 57.572 | +8.21% | -1.98% | 5.02x | 40.2 | 2026-11-25T13:42:51.864459+00:00 | Not calibrated | MODERATE 46/100 | EXTREME 92/100 | Do nothing | WATCH |
| 4 | MOODENG/USD | 0.02707 | 60.586 | 60.916 | +11.26% | -0.84% | 1.39x | 33.4 | 2026-11-25T13:42:51.864459+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 5 | INX/USD | 0.003944 | 25.291 | 34.840 | +2.95% | -1.50% | 0.79x | 33.0 | 2026-11-25T13:42:51.864459+00:00 | Not calibrated | WEAK 8/100 | EXTREME 96/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 72.754 | 0.33038 | -0.24% | 1.00x |
| 2 | VVV/USD | 62.766 | 24.979 | -1.65% | 5.31x |
| 3 | MOODENG/USD | 60.916 | 0.02707 | -0.84% | 1.39x |
| 4 | ZEUS/USD | 57.572 | 0.00501 | -1.98% | 5.02x |
| 5 | INX/USD | 34.840 | 0.003944 | -1.50% | 0.79x |

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

- Persisted scans: 1725; predictions: 14549; observations: 1045585.
- Matured sampled outcomes across 1/6/24/48h: 31966; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45625841935 · **Generation:** 1725 · **Legacy run:** 45625841935
**Main quote time:** 2026-11-25T13:42:56.229803+00:00 · **Legacy report time:** 2026-11-25T13:44:13.166356+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.33038 | 71.57 | -0.24% | 1.00x | WEAK 41/100 | HIGH 68/100 | Watch |
| 2 | VVV/USD | 24.979 | 69.53 | -1.65% | 5.31x | MODERATE 65/100 | HIGH 65/100 | Do nothing |
| 3 | ZEUS/USD | 0.00501 | 62.65 | -1.98% | 5.02x | MODERATE 46/100 | EXTREME 92/100 | Do nothing |
| 4 | MOODENG/USD | 0.02707 | 60.59 | -0.84% | 1.39x | WEAK 40/100 | VERY_HIGH 78/100 | Watch |
| 5 | INX/USD | 0.003944 | 25.29 | -1.50% | 0.79x | WEAK 8/100 | EXTREME 96/100 | Do nothing |

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
