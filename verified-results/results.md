# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T00:51:27.168854+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45091022852
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 1c5c2a0adf5c6b05c2a199b5749e035d1e325f7f (atomic ledger/results publication)
**Ledger generation:** 1358 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEARL/USD | 2.1 | 79.326 | 56.382 | +2.22% | +1.62% | 2.49x | 0.5 | 2026-11-23T00:51:21.053972+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | CPOOL/USD | 0.02285 | 49.742 | 26.812 | +2.33% | +1.63% | 2.48x | 43.9 | 2026-11-23T00:51:21.053972+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | AUD/USD | 0.66447 | 42.905 | 24.946 | +0.44% | +0.59% | 4.58x | 35.6 | 2026-11-23T00:51:21.053972+00:00 | Not calibrated | MODERATE 61/100 | HIGH 67/100 | Watch | WATCH |
| 4 | SPX/USD | 0.2835 | 37.485 | 23.715 | +0.35% | -0.25% | 5.20x | 21.2 | 2026-11-23T00:51:21.053972+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 5 | CC/USD | 0.07346 | 30.179 | 36.480 | +0.26% | -0.16% | 0.45x | 1.4 | 2026-11-23T00:51:21.053972+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 56.382 | 2.1 | +1.62% | 2.49x |
| 2 | CC/USD | 36.480 | 0.07346 | -0.16% | 0.45x |
| 3 | CPOOL/USD | 26.812 | 0.02285 | +1.63% | 2.48x |
| 4 | AUD/USD | 24.946 | 0.66447 | +0.59% | 4.58x |
| 5 | SPX/USD | 23.715 | 0.2835 | -0.25% | 5.20x |

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

- Persisted scans: 1358; predictions: 11157; observations: 822128.
- Matured sampled outcomes across 1/6/24/48h: 17549; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 64 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45091022852 · **Generation:** 1358 · **Legacy run:** 45091022852
**Main quote time:** 2026-11-23T00:51:27.168854+00:00 · **Legacy report time:** 2026-11-23T00:52:28.709146+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 2.1 | 79.33 | +1.62% | 2.49x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | CPOOL/USD ⭐ | 0.02285 | 49.74 | +1.63% | 2.48x | STRONG 75/100 | VERY_HIGH 82/100 | Watch |
| 3 | AUD/USD ⭐ | 0.66447 | 42.90 | +0.59% | 4.58x | STRONG 71/100 | HIGH 67/100 | Watch |
| 4 | SPX/USD | 0.2835 | 37.49 | -0.25% | 5.20x | WEAK 39/100 | VERY_HIGH 78/100 | Watch |
| 5 | CC/USD | 0.07346 | 30.18 | -0.16% | 0.45x | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 2.1 | 80.15 | +1.62% | 2.49x | 6369 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | CPOOL/USD ⭐ | 0.02283 | 61.14 | +1.63% | 2.48x | 9346 | STRONG 86/100 | VERY_HIGH 72/100 | Watch |
| 3 | AUD/USD ⭐ | 0.66447 | 42.84 | +0.59% | 4.58x | 3319 | STRONG 76/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** PEARL/USD, CPOOL/USD, AUD/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
