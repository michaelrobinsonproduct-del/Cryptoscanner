# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T23:21:09.491212+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44961229105
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 034fb3b9d5504f6be1558cd3d867bf31a2a3c02b (atomic ledger/results publication)
**Ledger generation:** 1200 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.7327 | 112.503 | 94.153 | +5.94% | +0.67% | 3.71x | 4.9 | 2026-11-21T23:21:01.465101+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XMR/USD | 491.64 | 98.517 | 96.341 | +7.75% | +0.62% | 0.91x | 7.3 | 2026-11-21T23:21:01.465101+00:00 | Not calibrated | STRONG 79/100 | HIGH 62/100 | Watch | WATCH |
| 3 | QNT/USD | 143.13 | 89.733 | 74.250 | +3.15% | +0.25% | 2.42x | 5.6 | 2026-11-21T23:21:01.465101+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | ETH/USD | 1681.31 | 89.479 | 81.767 | +3.83% | +0.35% | 1.60x | 0.1 | 2026-11-21T23:21:01.465101+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | PEARL/USD | 1.9629 | 83.654 | 79.497 | +7.36% | +0.48% | 1.18x | 16.8 | 2026-11-21T23:21:01.465101+00:00 | Not calibrated | STRONG 72/100 | HIGH 68/100 | Watch | WATCH |
| 6 | XRP/USD | 0.93079 | 81.530 | 71.955 | +2.43% | +0.41% | 1.75x | 0.1 | 2026-11-21T23:21:01.465101+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | ZEC/USD | 782.83 | 81.101 | 77.632 | +3.29% | +0.10% | 1.30x | 0.8 | 2026-11-21T23:21:01.465101+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |
| 8 | NIGHT/USD | 0.04454 | 80.751 | 82.598 | +5.50% | +0.07% | 0.78x | 6.7 | 2026-11-21T23:21:01.465101+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 9 | XLM/USD | 0.128775 | 79.050 | 62.186 | +1.24% | +0.37% | 2.55x | 3.0 | 2026-11-21T23:21:01.465101+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 10 | XBT/USD | 60182.1 | 78.501 | 71.367 | +2.34% | +0.32% | 1.55x | 0.0 | 2026-11-21T23:21:01.465101+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Consider small entry | WATCH |
| 11 | SOL/USD | 70.22 | 77.216 | 69.671 | +2.20% | +0.20% | 1.65x | 1.4 | 2026-11-21T23:21:01.465101+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0550676 | 71.552 | 65.150 | +1.46% | +0.23% | 1.52x | 0.1 | 2026-11-21T23:21:01.465101+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Consider small entry | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 96.341 | 491.64 | +0.62% | 0.91x |
| 2 | UNI/USD | 94.153 | 4.7327 | +0.67% | 3.71x |
| 3 | NIGHT/USD | 82.598 | 0.04454 | +0.07% | 0.78x |
| 4 | ETH/USD | 81.767 | 1681.31 | +0.35% | 1.60x |
| 5 | PEARL/USD | 79.497 | 1.9629 | +0.48% | 1.18x |
| 6 | ZEC/USD | 77.632 | 782.83 | +0.10% | 1.30x |
| 7 | QNT/USD | 74.250 | 143.13 | +0.25% | 2.42x |
| 8 | XRP/USD | 71.955 | 0.93079 | +0.41% | 1.75x |
| 9 | XBT/USD | 71.367 | 60182.1 | +0.32% | 1.55x |
| 10 | SOL/USD | 69.671 | 70.22 | +0.20% | 1.65x |
| 11 | XDG/USD | 65.150 | 0.0550676 | +0.23% | 1.52x |
| 12 | XLM/USD | 62.186 | 0.128775 | +0.37% | 2.55x |

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

- Persisted scans: 1200; predictions: 9709; observations: 725959.
- Matured sampled outcomes across 1/6/24/48h: 13049; gap abstentions: 21619. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44961229105 · **Generation:** 1200 · **Legacy run:** 44961229105
**Main quote time:** 2026-11-21T23:21:09.491212+00:00 · **Legacy report time:** 2026-11-21T23:22:00.895603+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.7327 | 112.50 | +0.67% | 3.71x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD | 491.64 | 98.52 | +0.62% | 0.91x | STRONG 79/100 | HIGH 62/100 | Watch |
| 3 | QNT/USD ⭐ | 143.13 | 89.73 | +0.25% | 2.42x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | ETH/USD ⭐ | 1681.31 | 89.48 | +0.35% | 1.60x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | PEARL/USD ⭐ | 1.9629 | 83.65 | +0.48% | 1.18x | STRONG 82/100 | HIGH 68/100 | Watch |
| 6 | XRP/USD ⭐ | 0.93079 | 81.53 | +0.41% | 1.75x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 7 | ZEC/USD ⭐ | 782.83 | 81.10 | +0.10% | 1.30x | STRONG 76/100 | HIGH 55/100 | Watch |
| 8 | NIGHT/USD | 0.04454 | 80.75 | +0.07% | 0.78x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 9 | XLM/USD | 0.128775 | 79.05 | +0.37% | 2.55x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 10 | XBT/USD ⭐ | 60182.1 | 78.50 | +0.32% | 1.55x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 11 | SOL/USD ⭐ | 70.22 | 77.22 | +0.20% | 1.65x | STRONG 84/100 | HIGH 55/100 | Watch |
| 12 | XDG/USD | 0.0550676 | 71.55 | +0.23% | 1.52x | STRONG 81/100 | HIGH 55/100 | Consider small entry |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD ⭐ | 1681.5 | 100.00 | +0.35% | 1.60x | 65635 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UNI/USD ⭐ | 4.7393 | 100.00 | +0.67% | 3.71x | 10583 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | QNT/USD ⭐ | 143.28 | 86.36 | +0.25% | 2.42x | 10998 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | ZEC/USD ⭐ | 781.26 | 85.09 | +0.10% | 1.30x | 39635 | STRONG 78/100 | HIGH 55/100 | Watch |
| 5 | XRP/USD ⭐ | 0.93125 | 84.93 | +0.41% | 1.75x | 45562 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 6 | XBT/USD ⭐ | 60193.3 | 83.44 | +0.32% | 1.55x | 194561 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 7 | PEARL/USD ⭐ | 1.9609 | 79.89 | +0.48% | 1.18x | 9972 | STRONG 80/100 | HIGH 68/100 | Watch |
| 8 | SOL/USD ⭐ | 70.24 | 79.09 | +0.20% | 1.65x | 46677 | STRONG 85/100 | HIGH 55/100 | Watch |

**Same-run overlap:** UNI/USD, QNT/USD, ETH/USD, PEARL/USD, XRP/USD, ZEC/USD, XBT/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
