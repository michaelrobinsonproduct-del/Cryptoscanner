# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T18:45:31.788489+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44591006491
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** ef90fe1e5a25e8688d447486371487797ec902fe (atomic ledger/results publication)
**Ledger generation:** 837 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.705 | 92.751 | 85.537 | +4.77% | -0.06% | 1.75x | 5.7 | 2026-11-19T18:45:24.142458+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 2 | HYPE/USD | 69.31 | 79.835 | 79.712 | +3.63% | -0.56% | 1.29x | 1.4 | 2026-11-19T18:45:24.142458+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 3 | TAO/USD | 195.8022 | 78.285 | 64.101 | +2.00% | -0.16% | 3.29x | 7.3 | 2026-11-19T18:45:24.142458+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 4 | CT/USD | 0.13 | 69.773 | 65.314 | +9.98% | +0.93% | 0.98x | 23.1 | 2026-11-19T18:45:24.142458+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 5 | AKT/USD | 0.551 | 68.923 | 69.409 | +6.37% | -0.14% | 1.02x | 14.5 | 2026-11-19T18:45:24.142458+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0588931 | 65.563 | 51.469 | +0.32% | -0.18% | 2.68x | 0.4 | 2026-11-19T18:45:24.142458+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 7 | CSPR/USD | 0.0017648 | 61.730 | 73.765 | +8.06% | -1.74% | 0.67x | 5.7 | 2026-11-19T18:45:24.142458+00:00 | Not calibrated | WEAK 36/100 | EXTREME 92/100 | Do nothing | WATCH |
| 8 | USELESS/USD | 0.1 | 59.617 | 65.927 | +4.65% | -0.12% | 0.43x | 8.0 | 2026-11-19T18:45:24.142458+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | LIGHTER/USD | 2.849 | 59.405 | 64.225 | +4.97% | -0.70% | 0.87x | 10.6 | 2026-11-19T18:45:24.142458+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 10 | TRX/USD | 0.31079 | 58.864 | 43.843 | +0.49% | +0.00% | 3.39x | 1.0 | 2026-11-19T18:45:24.142458+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 11 | PUMP/USD | 0.002709 | 57.176 | 67.159 | +4.35% | -0.33% | 0.17x | 11.1 | 2026-11-19T18:45:24.142458+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 12 | ETH/USD | 1781.97 | 55.410 | 57.816 | +0.41% | -0.28% | 0.90x | 0.1 | 2026-11-19T18:45:24.142458+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 85.537 | 22.705 | -0.06% | 1.75x |
| 2 | HYPE/USD | 79.712 | 69.31 | -0.56% | 1.29x |
| 3 | CSPR/USD | 73.765 | 0.0017648 | -1.74% | 0.67x |
| 4 | AKT/USD | 69.409 | 0.551 | -0.14% | 1.02x |
| 5 | PUMP/USD | 67.159 | 0.002709 | -0.33% | 0.17x |
| 6 | USELESS/USD | 65.927 | 0.1 | -0.12% | 0.43x |
| 7 | CT/USD | 65.314 | 0.13 | +0.93% | 0.98x |
| 8 | LIGHTER/USD | 64.225 | 2.849 | -0.70% | 0.87x |
| 9 | TAO/USD | 64.101 | 195.8022 | -0.16% | 3.29x |
| 10 | ETH/USD | 57.816 | 1781.97 | -0.28% | 0.90x |
| 11 | XDG/USD | 51.469 | 0.0588931 | -0.18% | 2.68x |
| 12 | TRX/USD | 43.843 | 0.31079 | +0.00% | 3.39x |

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

- Persisted scans: 837; predictions: 7188; observations: 505940.
- Matured sampled outcomes across 1/6/24/48h: 7175; gap abstentions: 15546. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44591006491 · **Generation:** 837 · **Legacy run:** 44591006491
**Main quote time:** 2026-11-19T18:45:31.788489+00:00 · **Legacy report time:** 2026-11-19T18:46:10.087711+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.705 | 92.75 | -0.06% | 1.75x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 2 | HYPE/USD | 69.31 | 79.84 | -0.56% | 1.29x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 3 | TAO/USD | 195.8022 | 78.29 | -0.16% | 3.29x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 4 | CT/USD | 0.13 | 69.77 | +0.93% | 0.98x | MODERATE 55/100 | VERY_HIGH 79/100 | Watch |
| 5 | AKT/USD | 0.551 | 68.92 | -0.14% | 1.02x | WEAK 39/100 | VERY_HIGH 79/100 | Watch |
| 6 | XDG/USD | 0.0588931 | 65.56 | -0.18% | 2.68x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 7 | CSPR/USD | 0.0017648 | 61.73 | -1.74% | 0.67x | WEAK 36/100 | EXTREME 92/100 | Do nothing |
| 8 | USELESS/USD | 0.1 | 59.62 | -0.12% | 0.43x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 9 | LIGHTER/USD | 2.849 | 59.40 | -0.70% | 0.87x | WEAK 30/100 | VERY_HIGH 79/100 | Do nothing |
| 10 | TRX/USD | 0.31079 | 58.86 | +0.00% | 3.39x | STRONG 74/100 | HIGH 55/100 | Watch |
| 11 | PUMP/USD | 0.002709 | 57.18 | -0.33% | 0.17x | WEAK 29/100 | VERY_HIGH 82/100 | Do nothing |
| 12 | ETH/USD | 1781.97 | 55.41 | -0.28% | 0.90x | WEAK 33/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
