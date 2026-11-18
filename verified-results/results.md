# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T02:00:07.839214+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44219927236
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 49c3aad65afc429c87d01d96fc2947d096233f65 (atomic ledger/results publication)
**Ledger generation:** 501 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 2s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 7.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKT/USD | 0.518 | 56.147 | 38.479 | +1.71% | +0.58% | 2.48x | 11.6 | 2026-11-18T02:00:05.424192+00:00 | Not calibrated | STRONG 78/100 | HIGH 66/100 | Watch | WATCH |
| 2 | TON/USD | 1.081 | 53.683 | 36.826 | +0.37% | +0.37% | 9.44x | 9.3 | 2026-11-18T02:00:05.424192+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 3 | UP/USD | 0.05503 | 38.241 | 43.746 | +3.85% | -0.65% | 0.77x | 29.2 | 2026-11-18T02:00:05.424192+00:00 | Not calibrated | WEAK 14/100 | EXTREME 92/100 | Do nothing | WATCH |
| 4 | CAP/USD | 0.102039 | 17.619 | 26.010 | +1.05% | +0.12% | 0.10x | 27.6 | 2026-11-18T02:00:05.424192+00:00 | Not calibrated | WEAK 19/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UP/USD | 43.746 | 0.05503 | -0.65% | 0.77x |
| 2 | AKT/USD | 38.479 | 0.518 | +0.58% | 2.48x |
| 3 | TON/USD | 36.826 | 1.081 | +0.37% | 9.44x |
| 4 | CAP/USD | 26.010 | 0.102039 | +0.12% | 0.10x |

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

- Persisted scans: 501; predictions: 4282; observations: 302116.
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

**Writer:** 44219927236 · **Generation:** 501 · **Legacy run:** 44219927236
**Main quote time:** 2026-11-18T02:00:07.839214+00:00 · **Legacy report time:** 2026-11-18T02:00:22.887191+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.518 | 56.15 | +0.58% | 2.48x | STRONG 88/100 | HIGH 66/100 | Consider small entry |
| 2 | TON/USD ⭐ | 1.081 | 53.68 | +0.37% | 9.44x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 3 | UP/USD | 0.05503 | 38.24 | -0.65% | 0.77x | WEAK 14/100 | EXTREME 92/100 | Do nothing |
| 4 | CAP/USD | 0.102039 | 17.62 | +0.12% | 0.10x | WEAK 19/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5183 | 55.66 | +0.58% | 2.48x | 3586 | STRONG 93/100 | HIGH 60/100 | Consider small entry |
| 2 | TON/USD ⭐ | 1.081 | 40.88 | +0.37% | 9.44x | 5294 | STRONG 85/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** AKT/USD, TON/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
