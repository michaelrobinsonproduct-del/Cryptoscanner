# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T23:50:02.417140+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44202710858
**Source SHA:** 113db7a045b71125e52affc5c74a39ca3094a032
**Previous ledger commit:** 37eea2991dd988adfeaad4850be92c8abe6d4915 (atomic ledger/results publication)
**Ledger generation:** 475 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INJ/USD | 7.363 | 102.934 | 97.284 | +6.73% | +0.54% | 1.29x | 5.4 | 2026-11-17T23:49:54.251347+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.3851 | 96.486 | 97.931 | +7.20% | +0.53% | 0.59x | 4.1 | 2026-11-17T23:49:54.251347+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | ZEC/USD | 962.28 | 92.582 | 98.233 | +6.47% | +0.24% | 0.32x | 3.5 | 2026-11-17T23:49:54.251347+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | SOL/USD | 74.99 | 82.986 | 88.296 | +4.85% | +0.00% | 0.47x | 1.3 | 2026-11-17T23:49:54.251347+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | RENDER/USD | 1.478 | 81.776 | 75.823 | +7.33% | -0.20% | 1.70x | 6.8 | 2026-11-17T23:49:54.251347+00:00 | Not calibrated | MODERATE 61/100 | HIGH 66/100 | Watch | WATCH |
| 6 | XRP/USD | 0.98323 | 76.517 | 75.822 | +2.98% | -0.05% | 1.10x | 0.1 | 2026-11-17T23:49:54.251347+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 7 | XMR/USD | 509.47 | 76.147 | 74.885 | +3.22% | -0.16% | 1.21x | 5.3 | 2026-11-17T23:49:54.251347+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 8 | VVV/USD | 21.085 | 72.039 | 76.975 | +4.65% | +0.14% | 0.44x | 6.6 | 2026-11-17T23:49:54.251347+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | TAO/USD | 197.4263 | 68.041 | 74.044 | +3.26% | -0.10% | 0.45x | 7.5 | 2026-11-17T23:49:54.251347+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | SUI/USD | 0.7368 | 65.168 | 71.252 | +2.42% | +0.15% | 0.32x | 1.4 | 2026-11-17T23:49:54.251347+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0599887 | 58.896 | 67.255 | +1.87% | +0.02% | 0.15x | 0.5 | 2026-11-17T23:49:54.251347+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | LTC/USD | 45.24 | 54.828 | 55.754 | +1.73% | +0.00% | 0.91x | 2.2 | 2026-11-17T23:49:54.251347+00:00 | Not calibrated | MODERATE 47/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.233 | 962.28 | +0.24% | 0.32x |
| 2 | NEAR/USD | 97.931 | 3.3851 | +0.53% | 0.59x |
| 3 | INJ/USD | 97.284 | 7.363 | +0.54% | 1.29x |
| 4 | SOL/USD | 88.296 | 74.99 | +0.00% | 0.47x |
| 5 | VVV/USD | 76.975 | 21.085 | +0.14% | 0.44x |
| 6 | RENDER/USD | 75.823 | 1.478 | -0.20% | 1.70x |
| 7 | XRP/USD | 75.822 | 0.98323 | -0.05% | 1.10x |
| 8 | XMR/USD | 74.885 | 509.47 | -0.16% | 1.21x |
| 9 | TAO/USD | 74.044 | 197.4263 | -0.10% | 0.45x |
| 10 | SUI/USD | 71.252 | 0.7368 | +0.15% | 0.32x |
| 11 | XDG/USD | 67.255 | 0.0599887 | +0.02% | 0.15x |
| 12 | LTC/USD | 55.754 | 45.24 | +0.00% | 0.91x |

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

- Persisted scans: 475; predictions: 4181; observations: 286282.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12398. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44202710858 · **Generation:** 475 · **Legacy run:** 44202710858
**Main quote time:** 2026-11-17T23:50:02.417140+00:00 · **Legacy report time:** 2026-11-17T23:50:10.904158+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 7.363 | 102.93 | +0.54% | 1.29x | STRONG 85/100 | HIGH 55/100 | Watch |
| 2 | NEAR/USD | 3.3851 | 96.49 | +0.53% | 0.59x | STRONG 78/100 | VERY_HIGH 70/100 | Watch |
| 3 | ZEC/USD | 962.28 | 92.58 | +0.24% | 0.32x | STRONG 76/100 | VERY_HIGH 70/100 | Watch |
| 4 | SOL/USD | 74.99 | 82.99 | +0.00% | 0.47x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 5 | RENDER/USD ⭐ | 1.478 | 81.78 | -0.20% | 1.70x | STRONG 71/100 | HIGH 66/100 | Watch |
| 6 | XRP/USD | 0.98323 | 76.52 | -0.05% | 1.10x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 7 | XMR/USD | 509.47 | 76.15 | -0.16% | 1.21x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 8 | VVV/USD | 21.085 | 72.04 | +0.14% | 0.44x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 9 | TAO/USD | 197.4263 | 68.04 | -0.10% | 0.45x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 10 | SUI/USD | 0.7368 | 65.17 | +0.15% | 0.32x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 11 | XDG/USD | 0.0599887 | 58.90 | +0.02% | 0.15x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 12 | LTC/USD | 45.24 | 54.83 | +0.00% | 0.91x | MODERATE 47/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | RENDER/USD ⭐ | 1.478 | 78.20 | +0.54% | 1.65x | 2655 | STRONG 94/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** RENDER/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
