# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T09:50:53.802016+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44891397531
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** d1d49533dc7891f68b24a00e646d66698e3477ef (atomic ledger/results publication)
**Ledger generation:** 1117 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.66 | 79.990 | 82.631 | +4.44% | +0.00% | 0.74x | 6.9 | 2026-11-21T09:50:44.951882+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | RARE/USD | 0.0141 | 75.743 | 59.890 | +6.01% | +3.00% | 1.08x | 28.5 | 2026-11-21T09:50:44.951882+00:00 | Not calibrated | MODERATE 63/100 | EXTREME 89/100 | Do nothing | WATCH |
| 3 | XMR/USD | 461.18 | 63.884 | 55.332 | +1.07% | +0.72% | 1.49x | 14.3 | 2026-11-21T09:50:44.951882+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ZAMA/USD | 0.05852 | 63.393 | 45.731 | +2.65% | +0.53% | 8.54x | 8.5 | 2026-11-21T09:50:44.951882+00:00 | Not calibrated | STRONG 87/100 | HIGH 67/100 | Watch | WATCH |
| 5 | CAP/USD | 0.093822 | 62.897 | 48.099 | +2.49% | -0.04% | 3.15x | 6.1 | 2026-11-21T09:50:44.951882+00:00 | Not calibrated | MODERATE 61/100 | HIGH 66/100 | Watch | WATCH |
| 6 | ETH/USD | 1636.33 | 61.500 | 62.322 | +1.05% | +0.01% | 0.91x | 0.1 | 2026-11-21T09:50:44.951882+00:00 | Not calibrated | MODERATE 51/100 | HIGH 62/100 | Watch | WATCH |
| 7 | TRX/USD | 0.30273 | 49.428 | 57.830 | +0.41% | +0.01% | 0.16x | 0.0 | 2026-11-21T09:50:44.951882+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | MORPHO/USD | 1.54725 | 35.767 | 34.134 | +1.03% | -0.12% | 1.22x | 15.3 | 2026-11-21T09:50:44.951882+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 82.631 | 21.66 | +0.00% | 0.74x |
| 2 | ETH/USD | 62.322 | 1636.33 | +0.01% | 0.91x |
| 3 | RARE/USD | 59.890 | 0.0141 | +3.00% | 1.08x |
| 4 | TRX/USD | 57.830 | 0.30273 | +0.01% | 0.16x |
| 5 | XMR/USD | 55.332 | 461.18 | +0.72% | 1.49x |
| 6 | CAP/USD | 48.099 | 0.093822 | -0.04% | 3.15x |
| 7 | ZAMA/USD | 45.731 | 0.05852 | +0.53% | 8.54x |
| 8 | MORPHO/USD | 34.134 | 1.54725 | -0.12% | 1.22x |

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

- Persisted scans: 1117; predictions: 8768; observations: 675495.
- Matured sampled outcomes across 1/6/24/48h: 11546; gap abstentions: 20303. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44891397531 · **Generation:** 1117 · **Legacy run:** 44891397531
**Main quote time:** 2026-11-21T09:50:53.802016+00:00 · **Legacy report time:** 2026-11-21T09:51:44.532734+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 21.66 | 79.99 | +0.00% | 0.74x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 2 | RARE/USD ⭐ | 0.0141 | 75.74 | +3.00% | 1.08x | STRONG 73/100 | EXTREME 89/100 | Do nothing |
| 3 | XMR/USD ⭐ | 461.18 | 63.88 | +0.72% | 1.49x | STRONG 82/100 | HIGH 61/100 | Watch |
| 4 | ZAMA/USD ⭐ | 0.05852 | 63.39 | +0.53% | 8.54x | STRONG 97/100 | HIGH 67/100 | Consider small entry |
| 5 | CAP/USD | 0.093822 | 62.90 | -0.04% | 3.15x | MODERATE 61/100 | HIGH 66/100 | Watch |
| 6 | ETH/USD | 1636.33 | 61.50 | +0.01% | 0.91x | MODERATE 51/100 | HIGH 62/100 | Watch |
| 7 | TRX/USD | 0.30273 | 49.43 | +0.01% | 0.16x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 8 | MORPHO/USD | 1.54725 | 35.77 | -0.12% | 1.22x | WEAK 23/100 | VERY_HIGH 79/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | RARE/USD ⭐ | 0.01418 | 79.55 | +3.00% | 1.08x | 7607 | STRONG 75/100 | EXTREME 89/100 | Do nothing |
| 2 | ZAMA/USD ⭐ | 0.05851 | 64.05 | +0.53% | 8.54x | 2973 | STRONG 92/100 | VERY_HIGH 73/100 | Watch |
| 3 | XMR/USD ⭐ | 460.53 | 52.29 | +0.72% | 1.49x | 11667 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** RARE/USD, XMR/USD, ZAMA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
