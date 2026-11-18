# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T03:35:07.801540+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44231386975
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** a5204c44dcae19060f1f5e7b7140afc4e14af63c (atomic ledger/results publication)
**Ledger generation:** 520 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PIEVERSE/USD | 2.17 | 84.086 | 68.509 | +5.93% | +0.12% | 2.66x | 9.7 | 2026-11-18T03:35:03.451249+00:00 | Not calibrated | STRONG 87/100 | HIGH 60/100 | Watch | WATCH |
| 2 | XMR/USD | 514.39 | 75.606 | 56.252 | +1.08% | +0.87% | 7.24x | 12.7 | 2026-11-18T03:35:03.451249+00:00 | Not calibrated | STRONG 88/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | SENT/USD | 0.018945 | 55.245 | 38.582 | +1.48% | +0.76% | 2.29x | 5.3 | 2026-11-18T03:35:03.451249+00:00 | Not calibrated | STRONG 83/100 | HIGH 67/100 | Watch | WATCH |
| 4 | TON/USD | 1.082 | 51.233 | 37.579 | +0.46% | +0.28% | 2.23x | 9.3 | 2026-11-18T03:35:03.451249+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 5 | AKT/USD | 0.5196 | 46.189 | 44.617 | +2.02% | +0.78% | 0.77x | 3.9 | 2026-11-18T03:35:03.451249+00:00 | Not calibrated | MODERATE 53/100 | HIGH 67/100 | Watch | WATCH |
| 6 | CC/USD | 0.08367 | 43.084 | 45.897 | +1.88% | +0.23% | 0.60x | 4.8 | 2026-11-18T03:35:03.451249+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 7 | ZAMA/USD | 0.06067 | 38.070 | 36.323 | +1.23% | +0.70% | 0.83x | 11.5 | 2026-11-18T03:35:03.451249+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | PEARL/USD | 1.8305 | 34.617 | 33.370 | +1.10% | +0.58% | 0.83x | 19.2 | 2026-11-18T03:35:03.451249+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 9 | ICNT/USD | 0.2781 | 21.073 | 28.351 | +0.72% | -1.80% | 1.17x | 18.0 | 2026-11-18T03:35:03.451249+00:00 | Not calibrated | WEAK 16/100 | VERY_HIGH 83/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PIEVERSE/USD | 68.509 | 2.17 | +0.12% | 2.66x |
| 2 | XMR/USD | 56.252 | 514.39 | +0.87% | 7.24x |
| 3 | CC/USD | 45.897 | 0.08367 | +0.23% | 0.60x |
| 4 | AKT/USD | 44.617 | 0.5196 | +0.78% | 0.77x |
| 5 | SENT/USD | 38.582 | 0.018945 | +0.76% | 2.29x |
| 6 | TON/USD | 37.579 | 1.082 | +0.28% | 2.23x |
| 7 | ZAMA/USD | 36.323 | 0.06067 | +0.70% | 0.83x |
| 8 | PEARL/USD | 33.370 | 1.8305 | +0.58% | 0.83x |
| 9 | ICNT/USD | 28.351 | 0.2781 | -1.80% | 1.17x |

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

- Persisted scans: 520; predictions: 4397; observations: 313687.
- Matured sampled outcomes across 1/6/24/48h: 3518; gap abstentions: 12424. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44231386975 · **Generation:** 520 · **Legacy run:** 44231386975
**Main quote time:** 2026-11-18T03:35:07.801540+00:00 · **Legacy report time:** 2026-11-18T03:35:27.194995+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD ⭐ | 2.17 | 84.09 | +0.12% | 2.66x | STRONG 97/100 | HIGH 60/100 | Watch |
| 2 | XMR/USD ⭐ | 514.39 | 75.61 | +0.87% | 7.24x | STRONG 98/100 | HIGH 61/100 | Consider small entry |
| 3 | SENT/USD ⭐ | 0.018945 | 55.25 | +0.76% | 2.29x | STRONG 93/100 | HIGH 67/100 | Consider small entry |
| 4 | TON/USD ⭐ | 1.082 | 51.23 | +0.28% | 2.23x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 5 | AKT/USD | 0.5196 | 46.19 | +0.78% | 0.77x | MODERATE 53/100 | HIGH 67/100 | Watch |
| 6 | CC/USD | 0.08367 | 43.08 | +0.23% | 0.60x | MODERATE 52/100 | VERY_HIGH 75/100 | Watch |
| 7 | ZAMA/USD | 0.06067 | 38.07 | +0.70% | 0.83x | WEAK 44/100 | VERY_HIGH 73/100 | Watch |
| 8 | PEARL/USD | 1.8305 | 34.62 | +0.58% | 0.83x | WEAK 42/100 | VERY_HIGH 73/100 | Watch |
| 9 | ICNT/USD | 0.2781 | 21.07 | -1.80% | 1.17x | WEAK 16/100 | VERY_HIGH 83/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD ⭐ | 2.17 | 73.15 | +0.12% | 2.66x | 2043 | STRONG 82/100 | VERY_HIGH 72/100 | Watch |
| 2 | XMR/USD ⭐ | 513.83 | 59.28 | +0.87% | 7.24x | 13235 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 3 | SENT/USD ⭐ | 0.018945 | 51.08 | +0.76% | 2.29x | 3845 | STRONG 91/100 | HIGH 67/100 | Consider small entry |
| 4 | TON/USD ⭐ | 1.082 | 38.68 | +0.28% | 2.23x | 5389 | STRONG 84/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** PIEVERSE/USD, XMR/USD, SENT/USD, TON/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
