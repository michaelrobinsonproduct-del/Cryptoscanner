# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T19:10:57.135595+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44939416187
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** b16cbdf28b15412c9e10dca8d361c8bd5bfa87bc (atomic ledger/results publication)
**Ledger generation:** 1174 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.6906 | 100.633 | 88.833 | +5.00% | -0.07% | 2.22x | 2.3 | 2026-11-21T19:10:47.833160+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XMR/USD | 484.25 | 95.772 | 94.586 | +6.13% | -0.46% | 1.35x | 6.6 | 2026-11-21T19:10:47.833160+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04538 | 90.408 | 90.274 | +7.48% | +0.18% | 0.93x | 6.6 | 2026-11-21T19:10:47.833160+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 4 | XBT/USD | 60175.8 | 85.230 | 71.292 | +2.33% | +0.38% | 2.20x | 0.0 | 2026-11-21T19:10:47.833160+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | ZEC/USD | 789.24 | 83.233 | 83.175 | +4.13% | -0.08% | 1.05x | 1.5 | 2026-11-21T19:10:47.833160+00:00 | Not calibrated | MODERATE 52/100 | HIGH 68/100 | Watch | WATCH |
| 6 | ETH/USD | 1682.23 | 82.594 | 82.165 | +3.88% | +0.23% | 0.93x | 0.1 | 2026-11-21T19:10:47.833160+00:00 | Not calibrated | STRONG 71/100 | HIGH 62/100 | Watch | WATCH |
| 7 | XRP/USD | 0.93455 | 76.021 | 74.531 | +2.84% | -0.02% | 1.16x | 0.7 | 2026-11-21T19:10:47.833160+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 8 | SOL/USD | 70.64 | 75.886 | 73.246 | +2.81% | -0.06% | 1.29x | 2.8 | 2026-11-21T19:10:47.833160+00:00 | Not calibrated | MODERATE 48/100 | HIGH 61/100 | Watch | WATCH |
| 9 | TAO/USD | 186 | 74.748 | 73.861 | +3.04% | -0.06% | 1.12x | 4.9 | 2026-11-21T19:10:47.833160+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 10 | XDG/USD | 0.055239 | 70.834 | 66.519 | +1.78% | +0.02% | 1.42x | 1.8 | 2026-11-21T19:10:47.833160+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 11 | BNB/USD | 548.12 | 68.365 | 57.726 | +1.57% | +0.23% | 1.95x | 1.6 | 2026-11-21T19:10:47.833160+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 12 | PEARL/USD | 2.0014 | 68.246 | 74.935 | +9.47% | -1.43% | 1.04x | 33.6 | 2026-11-21T19:10:47.833160+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 84/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 94.586 | 484.25 | -0.46% | 1.35x |
| 2 | NIGHT/USD | 90.274 | 0.04538 | +0.18% | 0.93x |
| 3 | UNI/USD | 88.833 | 4.6906 | -0.07% | 2.22x |
| 4 | ZEC/USD | 83.175 | 789.24 | -0.08% | 1.05x |
| 5 | ETH/USD | 82.165 | 1682.23 | +0.23% | 0.93x |
| 6 | PEARL/USD | 74.935 | 2.0014 | -1.43% | 1.04x |
| 7 | XRP/USD | 74.531 | 0.93455 | -0.02% | 1.16x |
| 8 | TAO/USD | 73.861 | 186 | -0.06% | 1.12x |
| 9 | SOL/USD | 73.246 | 70.64 | -0.06% | 1.29x |
| 10 | XBT/USD | 71.292 | 60175.8 | +0.38% | 2.20x |
| 11 | XDG/USD | 66.519 | 0.055239 | +0.02% | 1.42x |
| 12 | BNB/USD | 57.726 | 548.12 | +0.23% | 1.95x |

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

- Persisted scans: 1174; predictions: 9397; observations: 710151.
- Matured sampled outcomes across 1/6/24/48h: 12438; gap abstentions: 21170. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44939416187 · **Generation:** 1174 · **Legacy run:** 44939416187
**Main quote time:** 2026-11-21T19:10:57.135595+00:00 · **Legacy report time:** 2026-11-21T19:11:41.006688+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD | 4.6906 | 100.63 | -0.07% | 2.22x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | XMR/USD | 484.25 | 95.77 | -0.46% | 1.35x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 3 | NIGHT/USD | 0.04538 | 90.41 | +0.18% | 0.93x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 4 | XBT/USD ⭐ | 60175.8 | 85.23 | +0.38% | 2.20x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | ZEC/USD | 789.24 | 83.23 | -0.08% | 1.05x | MODERATE 52/100 | HIGH 68/100 | Watch |
| 6 | ETH/USD | 1682.23 | 82.59 | +0.23% | 0.93x | STRONG 71/100 | HIGH 62/100 | Watch |
| 7 | XRP/USD | 0.93455 | 76.02 | -0.02% | 1.16x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 8 | SOL/USD | 70.64 | 75.89 | -0.06% | 1.29x | MODERATE 48/100 | HIGH 61/100 | Watch |
| 9 | TAO/USD | 186 | 74.75 | -0.06% | 1.12x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 10 | XDG/USD | 0.055239 | 70.83 | +0.02% | 1.42x | STRONG 70/100 | HIGH 55/100 | Watch |
| 11 | BNB/USD | 548.12 | 68.36 | +0.23% | 1.95x | STRONG 79/100 | HIGH 55/100 | Watch |
| 12 | PEARL/USD | 2.0014 | 68.25 | -1.43% | 1.04x | WEAK 34/100 | VERY_HIGH 84/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XBT/USD ⭐ | 60186.1 | 86.08 | +0.38% | 2.20x | 227752 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
