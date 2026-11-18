# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T01:30:05.006664+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44216208186
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 2c2aa8d4c23cdc850d2817457c13060b9e450730 (atomic ledger/results publication)
**Ledger generation:** 495 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 2s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 7.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UP/USD | 0.05585 | 69.429 | 52.903 | +5.40% | +0.31% | 5.02x | 32.3 | 2026-11-18T01:30:03.109477+00:00 | Not calibrated | STRONG 80/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | AKE/USD | 0.01002568 | 39.046 | 27.053 | +0.41% | +0.89% | 1.76x | 21.5 | 2026-11-18T01:30:03.109477+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | AKT/USD | 0.5158 | 34.837 | 40.197 | +1.28% | +0.43% | 0.25x | 1.9 | 2026-11-18T01:30:03.109477+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 4 | CAP/USD | 0.101814 | 30.354 | 31.708 | +0.83% | +0.22% | 0.75x | 13.4 | 2026-11-18T01:30:03.109477+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 73/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UP/USD | 52.903 | 0.05585 | +0.31% | 5.02x |
| 2 | AKT/USD | 40.197 | 0.5158 | +0.43% | 0.25x |
| 3 | CAP/USD | 31.708 | 0.101814 | +0.22% | 0.75x |
| 4 | AKE/USD | 27.053 | 0.01002568 | +0.89% | 1.76x |

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

- Persisted scans: 495; predictions: 4265; observations: 298462.
- Matured sampled outcomes across 1/6/24/48h: 3399; gap abstentions: 12410. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44216208186 · **Generation:** 495 · **Legacy run:** 44216208186
**Main quote time:** 2026-11-18T01:30:05.006664+00:00 · **Legacy report time:** 2026-11-18T01:30:15.228847+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UP/USD ⭐ | 0.05585 | 69.43 | +0.31% | 5.02x | STRONG 90/100 | VERY_HIGH 79/100 | Watch |
| 2 | AKE/USD ⭐ | 0.01002568 | 39.05 | +0.89% | 1.76x | MODERATE 65/100 | VERY_HIGH 72/100 | Watch |
| 3 | AKT/USD | 0.5158 | 34.84 | +0.43% | 0.25x | MODERATE 47/100 | VERY_HIGH 75/100 | Watch |
| 4 | CAP/USD | 0.101814 | 30.35 | +0.22% | 0.75x | WEAK 40/100 | VERY_HIGH 73/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | UP/USD ⭐ | 0.05585 | 83.93 | +0.31% | 5.02x | 3661 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | AKE/USD ⭐ | 0.01005289 | 38.89 | +0.89% | 1.76x | 5790 | MODERATE 64/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** UP/USD, AKE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
