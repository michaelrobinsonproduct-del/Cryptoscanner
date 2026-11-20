# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T05:55:26.508165+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44684132775
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 808f445b16bb5dd69572de81ec5c6973ecbf9ed8 (atomic ledger/results publication)
**Ledger generation:** 936 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 605; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XLM/USD | 0.133922 | 73.051 | 61.409 | +0.92% | +0.92% | 1.71x | 0.1 | 2026-11-20T05:55:21.481528+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XRP/USD | 0.97025 | 67.075 | 62.873 | +1.15% | +0.56% | 1.14x | 0.3 | 2026-11-20T05:55:21.481528+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 3 | HBAR/USD | 0.054 | 55.349 | 41.473 | +0.45% | +1.07% | 1.85x | 1.9 | 2026-11-20T05:55:21.481528+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SKR/USD | 0.010231 | 53.630 | 38.711 | +1.84% | +1.34% | 1.82x | 10.8 | 2026-11-20T05:55:21.481528+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 73/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 62.873 | 0.97025 | +0.56% | 1.14x |
| 2 | XLM/USD | 61.409 | 0.133922 | +0.92% | 1.71x |
| 3 | HBAR/USD | 41.473 | 0.054 | +1.07% | 1.85x |
| 4 | SKR/USD | 38.711 | 0.010231 | +1.34% | 1.82x |

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

- Persisted scans: 936; predictions: 7960; observations: 565551.
- Matured sampled outcomes across 1/6/24/48h: 9301; gap abstentions: 17094. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44684132775 · **Generation:** 936 · **Legacy run:** 44684132775
**Main quote time:** 2026-11-20T05:55:26.508165+00:00 · **Legacy report time:** 2026-11-20T05:56:11.366488+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD ⭐ | 0.133922 | 73.05 | +0.92% | 1.71x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.97025 | 67.07 | +0.56% | 1.14x | STRONG 79/100 | HIGH 62/100 | Watch |
| 3 | HBAR/USD ⭐ | 0.054 | 55.35 | +1.07% | 1.85x | STRONG 83/100 | HIGH 55/100 | Consider small entry |
| 4 | SKR/USD ⭐ | 0.010231 | 53.63 | +1.34% | 1.82x | STRONG 77/100 | VERY_HIGH 73/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.96866 | 64.15 | +0.56% | 1.14x | 32822 | STRONG 77/100 | HIGH 62/100 | Watch |
| 2 | XLM/USD ⭐ | 0.133798 | 61.67 | +0.92% | 1.71x | 9929 | STRONG 86/100 | HIGH 55/100 | Consider small entry |
| 3 | AUD/USD | 0.66695 | 50.75 | +0.11% | 4.60x | 3994 | STRONG 70/100 | HIGH 55/100 | Watch |
| 4 | HBAR/USD ⭐ | 0.05398 | 50.38 | +1.07% | 1.85x | 8590 | STRONG 80/100 | HIGH 55/100 | Consider small entry |
| 5 | SKR/USD ⭐ | 0.010226 | 42.74 | +1.34% | 1.82x | 1586 | STRONG 71/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** XLM/USD, XRP/USD, HBAR/USD, SKR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
