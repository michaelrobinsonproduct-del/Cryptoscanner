# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T16:40:10.278396+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44349770225
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 535ff37927a67cafbdb89fe3bb5f012339a2a27a (atomic ledger/results publication)
**Ledger generation:** 614 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MEGA/USD | 0.05301 | 56.344 | 43.074 | +2.65% | +0.57% | 2.04x | 13.2 | 2026-11-18T16:40:07.208952+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | SENT/USD | 0.01948 | 51.493 | 57.347 | +4.34% | -0.08% | 0.46x | 8.2 | 2026-11-18T16:40:07.208952+00:00 | Not calibrated | WEAK 31/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | AKE/USD | 0.01009889 | 38.295 | 27.732 | +1.15% | -0.56% | 2.34x | 27.6 | 2026-11-18T16:40:07.208952+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 4 | CT/USD | 0.1154 | 32.929 | 37.238 | +2.12% | +0.17% | 0.48x | 17.4 | 2026-11-18T16:40:07.208952+00:00 | Not calibrated | WEAK 31/100 | EXTREME 88/100 | Do nothing | WATCH |
| 5 | TRUST/USD | 0.04888 | 32.031 | 43.696 | +3.67% | -1.51% | 0.59x | 28.6 | 2026-11-18T16:40:07.208952+00:00 | Not calibrated | WEAK 11/100 | EXTREME 97/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 57.347 | 0.01948 | -0.08% | 0.46x |
| 2 | TRUST/USD | 43.696 | 0.04888 | -1.51% | 0.59x |
| 3 | MEGA/USD | 43.074 | 0.05301 | +0.57% | 2.04x |
| 4 | CT/USD | 37.238 | 0.1154 | +0.17% | 0.48x |
| 5 | AKE/USD | 27.732 | 0.01009889 | -0.56% | 2.34x |

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

- Persisted scans: 614; predictions: 5266; observations: 370933.
- Matured sampled outcomes across 1/6/24/48h: 4499; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44349770225 · **Generation:** 614 · **Legacy run:** 44349770225
**Main quote time:** 2026-11-18T16:40:10.278396+00:00 · **Legacy report time:** 2026-11-18T16:40:39.363172+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.05301 | 56.34 | +0.57% | 2.04x | STRONG 88/100 | VERY_HIGH 73/100 | Watch |
| 2 | SENT/USD | 0.01948 | 51.49 | -0.08% | 0.46x | WEAK 31/100 | EXTREME 88/100 | Do nothing |
| 3 | AKE/USD | 0.01009889 | 38.29 | -0.56% | 2.34x | WEAK 39/100 | VERY_HIGH 78/100 | Watch |
| 4 | CT/USD | 0.1154 | 32.93 | +0.17% | 0.48x | WEAK 31/100 | EXTREME 88/100 | Do nothing |
| 5 | TRUST/USD | 0.04888 | 32.03 | -1.51% | 0.59x | WEAK 11/100 | EXTREME 97/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.05291 | 45.85 | +0.57% | 2.04x | 1174 | STRONG 83/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** MEGA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
