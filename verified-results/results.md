# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T04:45:24.021486+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44460388713
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** cc558a3dac7a0ef32938625efcd1ce939f9d577e (atomic ledger/results publication)
**Ledger generation:** 758 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.624 | 89.368 | 81.439 | +4.40% | +0.58% | 1.50x | 6.6 | 2026-11-19T04:45:15.818264+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XDG/USD | 0.0591587 | 70.824 | 54.922 | +0.77% | +0.18% | 2.68x | 0.0 | 2026-11-19T04:45:15.818264+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 3 | TAO/USD | 195.3942 | 68.369 | 64.378 | +1.79% | +0.28% | 1.26x | 6.3 | 2026-11-19T04:45:15.818264+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 4 | NEAR/USD | 3.3893 | 66.908 | 72.886 | +2.79% | -0.23% | 0.52x | 3.2 | 2026-11-19T04:45:15.818264+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | SOL/USD | 74.59 | 66.370 | 64.324 | +1.43% | +0.32% | 1.04x | 1.3 | 2026-11-19T04:45:15.818264+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 6 | HYPE/USD | 67.48 | 62.585 | 60.539 | +0.90% | -0.06% | 1.23x | 1.5 | 2026-11-19T04:45:15.818264+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 7 | ZEC/USD | 928.92 | 60.597 | 66.088 | +1.86% | +0.30% | 0.30x | 3.9 | 2026-11-19T04:45:15.818264+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | ADA/USD | 0.152788 | 60.038 | 60.331 | +1.01% | +0.15% | 0.90x | 3.5 | 2026-11-19T04:45:15.818264+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |
| 9 | XBT/USD | 63446.6 | 58.116 | 60.128 | +0.73% | +0.28% | 0.66x | 0.0 | 2026-11-19T04:45:15.818264+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | ETH/USD | 1798.45 | 57.207 | 64.316 | +1.33% | +0.27% | 0.16x | 0.1 | 2026-11-19T04:45:15.818264+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XRP/USD | 0.97378 | 56.608 | 60.008 | +0.77% | +0.35% | 0.48x | 0.7 | 2026-11-19T04:45:15.818264+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | USELESS/USD | 0.10021 | 55.722 | 63.813 | +4.87% | -0.07% | 0.23x | 16.0 | 2026-11-19T04:45:15.818264+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 81.439 | 22.624 | +0.58% | 1.50x |
| 2 | NEAR/USD | 72.886 | 3.3893 | -0.23% | 0.52x |
| 3 | ZEC/USD | 66.088 | 928.92 | +0.30% | 0.30x |
| 4 | TAO/USD | 64.378 | 195.3942 | +0.28% | 1.26x |
| 5 | SOL/USD | 64.324 | 74.59 | +0.32% | 1.04x |
| 6 | ETH/USD | 64.316 | 1798.45 | +0.27% | 0.16x |
| 7 | USELESS/USD | 63.813 | 0.10021 | -0.07% | 0.23x |
| 8 | HYPE/USD | 60.539 | 67.48 | -0.06% | 1.23x |
| 9 | ADA/USD | 60.331 | 0.152788 | +0.15% | 0.90x |
| 10 | XBT/USD | 60.128 | 63446.6 | +0.28% | 0.66x |
| 11 | XRP/USD | 60.008 | 0.97378 | +0.35% | 0.48x |
| 12 | XDG/USD | 54.922 | 0.0591587 | +0.18% | 2.68x |

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

- Persisted scans: 758; predictions: 6240; observations: 458628.
- Matured sampled outcomes across 1/6/24/48h: 6232; gap abstentions: 13680. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44460388713 · **Generation:** 758 · **Legacy run:** 44460388713
**Main quote time:** 2026-11-19T04:45:24.021486+00:00 · **Legacy report time:** 2026-11-19T04:46:01.164827+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.624 | 89.37 | +0.58% | 1.50x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XDG/USD | 0.0591587 | 70.82 | +0.18% | 2.68x | STRONG 80/100 | HIGH 55/100 | Watch |
| 3 | TAO/USD ⭐ | 195.3942 | 68.37 | +0.28% | 1.26x | STRONG 79/100 | HIGH 55/100 | Watch |
| 4 | NEAR/USD | 3.3893 | 66.91 | -0.23% | 0.52x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 5 | SOL/USD ⭐ | 74.59 | 66.37 | +0.32% | 1.04x | STRONG 78/100 | HIGH 62/100 | Watch |
| 6 | HYPE/USD | 67.48 | 62.59 | -0.06% | 1.23x | WEAK 41/100 | HIGH 68/100 | Watch |
| 7 | ZEC/USD | 928.92 | 60.60 | +0.30% | 0.30x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 8 | ADA/USD | 0.152788 | 60.04 | +0.15% | 0.90x | MODERATE 50/100 | HIGH 62/100 | Watch |
| 9 | XBT/USD | 63446.6 | 58.12 | +0.28% | 0.66x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 10 | ETH/USD | 1798.45 | 57.21 | +0.27% | 0.16x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 11 | XRP/USD | 0.97378 | 56.61 | +0.35% | 0.48x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 12 | USELESS/USD | 0.10021 | 55.72 | -0.07% | 0.23x | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.658 | 88.16 | +0.58% | 1.50x | 9537 | STRONG 94/100 | HIGH 61/100 | Consider small entry |
| 2 | SOL/USD ⭐ | 74.62 | 68.08 | +0.32% | 1.04x | 35050 | STRONG 79/100 | HIGH 62/100 | Watch |
| 3 | TAO/USD ⭐ | 195.3942 | 63.57 | +0.28% | 1.26x | 5009 | STRONG 77/100 | HIGH 55/100 | Watch |
| 4 | AKT/USD | 0.5342 | 61.53 | +0.34% | 1.01x | 3456 | MODERATE 66/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** VVV/USD, TAO/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
