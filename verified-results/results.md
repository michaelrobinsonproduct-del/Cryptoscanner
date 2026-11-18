# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T23:40:15.804840+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44422620794
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 7e7a8d68109a8db16f6d924e3778cae6252e5717 (atomic ledger/results publication)
**Ledger generation:** 697 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LUNA/USD | 4.353e-05 | 81.541 | 62.488 | +4.51% | +0.81% | 4.96x | 2.3 | 2026-11-18T23:40:11.127154+00:00 | Not calibrated | STRONG 96/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | TRX/USD | 0.30929 | 58.729 | 43.062 | +0.45% | +0.13% | 3.12x | 0.0 | 2026-11-18T23:40:11.127154+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 3 | MEGA/USD | 0.05543 | 56.965 | 65.393 | +7.34% | -0.14% | 0.23x | 21.6 | 2026-11-18T23:40:11.127154+00:00 | Not calibrated | WEAK 23/100 | EXTREME 100/100 | Do nothing | WATCH |
| 4 | AKE/USD | 0.01023319 | 47.646 | 44.562 | +2.49% | +1.27% | 0.67x | 14.8 | 2026-11-18T23:40:11.127154+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.0454 | 45.817 | 46.522 | +1.14% | +0.75% | 0.55x | 11.0 | 2026-11-18T23:40:11.127154+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | AKT/USD | 0.5183 | 36.860 | 40.242 | +1.77% | +1.05% | 0.14x | 7.7 | 2026-11-18T23:40:11.127154+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 65.393 | 0.05543 | -0.14% | 0.23x |
| 2 | LUNA/USD | 62.488 | 4.353e-05 | +0.81% | 4.96x |
| 3 | NIGHT/USD | 46.522 | 0.0454 | +0.75% | 0.55x |
| 4 | AKE/USD | 44.562 | 0.01023319 | +1.27% | 0.67x |
| 5 | TRX/USD | 43.062 | 0.30929 | +0.13% | 3.12x |
| 6 | AKT/USD | 40.242 | 0.5183 | +1.05% | 0.14x |

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

- Persisted scans: 697; predictions: 5639; observations: 421480.
- Matured sampled outcomes across 1/6/24/48h: 5499; gap abstentions: 13266. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44422620794 · **Generation:** 697 · **Legacy run:** 44422620794
**Main quote time:** 2026-11-18T23:40:15.804840+00:00 · **Legacy report time:** 2026-11-18T23:40:50.569500+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.353e-05 | 81.54 | +0.81% | 4.96x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | TRX/USD ⭐ | 0.30929 | 58.73 | +0.13% | 3.12x | STRONG 84/100 | HIGH 55/100 | Watch |
| 3 | MEGA/USD | 0.05543 | 56.97 | -0.14% | 0.23x | WEAK 23/100 | EXTREME 100/100 | Do nothing |
| 4 | AKE/USD | 0.01023319 | 47.65 | +1.27% | 0.67x | MODERATE 49/100 | VERY_HIGH 81/100 | Watch |
| 5 | NIGHT/USD | 0.0454 | 45.82 | +0.75% | 0.55x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 6 | AKT/USD | 0.5183 | 36.86 | +1.05% | 0.14x | MODERATE 48/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.345e-05 | 85.31 | +0.81% | 4.96x | 1831 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | TRX/USD ⭐ | 0.309373 | 57.02 | +0.13% | 3.12x | 4060 | STRONG 84/100 | HIGH 55/100 | Watch |

**Same-run overlap:** LUNA/USD, TRX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
