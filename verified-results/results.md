# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T03:17:10.408228+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45538598007
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a70442d87c3641717cc671f21bb7dfe1ff34d75e (atomic ledger/results publication)
**Ledger generation:** 1662 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.00967 | 77.105 | 52.601 | +2.11% | +1.90% | 6.78x | 20.7 | 2026-11-25T03:17:04.066302+00:00 | Not calibrated | STRONG 84/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 24.91 | 68.564 | 61.190 | +1.52% | +1.05% | 1.21x | 8.8 | 2026-11-25T03:17:04.066302+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 3 | XMR/USD | 511.06 | 57.377 | 50.024 | +0.29% | +1.29% | 1.09x | 10.4 | 2026-11-25T03:17:04.066302+00:00 | Not calibrated | MODERATE 59/100 | HIGH 68/100 | Watch | WATCH |
| 4 | DRV/USD | 0.32707 | 55.248 | 56.282 | +4.07% | +0.36% | 0.72x | 13.5 | 2026-11-25T03:17:04.066302+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 5 | ASTER/USD | 0.48217 | 32.317 | 32.229 | +0.28% | +0.69% | 0.67x | 4.1 | 2026-11-25T03:17:04.066302+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 61.190 | 24.91 | +1.05% | 1.21x |
| 2 | DRV/USD | 56.282 | 0.32707 | +0.36% | 0.72x |
| 3 | MON/USD | 52.601 | 0.00967 | +1.90% | 6.78x |
| 4 | XMR/USD | 50.024 | 511.06 | +1.29% | 1.09x |
| 5 | ASTER/USD | 32.229 | 0.48217 | +0.69% | 0.67x |

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

- Persisted scans: 1662; predictions: 14146; observations: 1007249.
- Matured sampled outcomes across 1/6/24/48h: 29777; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45538598007 · **Generation:** 1662 · **Legacy run:** 45538598007
**Main quote time:** 2026-11-25T03:17:10.408228+00:00 · **Legacy report time:** 2026-11-25T03:18:03.774276+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.00967 | 77.10 | +1.90% | 6.78x | STRONG 94/100 | HIGH 67/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 24.91 | 68.56 | +1.05% | 1.21x | STRONG 79/100 | HIGH 62/100 | Watch |
| 3 | XMR/USD ⭐ | 511.06 | 57.38 | +1.29% | 1.09x | MODERATE 69/100 | HIGH 68/100 | Watch |
| 4 | DRV/USD | 0.32707 | 55.25 | +0.36% | 0.72x | MODERATE 53/100 | VERY_HIGH 81/100 | Watch |
| 5 | ASTER/USD | 0.48217 | 32.32 | +0.69% | 0.67x | MODERATE 46/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.00966 | 70.66 | +1.90% | 6.78x | 18915 | STRONG 90/100 | HIGH 67/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 24.91 | 63.77 | +1.05% | 1.21x | 16181 | STRONG 77/100 | HIGH 62/100 | Watch |
| 3 | XMR/USD ⭐ | 510.93 | 43.79 | +1.29% | 1.09x | 6778 | MODERATE 67/100 | HIGH 62/100 | Watch |
| 4 | XAUT/USD | 3545.8 | 34.33 | +0.19% | 1.20x | 1717 | WEAK 42/100 | HIGH 67/100 | Watch |

**Same-run overlap:** MON/USD, VVV/USD, XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
