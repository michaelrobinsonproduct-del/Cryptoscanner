# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-15T01:26:10.205149+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43663041324
**Source SHA:** 7365446176ea693d0131fc36d69df44185d57614
**Previous ledger commit:** 617b9ff45c751015a3c68d346dc3f8c3577bb3c2 (atomic ledger/results publication)
**Ledger generation:** 426 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 606; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | JUP/USD | 0.249 | 49.279 | 34.861 | +0.42% | -0.12% | 2.93x | 23.3 | 2026-11-15T01:26:06.666875+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | LSK/USD | 0.144099 | 46.819 | 49.457 | +3.94% | +1.06% | 0.20x | 17.7 | 2026-11-15T01:26:06.666875+00:00 | Not calibrated | MODERATE 48/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | CAP/USD | 0.110545 | 44.443 | 35.227 | +1.13% | +0.84% | 1.50x | 18.6 | 2026-11-15T01:26:06.666875+00:00 | Not calibrated | MODERATE 62/100 | HIGH 66/100 | Watch | WATCH |
| 4 | ICNT/USD | 0.2412 | 36.742 | 36.301 | +1.09% | +0.46% | 0.81x | 4.1 | 2026-11-15T01:26:06.666875+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 5 | BAT/USD | 0.0922 | 27.782 | 27.893 | +0.30% | +0.37% | 0.80x | 17.4 | 2026-11-15T01:26:06.666875+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | FLR/USD | 0.00469 | 22.412 | 15.300 | +0.43% | +0.64% | 1.39x | 42.7 | 2026-11-15T01:26:06.666875+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LSK/USD | 49.457 | 0.144099 | +1.06% | 0.20x |
| 2 | ICNT/USD | 36.301 | 0.2412 | +0.46% | 0.81x |
| 3 | CAP/USD | 35.227 | 0.110545 | +0.84% | 1.50x |
| 4 | JUP/USD | 34.861 | 0.249 | -0.12% | 2.93x |
| 5 | BAT/USD | 27.893 | 0.0922 | +0.37% | 0.80x |
| 6 | FLR/USD | 15.300 | 0.00469 | +0.64% | 1.39x |

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

- Persisted scans: 426; predictions: 3628; observations: 256499.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 10633. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 43663041324 · **Generation:** 426 · **Legacy run:** 43663041324
**Main quote time:** 2026-11-15T01:26:10.205149+00:00 · **Legacy report time:** 2026-11-15T01:26:22.857293+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | JUP/USD | 0.249 | 49.28 | -0.12% | 2.93x | MODERATE 45/100 | VERY_HIGH 73/100 | Watch |
| 2 | LSK/USD | 0.144099 | 46.82 | +1.06% | 0.20x | MODERATE 48/100 | EXTREME 88/100 | Do nothing |
| 3 | CAP/USD ⭐ | 0.110545 | 44.44 | +0.84% | 1.50x | STRONG 72/100 | HIGH 66/100 | Watch |
| 4 | ICNT/USD | 0.2412 | 36.74 | +0.46% | 0.81x | MODERATE 48/100 | VERY_HIGH 74/100 | Watch |
| 5 | BAT/USD | 0.0922 | 27.78 | +0.37% | 0.80x | WEAK 39/100 | VERY_HIGH 73/100 | Watch |
| 6 | FLR/USD ⭐ | 0.00469 | 22.41 | +0.64% | 1.39x | MODERATE 51/100 | VERY_HIGH 82/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PAXG/USD | 3802.75 | 50.95 | +0.18% | 1.91x | 5379 | MODERATE 60/100 | HIGH 55/100 | Watch |
| 2 | CAP/USD ⭐ | 0.110545 | 50.86 | +0.84% | 1.50x | 9139 | STRONG 80/100 | HIGH 60/100 | Consider small entry |
| 3 | FLR/USD ⭐ | 0.00469 | 32.83 | +0.64% | 1.39x | 2929 | MODERATE 56/100 | VERY_HIGH 82/100 | Watch |

**Same-run overlap:** CAP/USD, FLR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
