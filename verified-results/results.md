# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T07:01:42.738034+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45955409915
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1be0b42fc22bb5da0af294e6c0227e8fa059249e (atomic ledger/results publication)
**Ledger generation:** 1974 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 743.06 | 112.669 | 99.933 | +9.01% | -0.45% | 3.76x | 0.1 | 2026-11-27T07:01:36.237992+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | HYPE/USD | 66.08 | 104.530 | 97.670 | +6.20% | +0.41% | 1.48x | 1.5 | 2026-11-27T07:01:36.237992+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ADA/USD | 0.152774 | 84.037 | 70.668 | +2.91% | -0.33% | 4.34x | 3.7 | 2026-11-27T07:01:36.237992+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 4 | VVV/USD | 27.215 | 82.572 | 77.259 | +3.94% | +1.24% | 0.91x | 10.7 | 2026-11-27T07:01:36.237992+00:00 | Not calibrated | MODERATE 66/100 | HIGH 68/100 | Watch | WATCH |
| 5 | UNI/USD | 4.8528 | 71.407 | 71.659 | +4.36% | -0.03% | 0.99x | 3.1 | 2026-11-27T07:01:36.237992+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 6 | ENA/USD | 0.1062 | 71.351 | 71.023 | +5.78% | +0.28% | 0.89x | 9.4 | 2026-11-27T07:01:36.237992+00:00 | Not calibrated | MODERATE 66/100 | HIGH 67/100 | Watch | WATCH |
| 7 | XRP/USD | 0.97147 | 69.169 | 76.273 | +3.05% | +0.17% | 0.20x | 0.1 | 2026-11-27T07:01:36.237992+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | ETH/USD | 1730.54 | 68.838 | 72.748 | +2.54% | +0.06% | 0.58x | 0.1 | 2026-11-27T07:01:36.237992+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | SOL/USD | 72.92 | 68.748 | 73.852 | +2.79% | +0.16% | 0.41x | 1.4 | 2026-11-27T07:01:36.237992+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | LINK/USD | 9.57478 | 68.437 | 76.968 | +3.31% | -0.06% | 0.18x | 2.3 | 2026-11-27T07:01:36.237992+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XAUT/USD | 3647 | 65.271 | 49.529 | +2.45% | +0.15% | 3.66x | 0.5 | 2026-11-27T07:01:36.237992+00:00 | Not calibrated | STRONG 78/100 | HIGH 60/100 | Watch | WATCH |
| 12 | XBT/USD | 61602.9 | 61.544 | 67.776 | +1.83% | +0.03% | 0.36x | 0.0 | 2026-11-27T07:01:36.237992+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 99.933 | 743.06 | -0.45% | 3.76x |
| 2 | HYPE/USD | 97.670 | 66.08 | +0.41% | 1.48x |
| 3 | VVV/USD | 77.259 | 27.215 | +1.24% | 0.91x |
| 4 | LINK/USD | 76.968 | 9.57478 | -0.06% | 0.18x |
| 5 | XRP/USD | 76.273 | 0.97147 | +0.17% | 0.20x |
| 6 | SOL/USD | 73.852 | 72.92 | +0.16% | 0.41x |
| 7 | ETH/USD | 72.748 | 1730.54 | +0.06% | 0.58x |
| 8 | UNI/USD | 71.659 | 4.8528 | -0.03% | 0.99x |
| 9 | ENA/USD | 71.023 | 0.1062 | +0.28% | 0.89x |
| 10 | ADA/USD | 70.668 | 0.152774 | -0.33% | 4.34x |
| 11 | XBT/USD | 67.776 | 61602.9 | +0.03% | 0.36x |
| 12 | XAUT/USD | 49.529 | 3647 | +0.15% | 3.66x |

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

- Persisted scans: 1974; predictions: 17390; observations: 1195475.
- Matured sampled outcomes across 1/6/24/48h: 38412; gap abstentions: 25603. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45955409915 · **Generation:** 1974 · **Legacy run:** 45955409915
**Main quote time:** 2026-11-27T07:01:42.738034+00:00 · **Legacy report time:** 2026-11-27T07:02:24.150407+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 743.06 | 112.67 | -0.45% | 3.76x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | HYPE/USD ⭐ | 66.08 | 104.53 | +0.41% | 1.48x | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | ADA/USD | 0.152774 | 84.04 | -0.33% | 4.34x | STRONG 72/100 | HIGH 61/100 | Watch |
| 4 | VVV/USD | 27.215 | 82.57 | +1.24% | 0.91x | MODERATE 66/100 | HIGH 68/100 | Watch |
| 5 | UNI/USD | 4.8528 | 71.41 | -0.03% | 0.99x | WEAK 41/100 | HIGH 68/100 | Watch |
| 6 | ENA/USD | 0.1062 | 71.35 | +0.28% | 0.89x | MODERATE 66/100 | HIGH 67/100 | Watch |
| 7 | XRP/USD | 0.97147 | 69.17 | +0.17% | 0.20x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 8 | ETH/USD | 1730.54 | 68.84 | +0.06% | 0.58x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 9 | SOL/USD | 72.92 | 68.75 | +0.16% | 0.41x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 10 | LINK/USD | 9.57478 | 68.44 | -0.06% | 0.18x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 11 | XAUT/USD | 3647 | 65.27 | +0.15% | 3.66x | STRONG 78/100 | HIGH 60/100 | Watch |
| 12 | XBT/USD | 61602.9 | 61.54 | +0.03% | 0.36x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 66.14 | 100.00 | +0.41% | 1.48x | 15603 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | BIGTIME/USD | 0.006422 | 76.84 | +1.09% | 1.74x | 5059 | STRONG 78/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
