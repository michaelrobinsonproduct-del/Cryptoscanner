# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T03:04:38.249649+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45931523901
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d97f8a500bfad30573c1bbfec9675520fee534e7 (atomic ledger/results publication)
**Ledger generation:** 1950 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 473.75 | 91.736 | 76.726 | +3.68% | +0.00% | 2.67x | 8.0 | 2026-11-27T03:04:30.187321+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Watch | WATCH |
| 2 | ZEC/USD | 747.58 | 84.403 | 96.721 | +9.67% | -0.74% | 0.14x | 6.6 | 2026-11-27T03:04:30.187321+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | SKY/USD | 0.04875 | 84.097 | 65.803 | +5.04% | +1.02% | 2.32x | 8.2 | 2026-11-27T03:04:30.187321+00:00 | Not calibrated | STRONG 97/100 | HIGH 60/100 | Consider small entry | WATCH |
| 4 | HYPE/USD | 65.11 | 83.156 | 85.978 | +4.64% | +0.05% | 0.69x | 3.1 | 2026-11-27T03:04:30.187321+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | SOL/USD | 72.57 | 70.898 | 70.395 | +2.30% | -0.26% | 1.18x | 1.4 | 2026-11-27T03:04:30.187321+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 6 | LINK/USD | 9.49155 | 67.882 | 69.284 | +2.41% | -0.52% | 1.12x | 5.1 | 2026-11-27T03:04:30.187321+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 7 | XRP/USD | 0.96237 | 66.365 | 69.152 | +2.08% | -0.27% | 0.86x | 0.8 | 2026-11-27T03:04:30.187321+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 8 | VVV/USD | 26.878 | 65.501 | 69.103 | +2.65% | +0.19% | 0.55x | 9.0 | 2026-11-27T03:04:30.187321+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XBT/USD | 61406.1 | 62.148 | 65.499 | +1.50% | -0.31% | 0.82x | 0.0 | 2026-11-27T03:04:30.187321+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 10 | ETH/USD | 1725.87 | 61.690 | 70.811 | +2.26% | -0.31% | 0.24x | 0.1 | 2026-11-27T03:04:30.187321+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | NEAR/USD | 3.1283 | 60.902 | 70.098 | +2.64% | -0.52% | 0.34x | 6.7 | 2026-11-27T03:04:30.187321+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0575853 | 53.023 | 56.518 | +2.15% | -0.22% | 0.76x | 1.2 | 2026-11-27T03:04:30.187321+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 96.721 | 747.58 | -0.74% | 0.14x |
| 2 | HYPE/USD | 85.978 | 65.11 | +0.05% | 0.69x |
| 3 | XMR/USD | 76.726 | 473.75 | +0.00% | 2.67x |
| 4 | ETH/USD | 70.811 | 1725.87 | -0.31% | 0.24x |
| 5 | SOL/USD | 70.395 | 72.57 | -0.26% | 1.18x |
| 6 | NEAR/USD | 70.098 | 3.1283 | -0.52% | 0.34x |
| 7 | LINK/USD | 69.284 | 9.49155 | -0.52% | 1.12x |
| 8 | XRP/USD | 69.152 | 0.96237 | -0.27% | 0.86x |
| 9 | VVV/USD | 69.103 | 26.878 | +0.19% | 0.55x |
| 10 | SKY/USD | 65.803 | 0.04875 | +1.02% | 2.32x |
| 11 | XBT/USD | 65.499 | 61406.1 | -0.31% | 0.82x |
| 12 | XDG/USD | 56.518 | 0.0575853 | -0.22% | 0.76x |

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

- Persisted scans: 1950; predictions: 17102; observations: 1181034.
- Matured sampled outcomes across 1/6/24/48h: 37538; gap abstentions: 25472. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45931523901 · **Generation:** 1950 · **Legacy run:** 45931523901
**Main quote time:** 2026-11-27T03:04:38.249649+00:00 · **Legacy report time:** 2026-11-27T03:05:16.471031+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 473.75 | 91.74 | +0.00% | 2.67x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD | 747.58 | 84.40 | -0.74% | 0.14x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 3 | SKY/USD ⭐ | 0.04875 | 84.10 | +1.02% | 2.32x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 4 | HYPE/USD | 65.11 | 83.16 | +0.05% | 0.69x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 5 | SOL/USD | 72.57 | 70.90 | -0.26% | 1.18x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 6 | LINK/USD | 9.49155 | 67.88 | -0.52% | 1.12x | WEAK 44/100 | HIGH 68/100 | Watch |
| 7 | XRP/USD | 0.96237 | 66.36 | -0.27% | 0.86x | WEAK 38/100 | HIGH 68/100 | Watch |
| 8 | VVV/USD | 26.878 | 65.50 | +0.19% | 0.55x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 9 | XBT/USD | 61406.1 | 62.15 | -0.31% | 0.82x | WEAK 36/100 | HIGH 68/100 | Watch |
| 10 | ETH/USD | 1725.87 | 61.69 | -0.31% | 0.24x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 11 | NEAR/USD | 3.1283 | 60.90 | -0.52% | 0.34x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | XDG/USD | 0.0575853 | 53.02 | -0.22% | 0.76x | WEAK 32/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 472.63 | 83.21 | +0.18% | 2.12x | 18458 | STRONG 92/100 | HIGH 61/100 | Watch |
| 2 | SUI/USD | 0.6825 | 82.52 | +0.06% | 4.22x | 4809 | STRONG 86/100 | HIGH 55/100 | Watch |
| 3 | SKY/USD ⭐ | 0.04887 | 79.82 | +1.29% | 1.80x | 6853 | STRONG 90/100 | HIGH 66/100 | Consider small entry |
| 4 | JUP/USD | 0.2467 | 72.83 | +0.06% | 1.93x | 2281 | STRONG 71/100 | HIGH 60/100 | Watch |

**Same-run overlap:** XMR/USD, SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
