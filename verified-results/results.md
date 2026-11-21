# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T02:15:25.098749+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44854778843
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 7ec5aa431355f88a2b3ac7ad9d514e52de720e33 (atomic ledger/results publication)
**Ledger generation:** 1062 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.205 | 59.831 | 67.659 | +2.25% | -0.52% | 0.48x | 6.1 | 2026-11-21T02:15:17.204167+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | SKY/USD | 0.04439 | 57.969 | 41.274 | +1.25% | +0.34% | 5.96x | 6.8 | 2026-11-21T02:15:17.204167+00:00 | Not calibrated | STRONG 84/100 | HIGH 60/100 | Watch | WATCH |
| 3 | XDG/USD | 0.0545532 | 57.368 | 58.560 | +0.51% | +0.18% | 0.79x | 0.1 | 2026-11-21T02:15:17.204167+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 4 | ADA/USD | 0.143344 | 53.438 | 55.431 | +0.35% | +0.23% | 0.69x | 4.0 | 2026-11-21T02:15:17.204167+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | DCR/USD | 10.22 | 49.132 | 32.857 | +1.14% | +0.26% | 6.24x | 11.7 | 2026-11-21T02:15:17.204167+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | STBL/USD | 0.016121 | 44.370 | 38.691 | +1.54% | +0.74% | 1.20x | 6.2 | 2026-11-21T02:15:17.204167+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 7 | ALGO/USD | 0.07342 | 35.722 | 37.843 | +0.36% | -0.10% | 0.84x | 6.8 | 2026-11-21T02:15:17.204167+00:00 | Not calibrated | WEAK 23/100 | HIGH 68/100 | Do nothing | WATCH |
| 8 | DOT/USD | 0.665 | 32.207 | 37.737 | +0.61% | -0.01% | 0.45x | 1.5 | 2026-11-21T02:15:17.204167+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 67.659 | 21.205 | -0.52% | 0.48x |
| 2 | XDG/USD | 58.560 | 0.0545532 | +0.18% | 0.79x |
| 3 | ADA/USD | 55.431 | 0.143344 | +0.23% | 0.69x |
| 4 | SKY/USD | 41.274 | 0.04439 | +0.34% | 5.96x |
| 5 | STBL/USD | 38.691 | 0.016121 | +0.74% | 1.20x |
| 6 | ALGO/USD | 37.843 | 0.07342 | -0.10% | 0.84x |
| 7 | DOT/USD | 37.737 | 0.665 | -0.01% | 0.45x |
| 8 | DCR/USD | 32.857 | 10.22 | +0.26% | 6.24x |

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

- Persisted scans: 1062; predictions: 8526; observations: 642056.
- Matured sampled outcomes across 1/6/24/48h: 10955; gap abstentions: 19366. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 16; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44854778843 · **Generation:** 1062 · **Legacy run:** 44854778843
**Main quote time:** 2026-11-21T02:15:25.098749+00:00 · **Legacy report time:** 2026-11-21T02:16:06.816571+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 21.205 | 59.83 | -0.52% | 0.48x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 2 | SKY/USD ⭐ | 0.04439 | 57.97 | +0.34% | 5.96x | STRONG 94/100 | HIGH 60/100 | Consider small entry |
| 3 | XDG/USD | 0.0545532 | 57.37 | +0.18% | 0.79x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 4 | ADA/USD | 0.143344 | 53.44 | +0.23% | 0.69x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 5 | DCR/USD | 10.22 | 49.13 | +0.26% | 6.24x | STRONG 75/100 | VERY_HIGH 73/100 | Watch |
| 6 | STBL/USD ⭐ | 0.016121 | 44.37 | +0.74% | 1.20x | MODERATE 67/100 | VERY_HIGH 74/100 | Watch |
| 7 | ALGO/USD | 0.07342 | 35.72 | -0.10% | 0.84x | WEAK 23/100 | HIGH 68/100 | Do nothing |
| 8 | DOT/USD | 0.665 | 32.21 | -0.01% | 0.45x | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.04438 | 49.32 | +0.34% | 5.96x | 5842 | STRONG 90/100 | HIGH 60/100 | Consider small entry |
| 2 | STBL/USD ⭐ | 0.016121 | 42.71 | +0.74% | 1.20x | 2011 | MODERATE 66/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** SKY/USD, STBL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
