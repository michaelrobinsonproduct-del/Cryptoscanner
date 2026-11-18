# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T05:45:04.356384+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44246344242
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** d3772aa9743f20f66093e239325a727931810050 (atomic ledger/results publication)
**Ledger generation:** 546 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.98583 | 73.097 | 57.300 | +0.34% | +0.16% | 3.71x | 0.1 | 2026-11-18T05:44:58.646671+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019894 | 69.349 | 69.213 | +6.56% | +0.88% | 0.57x | 13.6 | 2026-11-18T05:44:58.646671+00:00 | Not calibrated | MODERATE 60/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | VVV/USD | 21.168 | 67.445 | 49.427 | +0.68% | +0.60% | 18.26x | 8.0 | 2026-11-18T05:44:58.646671+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 4 | CT/USD | 0.1155 | 53.668 | 37.801 | +2.21% | +0.17% | 9.53x | 17.3 | 2026-11-18T05:44:58.646671+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | CC/USD | 0.0845 | 48.442 | 52.231 | +2.89% | +0.34% | 0.45x | 7.1 | 2026-11-18T05:44:58.646671+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 6 | XDC/USD | 0.03093 | 42.979 | 45.591 | +2.01% | +0.68% | 0.40x | 12.9 | 2026-11-18T05:44:58.646671+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | PEARL/USD | 1.8478 | 33.736 | 39.430 | +2.06% | +0.43% | 0.22x | 19.5 | 2026-11-18T05:44:58.646671+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 8 | MNT/USD | 0.3781 | 31.739 | 36.566 | +1.29% | +0.40% | 0.32x | 10.6 | 2026-11-18T05:44:58.646671+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 69.213 | 0.019894 | +0.88% | 0.57x |
| 2 | XRP/USD | 57.300 | 0.98583 | +0.16% | 3.71x |
| 3 | CC/USD | 52.231 | 0.0845 | +0.34% | 0.45x |
| 4 | VVV/USD | 49.427 | 21.168 | +0.60% | 18.26x |
| 5 | XDC/USD | 45.591 | 0.03093 | +0.68% | 0.40x |
| 6 | PEARL/USD | 39.430 | 1.8478 | +0.43% | 0.22x |
| 7 | CT/USD | 37.801 | 0.1155 | +0.17% | 9.53x |
| 8 | MNT/USD | 36.566 | 0.3781 | +0.40% | 0.32x |

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

- Persisted scans: 546; predictions: 4612; observations: 329521.
- Matured sampled outcomes across 1/6/24/48h: 3766; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44246344242 · **Generation:** 546 · **Legacy run:** 44246344242
**Main quote time:** 2026-11-18T05:45:04.356384+00:00 · **Legacy report time:** 2026-11-18T05:45:22.967551+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD | 0.98583 | 73.10 | +0.16% | 3.71x | STRONG 82/100 | HIGH 55/100 | Watch |
| 2 | SENT/USD | 0.019894 | 69.35 | +0.88% | 0.57x | MODERATE 60/100 | EXTREME 88/100 | Do nothing |
| 3 | VVV/USD ⭐ | 21.168 | 67.45 | +0.60% | 18.26x | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 4 | CT/USD ⭐ | 0.1155 | 53.67 | +0.17% | 9.53x | STRONG 77/100 | VERY_HIGH 73/100 | Watch |
| 5 | CC/USD | 0.0845 | 48.44 | +0.34% | 0.45x | MODERATE 54/100 | VERY_HIGH 75/100 | Watch |
| 6 | XDC/USD | 0.03093 | 42.98 | +0.68% | 0.40x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 7 | PEARL/USD | 1.8478 | 33.74 | +0.43% | 0.22x | WEAK 42/100 | VERY_HIGH 81/100 | Watch |
| 8 | MNT/USD | 0.3781 | 31.74 | +0.40% | 0.32x | WEAK 41/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.168 | 51.15 | +0.60% | 18.26x | 7387 | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 2 | CT/USD ⭐ | 0.1155 | 45.90 | +0.17% | 9.53x | 1229 | STRONG 73/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** VVV/USD, CT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
