# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T23:55:04.197983+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44203408618
**Source SHA:** 113db7a045b71125e52affc5c74a39ca3094a032
**Previous ledger commit:** 78722d7db647433378de982ca10d93a17a89a572 (atomic ledger/results publication)
**Ledger generation:** 476 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INJ/USD | 7.383 | 97.578 | 96.614 | +7.02% | -0.19% | 1.19x | 6.8 | 2026-11-17T23:54:57.482696+00:00 | Not calibrated | MODERATE 59/100 | HIGH 68/100 | Watch | WATCH |
| 2 | RENDER/USD | 1.484 | 96.246 | 72.690 | +7.77% | +1.71% | 2.56x | 13.5 | 2026-11-17T23:54:57.482696+00:00 | Not calibrated | STRONG 98/100 | HIGH 66/100 | Consider small entry | WATCH |
| 3 | NEAR/USD | 3.3861 | 94.359 | 98.080 | +7.23% | +0.30% | 0.48x | 3.8 | 2026-11-17T23:54:57.482696+00:00 | Not calibrated | STRONG 77/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | AKT/USD | 0.5109 | 92.986 | 76.112 | +6.79% | +0.37% | 4.03x | 2.0 | 2026-11-17T23:54:57.482696+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 5 | ZEC/USD | 964.44 | 91.600 | 98.497 | +6.71% | -0.07% | 0.35x | 3.0 | 2026-11-17T23:54:57.482696+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | XMR/USD | 508.38 | 82.746 | 72.644 | +3.00% | -0.18% | 2.10x | 6.7 | 2026-11-17T23:54:57.482696+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 7 | SOL/USD | 75.08 | 81.635 | 89.177 | +4.98% | +0.09% | 0.20x | 1.3 | 2026-11-17T23:54:57.482696+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XRP/USD | 0.98292 | 73.274 | 75.544 | +2.95% | -0.16% | 0.85x | 0.2 | 2026-11-17T23:54:57.482696+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 9 | TAO/USD | 197.3472 | 69.245 | 74.802 | +3.21% | -0.02% | 0.45x | 5.4 | 2026-11-17T23:54:57.482696+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | VVV/USD | 21.062 | 67.485 | 75.210 | +4.54% | -0.10% | 0.28x | 8.5 | 2026-11-17T23:54:57.482696+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0600212 | 64.317 | 67.859 | +1.93% | -0.03% | 0.66x | 0.0 | 2026-11-17T23:54:57.482696+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | SUI/USD | 0.7371 | 64.191 | 71.544 | +2.46% | -0.07% | 0.30x | 1.4 | 2026-11-17T23:54:57.482696+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.497 | 964.44 | -0.07% | 0.35x |
| 2 | NEAR/USD | 98.080 | 3.3861 | +0.30% | 0.48x |
| 3 | INJ/USD | 96.614 | 7.383 | -0.19% | 1.19x |
| 4 | SOL/USD | 89.177 | 75.08 | +0.09% | 0.20x |
| 5 | AKT/USD | 76.112 | 0.5109 | +0.37% | 4.03x |
| 6 | XRP/USD | 75.544 | 0.98292 | -0.16% | 0.85x |
| 7 | VVV/USD | 75.210 | 21.062 | -0.10% | 0.28x |
| 8 | TAO/USD | 74.802 | 197.3472 | -0.02% | 0.45x |
| 9 | RENDER/USD | 72.690 | 1.484 | +1.71% | 2.56x |
| 10 | XMR/USD | 72.644 | 508.38 | -0.18% | 2.10x |
| 11 | SUI/USD | 71.544 | 0.7371 | -0.07% | 0.30x |
| 12 | XDG/USD | 67.859 | 0.0600212 | -0.03% | 0.66x |

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

- Persisted scans: 476; predictions: 4193; observations: 286891.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12398. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44203408618 · **Generation:** 476 · **Legacy run:** 44203408618
**Main quote time:** 2026-11-17T23:55:04.197983+00:00 · **Legacy report time:** 2026-11-17T23:55:15.387825+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 7.383 | 97.58 | -0.19% | 1.19x | MODERATE 59/100 | HIGH 68/100 | Watch |
| 2 | RENDER/USD ⭐ | 1.484 | 96.25 | +1.71% | 2.56x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 3 | NEAR/USD | 3.3861 | 94.36 | +0.30% | 0.48x | STRONG 77/100 | VERY_HIGH 70/100 | Watch |
| 4 | AKT/USD | 0.5109 | 92.99 | +0.37% | 4.03x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 5 | ZEC/USD | 964.44 | 91.60 | -0.07% | 0.35x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 6 | XMR/USD | 508.38 | 82.75 | -0.18% | 2.10x | STRONG 71/100 | HIGH 61/100 | Watch |
| 7 | SOL/USD | 75.08 | 81.63 | +0.09% | 0.20x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 8 | XRP/USD | 0.98292 | 73.27 | -0.16% | 0.85x | WEAK 42/100 | HIGH 68/100 | Watch |
| 9 | TAO/USD | 197.3472 | 69.25 | -0.02% | 0.45x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 10 | VVV/USD | 21.062 | 67.48 | -0.10% | 0.28x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 11 | XDG/USD | 0.0600212 | 64.32 | -0.03% | 0.66x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 12 | SUI/USD | 0.7371 | 64.19 | -0.07% | 0.30x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | RENDER/USD ⭐ | 1.484 | 84.03 | +1.71% | 2.56x | 2753 | STRONG 100/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** RENDER/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
