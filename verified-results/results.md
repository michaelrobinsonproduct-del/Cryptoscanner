# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T23:25:26.449544+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44420493858
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** b389232f1bc390333c6b2fbb79699551cc3893dd (atomic ledger/results publication)
**Ledger generation:** 694 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MEGA/USD | 0.05551 | 82.716 | 68.076 | +7.49% | -0.07% | 7.01x | 16.2 | 2026-11-18T23:25:21.851680+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | LUNA/USD | 4.326e-05 | 78.686 | 57.821 | +3.87% | +1.96% | 2.11x | 2.3 | 2026-11-18T23:25:21.851680+00:00 | Not calibrated | STRONG 94/100 | HIGH 60/100 | Consider small entry | WATCH |
| 3 | NIGHT/USD | 0.04506 | 53.085 | 43.498 | +0.38% | -0.49% | 2.20x | 6.7 | 2026-11-18T23:25:21.851680+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 4 | AKT/USD | 0.5129 | 49.772 | 31.831 | +0.71% | +0.59% | 19.08x | 9.8 | 2026-11-18T23:25:21.851680+00:00 | Not calibrated | STRONG 80/100 | HIGH 60/100 | Watch | WATCH |
| 5 | TRX/USD | 0.308881 | 36.825 | 42.038 | +0.32% | +0.08% | 0.44x | 0.0 | 2026-11-18T23:25:21.851680+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | AKE/USD | 0.01010517 | 32.532 | 32.327 | +1.21% | +0.07% | 0.99x | 21.1 | 2026-11-18T23:25:21.851680+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 68.076 | 0.05551 | -0.07% | 7.01x |
| 2 | LUNA/USD | 57.821 | 4.326e-05 | +1.96% | 2.11x |
| 3 | NIGHT/USD | 43.498 | 0.04506 | -0.49% | 2.20x |
| 4 | TRX/USD | 42.038 | 0.308881 | +0.08% | 0.44x |
| 5 | AKE/USD | 32.327 | 0.01010517 | +0.07% | 0.99x |
| 6 | AKT/USD | 31.831 | 0.5129 | +0.59% | 19.08x |

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

- Persisted scans: 694; predictions: 5622; observations: 419653.
- Matured sampled outcomes across 1/6/24/48h: 5475; gap abstentions: 13230. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44420493858 · **Generation:** 694 · **Legacy run:** 44420493858
**Main quote time:** 2026-11-18T23:25:26.449544+00:00 · **Legacy report time:** 2026-11-18T23:25:58.120981+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD | 0.05551 | 82.72 | -0.07% | 7.01x | MODERATE 66/100 | VERY_HIGH 79/100 | Watch |
| 2 | LUNA/USD ⭐ | 4.326e-05 | 78.69 | +1.96% | 2.11x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | NIGHT/USD | 0.04506 | 53.08 | -0.49% | 2.20x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 4 | AKT/USD ⭐ | 0.5129 | 49.77 | +0.59% | 19.08x | STRONG 90/100 | HIGH 60/100 | Consider small entry |
| 5 | TRX/USD | 0.308881 | 36.82 | +0.08% | 0.44x | WEAK 38/100 | VERY_HIGH 70/100 | Watch |
| 6 | AKE/USD | 0.01010517 | 32.53 | +0.07% | 0.99x | WEAK 26/100 | VERY_HIGH 79/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.326e-05 | 82.93 | +1.96% | 2.11x | 1765 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | AKT/USD ⭐ | 0.5129 | 52.40 | +0.59% | 19.08x | 4029 | STRONG 91/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** LUNA/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
