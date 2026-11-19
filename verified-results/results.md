# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T04:40:22.755004+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44459829598
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 66d2b0361f083c3baaf0a8cb44f3b68cd19b073d (atomic ledger/results publication)
**Ledger generation:** 757 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.601 | 84.245 | 80.198 | +4.29% | +0.79% | 1.01x | 5.8 | 2026-11-19T04:40:16.665736+00:00 | Not calibrated | STRONG 77/100 | HIGH 62/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.4124 | 75.449 | 78.092 | +3.49% | -0.05% | 0.76x | 2.6 | 2026-11-19T04:40:16.665736+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 3 | SOL/USD | 74.69 | 67.706 | 65.277 | +1.56% | +0.38% | 1.05x | 1.3 | 2026-11-19T04:40:16.665736+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 4 | TAO/USD | 195.2023 | 64.937 | 63.707 | +1.69% | +0.14% | 1.05x | 6.2 | 2026-11-19T04:40:16.665736+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 5 | XBT/USD | 63444.8 | 63.203 | 60.108 | +0.73% | +0.17% | 1.23x | 0.0 | 2026-11-19T04:40:16.665736+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0591779 | 61.983 | 55.093 | +0.81% | +0.08% | 1.65x | 0.0 | 2026-11-19T04:40:16.665736+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |
| 7 | ADA/USD | 0.152835 | 61.771 | 61.434 | +1.05% | +0.14% | 0.96x | 1.8 | 2026-11-19T04:40:16.665736+00:00 | Not calibrated | MODERATE 51/100 | HIGH 62/100 | Watch | WATCH |
| 8 | ZEC/USD | 929.37 | 60.185 | 65.467 | +1.91% | +0.13% | 0.41x | 5.8 | 2026-11-19T04:40:16.665736+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | ETH/USD | 1798.64 | 57.163 | 64.391 | +1.35% | +0.09% | 0.23x | 0.1 | 2026-11-19T04:40:16.665736+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SUI/USD | 0.7252 | 56.063 | 60.445 | +0.88% | -0.07% | 0.60x | 1.4 | 2026-11-19T04:40:16.665736+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | XRP/USD | 0.97298 | 54.252 | 59.377 | +0.68% | +0.02% | 0.48x | 0.8 | 2026-11-19T04:40:16.665736+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | TRX/USD | 0.311324 | 39.274 | 45.014 | +0.66% | +0.12% | 0.36x | 0.0 | 2026-11-19T04:40:16.665736+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 80.198 | 22.601 | +0.79% | 1.01x |
| 2 | NEAR/USD | 78.092 | 3.4124 | -0.05% | 0.76x |
| 3 | ZEC/USD | 65.467 | 929.37 | +0.13% | 0.41x |
| 4 | SOL/USD | 65.277 | 74.69 | +0.38% | 1.05x |
| 5 | ETH/USD | 64.391 | 1798.64 | +0.09% | 0.23x |
| 6 | TAO/USD | 63.707 | 195.2023 | +0.14% | 1.05x |
| 7 | ADA/USD | 61.434 | 0.152835 | +0.14% | 0.96x |
| 8 | SUI/USD | 60.445 | 0.7252 | -0.07% | 0.60x |
| 9 | XBT/USD | 60.108 | 63444.8 | +0.17% | 1.23x |
| 10 | XRP/USD | 59.377 | 0.97298 | +0.02% | 0.48x |
| 11 | XDG/USD | 55.093 | 0.0591779 | +0.08% | 1.65x |
| 12 | TRX/USD | 45.014 | 0.311324 | +0.12% | 0.36x |

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

- Persisted scans: 757; predictions: 6228; observations: 458019.
- Matured sampled outcomes across 1/6/24/48h: 6219; gap abstentions: 13671. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44459829598 · **Generation:** 757 · **Legacy run:** 44459829598
**Main quote time:** 2026-11-19T04:40:22.755004+00:00 · **Legacy report time:** 2026-11-19T04:41:10.920932+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.601 | 84.25 | +0.79% | 1.01x | STRONG 87/100 | HIGH 62/100 | Watch |
| 2 | NEAR/USD | 3.4124 | 75.45 | -0.05% | 0.76x | WEAK 43/100 | HIGH 68/100 | Watch |
| 3 | SOL/USD ⭐ | 74.69 | 67.71 | +0.38% | 1.05x | STRONG 79/100 | HIGH 62/100 | Watch |
| 4 | TAO/USD ⭐ | 195.2023 | 64.94 | +0.14% | 1.05x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 5 | XBT/USD ⭐ | 63444.8 | 63.20 | +0.17% | 1.23x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 6 | XDG/USD | 0.0591779 | 61.98 | +0.08% | 1.65x | MODERATE 66/100 | HIGH 55/100 | Watch |
| 7 | ADA/USD | 0.152835 | 61.77 | +0.14% | 0.96x | MODERATE 51/100 | HIGH 62/100 | Watch |
| 8 | ZEC/USD | 929.37 | 60.19 | +0.13% | 0.41x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 9 | ETH/USD | 1798.64 | 57.16 | +0.09% | 0.23x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 10 | SUI/USD | 0.7252 | 56.06 | -0.07% | 0.60x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | XRP/USD | 0.97298 | 54.25 | +0.02% | 0.48x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 12 | TRX/USD | 0.311324 | 39.27 | +0.12% | 0.36x | WEAK 40/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.7 | 86.60 | +0.79% | 1.01x | 9445 | STRONG 83/100 | HIGH 68/100 | Watch |
| 2 | SOL/USD ⭐ | 74.75 | 70.42 | +0.38% | 1.05x | 34969 | STRONG 80/100 | HIGH 62/100 | Watch |
| 3 | TAO/USD ⭐ | 195.6146 | 67.85 | +0.14% | 1.05x | 4990 | MODERATE 69/100 | HIGH 62/100 | Watch |
| 4 | RENDER/USD | 1.443 | 66.30 | +0.70% | 1.64x | 1690 | STRONG 73/100 | HIGH 66/100 | Watch |
| 5 | XBT/USD ⭐ | 63464.2 | 62.51 | +0.17% | 1.23x | 147748 | MODERATE 66/100 | HIGH 62/100 | Watch |

**Same-run overlap:** VVV/USD, SOL/USD, TAO/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
