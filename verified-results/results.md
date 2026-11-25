# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T20:56:07.194542+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45699405185
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 6e424d6abbb0c511eff90a0d6966a7fbfcc27824 (atomic ledger/results publication)
**Ledger generation:** 1766 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 61.83 | 93.511 | 75.490 | +3.27% | +0.60% | 8.49x | 4.9 | 2026-11-25T20:55:58.847203+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | LTC/USD | 42.42 | 83.513 | 79.546 | +3.84% | -0.12% | 1.46x | 4.7 | 2026-11-25T20:55:58.847203+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 3 | DRV/USD | 0.35112 | 83.510 | 78.947 | +11.72% | +0.47% | 1.22x | 10.8 | 2026-11-25T20:55:58.847203+00:00 | Not calibrated | STRONG 72/100 | HIGH 68/100 | Watch | WATCH |
| 4 | LINK/USD | 9.10168 | 82.651 | 66.444 | +2.95% | +0.24% | 7.70x | 5.7 | 2026-11-25T20:55:58.847203+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | XMR/USD | 520.02 | 81.564 | 67.199 | +2.04% | -0.13% | 6.57x | 4.2 | 2026-11-25T20:55:58.847203+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.0165 | 78.128 | 82.888 | +4.58% | +0.23% | 0.41x | 8.3 | 2026-11-25T20:55:58.847203+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6635 | 74.520 | 71.544 | +2.47% | +0.21% | 1.19x | 1.5 | 2026-11-25T20:55:58.847203+00:00 | Not calibrated | STRONG 72/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XPL/USD | 0.0478 | 74.151 | 72.030 | +8.64% | +0.63% | 0.90x | 20.9 | 2026-11-25T20:55:58.847203+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 9 | PUMP/USD | 0.002539 | 71.825 | 69.237 | +4.10% | +0.60% | 0.96x | 3.9 | 2026-11-25T20:55:58.847203+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 10 | ZEC/USD | 760.7 | 71.513 | 72.965 | +2.95% | +0.75% | 0.48x | 5.4 | 2026-11-25T20:55:58.847203+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | SOL/USD | 70.5 | 70.456 | 63.342 | +1.29% | +0.37% | 1.53x | 1.4 | 2026-11-25T20:55:58.847203+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Consider small entry | WATCH |
| 12 | XRP/USD | 0.93971 | 68.853 | 67.149 | +1.74% | +0.38% | 0.98x | 0.1 | 2026-11-25T20:55:58.847203+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 82.888 | 3.0165 | +0.23% | 0.41x |
| 2 | LTC/USD | 79.546 | 42.42 | -0.12% | 1.46x |
| 3 | DRV/USD | 78.947 | 0.35112 | +0.47% | 1.22x |
| 4 | HYPE/USD | 75.490 | 61.83 | +0.60% | 8.49x |
| 5 | ZEC/USD | 72.965 | 760.7 | +0.75% | 0.48x |
| 6 | XPL/USD | 72.030 | 0.0478 | +0.63% | 0.90x |
| 7 | SUI/USD | 71.544 | 0.6635 | +0.21% | 1.19x |
| 8 | PUMP/USD | 69.237 | 0.002539 | +0.60% | 0.96x |
| 9 | XMR/USD | 67.199 | 520.02 | -0.13% | 6.57x |
| 10 | XRP/USD | 67.149 | 0.93971 | +0.38% | 0.98x |
| 11 | LINK/USD | 66.444 | 9.10168 | +0.24% | 7.70x |
| 12 | SOL/USD | 63.342 | 70.5 | +0.37% | 1.53x |

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

- Persisted scans: 1766; predictions: 14936; observations: 1070538.
- Matured sampled outcomes across 1/6/24/48h: 32678; gap abstentions: 23043. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45699405185 · **Generation:** 1766 · **Legacy run:** 45699405185
**Main quote time:** 2026-11-25T20:56:07.194542+00:00 · **Legacy report time:** 2026-11-25T20:57:19.399984+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 61.83 | 93.51 | +0.60% | 8.49x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | LTC/USD | 42.42 | 83.51 | -0.12% | 1.46x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 3 | DRV/USD ⭐ | 0.35112 | 83.51 | +0.47% | 1.22x | STRONG 82/100 | HIGH 68/100 | Watch |
| 4 | LINK/USD ⭐ | 9.10168 | 82.65 | +0.24% | 7.70x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | XMR/USD | 520.02 | 81.56 | -0.13% | 6.57x | STRONG 71/100 | HIGH 61/100 | Watch |
| 6 | NEAR/USD | 3.0165 | 78.13 | +0.23% | 0.41x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 7 | SUI/USD ⭐ | 0.6635 | 74.52 | +0.21% | 1.19x | STRONG 82/100 | HIGH 62/100 | Watch |
| 8 | XPL/USD | 0.0478 | 74.15 | +0.63% | 0.90x | MODERATE 57/100 | VERY_HIGH 74/100 | Watch |
| 9 | PUMP/USD | 0.002539 | 71.82 | +0.60% | 0.96x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 10 | ZEC/USD | 760.7 | 71.51 | +0.75% | 0.48x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 11 | SOL/USD | 70.5 | 70.46 | +0.37% | 1.53x | STRONG 80/100 | HIGH 55/100 | Consider small entry |
| 12 | XRP/USD | 0.93971 | 68.85 | +0.38% | 0.98x | MODERATE 64/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 61.99 | 97.85 | +0.60% | 8.49x | 22415 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD | 27.837 | 89.16 | +0.44% | 1.71x | 12987 | STRONG 80/100 | HIGH 67/100 | Consider small entry |
| 3 | LINK/USD ⭐ | 9.1105 | 84.35 | +0.24% | 7.70x | 7792 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SUI/USD ⭐ | 0.6647 | 79.26 | +0.21% | 1.19x | 7608 | STRONG 85/100 | HIGH 62/100 | Watch |
| 5 | DRV/USD ⭐ | 0.35257 | 77.94 | +0.47% | 1.22x | 12046 | STRONG 79/100 | HIGH 68/100 | Watch |

**Same-run overlap:** HYPE/USD, DRV/USD, LINK/USD, SUI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
