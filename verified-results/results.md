# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T05:11:37.256135+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45944100549
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d13b5ea854b64d3274543876e0840ec6f520fb04 (atomic ledger/results publication)
**Ledger generation:** 1963 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 602; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 760.09 | 95.851 | 96.507 | +11.51% | +0.78% | 0.55x | 7.0 | 2026-11-27T05:11:30.988128+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | HYPE/USD | 66.04 | 90.740 | 97.219 | +6.14% | +0.55% | 0.08x | 1.5 | 2026-11-27T05:11:30.988128+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | SOL/USD | 73.04 | 83.093 | 75.037 | +2.96% | +0.72% | 1.45x | 1.4 | 2026-11-27T05:11:30.988128+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 4 | VVV/USD | 27.175 | 81.710 | 78.017 | +3.79% | +0.17% | 1.28x | 7.0 | 2026-11-27T05:11:30.988128+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6858 | 80.480 | 71.459 | +2.71% | +0.60% | 1.60x | 2.9 | 2026-11-27T05:11:30.988128+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | XDG/USD | 0.0579352 | 80.323 | 62.882 | +2.77% | +0.49% | 10.21x | 0.0 | 2026-11-27T05:11:30.988128+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | ETH/USD | 1740.67 | 78.885 | 76.577 | +3.14% | +0.82% | 0.82x | 0.8 | 2026-11-27T05:11:30.988128+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 8 | LINK/USD | 9.66313 | 76.509 | 81.253 | +4.26% | +0.85% | 0.10x | 7.1 | 2026-11-27T05:11:30.988128+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XRP/USD | 0.96362 | 75.029 | 70.081 | +2.21% | +0.68% | 1.16x | 0.8 | 2026-11-27T05:11:30.988128+00:00 | Not calibrated | STRONG 73/100 | HIGH 62/100 | Watch | WATCH |
| 10 | ADA/USD | 0.152383 | 70.240 | 69.524 | +2.64% | +0.67% | 0.74x | 4.9 | 2026-11-27T05:11:30.988128+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XBT/USD | 61596.8 | 69.736 | 67.706 | +1.82% | +0.54% | 0.93x | 0.0 | 2026-11-27T05:11:30.988128+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 12 | LTC/USD | 44.77 | 66.598 | 69.248 | +2.35% | +0.67% | 0.40x | 4.5 | 2026-11-27T05:11:30.988128+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | HYPE/USD | 97.219 | 66.04 | +0.55% | 0.08x |
| 2 | ZEC/USD | 96.507 | 760.09 | +0.78% | 0.55x |
| 3 | LINK/USD | 81.253 | 9.66313 | +0.85% | 0.10x |
| 4 | VVV/USD | 78.017 | 27.175 | +0.17% | 1.28x |
| 5 | ETH/USD | 76.577 | 1740.67 | +0.82% | 0.82x |
| 6 | SOL/USD | 75.037 | 73.04 | +0.72% | 1.45x |
| 7 | SUI/USD | 71.459 | 0.6858 | +0.60% | 1.60x |
| 8 | XRP/USD | 70.081 | 0.96362 | +0.68% | 1.16x |
| 9 | ADA/USD | 69.524 | 0.152383 | +0.67% | 0.74x |
| 10 | LTC/USD | 69.248 | 44.77 | +0.67% | 0.40x |
| 11 | XBT/USD | 67.706 | 61596.8 | +0.54% | 0.93x |
| 12 | XDG/USD | 62.882 | 0.0579352 | +0.49% | 10.21x |

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

- Persisted scans: 1963; predictions: 17258; observations: 1188848.
- Matured sampled outcomes across 1/6/24/48h: 38042; gap abstentions: 25533. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45944100549 · **Generation:** 1963 · **Legacy run:** 45944100549
**Main quote time:** 2026-11-27T05:11:37.256135+00:00 · **Legacy report time:** 2026-11-27T05:12:29.563634+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 760.09 | 95.85 | +0.78% | 0.55x | STRONG 78/100 | VERY_HIGH 70/100 | Watch |
| 2 | HYPE/USD | 66.04 | 90.74 | +0.55% | 0.08x | STRONG 75/100 | VERY_HIGH 70/100 | Watch |
| 3 | SOL/USD ⭐ | 73.04 | 83.09 | +0.72% | 1.45x | STRONG 97/100 | HIGH 55/100 | Watch |
| 4 | VVV/USD ⭐ | 27.175 | 81.71 | +0.17% | 1.28x | STRONG 76/100 | HIGH 55/100 | Watch |
| 5 | SUI/USD ⭐ | 0.6858 | 80.48 | +0.60% | 1.60x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 6 | XDG/USD ⭐ | 0.0579352 | 80.32 | +0.49% | 10.21x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | ETH/USD | 1740.67 | 78.89 | +0.82% | 0.82x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 8 | LINK/USD | 9.66313 | 76.51 | +0.85% | 0.10x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 9 | XRP/USD ⭐ | 0.96362 | 75.03 | +0.68% | 1.16x | STRONG 83/100 | HIGH 62/100 | Watch |
| 10 | ADA/USD | 0.152383 | 70.24 | +0.67% | 0.74x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 11 | XBT/USD | 61596.8 | 69.74 | +0.54% | 0.93x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 12 | LTC/USD | 44.77 | 66.60 | +0.67% | 0.40x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD ⭐ | 73 | 88.05 | +0.72% | 1.45x | 34290 | STRONG 99/100 | HIGH 55/100 | Watch |
| 2 | XDG/USD ⭐ | 0.0578843 | 84.94 | +0.49% | 10.21x | 5548 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | VVV/USD ⭐ | 27.135 | 82.28 | +0.17% | 1.28x | 12664 | STRONG 76/100 | HIGH 55/100 | Watch |
| 4 | SUI/USD ⭐ | 0.6856 | 81.90 | +0.60% | 1.60x | 5101 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 5 | XRP/USD ⭐ | 0.96324 | 79.08 | +0.68% | 1.16x | 21367 | STRONG 85/100 | HIGH 62/100 | Watch |

**Same-run overlap:** SOL/USD, VVV/USD, SUI/USD, XDG/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
