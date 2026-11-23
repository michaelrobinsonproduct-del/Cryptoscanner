# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T02:51:16.891911+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45102389857
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** b1cb2eb7c1804530357abd51e5ed96f7e2655ad4 (atomic ledger/results publication)
**Ledger generation:** 1371 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.3641 | 66.355 | 48.609 | +3.38% | +0.55% | 5.05x | 16.5 | 2026-11-23T02:51:13.720768+00:00 | Not calibrated | STRONG 83/100 | HIGH 66/100 | Watch | WATCH |
| 2 | BLESS/USD | 0.016893 | 54.674 | 52.276 | +4.97% | +1.57% | 0.45x | 42.3 | 2026-11-23T02:51:13.720768+00:00 | Not calibrated | WEAK 42/100 | EXTREME 92/100 | Do nothing | WATCH |
| 3 | DRV/USD | 0.37131 | 50.320 | 44.201 | +0.67% | +0.13% | 1.55x | 10.5 | 2026-11-23T02:51:13.720768+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 4 | CAP/USD | 0.093884 | 24.782 | 31.665 | +0.33% | +0.04% | 0.29x | 6.1 | 2026-11-23T02:51:13.720768+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 75/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | BLESS/USD | 52.276 | 0.016893 | +1.57% | 0.45x |
| 2 | ICNT/USD | 48.609 | 0.3641 | +0.55% | 5.05x |
| 3 | DRV/USD | 44.201 | 0.37131 | +0.13% | 1.55x |
| 4 | CAP/USD | 31.665 | 0.093884 | +0.04% | 0.29x |

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

- Persisted scans: 1371; predictions: 11231; observations: 830044.
- Matured sampled outcomes across 1/6/24/48h: 18026; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 88 (sampled only; not a success-rate estimate).
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

**Writer:** 45102389857 · **Generation:** 1371 · **Legacy run:** 45102389857
**Main quote time:** 2026-11-23T02:51:16.891911+00:00 · **Legacy report time:** 2026-11-23T02:52:11.462676+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.3641 | 66.36 | +0.55% | 5.05x | STRONG 93/100 | HIGH 66/100 | Consider small entry |
| 2 | BLESS/USD | 0.016893 | 54.67 | +1.57% | 0.45x | WEAK 42/100 | EXTREME 92/100 | Do nothing |
| 3 | DRV/USD ⭐ | 0.37131 | 50.32 | +0.13% | 1.55x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 4 | CAP/USD | 0.093884 | 24.78 | +0.04% | 0.29x | WEAK 32/100 | VERY_HIGH 75/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.3647 | 76.16 | +0.55% | 5.05x | 2648 | STRONG 98/100 | HIGH 66/100 | Consider small entry |
| 2 | DRV/USD ⭐ | 0.37131 | 41.45 | +0.13% | 1.55x | 17503 | MODERATE 61/100 | HIGH 61/100 | Watch |

**Same-run overlap:** ICNT/USD, DRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
