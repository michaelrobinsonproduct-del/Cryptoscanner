# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T08:49:06.662172+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45004450248
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 15236305fe0eac4cc103d25b173e6fe4c3234126 (atomic ledger/results publication)
**Ledger generation:** 1259 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 790.66 | 78.698 | 62.250 | +1.60% | +0.29% | 5.45x | 8.0 | 2026-11-22T08:48:58.231577+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NEAR/USD | 2.912 | 76.521 | 58.310 | +0.89% | +0.64% | 10.92x | 5.8 | 2026-11-22T08:48:58.231577+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | TAO/USD | 189.4144 | 74.619 | 64.057 | +1.98% | +0.23% | 1.94x | 9.7 | 2026-11-22T08:48:58.231577+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | VVV/USD | 25.39 | 74.363 | 59.129 | +1.97% | +0.05% | 2.71x | 19.3 | 2026-11-22T08:48:58.231577+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 5 | LINK/USD | 8.62618 | 68.551 | 52.734 | +0.36% | +0.16% | 3.04x | 4.2 | 2026-11-22T08:48:58.231577+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 6 | INJ/USD | 6.06 | 62.901 | 49.377 | +1.46% | -0.30% | 3.90x | 1.7 | 2026-11-22T08:48:58.231577+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 7 | AVAX/USD | 6.582 | 56.870 | 45.338 | +0.29% | +0.27% | 2.02x | 3.0 | 2026-11-22T08:48:58.231577+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 8 | ZBCN/USD | 0.001836 | 55.099 | 57.358 | +6.31% | +0.54% | 0.50x | 38.3 | 2026-11-22T08:48:58.231577+00:00 | Not calibrated | WEAK 43/100 | EXTREME 87/100 | Do nothing | WATCH |
| 9 | ASTER/USD | 0.50047 | 53.209 | 53.070 | +3.05% | +0.11% | 0.96x | 5.4 | 2026-11-22T08:48:58.231577+00:00 | Not calibrated | MODERATE 47/100 | HIGH 67/100 | Watch | WATCH |
| 10 | ENA/USD | 0.0988 | 50.858 | 34.342 | +0.51% | +0.30% | 3.06x | 10.1 | 2026-11-22T08:48:58.231577+00:00 | Not calibrated | STRONG 75/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TAO/USD | 64.057 | 189.4144 | +0.23% | 1.94x |
| 2 | ZEC/USD | 62.250 | 790.66 | +0.29% | 5.45x |
| 3 | VVV/USD | 59.129 | 25.39 | +0.05% | 2.71x |
| 4 | NEAR/USD | 58.310 | 2.912 | +0.64% | 10.92x |
| 5 | ZBCN/USD | 57.358 | 0.001836 | +0.54% | 0.50x |
| 6 | ASTER/USD | 53.070 | 0.50047 | +0.11% | 0.96x |
| 7 | LINK/USD | 52.734 | 8.62618 | +0.16% | 3.04x |
| 8 | INJ/USD | 49.377 | 6.06 | -0.30% | 3.90x |
| 9 | AVAX/USD | 45.338 | 6.582 | +0.27% | 2.02x |
| 10 | ENA/USD | 34.342 | 0.0988 | +0.30% | 3.06x |

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

- Persisted scans: 1259; predictions: 10034; observations: 761840.
- Matured sampled outcomes across 1/6/24/48h: 14464; gap abstentions: 22121. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 59 (sampled only; not a success-rate estimate).
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

**Writer:** 45004450248 · **Generation:** 1259 · **Legacy run:** 45004450248
**Main quote time:** 2026-11-22T08:49:06.662172+00:00 · **Legacy report time:** 2026-11-22T08:49:53.955697+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 790.66 | 78.70 | +0.29% | 5.45x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 2.912 | 76.52 | +0.64% | 10.92x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | TAO/USD ⭐ | 189.4144 | 74.62 | +0.23% | 1.94x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 4 | VVV/USD | 25.39 | 74.36 | +0.05% | 2.71x | STRONG 77/100 | HIGH 61/100 | Watch |
| 5 | LINK/USD | 8.62618 | 68.55 | +0.16% | 3.04x | STRONG 79/100 | HIGH 55/100 | Watch |
| 6 | INJ/USD | 6.06 | 62.90 | -0.30% | 3.90x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 7 | AVAX/USD | 6.582 | 56.87 | +0.27% | 2.02x | STRONG 83/100 | HIGH 55/100 | Watch |
| 8 | ZBCN/USD | 0.001836 | 55.10 | +0.54% | 0.50x | WEAK 43/100 | EXTREME 87/100 | Do nothing |
| 9 | ASTER/USD | 0.50047 | 53.21 | +0.11% | 0.96x | MODERATE 47/100 | HIGH 67/100 | Watch |
| 10 | ENA/USD | 0.0988 | 50.86 | +0.30% | 3.06x | STRONG 75/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 789.9 | 68.82 | +0.29% | 5.45x | 29176 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 2 | TAO/USD ⭐ | 189.4144 | 65.22 | +0.23% | 1.94x | 7151 | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD ⭐ | 2.912 | 63.66 | +0.64% | 10.92x | 12356 | STRONG 97/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ZEC/USD, NEAR/USD, TAO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
