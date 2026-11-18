# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T17:10:10.893060+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44355471125
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 393046ad398ceb82ef6f4c4225c51a5b2d2b82b8 (atomic ledger/results publication)
**Ledger generation:** 620 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TRUST/USD | 0.04929 | 67.221 | 52.829 | +4.54% | -0.12% | 2.96x | 22.5 | 2026-11-18T17:10:06.791129+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019705 | 66.529 | 65.838 | +5.55% | +0.43% | 0.85x | 8.1 | 2026-11-18T17:10:06.791129+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | AKE/USD | 0.0100692 | 48.560 | 30.232 | +0.85% | +1.93% | 1.87x | 18.6 | 2026-11-18T17:10:06.791129+00:00 | Not calibrated | MODERATE 64/100 | HIGH 66/100 | Watch | WATCH |
| 4 | MEGA/USD | 0.05319 | 42.356 | 38.976 | +3.00% | +0.43% | 1.12x | 26.3 | 2026-11-18T17:10:06.791129+00:00 | Not calibrated | MODERATE 46/100 | EXTREME 86/100 | Do nothing | WATCH |
| 5 | CC/USD | 0.08249 | 37.250 | 36.136 | +0.44% | +0.72% | 0.75x | 4.8 | 2026-11-18T17:10:06.791129+00:00 | Not calibrated | MODERATE 49/100 | HIGH 67/100 | Watch | WATCH |
| 6 | ZAMA/USD | 0.06022 | 27.513 | 29.102 | +0.48% | +0.38% | 0.65x | 11.7 | 2026-11-18T17:10:06.791129+00:00 | Not calibrated | WEAK 39/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 65.838 | 0.019705 | +0.43% | 0.85x |
| 2 | TRUST/USD | 52.829 | 0.04929 | -0.12% | 2.96x |
| 3 | MEGA/USD | 38.976 | 0.05319 | +0.43% | 1.12x |
| 4 | CC/USD | 36.136 | 0.08249 | +0.72% | 0.75x |
| 5 | AKE/USD | 30.232 | 0.0100692 | +1.93% | 1.87x |
| 6 | ZAMA/USD | 29.102 | 0.06022 | +0.38% | 0.65x |

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

- Persisted scans: 620; predictions: 5292; observations: 374587.
- Matured sampled outcomes across 1/6/24/48h: 4568; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44355471125 · **Generation:** 620 · **Legacy run:** 44355471125
**Main quote time:** 2026-11-18T17:10:10.893060+00:00 · **Legacy report time:** 2026-11-18T17:10:34.080835+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TRUST/USD | 0.04929 | 67.22 | -0.12% | 2.96x | MODERATE 54/100 | VERY_HIGH 78/100 | Watch |
| 2 | SENT/USD | 0.019705 | 66.53 | +0.43% | 0.85x | MODERATE 63/100 | VERY_HIGH 74/100 | Watch |
| 3 | AKE/USD ⭐ | 0.0100692 | 48.56 | +1.93% | 1.87x | STRONG 74/100 | HIGH 66/100 | Watch |
| 4 | MEGA/USD ⭐ | 0.05319 | 42.36 | +0.43% | 1.12x | MODERATE 56/100 | EXTREME 86/100 | Do nothing |
| 5 | CC/USD | 0.08249 | 37.25 | +0.72% | 0.75x | MODERATE 49/100 | HIGH 67/100 | Watch |
| 6 | ZAMA/USD | 0.06022 | 27.51 | +0.38% | 0.65x | WEAK 39/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.05319 | 48.40 | +0.43% | 1.12x | 1190 | MODERATE 59/100 | EXTREME 86/100 | Do nothing |
| 2 | AKE/USD ⭐ | 0.01009478 | 46.69 | +1.93% | 1.87x | 2878 | MODERATE 68/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** AKE/USD, MEGA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
