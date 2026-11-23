# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T19:52:17.578475+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45252935391
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2f49ca5e18ae0a3103fad1003b57e9f1d15824d5 (atomic ledger/results publication)
**Ledger generation:** 1474 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 159.07 | 94.600 | 97.169 | +10.90% | -0.47% | 0.98x | 5.7 | 2026-11-23T19:52:11.226937+00:00 | Not calibrated | MODERATE 52/100 | HIGH 68/100 | Watch | WATCH |
| 2 | SUI/USD | 0.6782 | 88.210 | 77.544 | +3.43% | -0.87% | 4.04x | 3.0 | 2026-11-23T19:52:11.226937+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 3 | INJ/USD | 6.5 | 86.061 | 82.853 | +4.37% | -1.14% | 1.89x | 1.5 | 2026-11-23T19:52:11.226937+00:00 | Not calibrated | MODERATE 63/100 | HIGH 65/100 | Watch | WATCH |
| 4 | XDG/USD | 0.056724 | 84.775 | 73.227 | +2.61% | -0.69% | 13.68x | 0.0 | 2026-11-23T19:52:11.226937+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ALGO/USD | 0.08258 | 84.186 | 89.690 | +9.48% | -0.41% | 0.66x | 8.5 | 2026-11-23T19:52:11.226937+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | ATOM/USD | 1.2641 | 79.006 | 74.656 | +7.86% | -0.02% | 1.45x | 6.3 | 2026-11-23T19:52:11.226937+00:00 | Not calibrated | MODERATE 60/100 | HIGH 66/100 | Watch | WATCH |
| 7 | LTC/USD | 41.39 | 78.458 | 75.231 | +3.06% | -0.55% | 1.60x | 2.4 | 2026-11-23T19:52:11.226937+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XRP/USD | 0.94216 | 78.260 | 65.556 | +1.58% | -0.46% | 3.33x | 1.0 | 2026-11-23T19:52:11.226937+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 9 | SOL/USD | 72.8 | 76.949 | 75.133 | +3.07% | -0.37% | 1.37x | 2.7 | 2026-11-23T19:52:11.226937+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 10 | UAI/USD | 0.03268 | 70.173 | 73.036 | +10.52% | +0.34% | 0.54x | 6.1 | 2026-11-23T19:52:11.226937+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 11 | ADA/USD | 0.148253 | 69.160 | 71.692 | +2.52% | -0.58% | 1.04x | 2.0 | 2026-11-23T19:52:11.226937+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 12 | UNI/USD | 4.8774 | 65.510 | 78.183 | +4.19% | -0.81% | 0.14x | 6.2 | 2026-11-23T19:52:11.226937+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 97.169 | 159.07 | -0.47% | 0.98x |
| 2 | ALGO/USD | 89.690 | 0.08258 | -0.41% | 0.66x |
| 3 | INJ/USD | 82.853 | 6.5 | -1.14% | 1.89x |
| 4 | UNI/USD | 78.183 | 4.8774 | -0.81% | 0.14x |
| 5 | SUI/USD | 77.544 | 0.6782 | -0.87% | 4.04x |
| 6 | LTC/USD | 75.231 | 41.39 | -0.55% | 1.60x |
| 7 | SOL/USD | 75.133 | 72.8 | -0.37% | 1.37x |
| 8 | ATOM/USD | 74.656 | 1.2641 | -0.02% | 1.45x |
| 9 | XDG/USD | 73.227 | 0.056724 | -0.69% | 13.68x |
| 10 | UAI/USD | 73.036 | 0.03268 | +0.34% | 0.54x |
| 11 | ADA/USD | 71.692 | 0.148253 | -0.58% | 1.04x |
| 12 | XRP/USD | 65.556 | 0.94216 | -0.46% | 3.33x |

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

- Persisted scans: 1474; predictions: 12455; observations: 892768.
- Matured sampled outcomes across 1/6/24/48h: 22096; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45252935391 · **Generation:** 1474 · **Legacy run:** 45252935391
**Main quote time:** 2026-11-23T19:52:17.578475+00:00 · **Legacy report time:** 2026-11-23T19:53:26.496912+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 159.07 | 94.60 | -0.47% | 0.98x | MODERATE 52/100 | HIGH 68/100 | Watch |
| 2 | SUI/USD | 0.6782 | 88.21 | -0.87% | 4.04x | STRONG 74/100 | HIGH 61/100 | Watch |
| 3 | INJ/USD | 6.5 | 86.06 | -1.14% | 1.89x | MODERATE 63/100 | HIGH 65/100 | Watch |
| 4 | XDG/USD | 0.056724 | 84.77 | -0.69% | 13.68x | STRONG 72/100 | HIGH 61/100 | Watch |
| 5 | ALGO/USD | 0.08258 | 84.19 | -0.41% | 0.66x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 6 | ATOM/USD | 1.2641 | 79.01 | -0.02% | 1.45x | MODERATE 60/100 | HIGH 66/100 | Watch |
| 7 | LTC/USD | 41.39 | 78.46 | -0.55% | 1.60x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 8 | XRP/USD | 0.94216 | 78.26 | -0.46% | 3.33x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 9 | SOL/USD | 72.8 | 76.95 | -0.37% | 1.37x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 10 | UAI/USD | 0.03268 | 70.17 | +0.34% | 0.54x | MODERATE 65/100 | VERY_HIGH 82/100 | Watch |
| 11 | ADA/USD | 0.148253 | 69.16 | -0.58% | 1.04x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 12 | UNI/USD | 4.8774 | 65.51 | -0.81% | 0.14x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |

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
