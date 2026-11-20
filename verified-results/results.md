# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T06:45:39.833441+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44689947485
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 597f3aba93fdd95f498b7147b0eb27fa3fce6672 (atomic ledger/results publication)
**Ledger generation:** 943 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 605; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PROS/USD | 0.5825 | 63.167 | 61.173 | +8.13% | +0.92% | 0.74x | 29.4 | 2026-11-20T06:45:35.113652+00:00 | Not calibrated | MODERATE 52/100 | EXTREME 94/100 | Do nothing | WATCH |
| 2 | XRP/USD | 0.966 | 57.042 | 59.356 | +0.70% | +0.06% | 0.74x | 1.1 | 2026-11-20T06:45:35.113652+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | XLM/USD | 0.133747 | 55.350 | 59.328 | +0.79% | +0.25% | 0.48x | 2.4 | 2026-11-20T06:45:35.113652+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | AUD/USD | 0.66732 | 53.721 | 40.885 | +0.28% | +0.02% | 2.27x | 0.1 | 2026-11-20T06:45:35.113652+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 5 | SYRUP/USD | 0.09972 | 50.801 | 50.498 | +3.63% | +0.19% | 0.93x | 14.0 | 2026-11-20T06:45:35.113652+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | ICNT/USD | 0.4402 | 50.067 | 45.265 | +3.31% | +0.53% | 1.22x | 31.8 | 2026-11-20T06:45:35.113652+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 7 | SKR/USD | 0.010235 | 36.275 | 39.950 | +1.88% | +0.06% | 0.60x | 8.8 | 2026-11-20T06:45:35.113652+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PROS/USD | 61.173 | 0.5825 | +0.92% | 0.74x |
| 2 | XRP/USD | 59.356 | 0.966 | +0.06% | 0.74x |
| 3 | XLM/USD | 59.328 | 0.133747 | +0.25% | 0.48x |
| 4 | SYRUP/USD | 50.498 | 0.09972 | +0.19% | 0.93x |
| 5 | ICNT/USD | 45.265 | 0.4402 | +0.53% | 1.22x |
| 6 | AUD/USD | 40.885 | 0.66732 | +0.02% | 2.27x |
| 7 | SKR/USD | 39.950 | 0.010235 | +0.06% | 0.60x |

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

- Persisted scans: 943; predictions: 8003; observations: 569786.
- Matured sampled outcomes across 1/6/24/48h: 9396; gap abstentions: 17271. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44689947485 · **Generation:** 943 · **Legacy run:** 44689947485
**Main quote time:** 2026-11-20T06:45:39.833441+00:00 · **Legacy report time:** 2026-11-20T06:46:46.071853+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PROS/USD | 0.5825 | 63.17 | +0.92% | 0.74x | MODERATE 52/100 | EXTREME 94/100 | Do nothing |
| 2 | XRP/USD | 0.966 | 57.04 | +0.06% | 0.74x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 3 | XLM/USD | 0.133747 | 55.35 | +0.25% | 0.48x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 4 | AUD/USD | 0.66732 | 53.72 | +0.02% | 2.27x | STRONG 72/100 | HIGH 55/100 | Watch |
| 5 | SYRUP/USD | 0.09972 | 50.80 | +0.19% | 0.93x | WEAK 40/100 | VERY_HIGH 73/100 | Watch |
| 6 | ICNT/USD ⭐ | 0.4402 | 50.07 | +0.53% | 1.22x | MODERATE 60/100 | VERY_HIGH 74/100 | Watch |
| 7 | SKR/USD | 0.010235 | 36.27 | +0.06% | 0.60x | WEAK 38/100 | VERY_HIGH 82/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.4419 | 73.77 | +0.53% | 1.22x | 7636 | STRONG 72/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** ICNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
