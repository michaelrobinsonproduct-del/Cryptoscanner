# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T11:52:54.280954+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46141686505
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2b79aa8dd2d2955728976be7bfe3a1cd7d4c3b06 (atomic ledger/results publication)
**Ledger generation:** 2150 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05459 | 117.010 | 98.317 | +8.66% | +0.74% | 4.75x | 1.8 | 2026-11-28T11:52:49.751231+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XMR/USD | 428.98 | 83.557 | 82.759 | +5.33% | +1.07% | 0.54x | 19.1 | 2026-11-28T11:52:49.751231+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | SENT/USD | 0.024841 | 81.049 | 60.470 | +4.75% | +1.12% | 2.89x | 8.5 | 2026-11-28T11:52:49.751231+00:00 | Not calibrated | STRONG 96/100 | HIGH 67/100 | Consider small entry | WATCH |
| 4 | SPACE/USD | 0.004465 | 73.041 | 72.085 | +6.87% | -1.04% | 1.62x | 9.0 | 2026-11-28T11:52:49.751231+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 5 | VVV/USD | 27.001 | 72.235 | 73.149 | +4.86% | +0.93% | 0.44x | 8.9 | 2026-11-28T11:52:49.751231+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | CC/USD | 0.07441 | 34.574 | 33.657 | +0.35% | +0.16% | 1.01x | 5.4 | 2026-11-28T11:52:49.751231+00:00 | Not calibrated | WEAK 42/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 98.317 | 0.05459 | +0.74% | 4.75x |
| 2 | XMR/USD | 82.759 | 428.98 | +1.07% | 0.54x |
| 3 | VVV/USD | 73.149 | 27.001 | +0.93% | 0.44x |
| 4 | SPACE/USD | 72.085 | 0.004465 | -1.04% | 1.62x |
| 5 | SENT/USD | 60.470 | 0.024841 | +1.12% | 2.89x |
| 6 | CC/USD | 33.657 | 0.07441 | +0.16% | 1.01x |

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

- Persisted scans: 2150; predictions: 19174; observations: 1301946.
- Matured sampled outcomes across 1/6/24/48h: 45711; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46141686505 · **Generation:** 2150 · **Legacy run:** 46141686505
**Main quote time:** 2026-11-28T11:52:54.280954+00:00 · **Legacy report time:** 2026-11-28T11:53:52.907739+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.05459 | 117.01 | +0.74% | 4.75x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD | 428.98 | 83.56 | +1.07% | 0.54x | MODERATE 67/100 | VERY_HIGH 76/100 | Watch |
| 3 | SENT/USD ⭐ | 0.024841 | 81.05 | +1.12% | 2.89x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 4 | SPACE/USD | 0.004465 | 73.04 | -1.04% | 1.62x | MODERATE 57/100 | VERY_HIGH 77/100 | Watch |
| 5 | VVV/USD | 27.001 | 72.24 | +0.93% | 0.44x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 6 | CC/USD ⭐ | 0.07441 | 34.57 | +0.16% | 1.01x | MODERATE 52/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.05461 | 100.00 | +0.74% | 4.75x | 19001 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SENT/USD ⭐ | 0.024832 | 86.31 | +1.12% | 2.89x | 5837 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 3 | CC/USD ⭐ | 0.07441 | 38.69 | +0.16% | 1.01x | 4689 | MODERATE 54/100 | HIGH 67/100 | Watch |

**Same-run overlap:** NIGHT/USD, SENT/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
