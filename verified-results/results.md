# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T03:57:15.239257+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45543166644
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 6c0053651fb6b591b85f5c1a4541687a10dfdbf6 (atomic ledger/results publication)
**Ledger generation:** 1666 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.00981 | 68.368 | 68.314 | +3.59% | +0.51% | 0.75x | 10.2 | 2026-11-25T03:57:10.078088+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | DRV/USD | 0.32959 | 65.866 | 64.417 | +4.87% | -2.71% | 12.97x | 10.0 | 2026-11-25T03:57:10.078088+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 3 | SKY/USD | 0.0415 | 58.388 | 39.124 | +1.27% | +0.85% | 11.25x | 7.2 | 2026-11-25T03:57:10.078088+00:00 | Not calibrated | STRONG 84/100 | HIGH 60/100 | Watch | WATCH |
| 4 | XMR/USD | 512.75 | 55.911 | 55.064 | +0.62% | -0.22% | 1.19x | 5.3 | 2026-11-25T03:57:10.078088+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 5 | VVV/USD | 24.71 | 50.249 | 56.057 | +0.70% | +0.05% | 0.39x | 7.7 | 2026-11-25T03:57:10.078088+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | SYRUP/USD | 0.07066 | 17.194 | 28.207 | +1.42% | -1.10% | 0.45x | 26.9 | 2026-11-25T03:57:10.078088+00:00 | Not calibrated | WEAK 4/100 | EXTREME 97/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 68.314 | 0.00981 | +0.51% | 0.75x |
| 2 | DRV/USD | 64.417 | 0.32959 | -2.71% | 12.97x |
| 3 | VVV/USD | 56.057 | 24.71 | +0.05% | 0.39x |
| 4 | XMR/USD | 55.064 | 512.75 | -0.22% | 1.19x |
| 5 | SKY/USD | 39.124 | 0.0415 | +0.85% | 11.25x |
| 6 | SYRUP/USD | 28.207 | 0.07066 | -1.10% | 0.45x |

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

- Persisted scans: 1666; predictions: 14170; observations: 1009685.
- Matured sampled outcomes across 1/6/24/48h: 29885; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45543166644 · **Generation:** 1666 · **Legacy run:** 45543166644
**Main quote time:** 2026-11-25T03:57:15.239257+00:00 · **Legacy report time:** 2026-11-25T03:58:08.938953+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.00981 | 68.37 | +0.51% | 0.75x | MODERATE 59/100 | VERY_HIGH 76/100 | Watch |
| 2 | DRV/USD | 0.32959 | 65.87 | -2.71% | 12.97x | MODERATE 58/100 | VERY_HIGH 76/100 | Do nothing |
| 3 | SKY/USD ⭐ | 0.0415 | 58.39 | +0.85% | 11.25x | STRONG 94/100 | HIGH 60/100 | Consider small entry |
| 4 | XMR/USD | 512.75 | 55.91 | -0.22% | 1.19x | WEAK 38/100 | HIGH 68/100 | Watch |
| 5 | VVV/USD | 24.71 | 50.25 | +0.05% | 0.39x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 6 | SYRUP/USD | 0.07066 | 17.19 | -1.10% | 0.45x | WEAK 4/100 | EXTREME 97/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.04146 | 48.93 | +0.85% | 11.25x | 4355 | STRONG 89/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
