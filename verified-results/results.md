# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T09:00:43.255661+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44887420537
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** a33965d0d4b3e92ea7f38107fbe7791c40a952ce (atomic ledger/results publication)
**Ledger generation:** 1112 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.489 | 74.776 | 77.056 | +3.62% | -0.05% | 0.80x | 6.5 | 2026-11-21T09:00:36.816790+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 2 | TRX/USD | 0.302297 | 71.196 | 56.229 | +0.26% | -0.01% | 2.60x | 1.2 | 2026-11-21T09:00:36.816790+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ETH/USD | 1625.53 | 55.369 | 57.654 | +0.38% | +0.11% | 0.72x | 0.1 | 2026-11-21T09:00:36.816790+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | CAP/USD | 0.094183 | 48.008 | 48.777 | +2.88% | +0.50% | 0.68x | 10.2 | 2026-11-21T09:00:36.816790+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 5 | RARE/USD | 0.01391 | 45.601 | 49.504 | +4.59% | +0.51% | 0.36x | 29.1 | 2026-11-21T09:00:36.816790+00:00 | Not calibrated | WEAK 43/100 | EXTREME 87/100 | Do nothing | WATCH |
| 6 | CT/USD | 0.1241 | 37.001 | 36.904 | +2.48% | +1.06% | 0.48x | 24.3 | 2026-11-21T09:00:36.816790+00:00 | Not calibrated | WEAK 39/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 77.056 | 21.489 | -0.05% | 0.80x |
| 2 | ETH/USD | 57.654 | 1625.53 | +0.11% | 0.72x |
| 3 | TRX/USD | 56.229 | 0.302297 | -0.01% | 2.60x |
| 4 | RARE/USD | 49.504 | 0.01391 | +0.51% | 0.36x |
| 5 | CAP/USD | 48.777 | 0.094183 | +0.50% | 0.68x |
| 6 | CT/USD | 36.904 | 0.1241 | +1.06% | 0.48x |

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

- Persisted scans: 1112; predictions: 8734; observations: 672455.
- Matured sampled outcomes across 1/6/24/48h: 11473; gap abstentions: 20263. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44887420537 · **Generation:** 1112 · **Legacy run:** 44887420537
**Main quote time:** 2026-11-21T09:00:43.255661+00:00 · **Legacy report time:** 2026-11-21T09:01:33.357587+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 21.489 | 74.78 | -0.05% | 0.80x | WEAK 42/100 | HIGH 68/100 | Watch |
| 2 | TRX/USD | 0.302297 | 71.20 | -0.01% | 2.60x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 3 | ETH/USD | 1625.53 | 55.37 | +0.11% | 0.72x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 4 | CAP/USD | 0.094183 | 48.01 | +0.50% | 0.68x | MODERATE 49/100 | VERY_HIGH 81/100 | Watch |
| 5 | RARE/USD | 0.01391 | 45.60 | +0.51% | 0.36x | WEAK 43/100 | EXTREME 87/100 | Do nothing |
| 6 | CT/USD | 0.1241 | 37.00 | +1.06% | 0.48x | WEAK 39/100 | EXTREME 87/100 | Do nothing |

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
