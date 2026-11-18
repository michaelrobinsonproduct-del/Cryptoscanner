# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T23:20:20.436872+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44419754808
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 71dcadf92074f061fbc07c010101a06f78e6e4f8 (atomic ledger/results publication)
**Ledger generation:** 693 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MEGA/USD | 0.05522 | 81.859 | 66.225 | +6.93% | +0.13% | 17.69x | 19.9 | 2026-11-18T23:20:15.767149+00:00 | Not calibrated | STRONG 81/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04513 | 53.920 | 43.550 | +0.53% | -0.09% | 2.08x | 8.9 | 2026-11-18T23:20:15.767149+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LUNA/USD | 4.289e-05 | 48.633 | 51.496 | +2.98% | +0.63% | 0.40x | 2.3 | 2026-11-18T23:20:15.767149+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 4 | AKE/USD | 0.01014088 | 39.478 | 36.478 | +1.57% | +0.52% | 1.04x | 17.9 | 2026-11-18T23:20:15.767149+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 73/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 66.225 | 0.05522 | +0.13% | 17.69x |
| 2 | LUNA/USD | 51.496 | 4.289e-05 | +0.63% | 0.40x |
| 3 | NIGHT/USD | 43.550 | 0.04513 | -0.09% | 2.08x |
| 4 | AKE/USD | 36.478 | 0.01014088 | +0.52% | 1.04x |

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

- Persisted scans: 693; predictions: 5616; observations: 419044.
- Matured sampled outcomes across 1/6/24/48h: 5466; gap abstentions: 13218. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44419754808 · **Generation:** 693 · **Legacy run:** 44419754808
**Main quote time:** 2026-11-18T23:20:20.436872+00:00 · **Legacy report time:** 2026-11-18T23:20:56.857696+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.05522 | 81.86 | +0.13% | 17.69x | STRONG 91/100 | VERY_HIGH 73/100 | Watch |
| 2 | NIGHT/USD | 0.04513 | 53.92 | -0.09% | 2.08x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 3 | LUNA/USD | 4.289e-05 | 48.63 | +0.63% | 0.40x | MODERATE 54/100 | VERY_HIGH 75/100 | Watch |
| 4 | AKE/USD ⭐ | 0.01014088 | 39.48 | +0.52% | 1.04x | MODERATE 60/100 | VERY_HIGH 73/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.05522 | 67.78 | +0.13% | 17.69x | 1283 | STRONG 84/100 | VERY_HIGH 73/100 | Watch |
| 2 | AKE/USD ⭐ | 0.01014088 | 45.20 | +0.52% | 1.04x | 3371 | MODERATE 58/100 | VERY_HIGH 79/100 | Watch |
| 3 | AKT/USD | 0.5105 | 43.71 | +0.89% | 19.29x | 4044 | STRONG 77/100 | HIGH 60/100 | Watch |

**Same-run overlap:** MEGA/USD, AKE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
