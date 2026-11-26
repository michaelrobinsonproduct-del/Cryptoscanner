# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T01:26:06.152045+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45735562987
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** cbbb6ed2390fdfc084c403f0a5c88345c5383286 (atomic ledger/results publication)
**Ledger generation:** 1793 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XDG/USD | 0.0565096 | 73.252 | 56.908 | +0.98% | +0.27% | 2.53x | 0.0 | 2026-11-26T01:26:00.173418+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 30.222 | 71.615 | 75.151 | +3.52% | +0.31% | 0.49x | 8.9 | 2026-11-26T01:26:00.173418+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | ZEC/USD | 772.33 | 64.875 | 55.046 | +0.28% | +1.16% | 1.40x | 3.8 | 2026-11-26T01:26:00.173418+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ADA/USD | 0.147136 | 64.128 | 60.031 | +0.94% | +0.44% | 1.19x | 3.1 | 2026-11-26T01:26:00.173418+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 5 | XRP/USD | 0.94426 | 63.903 | 60.225 | +0.82% | +0.46% | 1.14x | 1.1 | 2026-11-26T01:26:00.173418+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 6 | SUI/USD | 0.6737 | 62.574 | 61.289 | +1.11% | +0.30% | 0.98x | 3.0 | 2026-11-26T01:26:00.173418+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 7 | SOL/USD | 71.04 | 62.022 | 60.760 | +0.92% | +0.32% | 0.96x | 1.4 | 2026-11-26T01:26:00.173418+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XBT/USD | 60760.1 | 58.868 | 59.531 | +0.65% | +0.42% | 0.73x | 0.0 | 2026-11-26T01:26:00.173418+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | LINK/USD | 9.12498 | 58.189 | 54.804 | +0.89% | +0.41% | 1.13x | 1.4 | 2026-11-26T01:26:00.173418+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 10 | NEAR/USD | 3.0881 | 57.867 | 61.824 | +1.25% | +0.10% | 0.55x | 3.9 | 2026-11-26T01:26:00.173418+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ETH/USD | 1702.57 | 57.033 | 60.006 | +0.72% | +0.34% | 0.54x | 0.1 | 2026-11-26T01:26:00.173418+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | LTC/USD | 43.16 | 55.626 | 60.059 | +1.05% | +0.42% | 0.35x | 4.6 | 2026-11-26T01:26:00.173418+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 75.151 | 30.222 | +0.31% | 0.49x |
| 2 | NEAR/USD | 61.824 | 3.0881 | +0.10% | 0.55x |
| 3 | SUI/USD | 61.289 | 0.6737 | +0.30% | 0.98x |
| 4 | SOL/USD | 60.760 | 71.04 | +0.32% | 0.96x |
| 5 | XRP/USD | 60.225 | 0.94426 | +0.46% | 1.14x |
| 6 | LTC/USD | 60.059 | 43.16 | +0.42% | 0.35x |
| 7 | ADA/USD | 60.031 | 0.147136 | +0.44% | 1.19x |
| 8 | ETH/USD | 60.006 | 1702.57 | +0.34% | 0.54x |
| 9 | XBT/USD | 59.531 | 60760.1 | +0.42% | 0.73x |
| 10 | XDG/USD | 56.908 | 0.0565096 | +0.27% | 2.53x |
| 11 | ZEC/USD | 55.046 | 772.33 | +1.16% | 1.40x |
| 12 | LINK/USD | 54.804 | 9.12498 | +0.41% | 1.13x |

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

- Persisted scans: 1793; predictions: 15251; observations: 1086981.
- Matured sampled outcomes across 1/6/24/48h: 33152; gap abstentions: 23576. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45735562987 · **Generation:** 1793 · **Legacy run:** 45735562987
**Main quote time:** 2026-11-26T01:26:06.152045+00:00 · **Legacy report time:** 2026-11-26T01:27:00.592448+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XDG/USD ⭐ | 0.0565096 | 73.25 | +0.27% | 2.53x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD | 30.222 | 71.61 | +0.31% | 0.49x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 3 | ZEC/USD | 772.33 | 64.87 | +1.16% | 1.40x | STRONG 77/100 | HIGH 55/100 | Watch |
| 4 | ADA/USD ⭐ | 0.147136 | 64.13 | +0.44% | 1.19x | STRONG 77/100 | HIGH 62/100 | Watch |
| 5 | XRP/USD ⭐ | 0.94426 | 63.90 | +0.46% | 1.14x | STRONG 77/100 | HIGH 62/100 | Watch |
| 6 | SUI/USD | 0.6737 | 62.57 | +0.30% | 0.98x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 7 | SOL/USD | 71.04 | 62.02 | +0.32% | 0.96x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 8 | XBT/USD | 60760.1 | 58.87 | +0.42% | 0.73x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 9 | LINK/USD | 9.12498 | 58.19 | +0.41% | 1.13x | MODERATE 64/100 | HIGH 62/100 | Watch |
| 10 | NEAR/USD | 3.0881 | 57.87 | +0.10% | 0.55x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 11 | ETH/USD | 1702.57 | 57.03 | +0.34% | 0.54x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 12 | LTC/USD | 43.16 | 55.63 | +0.42% | 0.35x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HONEY/USD | 0.000213 | 94.92 | +15.73% | 1.77x | 13453 | STRONG 77/100 | EXTREME 87/100 | Do nothing |
| 2 | XDG/USD ⭐ | 0.0564718 | 66.46 | +0.27% | 2.53x | 7772 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 3 | XRP/USD ⭐ | 0.94321 | 60.12 | +0.46% | 1.14x | 42684 | STRONG 75/100 | HIGH 62/100 | Watch |
| 4 | ADA/USD ⭐ | 0.147136 | 59.20 | +0.44% | 1.19x | 11009 | STRONG 75/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XDG/USD, ADA/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
