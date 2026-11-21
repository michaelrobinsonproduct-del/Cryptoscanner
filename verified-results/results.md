# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T22:31:08.650377+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44957010272
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 019bc8b26ca33728231e373b80d45d59e3a3550a (atomic ledger/results publication)
**Ledger generation:** 1195 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 492.85 | 106.452 | 95.840 | +8.01% | +0.47% | 1.82x | 8.3 | 2026-11-21T22:31:00.397278+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | UNI/USD | 4.7085 | 89.141 | 90.659 | +5.40% | +0.07% | 0.81x | 4.2 | 2026-11-21T22:31:00.397278+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 3 | TAO/USD | 185.2206 | 88.418 | 71.697 | +2.61% | +0.34% | 6.30x | 3.2 | 2026-11-21T22:31:00.397278+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | ZEC/USD | 786.37 | 88.025 | 80.586 | +3.76% | +0.35% | 1.57x | 1.4 | 2026-11-21T22:31:00.397278+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | WINGS/USD | 0.001926 | 85.479 | 77.103 | +9.93% | +1.69% | 0.99x | 5.2 | 2026-11-21T22:31:00.397278+00:00 | Not calibrated | STRONG 73/100 | HIGH 67/100 | Watch | WATCH |
| 6 | ETH/USD | 1679.95 | 83.561 | 81.179 | +3.74% | -0.04% | 1.26x | 0.1 | 2026-11-21T22:31:00.397278+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 7 | NIGHT/USD | 0.04489 | 83.093 | 86.681 | +6.32% | +0.13% | 0.57x | 11.1 | 2026-11-21T22:31:00.397278+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | XBT/USD | 60160.1 | 77.257 | 71.105 | +2.30% | +0.01% | 1.61x | 0.0 | 2026-11-21T22:31:00.397278+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 9 | QNT/USD | 142.79 | 71.503 | 71.823 | +2.90% | +0.63% | 0.65x | 7.0 | 2026-11-21T22:31:00.397278+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | AVAX/USD | 6.567 | 71.225 | 55.844 | +0.94% | +0.08% | 8.47x | 3.0 | 2026-11-21T22:31:00.397278+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 11 | XLM/USD | 0.128723 | 66.905 | 62.015 | +1.20% | +0.17% | 1.41x | 2.7 | 2026-11-21T22:31:00.397278+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 12 | SOL/USD | 70.06 | 66.814 | 68.040 | +1.96% | +0.04% | 0.86x | 1.4 | 2026-11-21T22:31:00.397278+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 95.840 | 492.85 | +0.47% | 1.82x |
| 2 | UNI/USD | 90.659 | 4.7085 | +0.07% | 0.81x |
| 3 | NIGHT/USD | 86.681 | 0.04489 | +0.13% | 0.57x |
| 4 | ETH/USD | 81.179 | 1679.95 | -0.04% | 1.26x |
| 5 | ZEC/USD | 80.586 | 786.37 | +0.35% | 1.57x |
| 6 | WINGS/USD | 77.103 | 0.001926 | +1.69% | 0.99x |
| 7 | QNT/USD | 71.823 | 142.79 | +0.63% | 0.65x |
| 8 | TAO/USD | 71.697 | 185.2206 | +0.34% | 6.30x |
| 9 | XBT/USD | 71.105 | 60160.1 | +0.01% | 1.61x |
| 10 | SOL/USD | 68.040 | 70.06 | +0.04% | 0.86x |
| 11 | XLM/USD | 62.015 | 0.128723 | +0.17% | 1.41x |
| 12 | AVAX/USD | 55.844 | 6.567 | +0.08% | 8.47x |

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

- Persisted scans: 1195; predictions: 9649; observations: 722919.
- Matured sampled outcomes across 1/6/24/48h: 12916; gap abstentions: 21537. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44957010272 · **Generation:** 1195 · **Legacy run:** 44957010272
**Main quote time:** 2026-11-21T22:31:08.650377+00:00 · **Legacy report time:** 2026-11-21T22:32:00.177504+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 492.85 | 106.45 | +0.47% | 1.82x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UNI/USD | 4.7085 | 89.14 | +0.07% | 0.81x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 3 | TAO/USD ⭐ | 185.2206 | 88.42 | +0.34% | 6.30x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | ZEC/USD ⭐ | 786.37 | 88.02 | +0.35% | 1.57x | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 5 | WINGS/USD | 0.001926 | 85.48 | +1.69% | 0.99x | STRONG 73/100 | HIGH 67/100 | Watch |
| 6 | ETH/USD | 1679.95 | 83.56 | -0.04% | 1.26x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 7 | NIGHT/USD | 0.04489 | 83.09 | +0.13% | 0.57x | MODERATE 57/100 | VERY_HIGH 76/100 | Watch |
| 8 | XBT/USD | 60160.1 | 77.26 | +0.01% | 1.61x | STRONG 74/100 | HIGH 55/100 | Watch |
| 9 | QNT/USD | 142.79 | 71.50 | +0.63% | 0.65x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 10 | AVAX/USD | 6.567 | 71.23 | +0.08% | 8.47x | STRONG 81/100 | HIGH 55/100 | Watch |
| 11 | XLM/USD | 0.128723 | 66.90 | +0.17% | 1.41x | MODERATE 68/100 | HIGH 55/100 | Watch |
| 12 | SOL/USD | 70.06 | 66.81 | +0.04% | 0.86x | MODERATE 53/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 786.38 | 93.53 | +0.35% | 1.57x | 39904 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD ⭐ | 492.85 | 89.72 | +0.47% | 1.82x | 12005 | STRONG 95/100 | HIGH 61/100 | Consider small entry |
| 3 | SPX/USD | 0.2796 | 78.74 | +1.05% | 2.08x | 2490 | STRONG 89/100 | HIGH 66/100 | Consider small entry |
| 4 | TAO/USD ⭐ | 185.208 | 77.30 | +0.34% | 6.30x | 10936 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XMR/USD, TAO/USD, ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
