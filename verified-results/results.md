# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T08:11:33.494401+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45136352815
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e3083f24c21267e3b1daac48d0b49ebcb9aa8e24 (atomic ledger/results publication)
**Ledger generation:** 1403 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BLESS/USD | 0.017871 | 77.471 | 68.025 | +11.05% | +0.69% | 1.60x | 31.0 | 2026-11-23T08:11:27.336272+00:00 | Not calibrated | STRONG 74/100 | HIGH 67/100 | Watch | WATCH |
| 2 | SUI/USD | 0.667 | 71.805 | 66.313 | +1.72% | +0.29% | 1.41x | 1.5 | 2026-11-23T08:11:27.336272+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 3 | KAS/USD | 0.02727 | 70.219 | 64.330 | +5.66% | +0.85% | 1.16x | 18.3 | 2026-11-23T08:11:27.336272+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | SOL/USD | 72.1 | 67.310 | 68.875 | +2.08% | +0.39% | 0.65x | 1.4 | 2026-11-23T08:11:27.336272+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | XLM/USD | 0.12898 | 60.254 | 60.789 | +1.14% | -0.06% | 0.98x | 3.9 | 2026-11-23T08:11:27.336272+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 6 | PAXG/USD | 3592.2 | 57.851 | 48.416 | +0.56% | -0.46% | 2.17x | 0.9 | 2026-11-23T08:11:27.336272+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 7 | UNI/USD | 4.739 | 57.574 | 47.745 | +1.23% | -0.04% | 2.00x | 3.8 | 2026-11-23T08:11:27.336272+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XRP/USD | 0.93598 | 54.879 | 60.995 | +0.91% | +0.18% | 0.30x | 0.7 | 2026-11-23T08:11:27.336272+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | LTC/USD | 40.62 | 48.208 | 49.770 | +1.15% | +0.05% | 0.82x | 2.5 | 2026-11-23T08:11:27.336272+00:00 | Not calibrated | WEAK 44/100 | HIGH 62/100 | Watch | WATCH |
| 10 | AVAX/USD | 6.723 | 47.739 | 39.338 | +0.61% | +0.25% | 1.71x | 4.5 | 2026-11-23T08:11:27.336272+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0555367 | 45.217 | 49.368 | +0.46% | +0.16% | 0.50x | 1.3 | 2026-11-23T08:11:27.336272+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | AUD/USD | 0.66483 | 41.197 | 42.722 | +0.49% | -0.02% | 0.86x | 1.8 | 2026-11-23T08:11:27.336272+00:00 | Not calibrated | WEAK 26/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SOL/USD | 68.875 | 72.1 | +0.39% | 0.65x |
| 2 | BLESS/USD | 68.025 | 0.017871 | +0.69% | 1.60x |
| 3 | SUI/USD | 66.313 | 0.667 | +0.29% | 1.41x |
| 4 | KAS/USD | 64.330 | 0.02727 | +0.85% | 1.16x |
| 5 | XRP/USD | 60.995 | 0.93598 | +0.18% | 0.30x |
| 6 | XLM/USD | 60.789 | 0.12898 | -0.06% | 0.98x |
| 7 | LTC/USD | 49.770 | 40.62 | +0.05% | 0.82x |
| 8 | XDG/USD | 49.368 | 0.0555367 | +0.16% | 0.50x |
| 9 | PAXG/USD | 48.416 | 3592.2 | -0.46% | 2.17x |
| 10 | UNI/USD | 47.745 | 4.739 | -0.04% | 2.00x |
| 11 | AUD/USD | 42.722 | 0.66483 | -0.02% | 0.86x |
| 12 | AVAX/USD | 39.338 | 6.723 | +0.25% | 1.71x |

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

- Persisted scans: 1403; predictions: 11603; observations: 849531.
- Matured sampled outcomes across 1/6/24/48h: 18912; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 127 (sampled only; not a success-rate estimate).
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

**Writer:** 45136352815 · **Generation:** 1403 · **Legacy run:** 45136352815
**Main quote time:** 2026-11-23T08:11:33.494401+00:00 · **Legacy report time:** 2026-11-23T08:12:41.253728+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BLESS/USD ⭐ | 0.017871 | 77.47 | +0.69% | 1.60x | STRONG 84/100 | HIGH 67/100 | Consider small entry |
| 2 | SUI/USD ⭐ | 0.667 | 71.80 | +0.29% | 1.41x | STRONG 91/100 | HIGH 55/100 | Watch |
| 3 | KAS/USD ⭐ | 0.02727 | 70.22 | +0.85% | 1.16x | STRONG 75/100 | VERY_HIGH 73/100 | Watch |
| 4 | SOL/USD | 72.1 | 67.31 | +0.39% | 0.65x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 5 | XLM/USD | 0.12898 | 60.25 | -0.06% | 0.98x | WEAK 35/100 | HIGH 68/100 | Watch |
| 6 | PAXG/USD | 3592.2 | 57.85 | -0.46% | 2.17x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 7 | UNI/USD | 4.739 | 57.57 | -0.04% | 2.00x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 8 | XRP/USD | 0.93598 | 54.88 | +0.18% | 0.30x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 9 | LTC/USD | 40.62 | 48.21 | +0.05% | 0.82x | WEAK 44/100 | HIGH 62/100 | Watch |
| 10 | AVAX/USD | 6.723 | 47.74 | +0.25% | 1.71x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 11 | XDG/USD | 0.0555367 | 45.22 | +0.16% | 0.50x | WEAK 43/100 | VERY_HIGH 70/100 | Watch |
| 12 | AUD/USD | 0.66483 | 41.20 | -0.02% | 0.86x | WEAK 26/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BLESS/USD ⭐ | 0.017871 | 79.57 | +0.69% | 1.60x | 5677 | STRONG 80/100 | VERY_HIGH 77/100 | Watch |
| 2 | KAS/USD ⭐ | 0.02733 | 75.55 | +0.85% | 1.16x | 2953 | STRONG 73/100 | VERY_HIGH 79/100 | Watch |
| 3 | SUI/USD ⭐ | 0.6664 | 71.06 | +0.29% | 1.41x | 6644 | STRONG 91/100 | HIGH 55/100 | Watch |

**Same-run overlap:** BLESS/USD, SUI/USD, KAS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
