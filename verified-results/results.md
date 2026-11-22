# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T07:40:58.538207+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44999227382
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** adf03a63e6f9ee10b8f98120f3669ced35f91f94 (atomic ledger/results publication)
**Ledger generation:** 1252 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BLESS/USD | 0.013291 | 91.134 | 68.123 | +7.75% | +2.65% | 1.98x | 34.1 | 2026-11-22T07:40:55.022532+00:00 | Not calibrated | STRONG 81/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | PIEVERSE/USD | 3.6385 | 78.532 | 69.852 | +6.92% | -0.36% | 2.05x | 18.7 | 2026-11-22T07:40:55.022532+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | ZEC/USD | 781.75 | 58.767 | 57.389 | +0.46% | -0.19% | 1.23x | 1.7 | 2026-11-22T07:40:55.022532+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 4 | VVV/USD | 25.026 | 51.955 | 54.943 | +0.51% | +0.67% | 0.36x | 7.2 | 2026-11-22T07:40:55.022532+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | PEARL/USD | 1.9619 | 34.197 | 33.476 | +0.70% | +0.23% | 0.95x | 26.6 | 2026-11-22T07:40:55.022532+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 74/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PIEVERSE/USD | 69.852 | 3.6385 | -0.36% | 2.05x |
| 2 | BLESS/USD | 68.123 | 0.013291 | +2.65% | 1.98x |
| 3 | ZEC/USD | 57.389 | 781.75 | -0.19% | 1.23x |
| 4 | VVV/USD | 54.943 | 25.026 | +0.67% | 0.36x |
| 5 | PEARL/USD | 33.476 | 1.9619 | +0.23% | 0.95x |

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

- Persisted scans: 1252; predictions: 9968; observations: 757578.
- Matured sampled outcomes across 1/6/24/48h: 14318; gap abstentions: 22058. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 57 (sampled only; not a success-rate estimate).
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

**Writer:** 44999227382 · **Generation:** 1252 · **Legacy run:** 44999227382
**Main quote time:** 2026-11-22T07:40:58.538207+00:00 · **Legacy report time:** 2026-11-22T07:41:46.066587+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BLESS/USD | 0.013291 | 91.13 | +2.65% | 1.98x | STRONG 81/100 | HIGH 67/100 | Consider small entry |
| 2 | PIEVERSE/USD | 3.6385 | 78.53 | -0.36% | 2.05x | MODERATE 64/100 | VERY_HIGH 72/100 | Watch |
| 3 | ZEC/USD | 781.75 | 58.77 | -0.19% | 1.23x | WEAK 39/100 | HIGH 68/100 | Watch |
| 4 | VVV/USD | 25.026 | 51.95 | +0.67% | 0.36x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 5 | PEARL/USD | 1.9619 | 34.20 | +0.23% | 0.95x | WEAK 37/100 | VERY_HIGH 74/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04443 | 44.17 | +0.41% | 12.76x | 8567 | STRONG 72/100 | HIGH 61/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
