# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T01:42:35.047966+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46094206111
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 6e9687214cbaacc8187a01f8331832b3a1ddca04 (atomic ledger/results publication)
**Ledger generation:** 2088 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 757.16 | 83.234 | 74.875 | +3.08% | +0.71% | 1.48x | 3.3 | 2026-11-28T01:42:28.380894+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 2 | HYPE/USD | 64.3 | 76.676 | 62.375 | +1.28% | -0.14% | 5.02x | 3.1 | 2026-11-28T01:42:28.380894+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 3 | PEPE/USD | 3.572e-06 | 66.654 | 50.111 | +0.85% | +0.31% | 6.69x | 2.8 | 2026-11-28T01:42:28.380894+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 4 | UNI/USD | 4.8843 | 64.563 | 57.208 | +1.08% | +0.18% | 1.65x | 3.7 | 2026-11-28T01:42:28.380894+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.0454 | 63.354 | 59.008 | +0.90% | +0.07% | 1.40x | 4.6 | 2026-11-28T01:42:28.380894+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 6 | PUMP/USD | 0.002629 | 62.098 | 45.764 | +1.15% | +0.27% | 9.57x | 3.8 | 2026-11-28T01:42:28.380894+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6753 | 61.770 | 56.328 | +0.40% | +0.03% | 1.53x | 3.0 | 2026-11-28T01:42:28.380894+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |
| 8 | XRP/USD | 0.95219 | 57.502 | 57.742 | +0.44% | -0.14% | 1.05x | 0.6 | 2026-11-28T01:42:28.380894+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 9 | SENT/USD | 0.024216 | 57.041 | 45.392 | +2.12% | -0.54% | 2.44x | 0.4 | 2026-11-28T01:42:28.380894+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 10 | XBT/USD | 60138.1 | 56.365 | 58.199 | +0.46% | +0.11% | 0.76x | 0.0 | 2026-11-28T01:42:28.380894+00:00 | Not calibrated | MODERATE 48/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0579225 | 56.121 | 57.976 | +0.43% | -0.01% | 0.82x | 0.1 | 2026-11-28T01:42:28.380894+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | SOL/USD | 72.01 | 55.445 | 58.314 | +0.57% | -0.07% | 0.75x | 1.4 | 2026-11-28T01:42:28.380894+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 74.875 | 757.16 | +0.71% | 1.48x |
| 2 | HYPE/USD | 62.375 | 64.3 | -0.14% | 5.02x |
| 3 | NEAR/USD | 59.008 | 3.0454 | +0.07% | 1.40x |
| 4 | SOL/USD | 58.314 | 72.01 | -0.07% | 0.75x |
| 5 | XBT/USD | 58.199 | 60138.1 | +0.11% | 0.76x |
| 6 | XDG/USD | 57.976 | 0.0579225 | -0.01% | 0.82x |
| 7 | XRP/USD | 57.742 | 0.95219 | -0.14% | 1.05x |
| 8 | UNI/USD | 57.208 | 4.8843 | +0.18% | 1.65x |
| 9 | SUI/USD | 56.328 | 0.6753 | +0.03% | 1.53x |
| 10 | PEPE/USD | 50.111 | 3.572e-06 | +0.31% | 6.69x |
| 11 | PUMP/USD | 45.764 | 0.002629 | +0.27% | 9.57x |
| 12 | SENT/USD | 45.392 | 0.024216 | -0.54% | 2.44x |

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

- Persisted scans: 2088; predictions: 18719; observations: 1264374.
- Matured sampled outcomes across 1/6/24/48h: 43061; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46094206111 · **Generation:** 2088 · **Legacy run:** 46094206111
**Main quote time:** 2026-11-28T01:42:35.047966+00:00 · **Legacy report time:** 2026-11-28T01:43:14.904370+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 757.16 | 83.23 | +0.71% | 1.48x | STRONG 97/100 | HIGH 55/100 | Watch |
| 2 | HYPE/USD | 64.3 | 76.68 | -0.14% | 5.02x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 3 | PEPE/USD ⭐ | 3.572e-06 | 66.65 | +0.31% | 6.69x | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 4 | UNI/USD ⭐ | 4.8843 | 64.56 | +0.18% | 1.65x | STRONG 77/100 | HIGH 55/100 | Watch |
| 5 | NEAR/USD ⭐ | 3.0454 | 63.35 | +0.07% | 1.40x | STRONG 77/100 | HIGH 55/100 | Watch |
| 6 | PUMP/USD | 0.002629 | 62.10 | +0.27% | 9.57x | STRONG 86/100 | HIGH 55/100 | Watch |
| 7 | SUI/USD | 0.6753 | 61.77 | +0.03% | 1.53x | MODERATE 66/100 | HIGH 55/100 | Watch |
| 8 | XRP/USD | 0.95219 | 57.50 | -0.14% | 1.05x | WEAK 39/100 | HIGH 68/100 | Watch |
| 9 | SENT/USD | 0.024216 | 57.04 | -0.54% | 2.44x | MODERATE 59/100 | VERY_HIGH 73/100 | Watch |
| 10 | XBT/USD | 60138.1 | 56.36 | +0.11% | 0.76x | MODERATE 48/100 | HIGH 62/100 | Watch |
| 11 | XDG/USD | 0.0579225 | 56.12 | -0.01% | 0.82x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 12 | SOL/USD | 72.01 | 55.44 | -0.07% | 0.75x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 756.2 | 86.36 | +0.71% | 1.48x | 33603 | STRONG 98/100 | HIGH 55/100 | Watch |
| 2 | NEAR/USD ⭐ | 3.0465 | 59.15 | +0.07% | 1.40x | 14260 | STRONG 75/100 | HIGH 55/100 | Watch |
| 3 | UNI/USD ⭐ | 4.8843 | 57.40 | +0.18% | 1.65x | 10159 | STRONG 74/100 | HIGH 55/100 | Watch |
| 4 | PEPE/USD ⭐ | 3.571e-06 | 53.90 | +0.31% | 6.69x | 6392 | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 5 | ADA/USD | 0.148645 | 53.39 | +0.14% | 1.62x | 11386 | MODERATE 62/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD, PEPE/USD, UNI/USD, NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
