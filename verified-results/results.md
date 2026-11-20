# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T09:50:42.584066+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44713976686
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** aa419b119d5c60e433b520e89a175d5982a026c4 (atomic ledger/results publication)
**Ledger generation:** 962 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 606; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AI/USD | 0.01371 | 40.000 | 41.462 | +4.10% | +0.96% | 0.38x | 36.4 | 2026-11-20T09:50:38.695330+00:00 | Not calibrated | WEAK 35/100 | EXTREME 94/100 | Do nothing | WATCH |
| 2 | SKR/USD | 0.01027 | 35.975 | 42.635 | +2.23% | -0.36% | 0.51x | 8.8 | 2026-11-20T09:50:38.695330+00:00 | Not calibrated | WEAK 23/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | HBAR/USD | 0.05394 | 35.839 | 40.031 | +0.33% | +0.06% | 0.55x | 5.6 | 2026-11-20T09:50:38.695330+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | WINGS/USD | 0.001871 | 28.556 | 25.358 | +1.46% | +1.08% | 0.78x | 32.1 | 2026-11-20T09:50:38.695330+00:00 | Not calibrated | WEAK 34/100 | EXTREME 86/100 | Do nothing | WATCH |
| 5 | MNT/USD | 0.3946 | 24.731 | 32.280 | +0.77% | +0.08% | 0.21x | 7.6 | 2026-11-20T09:50:38.695330+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKR/USD | 42.635 | 0.01027 | -0.36% | 0.51x |
| 2 | AI/USD | 41.462 | 0.01371 | +0.96% | 0.38x |
| 3 | HBAR/USD | 40.031 | 0.05394 | +0.06% | 0.55x |
| 4 | MNT/USD | 32.280 | 0.3946 | +0.08% | 0.21x |
| 5 | WINGS/USD | 25.358 | 0.001871 | +1.08% | 0.78x |

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

- Persisted scans: 962; predictions: 8149; observations: 581291.
- Matured sampled outcomes across 1/6/24/48h: 9727; gap abstentions: 17479. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44713976686 · **Generation:** 962 · **Legacy run:** 44713976686
**Main quote time:** 2026-11-20T09:50:42.584066+00:00 · **Legacy report time:** 2026-11-20T09:51:45.821851+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AI/USD | 0.01371 | 40.00 | +0.96% | 0.38x | WEAK 35/100 | EXTREME 94/100 | Do nothing |
| 2 | SKR/USD | 0.01027 | 35.98 | -0.36% | 0.51x | WEAK 23/100 | EXTREME 88/100 | Do nothing |
| 3 | HBAR/USD | 0.05394 | 35.84 | +0.06% | 0.55x | WEAK 38/100 | VERY_HIGH 70/100 | Watch |
| 4 | WINGS/USD | 0.001871 | 28.56 | +1.08% | 0.78x | WEAK 34/100 | EXTREME 86/100 | Do nothing |
| 5 | MNT/USD | 0.3946 | 24.73 | +0.08% | 0.21x | WEAK 32/100 | VERY_HIGH 82/100 | Do nothing |

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
