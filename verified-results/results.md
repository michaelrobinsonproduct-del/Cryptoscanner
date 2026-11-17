# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T23:20:03.548317+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44198369563
**Source SHA:** e9b1b6ee47d56a43a454042547735fcd1cdc45a9
**Previous ledger commit:** d6ba52e98eba3f07a2b31fd706c9b680cca0e721 (atomic ledger/results publication)
**Ledger generation:** 469 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 960.07 | 122.778 | 95.918 | +6.22% | +2.37% | 3.61x | 5.3 | 2026-11-17T23:19:56.694129+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | SOL/USD | 75.05 | 113.006 | 88.883 | +4.94% | +1.82% | 8.15x | 1.3 | 2026-11-17T23:19:56.694129+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | NEAR/USD | 3.3637 | 103.466 | 99.851 | +6.52% | +1.76% | 0.48x | 0.3 | 2026-11-17T23:19:56.694129+00:00 | Not calibrated | STRONG 80/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | INJ/USD | 7.319 | 101.438 | 94.883 | +6.09% | +1.86% | 0.72x | 5.5 | 2026-11-17T23:19:56.694129+00:00 | Not calibrated | STRONG 80/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | XRP/USD | 0.9855 | 99.211 | 77.030 | +3.22% | +1.44% | 3.74x | 1.0 | 2026-11-17T23:19:56.694129+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | TAO/USD | 196.8209 | 94.277 | 72.777 | +2.94% | +1.30% | 3.29x | 5.6 | 2026-11-17T23:19:56.694129+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | RENDER/USD | 1.469 | 88.662 | 72.115 | +6.68% | +2.01% | 1.65x | 13.6 | 2026-11-17T23:19:56.694129+00:00 | Not calibrated | STRONG 84/100 | HIGH 66/100 | Consider small entry | WATCH |
| 8 | WINGS/USD | 0.001935 | 77.237 | 71.125 | +8.77% | +1.42% | 0.90x | 10.3 | 2026-11-17T23:19:56.694129+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 9 | ETH/USD | 1823.57 | 76.333 | 56.745 | +0.27% | +0.92% | 6.78x | 0.2 | 2026-11-17T23:19:56.694129+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 10 | XMR/USD | 509.55 | 70.968 | 76.472 | +3.24% | +0.22% | 0.34x | 2.4 | 2026-11-17T23:19:56.694129+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | LTC/USD | 45.18 | 63.695 | 55.033 | +1.60% | +0.49% | 1.62x | 2.2 | 2026-11-17T23:19:56.694129+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 12 | TRX/USD | 0.307645 | 60.444 | 45.151 | +0.91% | +0.06% | 6.12x | 0.6 | 2026-11-17T23:19:56.694129+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 99.851 | 3.3637 | +1.76% | 0.48x |
| 2 | ZEC/USD | 95.918 | 960.07 | +2.37% | 3.61x |
| 3 | INJ/USD | 94.883 | 7.319 | +1.86% | 0.72x |
| 4 | SOL/USD | 88.883 | 75.05 | +1.82% | 8.15x |
| 5 | XRP/USD | 77.030 | 0.9855 | +1.44% | 3.74x |
| 6 | XMR/USD | 76.472 | 509.55 | +0.22% | 0.34x |
| 7 | TAO/USD | 72.777 | 196.8209 | +1.30% | 3.29x |
| 8 | RENDER/USD | 72.115 | 1.469 | +2.01% | 1.65x |
| 9 | WINGS/USD | 71.125 | 0.001935 | +1.42% | 0.90x |
| 10 | ETH/USD | 56.745 | 1823.57 | +0.92% | 6.78x |
| 11 | LTC/USD | 55.033 | 45.18 | +0.49% | 1.62x |
| 12 | TRX/USD | 45.151 | 0.307645 | +0.06% | 6.12x |

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

- Persisted scans: 469; predictions: 4109; observations: 282628.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12398. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44198369563 · **Generation:** 469 · **Legacy run:** 44198369563
**Main quote time:** 2026-11-17T23:20:03.548317+00:00 · **Legacy report time:** 2026-11-17T23:20:15.297689+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 960.07 | 122.78 | +2.37% | 3.61x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SOL/USD ⭐ | 75.05 | 113.01 | +1.82% | 8.15x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD | 3.3637 | 103.47 | +1.76% | 0.48x | STRONG 80/100 | VERY_HIGH 70/100 | Watch |
| 4 | INJ/USD | 7.319 | 101.44 | +1.86% | 0.72x | STRONG 80/100 | VERY_HIGH 70/100 | Watch |
| 5 | XRP/USD ⭐ | 0.9855 | 99.21 | +1.44% | 3.74x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | TAO/USD ⭐ | 196.8209 | 94.28 | +1.30% | 3.29x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | RENDER/USD | 1.469 | 88.66 | +2.01% | 1.65x | STRONG 84/100 | HIGH 66/100 | Consider small entry |
| 8 | WINGS/USD | 0.001935 | 77.24 | +1.42% | 0.90x | MODERATE 64/100 | VERY_HIGH 80/100 | Watch |
| 9 | ETH/USD | 1823.57 | 76.33 | +0.92% | 6.78x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 10 | XMR/USD | 509.55 | 70.97 | +0.22% | 0.34x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 11 | LTC/USD | 45.18 | 63.70 | +0.49% | 1.62x | STRONG 77/100 | HIGH 55/100 | Watch |
| 12 | TRX/USD | 0.307645 | 60.44 | +0.06% | 6.12x | STRONG 75/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD ⭐ | 75.06 | 100.00 | +1.17% | 8.60x | 36559 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.98447 | 98.34 | +1.08% | 6.58x | 30995 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ZEC/USD ⭐ | 960.79 | 97.26 | +1.38% | 1.89x | 26448 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SUI/USD | 0.7377 | 89.53 | +0.57% | 13.61x | 8331 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | USELESS/USD | 0.0973 | 89.07 | +3.24% | 10.58x | 4152 | STRONG 95/100 | VERY_HIGH 71/100 | Watch |
| 6 | AAVE/USD | 113.01 | 86.90 | +0.86% | 1.59x | 4158 | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 7 | XDG/USD | 0.0599857 | 83.50 | +0.44% | 4.19x | 7592 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 8 | TAO/USD ⭐ | 196.8209 | 81.99 | +0.70% | 2.90x | 5387 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ZEC/USD, SOL/USD, XRP/USD, TAO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
