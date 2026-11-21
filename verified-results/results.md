# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T21:30:57.135748+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44951800796
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 947006b2f5d63bfadd73277609d0fb2c19a83ab2 (atomic ledger/results publication)
**Ledger generation:** 1188 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 489 | 108.329 | 97.441 | +7.17% | -0.40% | 2.29x | 5.1 | 2026-11-21T21:30:49.438142+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | UNI/USD | 4.71 | 105.459 | 91.027 | +5.44% | +0.08% | 2.40x | 4.0 | 2026-11-21T21:30:49.438142+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04475 | 104.143 | 86.340 | +5.99% | +0.56% | 4.61x | 8.9 | 2026-11-21T21:30:49.438142+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | PEARL/USD | 2.0011 | 90.723 | 78.240 | +9.45% | +0.09% | 2.20x | 22.5 | 2026-11-21T21:30:49.438142+00:00 | Not calibrated | STRONG 80/100 | HIGH 67/100 | Watch | WATCH |
| 5 | ETH/USD | 1682.88 | 79.458 | 82.446 | +3.93% | -0.04% | 0.72x | 0.1 | 2026-11-21T21:30:49.438142+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | ZEC/USD | 791.9 | 75.126 | 84.877 | +4.48% | -0.33% | 0.19x | 3.0 | 2026-11-21T21:30:49.438142+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | SOL/USD | 70.38 | 73.122 | 71.303 | +2.43% | -0.07% | 1.22x | 1.4 | 2026-11-21T21:30:49.438142+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XBT/USD | 60283.3 | 70.325 | 72.572 | +2.51% | -0.06% | 0.81x | 0.0 | 2026-11-21T21:30:49.438142+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 9 | QNT/USD | 142.28 | 65.215 | 70.649 | +2.54% | -0.26% | 0.59x | 4.2 | 2026-11-21T21:30:49.438142+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | TAO/USD | 185.382 | 62.246 | 71.508 | +2.70% | -0.11% | 0.13x | 4.8 | 2026-11-21T21:30:49.438142+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XRP/USD | 0.92751 | 62.151 | 69.051 | +2.07% | -0.18% | 0.40x | 0.9 | 2026-11-21T21:30:49.438142+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | XDG/USD | 0.055123 | 60.099 | 65.837 | +1.56% | -0.03% | 0.44x | 0.2 | 2026-11-21T21:30:49.438142+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 97.441 | 489 | -0.40% | 2.29x |
| 2 | UNI/USD | 91.027 | 4.71 | +0.08% | 2.40x |
| 3 | NIGHT/USD | 86.340 | 0.04475 | +0.56% | 4.61x |
| 4 | ZEC/USD | 84.877 | 791.9 | -0.33% | 0.19x |
| 5 | ETH/USD | 82.446 | 1682.88 | -0.04% | 0.72x |
| 6 | PEARL/USD | 78.240 | 2.0011 | +0.09% | 2.20x |
| 7 | XBT/USD | 72.572 | 60283.3 | -0.06% | 0.81x |
| 8 | TAO/USD | 71.508 | 185.382 | -0.11% | 0.13x |
| 9 | SOL/USD | 71.303 | 70.38 | -0.07% | 1.22x |
| 10 | QNT/USD | 70.649 | 142.28 | -0.26% | 0.59x |
| 11 | XRP/USD | 69.051 | 0.92751 | -0.18% | 0.40x |
| 12 | XDG/USD | 65.837 | 0.055123 | -0.03% | 0.44x |

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

- Persisted scans: 1188; predictions: 9565; observations: 718663.
- Matured sampled outcomes across 1/6/24/48h: 12772; gap abstentions: 21464. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44951800796 · **Generation:** 1188 · **Legacy run:** 44951800796
**Main quote time:** 2026-11-21T21:30:57.135748+00:00 · **Legacy report time:** 2026-11-21T21:31:37.468029+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 489 | 108.33 | -0.40% | 2.29x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | UNI/USD ⭐ | 4.71 | 105.46 | +0.08% | 2.40x | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | NIGHT/USD ⭐ | 0.04475 | 104.14 | +0.56% | 4.61x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | PEARL/USD ⭐ | 2.0011 | 90.72 | +0.09% | 2.20x | STRONG 90/100 | HIGH 67/100 | Watch |
| 5 | ETH/USD | 1682.88 | 79.46 | -0.04% | 0.72x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 6 | ZEC/USD | 791.9 | 75.13 | -0.33% | 0.19x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 7 | SOL/USD | 70.38 | 73.12 | -0.07% | 1.22x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 8 | XBT/USD | 60283.3 | 70.32 | -0.06% | 0.81x | WEAK 40/100 | HIGH 68/100 | Watch |
| 9 | QNT/USD | 142.28 | 65.22 | -0.26% | 0.59x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 10 | TAO/USD | 185.382 | 62.25 | -0.11% | 0.13x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 11 | XRP/USD | 0.92751 | 62.15 | -0.18% | 0.40x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 12 | XDG/USD | 0.055123 | 60.10 | -0.03% | 0.44x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.7072 | 100.00 | +0.08% | 2.40x | 11042 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.04484 | 91.02 | +0.56% | 4.61x | 11511 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | PEARL/USD ⭐ | 2.0038 | 83.80 | +0.09% | 2.20x | 11133 | STRONG 82/100 | HIGH 67/100 | Watch |
| 4 | PIEVERSE/USD | 3.4051 | 81.81 | +0.38% | 5.21x | 2672 | STRONG 91/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** UNI/USD, NIGHT/USD, PEARL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
