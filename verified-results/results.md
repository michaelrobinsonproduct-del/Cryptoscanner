# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T23:00:35.275713+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44633660746
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** f2f1aef215a07f61d4de56b0bfd34cf2eaad5499 (atomic ledger/results publication)
**Ledger generation:** 875 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 602; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MEGA/USD | 0.06002 | 81.424 | 71.290 | +7.18% | +0.45% | 1.79x | 11.7 | 2026-11-19T23:00:26.959931+00:00 | Not calibrated | STRONG 81/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 21.932 | 71.857 | 60.007 | +1.20% | -0.10% | 2.23x | 6.8 | 2026-11-19T23:00:26.959931+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 3 | USELESS/USD | 0.09932 | 52.514 | 60.219 | +3.93% | -0.51% | 0.48x | 15.2 | 2026-11-19T23:00:26.959931+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 4 | INJ/USD | 7.081 | 49.719 | 52.023 | +1.43% | -0.06% | 0.80x | 7.1 | 2026-11-19T23:00:26.959931+00:00 | Not calibrated | WEAK 30/100 | HIGH 68/100 | Do nothing | WATCH |
| 5 | HYPE/USD | 67.09 | 48.209 | 55.706 | +0.31% | +0.06% | 0.22x | 3.0 | 2026-11-19T23:00:26.959931+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | SENT/USD | 0.021468 | 45.678 | 59.532 | +4.19% | -0.85% | 0.04x | 8.4 | 2026-11-19T23:00:26.959931+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 7 | AKT/USD | 0.537 | 44.010 | 53.308 | +3.67% | -0.33% | 0.24x | 9.3 | 2026-11-19T23:00:26.959931+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 8 | TRX/USD | 0.31043 | 35.291 | 44.250 | +0.37% | -0.04% | 0.12x | 1.2 | 2026-11-19T23:00:26.959931+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 71.290 | 0.06002 | +0.45% | 1.79x |
| 2 | USELESS/USD | 60.219 | 0.09932 | -0.51% | 0.48x |
| 3 | VVV/USD | 60.007 | 21.932 | -0.10% | 2.23x |
| 4 | SENT/USD | 59.532 | 0.021468 | -0.85% | 0.04x |
| 5 | HYPE/USD | 55.706 | 67.09 | +0.06% | 0.22x |
| 6 | AKT/USD | 53.308 | 0.537 | -0.33% | 0.24x |
| 7 | INJ/USD | 52.023 | 7.081 | -0.06% | 0.80x |
| 8 | TRX/USD | 44.250 | 0.31043 | -0.04% | 0.12x |

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

- Persisted scans: 875; predictions: 7614; observations: 528752.
- Matured sampled outcomes across 1/6/24/48h: 8081; gap abstentions: 15767. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 16; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44633660746 · **Generation:** 875 · **Legacy run:** 44633660746
**Main quote time:** 2026-11-19T23:00:35.275713+00:00 · **Legacy report time:** 2026-11-19T23:01:33.249762+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.06002 | 81.42 | +0.45% | 1.79x | STRONG 91/100 | HIGH 66/100 | Consider small entry |
| 2 | VVV/USD | 21.932 | 71.86 | -0.10% | 2.23x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 3 | USELESS/USD | 0.09932 | 52.51 | -0.51% | 0.48x | WEAK 26/100 | VERY_HIGH 82/100 | Do nothing |
| 4 | INJ/USD | 7.081 | 49.72 | -0.06% | 0.80x | WEAK 30/100 | HIGH 68/100 | Do nothing |
| 5 | HYPE/USD | 67.09 | 48.21 | +0.06% | 0.22x | WEAK 44/100 | VERY_HIGH 70/100 | Watch |
| 6 | SENT/USD | 0.021468 | 45.68 | -0.85% | 0.04x | WEAK 28/100 | VERY_HIGH 81/100 | Do nothing |
| 7 | AKT/USD | 0.537 | 44.01 | -0.33% | 0.24x | WEAK 27/100 | VERY_HIGH 81/100 | Do nothing |
| 8 | TRX/USD | 0.31043 | 35.29 | -0.04% | 0.12x | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.06002 | 71.50 | +0.45% | 1.79x | 2125 | STRONG 86/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** MEGA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
