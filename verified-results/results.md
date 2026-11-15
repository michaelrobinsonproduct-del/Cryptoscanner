# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-15T19:44:38.719219+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43754066051
**Source SHA:** 885b4a0465f5c74a8a87db5ca921c3c0a00021af
**Previous ledger commit:** fb09d9a430d6ccf15f3c79a647a21191b6552106 (atomic ledger/results publication)
**Ledger generation:** 438 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 157.3 | 108.215 | 89.184 | +9.76% | +0.81% | 5.53x | 21.6 | 2026-11-15T19:44:30.612112+00:00 | Not calibrated | STRONG 95/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | NEAR/USD | 3.1594 | 96.672 | 83.577 | +4.31% | +0.10% | 2.26x | 3.2 | 2026-11-15T19:44:30.612112+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ETH/USD | 1825.23 | 93.031 | 77.562 | +3.23% | +0.09% | 3.49x | 0.1 | 2026-11-15T19:44:30.612112+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Watch | WATCH |
| 4 | UNI/USD | 5.1942 | 90.714 | 97.987 | +6.39% | +0.08% | 0.23x | 3.5 | 2026-11-15T19:44:30.612112+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | XMR/USD | 499.49 | 88.494 | 95.748 | +6.24% | +0.10% | 0.23x | 5.8 | 2026-11-15T19:44:30.612112+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | CC/USD | 0.0832 | 87.918 | 85.743 | +7.20% | +0.12% | 1.16x | 8.4 | 2026-11-15T19:44:30.612112+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 7 | XRP/USD | 0.95974 | 87.166 | 89.791 | +5.03% | +0.36% | 0.56x | 0.8 | 2026-11-15T19:44:30.612112+00:00 | Not calibrated | STRONG 74/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | ZEC/USD | 901.08 | 86.439 | 83.264 | +4.31% | +0.18% | 1.23x | 3.8 | 2026-11-15T19:44:30.612112+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 9 | AAVE/USD | 107.87 | 86.084 | 85.913 | +7.28% | +0.06% | 0.98x | 8.3 | 2026-11-15T19:44:30.612112+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 10 | ASTER/USD | 0.54936 | 82.114 | 83.604 | +9.74% | +0.57% | 0.57x | 5.5 | 2026-11-15T19:44:30.612112+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | HYPE/USD | 67.2 | 79.658 | 85.713 | +4.49% | -0.03% | 0.41x | 1.5 | 2026-11-15T19:44:30.612112+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0589676 | 79.451 | 74.723 | +2.88% | +0.05% | 1.45x | 0.9 | 2026-11-15T19:44:30.612112+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UNI/USD | 97.987 | 5.1942 | +0.08% | 0.23x |
| 2 | XMR/USD | 95.748 | 499.49 | +0.10% | 0.23x |
| 3 | XRP/USD | 89.791 | 0.95974 | +0.36% | 0.56x |
| 4 | QNT/USD | 89.184 | 157.3 | +0.81% | 5.53x |
| 5 | AAVE/USD | 85.913 | 107.87 | +0.06% | 0.98x |
| 6 | CC/USD | 85.743 | 0.0832 | +0.12% | 1.16x |
| 7 | HYPE/USD | 85.713 | 67.2 | -0.03% | 0.41x |
| 8 | ASTER/USD | 83.604 | 0.54936 | +0.57% | 0.57x |
| 9 | NEAR/USD | 83.577 | 3.1594 | +0.10% | 2.26x |
| 10 | ZEC/USD | 83.264 | 901.08 | +0.18% | 1.23x |
| 11 | ETH/USD | 77.562 | 1825.23 | +0.09% | 3.49x |
| 12 | XDG/USD | 74.723 | 0.0589676 | +0.05% | 1.45x |

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

- Persisted scans: 438; predictions: 3772; observations: 263781.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 11132. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 43754066051 · **Generation:** 438 · **Legacy run:** 43754066051
**Main quote time:** 2026-11-15T19:44:38.719219+00:00 · **Legacy report time:** 2026-11-15T19:44:54.884610+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 157.3 | 108.22 | +0.81% | 5.53x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 3.1594 | 96.67 | +0.10% | 2.26x | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | ETH/USD ⭐ | 1825.23 | 93.03 | +0.09% | 3.49x | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | UNI/USD | 5.1942 | 90.71 | +0.08% | 0.23x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 5 | XMR/USD | 499.49 | 88.49 | +0.10% | 0.23x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 6 | CC/USD | 0.0832 | 87.92 | +0.12% | 1.16x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 7 | XRP/USD | 0.95974 | 87.17 | +0.36% | 0.56x | STRONG 74/100 | VERY_HIGH 70/100 | Watch |
| 8 | ZEC/USD ⭐ | 901.08 | 86.44 | +0.18% | 1.23x | STRONG 78/100 | HIGH 62/100 | Watch |
| 9 | AAVE/USD | 107.87 | 86.08 | +0.06% | 0.98x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 10 | ASTER/USD | 0.54936 | 82.11 | +0.57% | 0.57x | STRONG 71/100 | VERY_HIGH 70/100 | Watch |
| 11 | HYPE/USD | 67.2 | 79.66 | -0.03% | 0.41x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 12 | XDG/USD | 0.0589676 | 79.45 | +0.05% | 1.45x | STRONG 75/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.1602 | 100.00 | +0.10% | 2.26x | 16074 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | ETH/USD ⭐ | 1825.45 | 99.05 | +0.09% | 3.49x | 84300 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | QNT/USD ⭐ | 157.74 | 95.42 | +0.81% | 5.53x | 9531 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 4 | ZEC/USD ⭐ | 901.3 | 93.24 | +0.18% | 1.23x | 33216 | STRONG 82/100 | HIGH 62/100 | Watch |
| 5 | SUI/USD | 0.7235 | 92.00 | +0.08% | 1.82x | 21623 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** QNT/USD, NEAR/USD, ETH/USD, ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
