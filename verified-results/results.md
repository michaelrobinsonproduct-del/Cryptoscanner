# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T02:05:03.711937+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44220563006
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** eb03809c516d33fcd25edff7965f82ea766737b9 (atomic ledger/results publication)
**Ledger generation:** 502 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 8.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TON/USD | 1.09 | 63.443 | 42.877 | +1.21% | +1.11% | 13.07x | 9.2 | 2026-11-18T02:05:00.940767+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 2 | AKT/USD | 0.5171 | 55.068 | 38.224 | +1.53% | +0.37% | 2.60x | 9.7 | 2026-11-18T02:05:00.940767+00:00 | Not calibrated | STRONG 83/100 | HIGH 60/100 | Watch | WATCH |
| 3 | PEARL/USD | 1.8247 | 46.052 | 23.091 | +0.78% | +1.59% | 4.76x | 35.6 | 2026-11-18T02:05:00.940767+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | UP/USD | 0.05492 | 34.587 | 35.885 | +3.64% | +0.73% | 0.50x | 42.0 | 2026-11-18T02:05:00.940767+00:00 | Not calibrated | WEAK 32/100 | EXTREME 100/100 | Do nothing | WATCH |
| 5 | CAP/USD | 0.102009 | 26.545 | 36.577 | +1.02% | -0.08% | 0.04x | 6.1 | 2026-11-18T02:05:00.940767+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TON/USD | 42.877 | 1.09 | +1.11% | 13.07x |
| 2 | AKT/USD | 38.224 | 0.5171 | +0.37% | 2.60x |
| 3 | CAP/USD | 36.577 | 0.102009 | -0.08% | 0.04x |
| 4 | UP/USD | 35.885 | 0.05492 | +0.73% | 0.50x |
| 5 | PEARL/USD | 23.091 | 1.8247 | +1.59% | 4.76x |

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

- Persisted scans: 502; predictions: 4287; observations: 302725.
- Matured sampled outcomes across 1/6/24/48h: 3450; gap abstentions: 12410. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44220563006 · **Generation:** 502 · **Legacy run:** 44220563006
**Main quote time:** 2026-11-18T02:05:03.711937+00:00 · **Legacy report time:** 2026-11-18T02:05:18.612051+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD ⭐ | 1.09 | 63.44 | +1.11% | 13.07x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 2 | AKT/USD ⭐ | 0.5171 | 55.07 | +0.37% | 2.60x | STRONG 93/100 | HIGH 60/100 | Consider small entry |
| 3 | PEARL/USD ⭐ | 1.8247 | 46.05 | +1.59% | 4.76x | STRONG 73/100 | VERY_HIGH 72/100 | Watch |
| 4 | UP/USD | 0.05492 | 34.59 | +0.73% | 0.50x | WEAK 32/100 | EXTREME 100/100 | Do nothing |
| 5 | CAP/USD | 0.102009 | 26.55 | -0.08% | 0.04x | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD ⭐ | 1.09 | 53.23 | +1.11% | 13.07x | 5401 | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 2 | PEARL/USD ⭐ | 1.8323 | 52.48 | +1.59% | 4.76x | 4344 | STRONG 91/100 | HIGH 60/100 | Consider small entry |
| 3 | AKT/USD ⭐ | 0.5179 | 51.19 | +0.37% | 2.60x | 3592 | STRONG 86/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** TON/USD, AKT/USD, PEARL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
