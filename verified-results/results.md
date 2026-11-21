# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T16:20:55.064199+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44923947168
**Source SHA:** 7ac7b40f8385b7b363a3015feba153e001ac4fc4
**Previous ledger commit:** 6db78fe94b7af3717441fa8233e39d09895a43a0 (atomic ledger/results publication)
**Ledger generation:** 1156 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 23.14 | 111.784 | 97.623 | +11.58% | -0.17% | 3.28x | 4.8 | 2026-11-21T16:20:48.239261+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | UNI/USD | 4.7089 | 93.847 | 89.262 | +5.41% | +0.42% | 1.25x | 7.2 | 2026-11-21T16:20:48.239261+00:00 | Not calibrated | STRONG 82/100 | HIGH 62/100 | Watch | WATCH |
| 3 | XMR/USD | 477.52 | 86.003 | 83.267 | +4.65% | +0.45% | 1.05x | 8.6 | 2026-11-21T16:20:48.239261+00:00 | Not calibrated | STRONG 78/100 | HIGH 62/100 | Watch | WATCH |
| 4 | ZEC/USD | 782.95 | 81.218 | 76.082 | +3.30% | -0.43% | 1.73x | 4.1 | 2026-11-21T16:20:48.239261+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ETH/USD | 1675.16 | 72.914 | 79.109 | +3.45% | -0.18% | 0.47x | 0.1 | 2026-11-21T16:20:48.239261+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | USELESS/USD | 0.08202 | 68.735 | 72.456 | +10.09% | +0.22% | 0.52x | 24.4 | 2026-11-21T16:20:48.239261+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 7 | SOL/USD | 70.11 | 64.764 | 68.550 | +2.04% | +0.01% | 0.61x | 1.4 | 2026-11-21T16:20:48.239261+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XDG/USD | 0.054856 | 62.909 | 62.484 | +1.07% | -0.08% | 1.08x | 0.0 | 2026-11-21T16:20:48.239261+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 9 | XRP/USD | 0.92556 | 62.453 | 67.602 | +1.85% | +0.35% | 0.31x | 0.8 | 2026-11-21T16:20:48.239261+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | TAO/USD | 185.8827 | 62.158 | 71.876 | +2.98% | -0.70% | 0.38x | 7.9 | 2026-11-21T16:20:48.239261+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XBT/USD | 59735.8 | 62.016 | 66.055 | +1.58% | -0.06% | 0.62x | 0.0 | 2026-11-21T16:20:48.239261+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | BEAM/USD | 0.003533 | 58.400 | 72.593 | +7.78% | -1.78% | 0.47x | 8.5 | 2026-11-21T16:20:48.239261+00:00 | Not calibrated | WEAK 34/100 | EXTREME 85/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 97.623 | 23.14 | -0.17% | 3.28x |
| 2 | UNI/USD | 89.262 | 4.7089 | +0.42% | 1.25x |
| 3 | XMR/USD | 83.267 | 477.52 | +0.45% | 1.05x |
| 4 | ETH/USD | 79.109 | 1675.16 | -0.18% | 0.47x |
| 5 | ZEC/USD | 76.082 | 782.95 | -0.43% | 1.73x |
| 6 | BEAM/USD | 72.593 | 0.003533 | -1.78% | 0.47x |
| 7 | USELESS/USD | 72.456 | 0.08202 | +0.22% | 0.52x |
| 8 | TAO/USD | 71.876 | 185.8827 | -0.70% | 0.38x |
| 9 | SOL/USD | 68.550 | 70.11 | +0.01% | 0.61x |
| 10 | XRP/USD | 67.602 | 0.92556 | +0.35% | 0.31x |
| 11 | XBT/USD | 66.055 | 59735.8 | -0.06% | 0.62x |
| 12 | XDG/USD | 62.484 | 0.054856 | -0.08% | 1.08x |

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

- Persisted scans: 1156; predictions: 9181; observations: 699207.
- Matured sampled outcomes across 1/6/24/48h: 12080; gap abstentions: 20778. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44923947168 · **Generation:** 1156 · **Legacy run:** 44923947168
**Main quote time:** 2026-11-21T16:20:55.064199+00:00 · **Legacy report time:** 2026-11-21T16:22:00.258119+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 23.14 | 111.78 | -0.17% | 3.28x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | UNI/USD ⭐ | 4.7089 | 93.85 | +0.42% | 1.25x | STRONG 92/100 | HIGH 62/100 | Watch |
| 3 | XMR/USD ⭐ | 477.52 | 86.00 | +0.45% | 1.05x | STRONG 88/100 | HIGH 62/100 | Watch |
| 4 | ZEC/USD | 782.95 | 81.22 | -0.43% | 1.73x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 5 | ETH/USD | 1675.16 | 72.91 | -0.18% | 0.47x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 6 | USELESS/USD | 0.08202 | 68.74 | +0.22% | 0.52x | MODERATE 54/100 | VERY_HIGH 82/100 | Watch |
| 7 | SOL/USD | 70.11 | 64.76 | +0.01% | 0.61x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 8 | XDG/USD | 0.054856 | 62.91 | -0.08% | 1.08x | WEAK 41/100 | HIGH 68/100 | Watch |
| 9 | XRP/USD | 0.92556 | 62.45 | +0.35% | 0.31x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 10 | TAO/USD | 185.8827 | 62.16 | -0.70% | 0.38x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 11 | XBT/USD | 59735.8 | 62.02 | -0.06% | 0.62x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 12 | BEAM/USD | 0.003533 | 58.40 | -1.78% | 0.47x | WEAK 34/100 | EXTREME 85/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.7057 | 98.01 | +0.42% | 1.25x | 12168 | STRONG 94/100 | HIGH 62/100 | Watch |
| 2 | SHX/USD | 0.003506 | 89.32 | +0.31% | 12.21x | 2780 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | XMR/USD ⭐ | 477.52 | 86.54 | +0.45% | 1.05x | 12728 | STRONG 88/100 | HIGH 62/100 | Watch |

**Same-run overlap:** UNI/USD, XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
