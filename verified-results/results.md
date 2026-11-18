# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T13:25:13.061664+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44313413152
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 302ab6b75cc0a67974a76ad6237ac80df3c5be6e (atomic ledger/results publication)
**Ledger generation:** 576 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04641 | 63.330 | 68.963 | +3.39% | +0.24% | 0.32x | 6.5 | 2026-11-18T13:25:06.805064+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | VVV/USD | 21.382 | 61.368 | 53.181 | +1.69% | +1.53% | 1.05x | 14.0 | 2026-11-18T13:25:06.805064+00:00 | Not calibrated | MODERATE 61/100 | HIGH 68/100 | Watch | WATCH |
| 3 | AKT/USD | 0.5215 | 60.053 | 42.548 | +2.40% | +0.50% | 2.68x | 13.4 | 2026-11-18T13:25:06.805064+00:00 | Not calibrated | STRONG 80/100 | HIGH 66/100 | Watch | WATCH |
| 4 | SENT/USD | 0.019536 | 55.351 | 59.962 | +4.64% | +0.09% | 0.50x | 7.2 | 2026-11-18T13:25:06.805064+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | AKE/USD | 0.01013665 | 48.880 | 34.286 | +1.53% | +0.13% | 2.39x | 19.9 | 2026-11-18T13:25:06.805064+00:00 | Not calibrated | MODERATE 64/100 | HIGH 66/100 | Watch | WATCH |
| 6 | CC/USD | 0.08331 | 47.274 | 42.627 | +1.44% | -0.05% | 1.49x | 6.0 | 2026-11-18T13:25:06.805064+00:00 | Not calibrated | WEAK 44/100 | HIGH 66/100 | Watch | WATCH |
| 7 | TRX/USD | 0.309543 | 42.665 | 45.184 | +0.53% | +0.12% | 0.69x | 0.0 | 2026-11-18T13:25:06.805064+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | USELESS/USD | 0.1002 | 41.280 | 49.740 | +2.69% | -0.24% | 0.27x | 21.9 | 2026-11-18T13:25:06.805064+00:00 | Not calibrated | WEAK 16/100 | EXTREME 88/100 | Do nothing | WATCH |
| 9 | CAP/USD | 0.10173 | 27.879 | 33.521 | +0.75% | +0.65% | 0.11x | 6.1 | 2026-11-18T13:25:06.805064+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 68.963 | 0.04641 | +0.24% | 0.32x |
| 2 | SENT/USD | 59.962 | 0.019536 | +0.09% | 0.50x |
| 3 | VVV/USD | 53.181 | 21.382 | +1.53% | 1.05x |
| 4 | USELESS/USD | 49.740 | 0.1002 | -0.24% | 0.27x |
| 5 | TRX/USD | 45.184 | 0.309543 | +0.12% | 0.69x |
| 6 | CC/USD | 42.627 | 0.08331 | -0.05% | 1.49x |
| 7 | AKT/USD | 42.548 | 0.5215 | +0.50% | 2.68x |
| 8 | AKE/USD | 34.286 | 0.01013665 | +0.13% | 2.39x |
| 9 | CAP/USD | 33.521 | 0.10173 | +0.65% | 0.11x |

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

- Persisted scans: 576; predictions: 4871; observations: 347791.
- Matured sampled outcomes across 1/6/24/48h: 4226; gap abstentions: 13041. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44313413152 · **Generation:** 576 · **Legacy run:** 44313413152
**Main quote time:** 2026-11-18T13:25:13.061664+00:00 · **Legacy report time:** 2026-11-18T13:25:36.679948+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04641 | 63.33 | +0.24% | 0.32x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 2 | VVV/USD ⭐ | 21.382 | 61.37 | +1.53% | 1.05x | STRONG 71/100 | HIGH 68/100 | Watch |
| 3 | AKT/USD ⭐ | 0.5215 | 60.05 | +0.50% | 2.68x | STRONG 90/100 | HIGH 66/100 | Consider small entry |
| 4 | SENT/USD | 0.019536 | 55.35 | +0.09% | 0.50x | MODERATE 48/100 | VERY_HIGH 82/100 | Watch |
| 5 | AKE/USD ⭐ | 0.01013665 | 48.88 | +0.13% | 2.39x | STRONG 74/100 | HIGH 66/100 | Watch |
| 6 | CC/USD | 0.08331 | 47.27 | -0.05% | 1.49x | WEAK 44/100 | HIGH 66/100 | Watch |
| 7 | TRX/USD | 0.309543 | 42.67 | +0.12% | 0.69x | WEAK 41/100 | VERY_HIGH 70/100 | Watch |
| 8 | USELESS/USD | 0.1002 | 41.28 | -0.24% | 0.27x | WEAK 16/100 | EXTREME 88/100 | Do nothing |
| 9 | CAP/USD | 0.10173 | 27.88 | +0.65% | 0.11x | WEAK 44/100 | VERY_HIGH 82/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5215 | 71.65 | +0.50% | 2.68x | 4575 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 21.382 | 58.13 | +1.53% | 1.05x | 7027 | MODERATE 69/100 | HIGH 68/100 | Watch |
| 3 | AKE/USD ⭐ | 0.01013665 | 48.41 | +0.13% | 2.39x | 3126 | MODERATE 69/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** VVV/USD, AKT/USD, AKE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
