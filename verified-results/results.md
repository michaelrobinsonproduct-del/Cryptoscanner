# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T18:12:19.174629+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46047320528
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 9c72db382a0b4f76bb7bdcfa94c676b8036a58f3 (atomic ledger/results publication)
**Ledger generation:** 2042 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 750.26 | 100.706 | 97.334 | +10.06% | +1.07% | 0.80x | 5.3 | 2026-11-27T18:12:11.351693+00:00 | Not calibrated | STRONG 80/100 | HIGH 62/100 | Watch | WATCH |
| 2 | UNI/USD | 4.7887 | 86.542 | 71.231 | +2.98% | +0.52% | 2.27x | 4.2 | 2026-11-27T18:12:11.351693+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | XDG/USD | 0.057616 | 86.430 | 69.956 | +2.20% | +0.29% | 2.52x | 0.9 | 2026-11-27T18:12:11.351693+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | NIGHT/USD | 0.0496 | 85.412 | 70.311 | +2.33% | +0.02% | 3.26x | 2.0 | 2026-11-27T18:12:11.351693+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 5 | SPACE/USD | 0.004242 | 83.106 | 71.077 | +9.56% | +1.63% | 1.39x | 9.4 | 2026-11-27T18:12:11.351693+00:00 | Not calibrated | STRONG 87/100 | HIGH 67/100 | Watch | WATCH |
| 6 | HYPE/USD | 63.74 | 77.494 | 71.316 | +2.44% | +0.71% | 1.26x | 1.6 | 2026-11-27T18:12:11.351693+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 7 | LIGHTER/USD | 2.589 | 75.725 | 61.305 | +4.31% | -0.12% | 4.80x | 3.9 | 2026-11-27T18:12:11.351693+00:00 | Not calibrated | MODERATE 68/100 | HIGH 66/100 | Watch | WATCH |
| 8 | PAXG/USD | 3638.96 | 75.636 | 58.074 | +2.31% | +0.51% | 3.50x | 1.8 | 2026-11-27T18:12:11.351693+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | LINK/USD | 9.35454 | 72.887 | 60.493 | +0.93% | +0.12% | 2.18x | 2.0 | 2026-11-27T18:12:11.351693+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 10 | XRP/USD | 0.94755 | 71.505 | 58.406 | +0.51% | +0.33% | 2.15x | 0.3 | 2026-11-27T18:12:11.351693+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 11 | XAUT/USD | 3643.4 | 71.195 | 53.880 | +2.35% | +0.46% | 4.30x | 0.3 | 2026-11-27T18:12:11.351693+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 12 | SENT/USD | 0.022872 | 67.169 | 68.642 | +5.99% | +0.56% | 0.57x | 7.9 | 2026-11-27T18:12:11.351693+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.334 | 750.26 | +1.07% | 0.80x |
| 2 | HYPE/USD | 71.316 | 63.74 | +0.71% | 1.26x |
| 3 | UNI/USD | 71.231 | 4.7887 | +0.52% | 2.27x |
| 4 | SPACE/USD | 71.077 | 0.004242 | +1.63% | 1.39x |
| 5 | NIGHT/USD | 70.311 | 0.0496 | +0.02% | 3.26x |
| 6 | XDG/USD | 69.956 | 0.057616 | +0.29% | 2.52x |
| 7 | SENT/USD | 68.642 | 0.022872 | +0.56% | 0.57x |
| 8 | LIGHTER/USD | 61.305 | 2.589 | -0.12% | 4.80x |
| 9 | LINK/USD | 60.493 | 9.35454 | +0.12% | 2.18x |
| 10 | XRP/USD | 58.406 | 0.94755 | +0.33% | 2.15x |
| 11 | PAXG/USD | 58.074 | 3638.96 | +0.51% | 3.50x |
| 12 | XAUT/USD | 53.880 | 3643.4 | +0.46% | 4.30x |

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

- Persisted scans: 2042; predictions: 18206; observations: 1236519.
- Matured sampled outcomes across 1/6/24/48h: 40884; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
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

**Writer:** 46047320528 · **Generation:** 2042 · **Legacy run:** 46047320528
**Main quote time:** 2026-11-27T18:12:19.174629+00:00 · **Legacy report time:** 2026-11-27T18:13:02.182093+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 750.26 | 100.71 | +1.07% | 0.80x | STRONG 80/100 | HIGH 62/100 | Watch |
| 2 | UNI/USD ⭐ | 4.7887 | 86.54 | +0.52% | 2.27x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XDG/USD ⭐ | 0.057616 | 86.43 | +0.29% | 2.52x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | NIGHT/USD | 0.0496 | 85.41 | +0.02% | 3.26x | STRONG 88/100 | HIGH 55/100 | Watch |
| 5 | SPACE/USD ⭐ | 0.004242 | 83.11 | +1.63% | 1.39x | STRONG 97/100 | HIGH 67/100 | Watch |
| 6 | HYPE/USD ⭐ | 63.74 | 77.49 | +0.71% | 1.26x | STRONG 84/100 | HIGH 55/100 | Watch |
| 7 | LIGHTER/USD | 2.589 | 75.72 | -0.12% | 4.80x | MODERATE 68/100 | HIGH 66/100 | Watch |
| 8 | PAXG/USD ⭐ | 3638.96 | 75.64 | +0.51% | 3.50x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | LINK/USD | 9.35454 | 72.89 | +0.12% | 2.18x | STRONG 81/100 | HIGH 55/100 | Watch |
| 10 | XRP/USD | 0.94755 | 71.50 | +0.33% | 2.15x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 11 | XAUT/USD ⭐ | 3643.4 | 71.20 | +0.46% | 4.30x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 12 | SENT/USD | 0.022872 | 67.17 | +0.56% | 0.57x | MODERATE 64/100 | VERY_HIGH 82/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.7913 | 90.22 | +0.52% | 2.27x | 10178 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XDG/USD ⭐ | 0.0576133 | 85.29 | +0.29% | 2.52x | 12994 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | HYPE/USD ⭐ | 63.65 | 79.62 | +0.71% | 1.26x | 21219 | STRONG 85/100 | HIGH 55/100 | Watch |
| 4 | PAXG/USD ⭐ | 3636.97 | 79.19 | +0.51% | 3.50x | 4479 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | JUP/USD | 0.24604 | 78.03 | +0.79% | 2.58x | 2318 | STRONG 89/100 | HIGH 66/100 | Consider small entry |
| 6 | XAUT/USD ⭐ | 3642.7 | 75.79 | +0.46% | 4.30x | 2332 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | SPACE/USD ⭐ | 0.004235 | 75.70 | +1.63% | 1.39x | 2494 | STRONG 93/100 | HIGH 67/100 | Watch |
| 8 | W/USD | 0.00919 | 73.34 | +0.55% | 1.24x | 2464 | MODERATE 62/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** UNI/USD, XDG/USD, SPACE/USD, HYPE/USD, PAXG/USD, XAUT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
