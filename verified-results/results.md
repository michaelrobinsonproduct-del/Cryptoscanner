# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T16:11:57.158394+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45213317018
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7d95dc53c9cccce28f5d5b13a23534812d70f7fa (atomic ledger/results publication)
**Ledger generation:** 1452 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ADA/USD | 0.153832 | 116.674 | 98.117 | +6.38% | +0.71% | 4.43x | 3.1 | 2026-11-23T16:11:49.928162+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 848.11 | 100.219 | 94.342 | +6.34% | -1.19% | 2.18x | 10.1 | 2026-11-23T16:11:49.928162+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 71/100 | Watch | WATCH |
| 3 | SOL/USD | 75.6 | 99.031 | 99.338 | +7.04% | +0.32% | 0.81x | 1.3 | 2026-11-23T16:11:49.928162+00:00 | Not calibrated | STRONG 80/100 | HIGH 62/100 | Watch | WATCH |
| 4 | SUI/USD | 0.7107 | 98.169 | 98.597 | +8.39% | -0.13% | 1.02x | 2.8 | 2026-11-23T16:11:49.928162+00:00 | Not calibrated | MODERATE 59/100 | HIGH 68/100 | Watch | WATCH |
| 5 | ENA/USD | 0.1074 | 96.888 | 89.053 | +6.23% | -0.19% | 1.88x | 9.3 | 2026-11-23T16:11:49.928162+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 6 | INJ/USD | 6.848 | 96.614 | 94.923 | +9.96% | +1.30% | 0.52x | 5.8 | 2026-11-23T16:11:49.928162+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | XRP/USD | 0.98819 | 95.159 | 99.292 | +6.54% | -0.15% | 0.66x | 1.4 | 2026-11-23T16:11:49.928162+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0585233 | 91.264 | 95.677 | +5.86% | +0.03% | 0.54x | 0.7 | 2026-11-23T16:11:49.928162+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | LTC/USD | 42.64 | 91.079 | 95.881 | +6.18% | +0.45% | 0.30x | 4.7 | 2026-11-23T16:11:49.928162+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | HYPE/USD | 66.36 | 89.178 | 89.371 | +5.23% | -0.72% | 1.34x | 4.5 | 2026-11-23T16:11:49.928162+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 11 | XLM/USD | 0.134098 | 89.126 | 89.608 | +5.15% | +0.20% | 0.85x | 2.9 | 2026-11-23T16:11:49.928162+00:00 | Not calibrated | STRONG 75/100 | HIGH 62/100 | Watch | WATCH |
| 12 | UNI/USD | 5.0457 | 85.461 | 92.448 | +7.79% | -0.47% | 0.54x | 5.5 | 2026-11-23T16:11:49.928162+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SOL/USD | 99.338 | 75.6 | +0.32% | 0.81x |
| 2 | XRP/USD | 99.292 | 0.98819 | -0.15% | 0.66x |
| 3 | SUI/USD | 98.597 | 0.7107 | -0.13% | 1.02x |
| 4 | ADA/USD | 98.117 | 0.153832 | +0.71% | 4.43x |
| 5 | LTC/USD | 95.881 | 42.64 | +0.45% | 0.30x |
| 6 | XDG/USD | 95.677 | 0.0585233 | +0.03% | 0.54x |
| 7 | INJ/USD | 94.923 | 6.848 | +1.30% | 0.52x |
| 8 | ZEC/USD | 94.342 | 848.11 | -1.19% | 2.18x |
| 9 | UNI/USD | 92.448 | 5.0457 | -0.47% | 0.54x |
| 10 | XLM/USD | 89.608 | 0.134098 | +0.20% | 0.85x |
| 11 | HYPE/USD | 89.371 | 66.36 | -0.72% | 1.34x |
| 12 | ENA/USD | 89.053 | 0.1074 | -0.19% | 1.88x |

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

- Persisted scans: 1452; predictions: 12191; observations: 879370.
- Matured sampled outcomes across 1/6/24/48h: 21004; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 1; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45213317018 · **Generation:** 1452 · **Legacy run:** 45213317018
**Main quote time:** 2026-11-23T16:11:57.158394+00:00 · **Legacy report time:** 2026-11-23T16:13:06.290943+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.153832 | 116.67 | +0.71% | 4.43x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD | 848.11 | 100.22 | -1.19% | 2.18x | STRONG 75/100 | VERY_HIGH 71/100 | Watch |
| 3 | SOL/USD | 75.6 | 99.03 | +0.32% | 0.81x | STRONG 80/100 | HIGH 62/100 | Watch |
| 4 | SUI/USD | 0.7107 | 98.17 | -0.13% | 1.02x | MODERATE 59/100 | HIGH 68/100 | Watch |
| 5 | ENA/USD | 0.1074 | 96.89 | -0.19% | 1.88x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 6 | INJ/USD | 6.848 | 96.61 | +1.30% | 0.52x | STRONG 78/100 | VERY_HIGH 70/100 | Watch |
| 7 | XRP/USD | 0.98819 | 95.16 | -0.15% | 0.66x | MODERATE 53/100 | VERY_HIGH 76/100 | Watch |
| 8 | XDG/USD | 0.0585233 | 91.26 | +0.03% | 0.54x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 9 | LTC/USD | 42.64 | 91.08 | +0.45% | 0.30x | STRONG 76/100 | VERY_HIGH 70/100 | Watch |
| 10 | HYPE/USD | 66.36 | 89.18 | -0.72% | 1.34x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 11 | XLM/USD | 0.134098 | 89.13 | +0.20% | 0.85x | STRONG 75/100 | HIGH 62/100 | Watch |
| 12 | UNI/USD | 5.0457 | 85.46 | -0.47% | 0.54x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.154519 | 100.00 | +0.71% | 4.43x | 11992 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ETH/USD | 1774.48 | 88.89 | +0.05% | 1.00x | 52222 | MODERATE 69/100 | HIGH 62/100 | Watch |

**Same-run overlap:** ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
