# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T07:21:48.331257+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45957673238
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c495b03842a8bd3246dececd3a83022e35f249fa (atomic ledger/results publication)
**Ledger generation:** 1976 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 752.16 | 101.594 | 97.206 | +10.34% | +0.76% | 1.06x | 5.6 | 2026-11-27T07:21:41.849364+00:00 | Not calibrated | STRONG 85/100 | HIGH 62/100 | Watch | WATCH |
| 2 | XRP/USD | 0.97706 | 97.305 | 80.424 | +3.64% | +0.38% | 2.99x | 0.1 | 2026-11-27T07:21:41.849364+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | HYPE/USD | 66.16 | 95.909 | 97.815 | +6.33% | -0.24% | 0.93x | 3.0 | 2026-11-27T07:21:41.849364+00:00 | Not calibrated | MODERATE 53/100 | HIGH 68/100 | Watch | WATCH |
| 4 | ADA/USD | 0.153173 | 88.553 | 72.605 | +3.17% | +0.19% | 3.09x | 2.9 | 2026-11-27T07:21:41.849364+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 5 | LINK/USD | 9.57402 | 80.943 | 76.091 | +3.30% | +0.11% | 1.43x | 4.0 | 2026-11-27T07:21:41.849364+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 6 | ENA/USD | 0.1066 | 78.013 | 73.892 | +6.18% | +0.00% | 1.41x | 9.4 | 2026-11-27T07:21:41.849364+00:00 | Not calibrated | STRONG 74/100 | HIGH 60/100 | Watch | WATCH |
| 7 | UNI/USD | 4.8927 | 75.969 | 77.093 | +5.22% | +0.38% | 0.70x | 4.7 | 2026-11-27T07:21:41.849364+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | HBAR/USD | 0.05563 | 73.091 | 55.479 | +3.09% | +0.52% | 3.95x | 1.8 | 2026-11-27T07:21:41.849364+00:00 | Not calibrated | STRONG 92/100 | HIGH 60/100 | Consider small entry | WATCH |
| 9 | SOL/USD | 72.93 | 72.649 | 73.951 | +2.81% | -0.15% | 0.95x | 1.4 | 2026-11-27T07:21:41.849364+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 10 | ETH/USD | 1733.25 | 69.989 | 73.295 | +2.70% | -0.04% | 0.69x | 1.2 | 2026-11-27T07:21:41.849364+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | VVV/USD | 27.115 | 69.958 | 75.127 | +3.56% | -1.37% | 1.17x | 9.6 | 2026-11-27T07:21:41.849364+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 12 | XBT/USD | 61754.2 | 66.725 | 69.527 | +2.08% | +0.05% | 0.70x | 0.0 | 2026-11-27T07:21:41.849364+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | HYPE/USD | 97.815 | 66.16 | -0.24% | 0.93x |
| 2 | ZEC/USD | 97.206 | 752.16 | +0.76% | 1.06x |
| 3 | XRP/USD | 80.424 | 0.97706 | +0.38% | 2.99x |
| 4 | UNI/USD | 77.093 | 4.8927 | +0.38% | 0.70x |
| 5 | LINK/USD | 76.091 | 9.57402 | +0.11% | 1.43x |
| 6 | VVV/USD | 75.127 | 27.115 | -1.37% | 1.17x |
| 7 | SOL/USD | 73.951 | 72.93 | -0.15% | 0.95x |
| 8 | ENA/USD | 73.892 | 0.1066 | +0.00% | 1.41x |
| 9 | ETH/USD | 73.295 | 1733.25 | -0.04% | 0.69x |
| 10 | ADA/USD | 72.605 | 0.153173 | +0.19% | 3.09x |
| 11 | XBT/USD | 69.527 | 61754.2 | +0.05% | 0.70x |
| 12 | HBAR/USD | 55.479 | 0.05563 | +0.52% | 3.95x |

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

- Persisted scans: 1976; predictions: 17414; observations: 1196681.
- Matured sampled outcomes across 1/6/24/48h: 38477; gap abstentions: 25623. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45957673238 · **Generation:** 1976 · **Legacy run:** 45957673238
**Main quote time:** 2026-11-27T07:21:48.331257+00:00 · **Legacy report time:** 2026-11-27T07:22:34.227750+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 752.16 | 101.59 | +0.76% | 1.06x | STRONG 95/100 | HIGH 62/100 | Watch |
| 2 | XRP/USD ⭐ | 0.97706 | 97.31 | +0.38% | 2.99x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | HYPE/USD | 66.16 | 95.91 | -0.24% | 0.93x | MODERATE 53/100 | HIGH 68/100 | Watch |
| 4 | ADA/USD ⭐ | 0.153173 | 88.55 | +0.19% | 3.09x | STRONG 99/100 | HIGH 55/100 | Watch |
| 5 | LINK/USD ⭐ | 9.57402 | 80.94 | +0.11% | 1.43x | STRONG 85/100 | HIGH 55/100 | Watch |
| 6 | ENA/USD | 0.1066 | 78.01 | +0.00% | 1.41x | STRONG 74/100 | HIGH 60/100 | Watch |
| 7 | UNI/USD | 4.8927 | 75.97 | +0.38% | 0.70x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 8 | HBAR/USD | 0.05563 | 73.09 | +0.52% | 3.95x | STRONG 92/100 | HIGH 60/100 | Consider small entry |
| 9 | SOL/USD | 72.93 | 72.65 | -0.15% | 0.95x | WEAK 41/100 | HIGH 68/100 | Watch |
| 10 | ETH/USD | 1733.25 | 69.99 | -0.04% | 0.69x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 11 | VVV/USD | 27.115 | 69.96 | -1.37% | 1.17x | MODERATE 45/100 | VERY_HIGH 72/100 | Do nothing |
| 12 | XBT/USD | 61754.2 | 66.72 | +0.05% | 0.70x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.97688 | 100.00 | +0.38% | 2.99x | 21981 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 751.49 | 95.86 | +0.76% | 1.06x | 39408 | STRONG 93/100 | HIGH 62/100 | Watch |
| 3 | ADA/USD ⭐ | 0.153173 | 89.31 | +0.19% | 3.09x | 9673 | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | LINK/USD ⭐ | 9.57585 | 86.90 | +0.11% | 1.43x | 7618 | STRONG 88/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD, XRP/USD, ADA/USD, LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
