# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T17:52:28.387464+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46044822508
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4cfd82cda9228b81d4e01a667c3dacc5e977a933 (atomic ledger/results publication)
**Ledger generation:** 2040 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 736.16 | 98.381 | 95.108 | +8.00% | +0.56% | 1.05x | 9.8 | 2026-11-27T17:52:21.283226+00:00 | Not calibrated | STRONG 84/100 | HIGH 62/100 | Watch | WATCH |
| 2 | HYPE/USD | 63.17 | 74.097 | 64.896 | +1.53% | -1.16% | 2.63x | 1.6 | 2026-11-27T17:52:21.283226+00:00 | Not calibrated | MODERATE 67/100 | HIGH 65/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04952 | 72.391 | 68.743 | +2.17% | -0.20% | 1.47x | 2.0 | 2026-11-27T17:52:21.283226+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XDG/USD | 0.0572398 | 68.012 | 65.465 | +1.53% | -0.65% | 1.58x | 0.6 | 2026-11-27T17:52:21.283226+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 5 | PAXG/USD | 3621.8 | 64.095 | 54.871 | +1.83% | -0.18% | 2.01x | 1.3 | 2026-11-27T17:52:21.283226+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 6 | FET/USD | 0.1257 | 62.267 | 56.135 | +4.40% | -0.08% | 1.65x | 23.9 | 2026-11-27T17:52:21.283226+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | SPACE/USD | 0.004175 | 61.992 | 69.797 | +7.83% | -0.17% | 0.30x | 12.0 | 2026-11-27T17:52:21.283226+00:00 | Not calibrated | WEAK 31/100 | EXTREME 94/100 | Do nothing | WATCH |
| 8 | SENT/USD | 0.02274 | 61.416 | 67.858 | +5.38% | +0.24% | 0.23x | 0.9 | 2026-11-27T17:52:21.283226+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 9 | VVV/USD | 26.532 | 61.086 | 55.317 | +1.33% | +0.01% | 1.57x | 6.4 | 2026-11-27T17:52:21.283226+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |
| 10 | SOL/USD | 71.51 | 57.882 | 59.925 | +0.80% | -0.52% | 1.05x | 1.4 | 2026-11-27T17:52:21.283226+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 11 | LINK/USD | 9.30397 | 57.446 | 55.739 | +0.38% | -0.22% | 1.28x | 3.9 | 2026-11-27T17:52:21.283226+00:00 | Not calibrated | WEAK 39/100 | HIGH 61/100 | Watch | WATCH |
| 12 | UNI/USD | 4.7532 | 55.458 | 65.473 | +2.22% | -0.29% | 0.14x | 4.6 | 2026-11-27T17:52:21.283226+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 95.108 | 736.16 | +0.56% | 1.05x |
| 2 | SPACE/USD | 69.797 | 0.004175 | -0.17% | 0.30x |
| 3 | NIGHT/USD | 68.743 | 0.04952 | -0.20% | 1.47x |
| 4 | SENT/USD | 67.858 | 0.02274 | +0.24% | 0.23x |
| 5 | UNI/USD | 65.473 | 4.7532 | -0.29% | 0.14x |
| 6 | XDG/USD | 65.465 | 0.0572398 | -0.65% | 1.58x |
| 7 | HYPE/USD | 64.896 | 63.17 | -1.16% | 2.63x |
| 8 | SOL/USD | 59.925 | 71.51 | -0.52% | 1.05x |
| 9 | FET/USD | 56.135 | 0.1257 | -0.08% | 1.65x |
| 10 | LINK/USD | 55.739 | 9.30397 | -0.22% | 1.28x |
| 11 | VVV/USD | 55.317 | 26.532 | +0.01% | 1.57x |
| 12 | PAXG/USD | 54.871 | 3621.8 | -0.18% | 2.01x |

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

- Persisted scans: 2040; predictions: 18182; observations: 1235309.
- Matured sampled outcomes across 1/6/24/48h: 40791; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46044822508 · **Generation:** 2040 · **Legacy run:** 46044822508
**Main quote time:** 2026-11-27T17:52:28.387464+00:00 · **Legacy report time:** 2026-11-27T17:53:19.583540+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 736.16 | 98.38 | +0.56% | 1.05x | STRONG 94/100 | HIGH 62/100 | Watch |
| 2 | HYPE/USD | 63.17 | 74.10 | -1.16% | 2.63x | MODERATE 67/100 | HIGH 65/100 | Watch |
| 3 | NIGHT/USD | 0.04952 | 72.39 | -0.20% | 1.47x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 4 | XDG/USD | 0.0572398 | 68.01 | -0.65% | 1.58x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 5 | PAXG/USD | 3621.8 | 64.10 | -0.18% | 2.01x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 6 | FET/USD | 0.1257 | 62.27 | -0.08% | 1.65x | WEAK 41/100 | VERY_HIGH 73/100 | Watch |
| 7 | SPACE/USD | 0.004175 | 61.99 | -0.17% | 0.30x | WEAK 31/100 | EXTREME 94/100 | Do nothing |
| 8 | SENT/USD | 0.02274 | 61.42 | +0.24% | 0.23x | MODERATE 61/100 | VERY_HIGH 82/100 | Watch |
| 9 | VVV/USD | 26.532 | 61.09 | +0.01% | 1.57x | MODERATE 66/100 | HIGH 55/100 | Watch |
| 10 | SOL/USD | 71.51 | 57.88 | -0.52% | 1.05x | WEAK 39/100 | HIGH 68/100 | Watch |
| 11 | LINK/USD | 9.30397 | 57.45 | -0.22% | 1.28x | WEAK 39/100 | HIGH 61/100 | Watch |
| 12 | UNI/USD | 4.7532 | 55.46 | -0.29% | 0.14x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 736.14 | 86.87 | +0.56% | 1.05x | 39284 | STRONG 88/100 | HIGH 62/100 | Watch |

**Same-run overlap:** ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
