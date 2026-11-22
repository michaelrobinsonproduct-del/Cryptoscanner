# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T00:50:47.345778+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44968499108
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** da6d0bf58b5da15d28a19db9488adae704a599ff (atomic ledger/results publication)
**Ledger generation:** 1210 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.102 | 71.915 | 58.287 | +0.81% | -0.27% | 3.41x | 4.8 | 2026-11-22T00:50:40.226455+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04463 | 66.689 | 47.734 | +0.79% | +0.79% | 3.69x | 11.2 | 2026-11-22T00:50:40.226455+00:00 | Not calibrated | STRONG 83/100 | HIGH 61/100 | Watch | WATCH |
| 3 | PEPE/USD | 3.413e-06 | 63.153 | 46.389 | +0.29% | +0.35% | 14.62x | 2.9 | 2026-11-22T00:50:40.226455+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 4 | BNB/USD | 549.2 | 45.478 | 45.891 | +0.33% | +0.09% | 0.92x | 1.6 | 2026-11-22T00:50:40.226455+00:00 | Not calibrated | WEAK 43/100 | HIGH 62/100 | Watch | WATCH |
| 5 | CAP/USD | 0.092536 | 44.425 | 37.175 | +0.63% | +0.33% | 1.56x | 6.2 | 2026-11-22T00:50:40.226455+00:00 | Not calibrated | MODERATE 67/100 | HIGH 60/100 | Watch | WATCH |
| 6 | BLESS/USD | 0.012489 | 36.693 | 32.797 | +1.25% | +1.23% | 0.77x | 31.4 | 2026-11-22T00:50:40.226455+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 7 | ZAMA/USD | 0.0607 | 18.927 | 29.401 | +0.43% | -0.34% | 0.12x | 9.9 | 2026-11-22T00:50:40.226455+00:00 | Not calibrated | WEAK 14/100 | EXTREME 88/100 | Do nothing | WATCH |
| 8 | TRAC/USD | 0.2786 | 16.017 | 25.177 | +0.72% | -0.92% | 0.55x | 21.5 | 2026-11-22T00:50:40.226455+00:00 | Not calibrated | WEAK 3/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 58.287 | 25.102 | -0.27% | 3.41x |
| 2 | NIGHT/USD | 47.734 | 0.04463 | +0.79% | 3.69x |
| 3 | PEPE/USD | 46.389 | 3.413e-06 | +0.35% | 14.62x |
| 4 | BNB/USD | 45.891 | 549.2 | +0.09% | 0.92x |
| 5 | CAP/USD | 37.175 | 0.092536 | +0.33% | 1.56x |
| 6 | BLESS/USD | 32.797 | 0.012489 | +1.23% | 0.77x |
| 7 | ZAMA/USD | 29.401 | 0.0607 | -0.34% | 0.12x |
| 8 | TRAC/USD | 25.177 | 0.2786 | -0.92% | 0.55x |

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

- Persisted scans: 1210; predictions: 9789; observations: 732038.
- Matured sampled outcomes across 1/6/24/48h: 13292; gap abstentions: 21745. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44968499108 · **Generation:** 1210 · **Legacy run:** 44968499108
**Main quote time:** 2026-11-22T00:50:47.345778+00:00 · **Legacy report time:** 2026-11-22T00:51:30.135875+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.102 | 71.92 | -0.27% | 3.41x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.04463 | 66.69 | +0.79% | 3.69x | STRONG 93/100 | HIGH 61/100 | Consider small entry |
| 3 | PEPE/USD | 3.413e-06 | 63.15 | +0.35% | 14.62x | STRONG 87/100 | HIGH 55/100 | Watch |
| 4 | BNB/USD | 549.2 | 45.48 | +0.09% | 0.92x | WEAK 43/100 | HIGH 62/100 | Watch |
| 5 | CAP/USD | 0.092536 | 44.42 | +0.33% | 1.56x | MODERATE 67/100 | HIGH 60/100 | Watch |
| 6 | BLESS/USD | 0.012489 | 36.69 | +1.23% | 0.77x | WEAK 38/100 | VERY_HIGH 74/100 | Watch |
| 7 | ZAMA/USD | 0.0607 | 18.93 | -0.34% | 0.12x | WEAK 14/100 | EXTREME 88/100 | Do nothing |
| 8 | TRAC/USD | 0.2786 | 16.02 | -0.92% | 0.55x | WEAK 3/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD | 0.129042 | 60.61 | +0.06% | 5.20x | 14059 | STRONG 75/100 | HIGH 55/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.04463 | 52.54 | +0.79% | 3.69x | 10840 | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 3 | XMR/USD | 492.47 | 48.72 | +0.16% | 1.68x | 11619 | MODERATE 59/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
