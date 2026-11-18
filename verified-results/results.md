# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T21:40:09.252495+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44403743839
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 4ffd4a1a1d58a7f099c55941ed3d5aef012bb21b (atomic ledger/results publication)
**Ledger generation:** 674 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.020173 | 71.527 | 73.452 | +8.06% | +0.23% | 0.69x | 5.5 | 2026-11-18T21:40:05.384182+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | VVV/USD | 21.35 | 58.831 | 56.071 | +1.54% | +0.25% | 1.15x | 6.1 | 2026-11-18T21:40:05.384182+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 3 | TRX/USD | 0.308696 | 42.567 | 41.659 | +0.26% | +0.02% | 1.08x | 0.0 | 2026-11-18T21:40:05.384182+00:00 | Not calibrated | MODERATE 46/100 | HIGH 62/100 | Watch | WATCH |
| 4 | AKT/USD | 0.512 | 36.645 | 30.588 | +0.53% | -0.23% | 1.72x | 9.8 | 2026-11-18T21:40:05.384182+00:00 | Not calibrated | WEAK 38/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 73.452 | 0.020173 | +0.23% | 0.69x |
| 2 | VVV/USD | 56.071 | 21.35 | +0.25% | 1.15x |
| 3 | TRX/USD | 41.659 | 0.308696 | +0.02% | 1.08x |
| 4 | AKT/USD | 30.588 | 0.512 | -0.23% | 1.72x |

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

- Persisted scans: 674; predictions: 5547; observations: 407473.
- Matured sampled outcomes across 1/6/24/48h: 5200; gap abstentions: 13146. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44403743839 · **Generation:** 674 · **Legacy run:** 44403743839
**Main quote time:** 2026-11-18T21:40:09.252495+00:00 · **Legacy report time:** 2026-11-18T21:40:35.988184+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.020173 | 71.53 | +0.23% | 0.69x | MODERATE 66/100 | VERY_HIGH 82/100 | Watch |
| 2 | VVV/USD ⭐ | 21.35 | 58.83 | +0.25% | 1.15x | STRONG 74/100 | HIGH 62/100 | Watch |
| 3 | TRX/USD | 0.308696 | 42.57 | +0.02% | 1.08x | MODERATE 46/100 | HIGH 62/100 | Watch |
| 4 | AKT/USD | 0.512 | 36.65 | -0.23% | 1.72x | WEAK 38/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.35 | 56.59 | +0.25% | 1.15x | 7569 | STRONG 73/100 | HIGH 62/100 | Watch |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
