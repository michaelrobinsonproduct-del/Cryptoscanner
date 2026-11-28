# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T02:22:52.208003+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46097503582
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 5ce324d6846e8c64519bb758c0f48ebbe85f9845 (atomic ledger/results publication)
**Ledger generation:** 2092 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 756.16 | 76.529 | 73.853 | +2.94% | +0.10% | 1.22x | 3.4 | 2026-11-28T02:22:44.619031+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 2 | XBT/USD | 60097 | 67.431 | 57.718 | +0.39% | +0.11% | 1.92x | 0.0 | 2026-11-28T02:22:44.619031+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 3 | XDG/USD | 0.0578888 | 61.917 | 57.559 | +0.38% | +0.02% | 1.43x | 0.2 | 2026-11-28T02:22:44.619031+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |
| 4 | XRP/USD | 0.95197 | 61.025 | 57.474 | +0.41% | -0.11% | 1.41x | 0.8 | 2026-11-28T02:22:44.619031+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.054 | 59.946 | 61.829 | +1.19% | -0.02% | 0.82x | 2.9 | 2026-11-28T02:22:44.619031+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 6 | PEPE/USD | 3.562e-06 | 59.119 | 48.248 | +0.56% | -0.03% | 2.10x | 2.8 | 2026-11-28T02:22:44.619031+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 7 | HYPE/USD | 64.36 | 58.800 | 63.038 | +1.37% | +0.00% | 0.58x | 3.1 | 2026-11-28T02:22:44.619031+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | TAO/USD | 188.6874 | 53.751 | 60.054 | +0.93% | +0.02% | 0.36x | 2.9 | 2026-11-28T02:22:44.619031+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XMR/USD | 408.87 | 53.106 | 50.898 | +0.39% | -0.51% | 1.48x | 13.7 | 2026-11-28T02:22:44.619031+00:00 | Not calibrated | WEAK 42/100 | HIGH 67/100 | Watch | WATCH |
| 10 | SENT/USD | 0.024329 | 52.806 | 45.697 | +2.59% | +0.06% | 1.68x | 6.6 | 2026-11-28T02:22:44.619031+00:00 | Not calibrated | MODERATE 61/100 | HIGH 67/100 | Watch | WATCH |
| 11 | ETH/USD | 1667.04 | 52.556 | 57.553 | +0.37% | +0.13% | 0.43x | 0.1 | 2026-11-28T02:22:44.619031+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | SOL/USD | 71.91 | 52.107 | 57.335 | +0.43% | +0.03% | 0.46x | 1.4 | 2026-11-28T02:22:44.619031+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 73.853 | 756.16 | +0.10% | 1.22x |
| 2 | HYPE/USD | 63.038 | 64.36 | +0.00% | 0.58x |
| 3 | NEAR/USD | 61.829 | 3.054 | -0.02% | 0.82x |
| 4 | TAO/USD | 60.054 | 188.6874 | +0.02% | 0.36x |
| 5 | XBT/USD | 57.718 | 60097 | +0.11% | 1.92x |
| 6 | XDG/USD | 57.559 | 0.0578888 | +0.02% | 1.43x |
| 7 | ETH/USD | 57.553 | 1667.04 | +0.13% | 0.43x |
| 8 | XRP/USD | 57.474 | 0.95197 | -0.11% | 1.41x |
| 9 | SOL/USD | 57.335 | 71.91 | +0.03% | 0.46x |
| 10 | XMR/USD | 50.898 | 408.87 | -0.51% | 1.48x |
| 11 | PEPE/USD | 48.248 | 3.562e-06 | -0.03% | 2.10x |
| 12 | SENT/USD | 45.697 | 0.024329 | +0.06% | 1.68x |

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

- Persisted scans: 2092; predictions: 18767; observations: 1266798.
- Matured sampled outcomes across 1/6/24/48h: 43223; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46097503582 · **Generation:** 2092 · **Legacy run:** 46097503582
**Main quote time:** 2026-11-28T02:22:52.208003+00:00 · **Legacy report time:** 2026-11-28T02:23:38.451602+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 756.16 | 76.53 | +0.10% | 1.22x | STRONG 73/100 | HIGH 62/100 | Watch |
| 2 | XBT/USD ⭐ | 60097 | 67.43 | +0.11% | 1.92x | STRONG 79/100 | HIGH 55/100 | Watch |
| 3 | XDG/USD | 0.0578888 | 61.92 | +0.02% | 1.43x | MODERATE 66/100 | HIGH 55/100 | Watch |
| 4 | XRP/USD | 0.95197 | 61.03 | -0.11% | 1.41x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 5 | NEAR/USD | 3.054 | 59.95 | -0.02% | 0.82x | WEAK 35/100 | HIGH 68/100 | Watch |
| 6 | PEPE/USD | 3.562e-06 | 59.12 | -0.03% | 2.10x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 7 | HYPE/USD | 64.36 | 58.80 | +0.00% | 0.58x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 8 | TAO/USD | 188.6874 | 53.75 | +0.02% | 0.36x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 9 | XMR/USD | 408.87 | 53.11 | -0.51% | 1.48x | WEAK 42/100 | HIGH 67/100 | Watch |
| 10 | SENT/USD ⭐ | 0.024329 | 52.81 | +0.06% | 1.68x | STRONG 71/100 | HIGH 67/100 | Watch |
| 11 | ETH/USD | 1667.04 | 52.56 | +0.13% | 0.43x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 12 | SOL/USD | 71.91 | 52.11 | +0.03% | 0.46x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 756.11 | 79.38 | +0.10% | 1.22x | 31966 | STRONG 75/100 | HIGH 62/100 | Watch |
| 2 | SENT/USD ⭐ | 0.024336 | 67.77 | +0.06% | 1.68x | 3937 | STRONG 79/100 | HIGH 67/100 | Watch |
| 3 | BIGTIME/USD | 0.005805 | 62.59 | +2.45% | 2.26x | 5250 | STRONG 76/100 | VERY_HIGH 79/100 | Watch |
| 4 | XBT/USD ⭐ | 60126.4 | 61.22 | +0.11% | 1.92x | 163034 | STRONG 76/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD, XBT/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
