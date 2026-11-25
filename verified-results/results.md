# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T23:25:54.347274+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45721128278
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4639cfe379ccbb96c0382d9f56da9ceb967935b7 (atomic ledger/results publication)
**Ledger generation:** 1781 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.0112 | 90.961 | 83.420 | +4.39% | -0.18% | 1.84x | 4.7 | 2026-11-25T23:25:45.831673+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ZEC/USD | 758.52 | 84.963 | 71.488 | +2.66% | +0.72% | 1.99x | 4.2 | 2026-11-25T23:25:45.831673+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | HYPE/USD | 61.17 | 83.154 | 68.563 | +2.17% | -0.08% | 3.87x | 3.3 | 2026-11-25T23:25:45.831673+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SUI/USD | 0.6637 | 76.165 | 71.760 | +2.50% | +0.20% | 1.34x | 1.5 | 2026-11-25T23:25:45.831673+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 5 | SOL/USD | 70.27 | 74.104 | 61.027 | +0.96% | -0.06% | 2.34x | 1.4 | 2026-11-25T23:25:45.831673+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XMR/USD | 520.38 | 72.847 | 68.173 | +2.12% | +0.28% | 1.33x | 3.3 | 2026-11-25T23:25:45.831673+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 7 | LTC/USD | 42.36 | 71.500 | 79.695 | +3.70% | -0.07% | 0.22x | 2.4 | 2026-11-25T23:25:45.831673+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | PUMP/USD | 0.002548 | 64.072 | 70.879 | +4.47% | -0.04% | 0.34x | 7.9 | 2026-11-25T23:25:45.831673+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | XDG/USD | 0.0557292 | 63.236 | 54.145 | +0.89% | -0.04% | 1.93x | 0.4 | 2026-11-25T23:25:45.831673+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 10 | XAUT/USD | 3570.1 | 60.887 | 45.228 | +0.92% | +0.13% | 4.48x | 0.3 | 2026-11-25T23:25:45.831673+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 11 | XRP/USD | 0.93394 | 59.630 | 62.776 | +1.12% | +0.17% | 0.60x | 0.1 | 2026-11-25T23:25:45.831673+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | ETH/USD | 1687.41 | 57.772 | 59.018 | +0.58% | +0.33% | 0.71x | 0.1 | 2026-11-25T23:25:45.831673+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 83.420 | 3.0112 | -0.18% | 1.84x |
| 2 | LTC/USD | 79.695 | 42.36 | -0.07% | 0.22x |
| 3 | SUI/USD | 71.760 | 0.6637 | +0.20% | 1.34x |
| 4 | ZEC/USD | 71.488 | 758.52 | +0.72% | 1.99x |
| 5 | PUMP/USD | 70.879 | 0.002548 | -0.04% | 0.34x |
| 6 | HYPE/USD | 68.563 | 61.17 | -0.08% | 3.87x |
| 7 | XMR/USD | 68.173 | 520.38 | +0.28% | 1.33x |
| 8 | XRP/USD | 62.776 | 0.93394 | +0.17% | 0.60x |
| 9 | SOL/USD | 61.027 | 70.27 | -0.06% | 2.34x |
| 10 | ETH/USD | 59.018 | 1687.41 | +0.33% | 0.71x |
| 11 | XDG/USD | 54.145 | 0.0557292 | -0.04% | 1.93x |
| 12 | XAUT/USD | 45.228 | 3570.1 | +0.13% | 4.48x |

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

- Persisted scans: 1781; predictions: 15116; observations: 1079673.
- Matured sampled outcomes across 1/6/24/48h: 32883; gap abstentions: 23373. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45721128278 · **Generation:** 1781 · **Legacy run:** 45721128278
**Main quote time:** 2026-11-25T23:25:54.347274+00:00 · **Legacy report time:** 2026-11-25T23:26:57.861474+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.0112 | 90.96 | -0.18% | 1.84x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 2 | ZEC/USD ⭐ | 758.52 | 84.96 | +0.72% | 1.99x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 3 | HYPE/USD | 61.17 | 83.15 | -0.08% | 3.87x | STRONG 72/100 | HIGH 61/100 | Watch |
| 4 | SUI/USD ⭐ | 0.6637 | 76.17 | +0.20% | 1.34x | STRONG 83/100 | HIGH 55/100 | Watch |
| 5 | SOL/USD | 70.27 | 74.10 | -0.06% | 2.34x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 6 | XMR/USD ⭐ | 520.38 | 72.85 | +0.28% | 1.33x | STRONG 91/100 | HIGH 55/100 | Watch |
| 7 | LTC/USD | 42.36 | 71.50 | -0.07% | 0.22x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 8 | PUMP/USD | 0.002548 | 64.07 | -0.04% | 0.34x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 9 | XDG/USD | 0.0557292 | 63.24 | -0.04% | 1.93x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 10 | XAUT/USD | 3570.1 | 60.89 | +0.13% | 4.48x | STRONG 75/100 | HIGH 55/100 | Watch |
| 11 | XRP/USD | 0.93394 | 59.63 | +0.17% | 0.60x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 12 | ETH/USD | 1687.41 | 57.77 | +0.33% | 0.71x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD | 0.127508 | 86.33 | +0.11% | 3.46x | 8180 | STRONG 88/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD ⭐ | 759.77 | 85.70 | +0.72% | 1.99x | 43189 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 3 | SUI/USD ⭐ | 0.6637 | 77.96 | +0.20% | 1.34x | 7534 | STRONG 84/100 | HIGH 55/100 | Watch |
| 4 | XMR/USD ⭐ | 520.06 | 71.47 | +0.28% | 1.33x | 8201 | STRONG 91/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD, SUI/USD, XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
