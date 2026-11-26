# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T06:26:18.718280+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45767985089
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** b3631ba9d99876b008c3cd3d23d54d211fe92486 (atomic ledger/results publication)
**Ledger generation:** 1824 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LINK/USD | 9.1805 | 76.628 | 61.906 | +1.50% | -0.06% | 3.55x | 2.9 | 2026-11-26T06:26:12.602906+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XRP/USD | 0.95317 | 73.309 | 66.995 | +1.77% | -0.18% | 1.72x | 0.8 | 2026-11-26T06:26:12.602906+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 3 | INJ/USD | 6.12 | 72.657 | 58.472 | +2.79% | -0.16% | 5.84x | 6.5 | 2026-11-26T06:26:12.602906+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SKY/USD | 0.0438 | 71.569 | 61.143 | +4.58% | +0.87% | 1.61x | 9.1 | 2026-11-26T06:26:12.602906+00:00 | Not calibrated | STRONG 81/100 | HIGH 60/100 | Consider small entry | WATCH |
| 5 | XDG/USD | 0.0564879 | 67.012 | 56.893 | +0.94% | -0.10% | 2.06x | 0.3 | 2026-11-26T06:26:12.602906+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SOL/USD | 70.75 | 66.184 | 57.873 | +0.51% | +0.00% | 1.83x | 1.4 | 2026-11-26T06:26:12.602906+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 7 | ADA/USD | 0.148232 | 65.939 | 65.169 | +1.69% | -0.07% | 1.11x | 3.3 | 2026-11-26T06:26:12.602906+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XMR/USD | 523.15 | 62.006 | 60.909 | +1.20% | +0.17% | 1.03x | 5.0 | 2026-11-26T06:26:12.602906+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 9 | LTC/USD | 43.6 | 61.541 | 68.440 | +2.08% | +0.21% | 0.21x | 2.3 | 2026-11-26T06:26:12.602906+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | QNT/USD | 147.95 | 57.873 | 63.579 | +2.18% | +0.14% | 0.36x | 4.1 | 2026-11-26T06:26:12.602906+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | PUMP/USD | 0.002641 | 56.090 | 60.466 | +2.48% | -0.45% | 0.79x | 3.8 | 2026-11-26T06:26:12.602906+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | TAO/USD | 183.1698 | 54.127 | 59.012 | +0.87% | -0.10% | 0.56x | 4.1 | 2026-11-26T06:26:12.602906+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 68.440 | 43.6 | +0.21% | 0.21x |
| 2 | XRP/USD | 66.995 | 0.95317 | -0.18% | 1.72x |
| 3 | ADA/USD | 65.169 | 0.148232 | -0.07% | 1.11x |
| 4 | QNT/USD | 63.579 | 147.95 | +0.14% | 0.36x |
| 5 | LINK/USD | 61.906 | 9.1805 | -0.06% | 3.55x |
| 6 | SKY/USD | 61.143 | 0.0438 | +0.87% | 1.61x |
| 7 | XMR/USD | 60.909 | 523.15 | +0.17% | 1.03x |
| 8 | PUMP/USD | 60.466 | 0.002641 | -0.45% | 0.79x |
| 9 | TAO/USD | 59.012 | 183.1698 | -0.10% | 0.56x |
| 10 | INJ/USD | 58.472 | 6.12 | -0.16% | 5.84x |
| 11 | SOL/USD | 57.873 | 70.75 | +0.00% | 1.83x |
| 12 | XDG/USD | 56.893 | 0.0564879 | -0.10% | 2.06x |

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

- Persisted scans: 1824; predictions: 15623; observations: 1105860.
- Matured sampled outcomes across 1/6/24/48h: 33887; gap abstentions: 24065. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45767985089 · **Generation:** 1824 · **Legacy run:** 45767985089
**Main quote time:** 2026-11-26T06:26:18.718280+00:00 · **Legacy report time:** 2026-11-26T06:27:36.998793+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD | 9.1805 | 76.63 | -0.06% | 3.55x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 2 | XRP/USD | 0.95317 | 73.31 | -0.18% | 1.72x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 3 | INJ/USD | 6.12 | 72.66 | -0.16% | 5.84x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 4 | SKY/USD ⭐ | 0.0438 | 71.57 | +0.87% | 1.61x | STRONG 91/100 | HIGH 60/100 | Consider small entry |
| 5 | XDG/USD | 0.0564879 | 67.01 | -0.10% | 2.06x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 6 | SOL/USD | 70.75 | 66.18 | +0.00% | 1.83x | MODERATE 68/100 | HIGH 55/100 | Watch |
| 7 | ADA/USD | 0.148232 | 65.94 | -0.07% | 1.11x | WEAK 43/100 | HIGH 68/100 | Watch |
| 8 | XMR/USD | 523.15 | 62.01 | +0.17% | 1.03x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 9 | LTC/USD | 43.6 | 61.54 | +0.21% | 0.21x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 10 | QNT/USD | 147.95 | 57.87 | +0.14% | 0.36x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 11 | PUMP/USD | 0.002641 | 56.09 | -0.45% | 0.79x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 12 | TAO/USD | 183.1698 | 54.13 | -0.10% | 0.56x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.04372 | 83.06 | +0.87% | 1.61x | 4097 | STRONG 97/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
