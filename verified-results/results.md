# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T06:00:33.280108+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44684655804
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** fd9c475d64fe9c05de1ca52970eed06959bb6155 (atomic ledger/results publication)
**Ledger generation:** 937 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 605; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XLM/USD | 0.133856 | 65.481 | 59.901 | +0.87% | +1.00% | 1.06x | 2.4 | 2026-11-20T06:00:28.251808+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 2 | XRP/USD | 0.96818 | 64.953 | 61.052 | +0.93% | +0.52% | 1.13x | 0.9 | 2026-11-20T06:00:28.251808+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 3 | SKR/USD | 0.010294 | 61.154 | 43.627 | +2.47% | +1.65% | 1.93x | 9.7 | 2026-11-20T06:00:28.251808+00:00 | Not calibrated | STRONG 76/100 | HIGH 67/100 | Watch | WATCH |
| 4 | HBAR/USD | 0.05391 | 59.349 | 40.801 | +0.28% | +0.71% | 3.07x | 1.9 | 2026-11-20T06:00:28.251808+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 61.052 | 0.96818 | +0.52% | 1.13x |
| 2 | XLM/USD | 59.901 | 0.133856 | +1.00% | 1.06x |
| 3 | SKR/USD | 43.627 | 0.010294 | +1.65% | 1.93x |
| 4 | HBAR/USD | 40.801 | 0.05391 | +0.71% | 3.07x |

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

- Persisted scans: 937; predictions: 7964; observations: 566156.
- Matured sampled outcomes across 1/6/24/48h: 9325; gap abstentions: 17101. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44684655804 · **Generation:** 937 · **Legacy run:** 44684655804
**Main quote time:** 2026-11-20T06:00:33.280108+00:00 · **Legacy report time:** 2026-11-20T06:01:41.169729+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD ⭐ | 0.133856 | 65.48 | +1.00% | 1.06x | STRONG 78/100 | HIGH 62/100 | Watch |
| 2 | XRP/USD ⭐ | 0.96818 | 64.95 | +0.52% | 1.13x | STRONG 77/100 | HIGH 62/100 | Watch |
| 3 | SKR/USD ⭐ | 0.010294 | 61.15 | +1.65% | 1.93x | STRONG 86/100 | HIGH 67/100 | Consider small entry |
| 4 | HBAR/USD ⭐ | 0.05391 | 59.35 | +0.71% | 3.07x | STRONG 95/100 | HIGH 55/100 | Consider small entry |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.96966 | 65.86 | +0.52% | 1.13x | 32833 | STRONG 78/100 | HIGH 62/100 | Watch |
| 2 | XLM/USD ⭐ | 0.133827 | 57.80 | +1.00% | 1.06x | 9927 | STRONG 74/100 | HIGH 62/100 | Watch |
| 3 | SKR/USD ⭐ | 0.010294 | 55.65 | +1.65% | 1.93x | 1596 | STRONG 83/100 | HIGH 67/100 | Consider small entry |
| 4 | AUD/USD | 0.66674 | 50.36 | +0.11% | 3.05x | 3994 | STRONG 70/100 | HIGH 55/100 | Watch |
| 5 | HBAR/USD ⭐ | 0.05397 | 50.28 | +0.71% | 3.07x | 8691 | STRONG 90/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XLM/USD, XRP/USD, SKR/USD, HBAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
