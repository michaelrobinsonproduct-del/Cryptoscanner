# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T04:57:42.601162+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46109681093
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 515ca476c354945b14b570ad265f0fc7951762b2 (atomic ledger/results publication)
**Ledger generation:** 2108 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 746.02 | 77.242 | 64.169 | +1.56% | -0.39% | 3.60x | 3.5 | 2026-11-28T04:57:36.261420+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SENT/USD | 0.024672 | 76.813 | 58.818 | +4.04% | +0.60% | 5.95x | 0.8 | 2026-11-28T04:57:36.261420+00:00 | Not calibrated | STRONG 93/100 | HIGH 67/100 | Consider small entry | WATCH |
| 3 | XMR/USD | 418.66 | 75.740 | 73.382 | +2.80% | -0.08% | 1.27x | 2.4 | 2026-11-28T04:57:36.261420+00:00 | Not calibrated | MODERATE 48/100 | HIGH 61/100 | Watch | WATCH |
| 4 | NEAR/USD | 3.0293 | 68.055 | 55.924 | +0.37% | -0.57% | 4.22x | 3.3 | 2026-11-28T04:57:36.261420+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 5 | VVV/USD | 26.331 | 52.785 | 58.712 | +2.26% | -0.08% | 0.45x | 6.8 | 2026-11-28T04:57:36.261420+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | HYPE/USD | 63.99 | 48.541 | 59.732 | +0.79% | -0.64% | 0.20x | 1.6 | 2026-11-28T04:57:36.261420+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | BCH/USD | 208.25 | 33.567 | 38.874 | +0.60% | -0.51% | 0.72x | 3.4 | 2026-11-28T04:57:36.261420+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 8 | SEI/USD | 0.03869 | 28.528 | 34.014 | +0.73% | +0.36% | 0.27x | 7.8 | 2026-11-28T04:57:36.261420+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | SPX/USD | 0.2734 | 17.736 | 23.492 | +0.37% | +0.22% | 0.31x | 21.9 | 2026-11-28T04:57:36.261420+00:00 | Not calibrated | WEAK 29/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 73.382 | 418.66 | -0.08% | 1.27x |
| 2 | ZEC/USD | 64.169 | 746.02 | -0.39% | 3.60x |
| 3 | HYPE/USD | 59.732 | 63.99 | -0.64% | 0.20x |
| 4 | SENT/USD | 58.818 | 0.024672 | +0.60% | 5.95x |
| 5 | VVV/USD | 58.712 | 26.331 | -0.08% | 0.45x |
| 6 | NEAR/USD | 55.924 | 3.0293 | -0.57% | 4.22x |
| 7 | BCH/USD | 38.874 | 208.25 | -0.51% | 0.72x |
| 8 | SEI/USD | 34.014 | 0.03869 | +0.36% | 0.27x |
| 9 | SPX/USD | 23.492 | 0.2734 | +0.22% | 0.31x |

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

- Persisted scans: 2108; predictions: 18931; observations: 1276494.
- Matured sampled outcomes across 1/6/24/48h: 43990; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46109681093 · **Generation:** 2108 · **Legacy run:** 46109681093
**Main quote time:** 2026-11-28T04:57:42.601162+00:00 · **Legacy report time:** 2026-11-28T04:58:30.102631+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 746.02 | 77.24 | -0.39% | 3.60x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 2 | SENT/USD ⭐ | 0.024672 | 76.81 | +0.60% | 5.95x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 3 | XMR/USD | 418.66 | 75.74 | -0.08% | 1.27x | MODERATE 48/100 | HIGH 61/100 | Watch |
| 4 | NEAR/USD | 3.0293 | 68.05 | -0.57% | 4.22x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 5 | VVV/USD | 26.331 | 52.79 | -0.08% | 0.45x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | HYPE/USD | 63.99 | 48.54 | -0.64% | 0.20x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | BCH/USD | 208.25 | 33.57 | -0.51% | 0.72x | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing |
| 8 | SEI/USD | 0.03869 | 28.53 | +0.36% | 0.27x | WEAK 44/100 | VERY_HIGH 75/100 | Watch |
| 9 | SPX/USD | 0.2734 | 17.74 | +0.22% | 0.31x | WEAK 29/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.024672 | 88.04 | +0.60% | 5.95x | 4342 | STRONG 100/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
