# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T08:53:47.967098+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44886712739
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 2d8c85132fb37041e66761749741bf5cfd602ebf (atomic ledger/results publication)
**Ledger generation:** 1111 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.619 | 76.960 | 80.768 | +4.24% | +0.61% | 0.31x | 7.9 | 2026-11-21T08:53:42.770797+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | CAP/USD | 0.09429 | 66.090 | 52.622 | +3.00% | +0.32% | 2.19x | 4.1 | 2026-11-21T08:53:42.770797+00:00 | Not calibrated | STRONG 88/100 | HIGH 60/100 | Watch | WATCH |
| 3 | ETH/USD | 1629.23 | 57.690 | 58.486 | +0.61% | +0.88% | 0.48x | 1.6 | 2026-11-21T08:53:42.770797+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | TRX/USD | 0.302537 | 56.226 | 57.030 | +0.34% | +0.20% | 0.82x | 0.0 | 2026-11-21T08:53:42.770797+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 5 | RARE/USD | 0.01384 | 35.301 | 45.805 | +4.06% | -1.43% | 0.66x | 29.1 | 2026-11-21T08:53:42.770797+00:00 | Not calibrated | WEAK 13/100 | EXTREME 97/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 80.768 | 21.619 | +0.61% | 0.31x |
| 2 | ETH/USD | 58.486 | 1629.23 | +0.88% | 0.48x |
| 3 | TRX/USD | 57.030 | 0.302537 | +0.20% | 0.82x |
| 4 | CAP/USD | 52.622 | 0.09429 | +0.32% | 2.19x |
| 5 | RARE/USD | 45.805 | 0.01384 | -1.43% | 0.66x |

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

- Persisted scans: 1111; predictions: 8728; observations: 671847.
- Matured sampled outcomes across 1/6/24/48h: 11453; gap abstentions: 20253. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44886712739 · **Generation:** 1111 · **Legacy run:** 44886712739
**Main quote time:** 2026-11-21T08:53:47.967098+00:00 · **Legacy report time:** 2026-11-21T08:54:29.929680+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 21.619 | 76.96 | +0.61% | 0.31x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 2 | CAP/USD ⭐ | 0.09429 | 66.09 | +0.32% | 2.19x | STRONG 98/100 | HIGH 60/100 | Consider small entry |
| 3 | ETH/USD | 1629.23 | 57.69 | +0.88% | 0.48x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 4 | TRX/USD | 0.302537 | 56.23 | +0.20% | 0.82x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 5 | RARE/USD | 0.01384 | 35.30 | -1.43% | 0.66x | WEAK 13/100 | EXTREME 97/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CAP/USD ⭐ | 0.09429 | 65.93 | +0.32% | 2.19x | 4808 | STRONG 98/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** CAP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
