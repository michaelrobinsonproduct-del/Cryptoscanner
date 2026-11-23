# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T20:12:23.034024+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45256420652
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 18b49c5ffdf6bd6641d7e41034cd09e5e530f547 (atomic ledger/results publication)
**Ledger generation:** 1476 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 158.96 | 96.353 | 97.176 | +10.82% | +0.05% | 0.89x | 5.6 | 2026-11-23T20:12:13.902001+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 2 | ALGO/USD | 0.08255 | 82.853 | 91.614 | +9.44% | -0.01% | 0.13x | 4.8 | 2026-11-23T20:12:13.902001+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | INJ/USD | 6.482 | 82.488 | 80.143 | +4.08% | -0.26% | 1.36x | 3.1 | 2026-11-23T20:12:13.902001+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 4 | UAI/USD | 0.03224 | 81.954 | 71.373 | +9.03% | -0.88% | 3.37x | 9.3 | 2026-11-23T20:12:13.902001+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | ATOM/USD | 1.2588 | 81.763 | 72.349 | +7.41% | -0.67% | 2.28x | 11.1 | 2026-11-23T20:12:13.902001+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 6 | UNI/USD | 4.8666 | 79.316 | 77.494 | +3.96% | -0.41% | 1.39x | 4.5 | 2026-11-23T20:12:13.902001+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XRP/USD | 0.94085 | 76.800 | 64.779 | +1.44% | -0.32% | 2.36x | 0.5 | 2026-11-23T20:12:13.902001+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6765 | 76.547 | 74.989 | +3.17% | -0.37% | 1.34x | 4.4 | 2026-11-23T20:12:13.902001+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 9 | LTC/USD | 41.48 | 74.998 | 76.802 | +3.29% | -0.05% | 0.84x | 2.4 | 2026-11-23T20:12:13.902001+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 10 | SOL/USD | 72.87 | 74.276 | 76.514 | +3.17% | -0.08% | 0.82x | 1.4 | 2026-11-23T20:12:13.902001+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 11 | HYPE/USD | 64.45 | 71.402 | 69.654 | +2.20% | +0.09% | 1.13x | 1.6 | 2026-11-23T20:12:13.902001+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 12 | SHX/USD | 0.003663 | 71.147 | 72.199 | +8.53% | -0.43% | 1.11x | 8.2 | 2026-11-23T20:12:13.902001+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 80/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 97.176 | 158.96 | +0.05% | 0.89x |
| 2 | ALGO/USD | 91.614 | 0.08255 | -0.01% | 0.13x |
| 3 | INJ/USD | 80.143 | 6.482 | -0.26% | 1.36x |
| 4 | UNI/USD | 77.494 | 4.8666 | -0.41% | 1.39x |
| 5 | LTC/USD | 76.802 | 41.48 | -0.05% | 0.84x |
| 6 | SOL/USD | 76.514 | 72.87 | -0.08% | 0.82x |
| 7 | SUI/USD | 74.989 | 0.6765 | -0.37% | 1.34x |
| 8 | ATOM/USD | 72.349 | 1.2588 | -0.67% | 2.28x |
| 9 | SHX/USD | 72.199 | 0.003663 | -0.43% | 1.11x |
| 10 | UAI/USD | 71.373 | 0.03224 | -0.88% | 3.37x |
| 11 | HYPE/USD | 69.654 | 64.45 | +0.09% | 1.13x |
| 12 | XRP/USD | 64.779 | 0.94085 | -0.32% | 2.36x |

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

- Persisted scans: 1476; predictions: 12479; observations: 893986.
- Matured sampled outcomes across 1/6/24/48h: 22192; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45256420652 · **Generation:** 1476 · **Legacy run:** 45256420652
**Main quote time:** 2026-11-23T20:12:23.034024+00:00 · **Legacy report time:** 2026-11-23T20:13:08.040676+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 158.96 | 96.35 | +0.05% | 0.89x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 2 | ALGO/USD | 0.08255 | 82.85 | -0.01% | 0.13x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 3 | INJ/USD | 6.482 | 82.49 | -0.26% | 1.36x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 4 | UAI/USD | 0.03224 | 81.95 | -0.88% | 3.37x | STRONG 71/100 | VERY_HIGH 73/100 | Watch |
| 5 | ATOM/USD | 1.2588 | 81.76 | -0.67% | 2.28x | MODERATE 66/100 | VERY_HIGH 72/100 | Watch |
| 6 | UNI/USD | 4.8666 | 79.32 | -0.41% | 1.39x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 7 | XRP/USD | 0.94085 | 76.80 | -0.32% | 2.36x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 8 | SUI/USD | 0.6765 | 76.55 | -0.37% | 1.34x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 9 | LTC/USD | 41.48 | 75.00 | -0.05% | 0.84x | WEAK 42/100 | HIGH 68/100 | Watch |
| 10 | SOL/USD | 72.87 | 74.28 | -0.08% | 0.82x | WEAK 42/100 | HIGH 68/100 | Watch |
| 11 | HYPE/USD ⭐ | 64.45 | 71.40 | +0.09% | 1.13x | STRONG 71/100 | HIGH 62/100 | Watch |
| 12 | SHX/USD | 0.003663 | 71.15 | -0.43% | 1.11x | MODERATE 46/100 | VERY_HIGH 80/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 64.57 | 78.43 | +0.09% | 1.13x | 28510 | STRONG 74/100 | HIGH 62/100 | Watch |

**Same-run overlap:** HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
