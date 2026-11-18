# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T14:25:11.685094+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44323930310
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** bd1ed5b6046655df9a0ac4cb31365efecd1eaa28 (atomic ledger/results publication)
**Ledger generation:** 588 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 23.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.0468 | 76.567 | 68.704 | +4.25% | -0.59% | 2.08x | 19.3 | 2026-11-18T14:25:04.692069+00:00 | Not calibrated | MODERATE 63/100 | HIGH 67/100 | Watch | WATCH |
| 2 | XRP/USD | 0.98717 | 62.992 | 58.255 | +0.47% | -0.05% | 1.50x | 0.1 | 2026-11-18T14:25:04.692069+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 3 | CT/USD | 0.1215 | 55.302 | 63.584 | +7.52% | -0.41% | 0.38x | 24.7 | 2026-11-18T14:25:04.692069+00:00 | Not calibrated | WEAK 23/100 | EXTREME 100/100 | Do nothing | WATCH |
| 4 | SENT/USD | 0.019476 | 51.865 | 57.215 | +4.32% | +0.17% | 0.38x | 8.2 | 2026-11-18T14:25:04.692069+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | VVV/USD | 21.169 | 47.088 | 50.917 | +0.68% | -0.41% | 0.82x | 4.3 | 2026-11-18T14:25:04.692069+00:00 | Not calibrated | WEAK 29/100 | HIGH 68/100 | Do nothing | WATCH |
| 6 | AKT/USD | 0.5228 | 45.602 | 48.159 | +2.65% | +0.52% | 0.48x | 5.7 | 2026-11-18T14:25:04.692069+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 7 | CC/USD | 0.08301 | 42.726 | 40.480 | +1.07% | -0.17% | 1.31x | 4.8 | 2026-11-18T14:25:04.692069+00:00 | Not calibrated | WEAK 41/100 | HIGH 66/100 | Watch | WATCH |
| 8 | TRX/USD | 0.309813 | 38.408 | 45.755 | +0.62% | +0.06% | 0.23x | 0.6 | 2026-11-18T14:25:04.692069+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | PEARL/USD | 1.8548 | 31.159 | 35.203 | +2.45% | +0.92% | 0.14x | 40.6 | 2026-11-18T14:25:04.692069+00:00 | Not calibrated | WEAK 31/100 | EXTREME 92/100 | Do nothing | WATCH |
| 10 | W/USD | 0.00902 | 29.975 | 33.239 | +1.01% | +0.22% | 0.56x | 11.1 | 2026-11-18T14:25:04.692069+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 68.704 | 0.0468 | -0.59% | 2.08x |
| 2 | CT/USD | 63.584 | 0.1215 | -0.41% | 0.38x |
| 3 | XRP/USD | 58.255 | 0.98717 | -0.05% | 1.50x |
| 4 | SENT/USD | 57.215 | 0.019476 | +0.17% | 0.38x |
| 5 | VVV/USD | 50.917 | 21.169 | -0.41% | 0.82x |
| 6 | AKT/USD | 48.159 | 0.5228 | +0.52% | 0.48x |
| 7 | TRX/USD | 45.755 | 0.309813 | +0.06% | 0.23x |
| 8 | CC/USD | 40.480 | 0.08301 | -0.17% | 1.31x |
| 9 | PEARL/USD | 35.203 | 1.8548 | +0.92% | 0.14x |
| 10 | W/USD | 33.239 | 0.00902 | +0.22% | 0.56x |

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

- Persisted scans: 588; predictions: 5004; observations: 355099.
- Matured sampled outcomes across 1/6/24/48h: 4226; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44323930310 · **Generation:** 588 · **Legacy run:** 44323930310
**Main quote time:** 2026-11-18T14:25:11.685094+00:00 · **Legacy report time:** 2026-11-18T14:25:34.501897+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.0468 | 76.57 | -0.59% | 2.08x | MODERATE 63/100 | HIGH 67/100 | Watch |
| 2 | XRP/USD | 0.98717 | 62.99 | -0.05% | 1.50x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 3 | CT/USD | 0.1215 | 55.30 | -0.41% | 0.38x | WEAK 23/100 | EXTREME 100/100 | Do nothing |
| 4 | SENT/USD | 0.019476 | 51.87 | +0.17% | 0.38x | MODERATE 46/100 | VERY_HIGH 82/100 | Watch |
| 5 | VVV/USD | 21.169 | 47.09 | -0.41% | 0.82x | WEAK 29/100 | HIGH 68/100 | Do nothing |
| 6 | AKT/USD | 0.5228 | 45.60 | +0.52% | 0.48x | MODERATE 53/100 | VERY_HIGH 75/100 | Watch |
| 7 | CC/USD | 0.08301 | 42.73 | -0.17% | 1.31x | WEAK 41/100 | HIGH 66/100 | Watch |
| 8 | TRX/USD | 0.309813 | 38.41 | +0.06% | 0.23x | WEAK 39/100 | VERY_HIGH 70/100 | Watch |
| 9 | PEARL/USD | 1.8548 | 31.16 | +0.92% | 0.14x | WEAK 31/100 | EXTREME 92/100 | Do nothing |
| 10 | W/USD | 0.00902 | 29.98 | +0.22% | 0.56x | WEAK 40/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
