# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-15T19:39:36.381799+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43753611722
**Source SHA:** 885b4a0465f5c74a8a87db5ca921c3c0a00021af
**Previous ledger commit:** 5fd8ac3514f55b2d929f93f7c9bd85f5702065e0 (atomic ledger/results publication)
**Ledger generation:** 437 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 5.1784 | 108.389 | 95.669 | +6.07% | +0.50% | 2.02x | 3.5 | 2026-11-15T19:39:29.813982+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | QNT/USD | 156.28 | 108.199 | 96.159 | +9.05% | +0.34% | 2.04x | 7.7 | 2026-11-15T19:39:29.813982+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | NEAR/USD | 3.1539 | 97.762 | 82.302 | +4.13% | +0.09% | 4.05x | 3.2 | 2026-11-15T19:39:29.813982+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ZEC/USD | 900.64 | 97.541 | 83.129 | +4.26% | -0.12% | 3.86x | 3.3 | 2026-11-15T19:39:29.813982+00:00 | Not calibrated | STRONG 79/100 | HIGH 61/100 | Watch | WATCH |
| 5 | AAVE/USD | 107.97 | 93.650 | 86.409 | +7.38% | +0.03% | 1.71x | 7.4 | 2026-11-15T19:39:29.813982+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 6 | ETH/USD | 1823.71 | 92.880 | 76.960 | +3.14% | +0.18% | 7.14x | 0.1 | 2026-11-15T19:39:29.813982+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Watch | WATCH |
| 7 | CC/USD | 0.08317 | 92.176 | 86.951 | +7.16% | +0.34% | 1.35x | 6.0 | 2026-11-15T19:39:29.813982+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Watch | WATCH |
| 8 | XRP/USD | 0.95881 | 89.533 | 89.443 | +4.93% | +0.61% | 0.71x | 0.1 | 2026-11-15T19:39:29.813982+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XMR/USD | 499.05 | 86.145 | 93.388 | +6.14% | -0.11% | 0.33x | 9.2 | 2026-11-15T19:39:29.813982+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0589212 | 84.685 | 74.606 | +2.80% | +0.16% | 1.93x | 0.0 | 2026-11-15T19:39:29.813982+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 11 | AVAX/USD | 7.241 | 82.725 | 68.412 | +2.01% | +0.32% | 2.27x | 1.4 | 2026-11-15T19:39:29.813982+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 12 | ASTER/USD | 0.54786 | 82.644 | 83.120 | +9.45% | +0.35% | 0.78x | 6.4 | 2026-11-15T19:39:29.813982+00:00 | Not calibrated | STRONG 71/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 96.159 | 156.28 | +0.34% | 2.04x |
| 2 | UNI/USD | 95.669 | 5.1784 | +0.50% | 2.02x |
| 3 | XMR/USD | 93.388 | 499.05 | -0.11% | 0.33x |
| 4 | XRP/USD | 89.443 | 0.95881 | +0.61% | 0.71x |
| 5 | CC/USD | 86.951 | 0.08317 | +0.34% | 1.35x |
| 6 | AAVE/USD | 86.409 | 107.97 | +0.03% | 1.71x |
| 7 | ZEC/USD | 83.129 | 900.64 | -0.12% | 3.86x |
| 8 | ASTER/USD | 83.120 | 0.54786 | +0.35% | 0.78x |
| 9 | NEAR/USD | 82.302 | 3.1539 | +0.09% | 4.05x |
| 10 | ETH/USD | 76.960 | 1823.71 | +0.18% | 7.14x |
| 11 | XDG/USD | 74.606 | 0.0589212 | +0.16% | 1.93x |
| 12 | AVAX/USD | 68.412 | 7.241 | +0.32% | 2.27x |

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

- Persisted scans: 437; predictions: 3760; observations: 263174.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 11129. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 43753611722 · **Generation:** 437 · **Legacy run:** 43753611722
**Main quote time:** 2026-11-15T19:39:36.381799+00:00 · **Legacy report time:** 2026-11-15T19:39:51.946086+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 5.1784 | 108.39 | +0.50% | 2.02x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | QNT/USD ⭐ | 156.28 | 108.20 | +0.34% | 2.04x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD ⭐ | 3.1539 | 97.76 | +0.09% | 4.05x | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | ZEC/USD | 900.64 | 97.54 | -0.12% | 3.86x | STRONG 79/100 | HIGH 61/100 | Watch |
| 5 | AAVE/USD | 107.97 | 93.65 | +0.03% | 1.71x | STRONG 82/100 | HIGH 55/100 | Watch |
| 6 | ETH/USD ⭐ | 1823.71 | 92.88 | +0.18% | 7.14x | STRONG 100/100 | HIGH 55/100 | Watch |
| 7 | CC/USD ⭐ | 0.08317 | 92.18 | +0.34% | 1.35x | STRONG 100/100 | HIGH 55/100 | Watch |
| 8 | XRP/USD | 0.95881 | 89.53 | +0.61% | 0.71x | STRONG 75/100 | VERY_HIGH 70/100 | Watch |
| 9 | XMR/USD | 499.05 | 86.15 | -0.11% | 0.33x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 10 | XDG/USD ⭐ | 0.0589212 | 84.69 | +0.16% | 1.93x | STRONG 87/100 | HIGH 55/100 | Watch |
| 11 | AVAX/USD | 7.241 | 82.73 | +0.32% | 2.27x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 12 | ASTER/USD | 0.54786 | 82.64 | +0.35% | 0.78x | STRONG 71/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.1542 | 100.00 | +0.09% | 4.05x | 16092 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | UNI/USD ⭐ | 5.1784 | 100.00 | +0.50% | 2.02x | 12741 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ETH/USD ⭐ | 1823.71 | 98.14 | +0.18% | 7.14x | 84504 | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | LINK/USD | 9.23525 | 94.54 | +0.41% | 1.48x | 12075 | STRONG 92/100 | HIGH 55/100 | Watch |
| 5 | SUI/USD | 0.7234 | 90.65 | +0.18% | 1.46x | 21640 | STRONG 80/100 | HIGH 55/100 | Watch |
| 6 | QNT/USD ⭐ | 156.31 | 90.15 | +0.34% | 2.04x | 9532 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | XDG/USD ⭐ | 0.0589336 | 90.05 | +0.16% | 1.93x | 21604 | STRONG 90/100 | HIGH 55/100 | Watch |
| 8 | CC/USD ⭐ | 0.08307 | 89.16 | +0.34% | 1.35x | 8874 | STRONG 100/100 | HIGH 55/100 | Watch |

**Same-run overlap:** UNI/USD, QNT/USD, NEAR/USD, ETH/USD, CC/USD, XDG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
