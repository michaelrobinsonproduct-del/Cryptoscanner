# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T03:45:21.673476+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44453540857
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** ed687e7976a07cc78425bd5ddec26ab64c75a2b4 (atomic ledger/results publication)
**Ledger generation:** 746 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.3634 | 83.273 | 66.932 | +2.00% | +0.27% | 4.24x | 4.2 | 2026-11-19T03:45:14.530800+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | LUNA/USD | 4.764e-05 | 74.448 | 75.727 | +9.42% | -0.95% | 1.35x | 4.2 | 2026-11-19T03:45:14.530800+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |
| 3 | SUI/USD | 0.7213 | 72.271 | 55.950 | +0.33% | +0.26% | 6.04x | 2.8 | 2026-11-19T03:45:14.530800+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | ETH/USD | 1779.29 | 72.215 | 56.365 | +0.26% | +0.17% | 2.58x | 0.8 | 2026-11-19T03:45:14.530800+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 5 | TAO/USD | 192.632 | 71.027 | 53.826 | +0.35% | +0.44% | 4.20x | 7.2 | 2026-11-19T03:45:14.530800+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | VVV/USD | 22.235 | 65.206 | 62.688 | +2.60% | +0.62% | 0.94x | 10.3 | 2026-11-19T03:45:14.530800+00:00 | Not calibrated | MODERATE 58/100 | HIGH 68/100 | Watch | WATCH |
| 7 | SOL/USD | 73.74 | 61.774 | 55.548 | +0.27% | +0.39% | 1.43x | 2.7 | 2026-11-19T03:45:14.530800+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 8 | ONDO/USD | 0.29895 | 53.987 | 35.501 | +0.44% | +0.70% | 10.60x | 4.7 | 2026-11-19T03:45:14.530800+00:00 | Not calibrated | STRONG 82/100 | HIGH 60/100 | Watch | WATCH |
| 9 | AKT/USD | 0.5215 | 49.887 | 33.348 | +0.68% | +0.31% | 4.13x | 5.8 | 2026-11-19T03:45:14.530800+00:00 | Not calibrated | STRONG 80/100 | HIGH 67/100 | Watch | WATCH |
| 10 | LTC/USD | 44.24 | 48.528 | 48.799 | +0.52% | +0.20% | 0.87x | 2.3 | 2026-11-19T03:45:14.530800+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 11 | TRX/USD | 0.310125 | 39.554 | 41.955 | +0.27% | +0.07% | 0.72x | 0.6 | 2026-11-19T03:45:14.530800+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | DRV/USD | 0.26774 | 38.388 | 39.019 | +1.15% | +0.18% | 0.85x | 4.9 | 2026-11-19T03:45:14.530800+00:00 | Not calibrated | WEAK 39/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LUNA/USD | 75.727 | 4.764e-05 | -0.95% | 1.35x |
| 2 | NEAR/USD | 66.932 | 3.3634 | +0.27% | 4.24x |
| 3 | VVV/USD | 62.688 | 22.235 | +0.62% | 0.94x |
| 4 | ETH/USD | 56.365 | 1779.29 | +0.17% | 2.58x |
| 5 | SUI/USD | 55.950 | 0.7213 | +0.26% | 6.04x |
| 6 | SOL/USD | 55.548 | 73.74 | +0.39% | 1.43x |
| 7 | TAO/USD | 53.826 | 192.632 | +0.44% | 4.20x |
| 8 | LTC/USD | 48.799 | 44.24 | +0.20% | 0.87x |
| 9 | TRX/USD | 41.955 | 0.310125 | +0.07% | 0.72x |
| 10 | DRV/USD | 39.019 | 0.26774 | +0.18% | 0.85x |
| 11 | ONDO/USD | 35.501 | 0.29895 | +0.70% | 10.60x |
| 12 | AKT/USD | 33.348 | 0.5215 | +0.31% | 4.13x |

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

- Persisted scans: 746; predictions: 6096; observations: 451321.
- Matured sampled outcomes across 1/6/24/48h: 6056; gap abstentions: 13563. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44453540857 · **Generation:** 746 · **Legacy run:** 44453540857
**Main quote time:** 2026-11-19T03:45:21.673476+00:00 · **Legacy report time:** 2026-11-19T03:46:09.067971+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.3634 | 83.27 | +0.27% | 4.24x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | LUNA/USD | 4.764e-05 | 74.45 | -0.95% | 1.35x | MODERATE 57/100 | HIGH 66/100 | Watch |
| 3 | SUI/USD ⭐ | 0.7213 | 72.27 | +0.26% | 6.04x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | ETH/USD ⭐ | 1779.29 | 72.22 | +0.17% | 2.58x | STRONG 91/100 | HIGH 55/100 | Watch |
| 5 | TAO/USD | 192.632 | 71.03 | +0.44% | 4.20x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 6 | VVV/USD | 22.235 | 65.21 | +0.62% | 0.94x | MODERATE 58/100 | HIGH 68/100 | Watch |
| 7 | SOL/USD ⭐ | 73.74 | 61.77 | +0.39% | 1.43x | STRONG 86/100 | HIGH 55/100 | Watch |
| 8 | ONDO/USD | 0.29895 | 53.99 | +0.70% | 10.60x | STRONG 82/100 | HIGH 60/100 | Watch |
| 9 | AKT/USD | 0.5215 | 49.89 | +0.31% | 4.13x | STRONG 80/100 | HIGH 67/100 | Watch |
| 10 | LTC/USD | 44.24 | 48.53 | +0.20% | 0.87x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 11 | TRX/USD | 0.310125 | 39.55 | +0.07% | 0.72x | WEAK 40/100 | VERY_HIGH 70/100 | Watch |
| 12 | DRV/USD | 0.26774 | 38.39 | +0.18% | 0.85x | WEAK 39/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.3773 | 81.00 | +0.27% | 4.24x | 13709 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ETH/USD ⭐ | 1781.11 | 63.02 | +0.17% | 2.58x | 57983 | STRONG 87/100 | HIGH 55/100 | Watch |
| 3 | SUI/USD ⭐ | 0.7213 | 62.03 | +0.26% | 6.04x | 6647 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 4 | SOL/USD ⭐ | 73.84 | 57.07 | +0.39% | 1.43x | 35128 | STRONG 84/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NEAR/USD, SUI/USD, ETH/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
