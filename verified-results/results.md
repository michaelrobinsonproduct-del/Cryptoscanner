# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T11:00:46.644370+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44723836663
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** def8cd94bb37f34d07b937f6b8f6d9c08554081e (atomic ledger/results publication)
**Ledger generation:** 969 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 607; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XLM/USD | 0.133255 | 60.345 | 56.202 | +0.42% | -0.36% | 1.59x | 3.5 | 2026-11-20T11:00:40.748650+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 2 | HBAR/USD | 0.05418 | 55.857 | 42.971 | +0.78% | -0.42% | 5.07x | 5.5 | 2026-11-20T11:00:40.748650+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 3 | SYRUP/USD | 0.09794 | 52.890 | 39.974 | +1.78% | -0.42% | 3.65x | 9.2 | 2026-11-20T11:00:40.748650+00:00 | Not calibrated | MODERATE 56/100 | HIGH 66/100 | Watch | WATCH |
| 4 | PROS/USD | 0.5935 | 52.687 | 61.717 | +10.17% | -0.10% | 0.15x | 28.6 | 2026-11-20T11:00:40.748650+00:00 | Not calibrated | WEAK 21/100 | EXTREME 100/100 | Do nothing | WATCH |
| 5 | SENT/USD | 0.021935 | 52.420 | 50.213 | +3.03% | -1.31% | 1.87x | 8.2 | 2026-11-20T11:00:40.748650+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 6 | XRP/USD | 0.96274 | 51.314 | 57.183 | +0.36% | -0.48% | 0.65x | 0.7 | 2026-11-20T11:00:40.748650+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | ATOM/USD | 1.2678 | 42.188 | 31.943 | +0.50% | -0.31% | 2.18x | 8.7 | 2026-11-20T11:00:40.748650+00:00 | Not calibrated | MODERATE 51/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PROS/USD | 61.717 | 0.5935 | -0.10% | 0.15x |
| 2 | XRP/USD | 57.183 | 0.96274 | -0.48% | 0.65x |
| 3 | XLM/USD | 56.202 | 0.133255 | -0.36% | 1.59x |
| 4 | SENT/USD | 50.213 | 0.021935 | -1.31% | 1.87x |
| 5 | HBAR/USD | 42.971 | 0.05418 | -0.42% | 5.07x |
| 6 | SYRUP/USD | 39.974 | 0.09794 | -0.42% | 3.65x |
| 7 | ATOM/USD | 31.943 | 1.2678 | -0.31% | 2.18x |

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

- Persisted scans: 969; predictions: 8180; observations: 585537.
- Matured sampled outcomes across 1/6/24/48h: 9820; gap abstentions: 17479. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44723836663 · **Generation:** 969 · **Legacy run:** 44723836663
**Main quote time:** 2026-11-20T11:00:46.644370+00:00 · **Legacy report time:** 2026-11-20T11:01:44.598861+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD | 0.133255 | 60.34 | -0.36% | 1.59x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 2 | HBAR/USD | 0.05418 | 55.86 | -0.42% | 5.07x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 3 | SYRUP/USD | 0.09794 | 52.89 | -0.42% | 3.65x | MODERATE 56/100 | HIGH 66/100 | Watch |
| 4 | PROS/USD | 0.5935 | 52.69 | -0.10% | 0.15x | WEAK 21/100 | EXTREME 100/100 | Do nothing |
| 5 | SENT/USD | 0.021935 | 52.42 | -1.31% | 1.87x | MODERATE 46/100 | VERY_HIGH 70/100 | Do nothing |
| 6 | XRP/USD | 0.96274 | 51.31 | -0.48% | 0.65x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | ATOM/USD | 1.2678 | 42.19 | -0.31% | 2.18x | MODERATE 51/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
