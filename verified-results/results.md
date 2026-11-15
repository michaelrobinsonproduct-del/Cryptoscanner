# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-15T20:04:40.678593+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43755932334
**Source SHA:** 885b4a0465f5c74a8a87db5ca921c3c0a00021af
**Previous ledger commit:** 5ab42ef85fcf9dea0558ceaace720c56e86d1ce9 (atomic ledger/results publication)
**Ledger generation:** 442 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 155.22 | 102.617 | 92.914 | +8.31% | -1.06% | 6.98x | 14.2 | 2026-11-15T20:04:32.629467+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 71/100 | Watch | WATCH |
| 2 | UNI/USD | 5.176 | 100.853 | 94.889 | +6.02% | -0.11% | 1.65x | 4.2 | 2026-11-15T20:04:32.629467+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04958 | 97.337 | 84.406 | +4.49% | +0.16% | 2.21x | 4.0 | 2026-11-15T20:04:32.629467+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Watch | WATCH |
| 4 | NEAR/USD | 3.1703 | 96.452 | 86.416 | +4.67% | +0.35% | 1.83x | 2.5 | 2026-11-15T20:04:32.629467+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | XMR/USD | 501 | 91.033 | 97.106 | +6.56% | +0.19% | 0.30x | 5.8 | 2026-11-15T20:04:32.629467+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | ASTER/USD | 0.54813 | 90.368 | 82.550 | +9.50% | -0.36% | 1.96x | 5.1 | 2026-11-15T20:04:32.629467+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0588635 | 87.470 | 73.298 | +2.70% | +0.08% | 2.37x | 1.2 | 2026-11-15T20:04:32.629467+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 8 | XRP/USD | 0.9583 | 84.544 | 89.052 | +4.87% | +0.08% | 0.51x | 0.1 | 2026-11-15T20:04:32.629467+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | ADA/USD | 0.154275 | 84.315 | 84.273 | +4.48% | +0.14% | 0.93x | 4.2 | 2026-11-15T20:04:32.629467+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 10 | CC/USD | 0.0832 | 81.431 | 86.888 | +7.20% | +0.11% | 0.40x | 6.0 | 2026-11-15T20:04:32.629467+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | AAVE/USD | 108.36 | 78.965 | 87.341 | +7.77% | +0.20% | 0.06x | 5.5 | 2026-11-15T20:04:32.629467+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | HYPE/USD | 67.11 | 77.695 | 84.733 | +4.35% | -0.07% | 0.33x | 1.5 | 2026-11-15T20:04:32.629467+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 97.106 | 501 | +0.19% | 0.30x |
| 2 | UNI/USD | 94.889 | 5.176 | -0.11% | 1.65x |
| 3 | QNT/USD | 92.914 | 155.22 | -1.06% | 6.98x |
| 4 | XRP/USD | 89.052 | 0.9583 | +0.08% | 0.51x |
| 5 | AAVE/USD | 87.341 | 108.36 | +0.20% | 0.06x |
| 6 | CC/USD | 86.888 | 0.0832 | +0.11% | 0.40x |
| 7 | NEAR/USD | 86.416 | 3.1703 | +0.35% | 1.83x |
| 8 | HYPE/USD | 84.733 | 67.11 | -0.07% | 0.33x |
| 9 | NIGHT/USD | 84.406 | 0.04958 | +0.16% | 2.21x |
| 10 | ADA/USD | 84.273 | 0.154275 | +0.14% | 0.93x |
| 11 | ASTER/USD | 82.550 | 0.54813 | -0.36% | 1.96x |
| 12 | XDG/USD | 73.298 | 0.0588635 | +0.08% | 2.37x |

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

- Persisted scans: 442; predictions: 3820; observations: 266209.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 11135. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 43755932334 · **Generation:** 442 · **Legacy run:** 43755932334
**Main quote time:** 2026-11-15T20:04:40.678593+00:00 · **Legacy report time:** 2026-11-15T20:04:52.739832+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 155.22 | 102.62 | -1.06% | 6.98x | STRONG 75/100 | VERY_HIGH 71/100 | Watch |
| 2 | UNI/USD | 5.176 | 100.85 | -0.11% | 1.65x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | NIGHT/USD ⭐ | 0.04958 | 97.34 | +0.16% | 2.21x | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | NEAR/USD ⭐ | 3.1703 | 96.45 | +0.35% | 1.83x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | XMR/USD | 501 | 91.03 | +0.19% | 0.30x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 6 | ASTER/USD | 0.54813 | 90.37 | -0.36% | 1.96x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 7 | XDG/USD ⭐ | 0.0588635 | 87.47 | +0.08% | 2.37x | STRONG 99/100 | HIGH 55/100 | Watch |
| 8 | XRP/USD | 0.9583 | 84.54 | +0.08% | 0.51x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 9 | ADA/USD | 0.154275 | 84.32 | +0.14% | 0.93x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 10 | CC/USD | 0.0832 | 81.43 | +0.11% | 0.40x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 11 | AAVE/USD | 108.36 | 78.96 | +0.20% | 0.06x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 12 | HYPE/USD | 67.11 | 77.69 | -0.07% | 0.33x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04961 | 100.00 | +0.16% | 2.21x | 18811 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | NEAR/USD ⭐ | 3.1694 | 96.16 | +0.35% | 1.83x | 16019 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XDG/USD ⭐ | 0.0588374 | 89.59 | +0.08% | 2.37x | 21666 | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | XLM/USD | 0.139577 | 85.59 | +0.11% | 1.22x | 15483 | MODERATE 68/100 | HIGH 62/100 | Watch |

**Same-run overlap:** NIGHT/USD, NEAR/USD, XDG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
