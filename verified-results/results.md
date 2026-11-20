# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T07:40:38.080123+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44696587180
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 506ee5907f1f75959987bbe57067172dd22c5870 (atomic ledger/results publication)
**Ledger generation:** 949 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 605; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.4732 | 104.082 | 69.539 | +11.05% | +3.91% | 2.56x | 29.7 | 2026-11-20T07:40:32.593473+00:00 | Not calibrated | STRONG 95/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 2 | XRP/USD | 0.9633 | 71.353 | 57.229 | +0.42% | -0.18% | 3.68x | 1.5 | 2026-11-20T07:40:32.593473+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XLM/USD | 0.134267 | 66.627 | 62.260 | +1.18% | -0.07% | 1.47x | 2.0 | 2026-11-20T07:40:32.593473+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SKR/USD | 0.010392 | 65.439 | 50.537 | +3.44% | +1.30% | 1.84x | 9.6 | 2026-11-20T07:40:32.593473+00:00 | Not calibrated | STRONG 78/100 | HIGH 67/100 | Watch | WATCH |
| 5 | ATOM/USD | 1.2681 | 49.478 | 32.657 | +0.52% | +0.36% | 2.52x | 7.1 | 2026-11-20T07:40:32.593473+00:00 | Not calibrated | STRONG 80/100 | HIGH 60/100 | Watch | WATCH |
| 6 | SYRUP/USD | 0.09944 | 42.904 | 50.433 | +3.34% | -0.77% | 0.63x | 10.1 | 2026-11-20T07:40:32.593473+00:00 | Not calibrated | WEAK 21/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | AUD/USD | 0.66756 | 41.646 | 40.661 | +0.31% | -0.01% | 1.11x | 1.0 | 2026-11-20T07:40:32.593473+00:00 | Not calibrated | WEAK 31/100 | HIGH 68/100 | Do nothing | WATCH |
| 8 | HBAR/USD | 0.05391 | 33.663 | 40.477 | +0.28% | +0.00% | 0.32x | 3.7 | 2026-11-20T07:40:32.593473+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ICNT/USD | 69.539 | 0.4732 | +3.91% | 2.56x |
| 2 | XLM/USD | 62.260 | 0.134267 | -0.07% | 1.47x |
| 3 | XRP/USD | 57.229 | 0.9633 | -0.18% | 3.68x |
| 4 | SKR/USD | 50.537 | 0.010392 | +1.30% | 1.84x |
| 5 | SYRUP/USD | 50.433 | 0.09944 | -0.77% | 0.63x |
| 6 | AUD/USD | 40.661 | 0.66756 | -0.01% | 1.11x |
| 7 | HBAR/USD | 40.477 | 0.05391 | +0.00% | 0.32x |
| 8 | ATOM/USD | 32.657 | 1.2681 | +0.36% | 2.52x |

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

- Persisted scans: 949; predictions: 8056; observations: 573416.
- Matured sampled outcomes across 1/6/24/48h: 9488; gap abstentions: 17418. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44696587180 · **Generation:** 949 · **Legacy run:** 44696587180
**Main quote time:** 2026-11-20T07:40:38.080123+00:00 · **Legacy report time:** 2026-11-20T07:41:34.081565+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.4732 | 104.08 | +3.91% | 2.56x | STRONG 100/100 | VERY_HIGH 77/100 | Watch |
| 2 | XRP/USD | 0.9633 | 71.35 | -0.18% | 3.68x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 3 | XLM/USD | 0.134267 | 66.63 | -0.07% | 1.47x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 4 | SKR/USD ⭐ | 0.010392 | 65.44 | +1.30% | 1.84x | STRONG 88/100 | HIGH 67/100 | Consider small entry |
| 5 | ATOM/USD ⭐ | 1.2681 | 49.48 | +0.36% | 2.52x | STRONG 90/100 | HIGH 60/100 | Consider small entry |
| 6 | SYRUP/USD | 0.09944 | 42.90 | -0.77% | 0.63x | WEAK 21/100 | EXTREME 87/100 | Do nothing |
| 7 | AUD/USD | 0.66756 | 41.65 | -0.01% | 1.11x | WEAK 31/100 | HIGH 68/100 | Do nothing |
| 8 | HBAR/USD | 0.05391 | 33.66 | +0.00% | 0.32x | WEAK 37/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.4718 | 89.83 | +3.91% | 2.56x | 7914 | STRONG 100/100 | VERY_HIGH 77/100 | Watch |
| 2 | SKR/USD ⭐ | 0.010409 | 65.09 | +1.30% | 1.84x | 1647 | STRONG 78/100 | VERY_HIGH 79/100 | Watch |
| 3 | ATOM/USD ⭐ | 1.2671 | 49.44 | +0.36% | 2.52x | 3294 | STRONG 90/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** ICNT/USD, SKR/USD, ATOM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
