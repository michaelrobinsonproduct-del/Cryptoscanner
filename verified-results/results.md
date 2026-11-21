# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T19:01:17.430632+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44938487585
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** b58a4b876bbeffb7b7ac6ff6a395698abea76444 (atomic ledger/results publication)
**Ledger generation:** 1173 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.6867 | 103.542 | 88.435 | +4.91% | +0.02% | 4.57x | 1.9 | 2026-11-21T19:01:09.302706+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | XMR/USD | 484.53 | 100.295 | 93.884 | +6.19% | +0.24% | 1.52x | 8.9 | 2026-11-21T19:01:09.302706+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | NIGHT/USD | 0.04533 | 93.371 | 90.177 | +7.37% | +0.33% | 1.15x | 6.6 | 2026-11-21T19:01:09.302706+00:00 | Not calibrated | STRONG 82/100 | HIGH 62/100 | Watch | WATCH |
| 4 | XRP/USD | 0.93418 | 86.855 | 74.246 | +2.80% | +0.12% | 2.20x | 0.7 | 2026-11-21T19:01:09.302706+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 5 | ETH/USD | 1678.37 | 84.251 | 80.496 | +3.65% | -0.08% | 1.41x | 0.1 | 2026-11-21T19:01:09.302706+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0551479 | 80.604 | 66.249 | +1.61% | -0.13% | 2.79x | 0.0 | 2026-11-21T19:01:09.302706+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 7 | SOL/USD | 70.58 | 80.201 | 73.343 | +2.72% | -0.01% | 1.69x | 1.4 | 2026-11-21T19:01:09.302706+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 8 | PEARL/USD | 2.0163 | 77.135 | 78.383 | +10.28% | -0.56% | 1.16x | 27.4 | 2026-11-21T19:01:09.302706+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 9 | ZEC/USD | 787.32 | 76.792 | 81.718 | +3.88% | -0.28% | 0.65x | 0.9 | 2026-11-21T19:01:09.302706+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | TAO/USD | 186.0717 | 69.059 | 73.960 | +3.08% | +0.02% | 0.50x | 5.2 | 2026-11-21T19:01:09.302706+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | WINGS/USD | 0.001867 | 67.349 | 70.340 | +6.56% | +0.11% | 0.65x | 16.1 | 2026-11-21T19:01:09.302706+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 12 | XBT/USD | 60000.4 | 63.886 | 69.204 | +2.03% | -0.04% | 0.49x | 0.0 | 2026-11-21T19:01:09.302706+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 93.884 | 484.53 | +0.24% | 1.52x |
| 2 | NIGHT/USD | 90.177 | 0.04533 | +0.33% | 1.15x |
| 3 | UNI/USD | 88.435 | 4.6867 | +0.02% | 4.57x |
| 4 | ZEC/USD | 81.718 | 787.32 | -0.28% | 0.65x |
| 5 | ETH/USD | 80.496 | 1678.37 | -0.08% | 1.41x |
| 6 | PEARL/USD | 78.383 | 2.0163 | -0.56% | 1.16x |
| 7 | XRP/USD | 74.246 | 0.93418 | +0.12% | 2.20x |
| 8 | TAO/USD | 73.960 | 186.0717 | +0.02% | 0.50x |
| 9 | SOL/USD | 73.343 | 70.58 | -0.01% | 1.69x |
| 10 | WINGS/USD | 70.340 | 0.001867 | +0.11% | 0.65x |
| 11 | XBT/USD | 69.204 | 60000.4 | -0.04% | 0.49x |
| 12 | XDG/USD | 66.249 | 0.0551479 | -0.13% | 2.79x |

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

- Persisted scans: 1173; predictions: 9385; observations: 709543.
- Matured sampled outcomes across 1/6/24/48h: 12414; gap abstentions: 21146. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44938487585 · **Generation:** 1173 · **Legacy run:** 44938487585
**Main quote time:** 2026-11-21T19:01:17.430632+00:00 · **Legacy report time:** 2026-11-21T19:02:04.970855+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD | 4.6867 | 103.54 | +0.02% | 4.57x | STRONG 95/100 | HIGH 55/100 | Watch |
| 2 | XMR/USD ⭐ | 484.53 | 100.30 | +0.24% | 1.52x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NIGHT/USD ⭐ | 0.04533 | 93.37 | +0.33% | 1.15x | STRONG 92/100 | HIGH 62/100 | Watch |
| 4 | XRP/USD ⭐ | 0.93418 | 86.86 | +0.12% | 2.20x | STRONG 98/100 | HIGH 55/100 | Watch |
| 5 | ETH/USD | 1678.37 | 84.25 | -0.08% | 1.41x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 6 | XDG/USD | 0.0551479 | 80.60 | -0.13% | 2.79x | STRONG 70/100 | HIGH 61/100 | Watch |
| 7 | SOL/USD | 70.58 | 80.20 | -0.01% | 1.69x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 8 | PEARL/USD | 2.0163 | 77.13 | -0.56% | 1.16x | WEAK 39/100 | VERY_HIGH 80/100 | Watch |
| 9 | ZEC/USD | 787.32 | 76.79 | -0.28% | 0.65x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 10 | TAO/USD | 186.0717 | 69.06 | +0.02% | 0.50x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 11 | WINGS/USD | 0.001867 | 67.35 | +0.11% | 0.65x | MODERATE 49/100 | VERY_HIGH 81/100 | Watch |
| 12 | XBT/USD | 60000.4 | 63.89 | -0.04% | 0.49x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 483.82 | 89.58 | +0.24% | 1.52x | 12730 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.93417 | 89.50 | +0.12% | 2.20x | 58328 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | NIGHT/USD ⭐ | 0.04547 | 82.74 | +0.33% | 1.15x | 11613 | STRONG 81/100 | HIGH 68/100 | Watch |
| 4 | QNT/USD | 141.76 | 77.59 | +0.50% | 1.95x | 11169 | STRONG 84/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XMR/USD, NIGHT/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
