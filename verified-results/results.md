# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T06:30:07.811223+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44251719663
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 8f9d4e6d5b8137a1030edf7bdb1fef1b08940f3a (atomic ledger/results publication)
**Ledger generation:** 555 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.3006 | 84.005 | 65.059 | +8.87% | +3.26% | 1.26x | 26.6 | 2026-11-18T06:30:01.282011+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | CC/USD | 0.0842 | 63.196 | 50.384 | +2.52% | -0.44% | 3.17x | 5.9 | 2026-11-18T06:30:01.282011+00:00 | Not calibrated | MODERATE 62/100 | HIGH 66/100 | Watch | WATCH |
| 3 | PEARL/USD | 1.849 | 59.812 | 48.815 | +2.13% | +0.53% | 1.83x | 1.6 | 2026-11-18T06:30:01.282011+00:00 | Not calibrated | STRONG 75/100 | HIGH 60/100 | Watch | WATCH |
| 4 | SENT/USD | 0.019442 | 58.829 | 57.435 | +4.14% | -2.47% | 2.38x | 5.1 | 2026-11-18T06:30:01.282011+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 5 | XRP/USD | 0.98518 | 49.805 | 56.837 | +0.27% | +0.14% | 0.23x | 0.1 | 2026-11-18T06:30:01.282011+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.411 | 46.893 | 56.868 | +0.54% | -0.16% | 0.08x | 3.8 | 2026-11-18T06:30:01.282011+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | MNT/USD | 0.3779 | 26.355 | 33.541 | +1.23% | -0.21% | 0.39x | 15.9 | 2026-11-18T06:30:01.282011+00:00 | Not calibrated | WEAK 13/100 | EXTREME 87/100 | Do nothing | WATCH |
| 8 | AKT/USD | 0.5154 | 26.323 | 33.029 | +1.20% | +0.21% | 0.22x | 15.6 | 2026-11-18T06:30:01.282011+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ICNT/USD | 65.059 | 0.3006 | +3.26% | 1.26x |
| 2 | SENT/USD | 57.435 | 0.019442 | -2.47% | 2.38x |
| 3 | NEAR/USD | 56.868 | 3.411 | -0.16% | 0.08x |
| 4 | XRP/USD | 56.837 | 0.98518 | +0.14% | 0.23x |
| 5 | CC/USD | 50.384 | 0.0842 | -0.44% | 3.17x |
| 6 | PEARL/USD | 48.815 | 1.849 | +0.53% | 1.83x |
| 7 | MNT/USD | 33.541 | 0.3779 | -0.21% | 0.39x |
| 8 | AKT/USD | 33.029 | 0.5154 | +0.21% | 0.22x |

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

- Persisted scans: 555; predictions: 4684; observations: 335002.
- Matured sampled outcomes across 1/6/24/48h: 3970; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 16; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44251719663 · **Generation:** 555 · **Legacy run:** 44251719663
**Main quote time:** 2026-11-18T06:30:07.811223+00:00 · **Legacy report time:** 2026-11-18T06:30:27.088636+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.3006 | 84.01 | +3.26% | 1.26x | STRONG 77/100 | VERY_HIGH 82/100 | Watch |
| 2 | CC/USD | 0.0842 | 63.20 | -0.44% | 3.17x | MODERATE 62/100 | HIGH 66/100 | Watch |
| 3 | PEARL/USD ⭐ | 1.849 | 59.81 | +0.53% | 1.83x | STRONG 85/100 | HIGH 60/100 | Consider small entry |
| 4 | SENT/USD | 0.019442 | 58.83 | -2.47% | 2.38x | MODERATE 59/100 | VERY_HIGH 77/100 | Do nothing |
| 5 | XRP/USD | 0.98518 | 49.81 | +0.14% | 0.23x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 6 | NEAR/USD | 3.411 | 46.89 | -0.16% | 0.08x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | MNT/USD | 0.3779 | 26.36 | -0.21% | 0.39x | WEAK 13/100 | EXTREME 87/100 | Do nothing |
| 8 | AKT/USD | 0.5154 | 26.32 | +0.21% | 0.22x | WEAK 38/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.3013 | 81.08 | +3.26% | 1.26x | 4780 | STRONG 76/100 | VERY_HIGH 82/100 | Watch |
| 2 | PEARL/USD ⭐ | 1.849 | 69.21 | +0.53% | 1.83x | 3785 | STRONG 90/100 | HIGH 60/100 | Consider small entry |
| 3 | TRX/USD | 0.308251 | 50.56 | +0.24% | 2.41x | 4090 | STRONG 80/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ICNT/USD, PEARL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
