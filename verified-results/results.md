# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T14:45:35.066213+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44547048867
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** fe3343b4f9be3f8b04ae1680391554f4d4489451 (atomic ledger/results publication)
**Ledger generation:** 795 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 594; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 945.16 | 95.377 | 78.533 | +3.64% | +0.37% | 17.93x | 3.9 | 2026-11-19T14:45:25.910203+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | HYPE/USD | 69.1 | 95.223 | 76.061 | +3.32% | +0.83% | 3.91x | 4.3 | 2026-11-19T14:45:25.910203+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | PUMP/USD | 0.002764 | 92.969 | 83.814 | +6.47% | +0.69% | 1.57x | 10.9 | 2026-11-19T14:45:25.910203+00:00 | Not calibrated | STRONG 86/100 | HIGH 61/100 | Consider small entry | WATCH |
| 4 | SOL/USD | 75.2 | 86.271 | 69.471 | +2.26% | +0.36% | 6.83x | 2.7 | 2026-11-19T14:45:25.910203+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | VVV/USD | 23.286 | 86.061 | 94.854 | +7.45% | -0.04% | 0.14x | 10.3 | 2026-11-19T14:45:25.910203+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | ADA/USD | 0.155123 | 81.568 | 72.454 | +2.56% | +0.21% | 1.81x | 0.9 | 2026-11-19T14:45:25.910203+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | XRP/USD | 0.99012 | 77.515 | 72.153 | +2.46% | +0.04% | 1.52x | 0.1 | 2026-11-19T14:45:25.910203+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 8 | SENT/USD | 0.022086 | 75.811 | 76.504 | +7.19% | +0.93% | 0.47x | 4.1 | 2026-11-19T14:45:25.910203+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | ETH/USD | 1805.65 | 72.347 | 66.546 | +1.74% | -0.06% | 1.61x | 1.3 | 2026-11-19T14:45:25.910203+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 10 | XDG/USD | 0.059599 | 69.916 | 61.765 | +1.52% | +0.15% | 1.74x | 1.0 | 2026-11-19T14:45:25.910203+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 11 | LTC/USD | 44.33 | 69.207 | 54.883 | +0.73% | -0.14% | 3.00x | 2.3 | 2026-11-19T14:45:25.910203+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 12 | XBT/USD | 63863.9 | 68.925 | 64.766 | +1.40% | +0.04% | 1.40x | 0.0 | 2026-11-19T14:45:25.910203+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 94.854 | 23.286 | -0.04% | 0.14x |
| 2 | PUMP/USD | 83.814 | 0.002764 | +0.69% | 1.57x |
| 3 | ZEC/USD | 78.533 | 945.16 | +0.37% | 17.93x |
| 4 | SENT/USD | 76.504 | 0.022086 | +0.93% | 0.47x |
| 5 | HYPE/USD | 76.061 | 69.1 | +0.83% | 3.91x |
| 6 | ADA/USD | 72.454 | 0.155123 | +0.21% | 1.81x |
| 7 | XRP/USD | 72.153 | 0.99012 | +0.04% | 1.52x |
| 8 | SOL/USD | 69.471 | 75.2 | +0.36% | 6.83x |
| 9 | ETH/USD | 66.546 | 1805.65 | -0.06% | 1.61x |
| 10 | XBT/USD | 64.766 | 63863.9 | +0.04% | 1.40x |
| 11 | XDG/USD | 61.765 | 0.059599 | +0.15% | 1.74x |
| 12 | LTC/USD | 54.883 | 44.33 | -0.14% | 3.00x |

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

- Persisted scans: 795; predictions: 6684; observations: 480858.
- Matured sampled outcomes across 1/6/24/48h: 6683; gap abstentions: 15121. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44547048867 · **Generation:** 795 · **Legacy run:** 44547048867
**Main quote time:** 2026-11-19T14:45:35.066213+00:00 · **Legacy report time:** 2026-11-19T14:46:19.809535+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 945.16 | 95.38 | +0.37% | 17.93x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HYPE/USD ⭐ | 69.1 | 95.22 | +0.83% | 3.91x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | PUMP/USD ⭐ | 0.002764 | 92.97 | +0.69% | 1.57x | STRONG 96/100 | HIGH 61/100 | Consider small entry |
| 4 | SOL/USD ⭐ | 75.2 | 86.27 | +0.36% | 6.83x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | VVV/USD | 23.286 | 86.06 | -0.04% | 0.14x | WEAK 43/100 | VERY_HIGH 82/100 | Watch |
| 6 | ADA/USD ⭐ | 0.155123 | 81.57 | +0.21% | 1.81x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 7 | XRP/USD | 0.99012 | 77.51 | +0.04% | 1.52x | STRONG 74/100 | HIGH 55/100 | Watch |
| 8 | SENT/USD | 0.022086 | 75.81 | +0.93% | 0.47x | MODERATE 68/100 | VERY_HIGH 75/100 | Watch |
| 9 | ETH/USD | 1805.65 | 72.35 | -0.06% | 1.61x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 10 | XDG/USD | 0.059599 | 69.92 | +0.15% | 1.74x | STRONG 70/100 | HIGH 55/100 | Watch |
| 11 | LTC/USD | 44.33 | 69.21 | -0.14% | 3.00x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 12 | XBT/USD | 63863.9 | 68.92 | +0.04% | 1.40x | MODERATE 69/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 69.29 | 97.07 | +0.83% | 3.91x | 13933 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 945.51 | 96.60 | +0.37% | 17.93x | 20791 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SOL/USD ⭐ | 75.28 | 86.82 | +0.36% | 6.83x | 36863 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | PUMP/USD ⭐ | 0.002764 | 82.87 | +0.69% | 1.57x | 4644 | STRONG 91/100 | HIGH 61/100 | Consider small entry |
| 5 | ADA/USD ⭐ | 0.155236 | 76.88 | +0.21% | 1.81x | 12000 | STRONG 93/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ZEC/USD, HYPE/USD, PUMP/USD, SOL/USD, ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
