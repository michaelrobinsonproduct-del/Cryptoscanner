# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T14:25:29.394423+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44543417520
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 5e9addab7206ab9dafc4a14bf315e938717422e2 (atomic ledger/results publication)
**Ledger generation:** 792 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 594; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PUMP/USD | 0.002744 | 96.935 | 81.205 | +5.70% | +0.15% | 4.64x | 7.3 | 2026-11-19T14:25:23.525411+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Watch | WATCH |
| 2 | VVV/USD | 23.21 | 89.740 | 96.771 | +7.10% | +0.41% | 0.09x | 6.5 | 2026-11-19T14:25:23.525411+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | TAO/USD | 198.8374 | 82.950 | 76.226 | +3.58% | -0.05% | 1.70x | 7.7 | 2026-11-19T14:25:23.525411+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.92e-06 | 82.899 | 70.817 | +4.64% | -0.58% | 2.68x | 5.1 | 2026-11-19T14:25:23.525411+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XBT/USD | 63847.9 | 78.804 | 64.588 | +1.37% | -0.01% | 2.42x | 0.0 | 2026-11-19T14:25:23.525411+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 6 | ETH/USD | 1806.21 | 71.758 | 67.377 | +1.77% | -0.14% | 1.51x | 0.1 | 2026-11-19T14:25:23.525411+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 7 | SOL/USD | 74.93 | 70.685 | 67.564 | +1.89% | -0.05% | 1.34x | 1.3 | 2026-11-19T14:25:23.525411+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ZEC/USD | 942.41 | 70.394 | 77.478 | +3.34% | -0.22% | 0.40x | 1.8 | 2026-11-19T14:25:23.525411+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | QNT/USD | 154.36 | 67.859 | 56.362 | +1.52% | -0.70% | 5.62x | 0.6 | 2026-11-19T14:25:23.525411+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 10 | XRP/USD | 0.98998 | 67.187 | 71.698 | +2.44% | +0.00% | 0.55x | 0.8 | 2026-11-19T14:25:23.525411+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | GRASS/USD | 0.4438 | 65.584 | 71.799 | +9.53% | -0.31% | 0.54x | 13.6 | 2026-11-19T14:25:23.525411+00:00 | Not calibrated | WEAK 33/100 | EXTREME 87/100 | Do nothing | WATCH |
| 12 | AKT/USD | 0.5534 | 63.831 | 71.095 | +6.83% | +0.09% | 0.23x | 10.9 | 2026-11-19T14:25:23.525411+00:00 | Not calibrated | MODERATE 47/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 96.771 | 23.21 | +0.41% | 0.09x |
| 2 | PUMP/USD | 81.205 | 0.002744 | +0.15% | 4.64x |
| 3 | ZEC/USD | 77.478 | 942.41 | -0.22% | 0.40x |
| 4 | TAO/USD | 76.226 | 198.8374 | -0.05% | 1.70x |
| 5 | GRASS/USD | 71.799 | 0.4438 | -0.31% | 0.54x |
| 6 | XRP/USD | 71.698 | 0.98998 | +0.00% | 0.55x |
| 7 | AKT/USD | 71.095 | 0.5534 | +0.09% | 0.23x |
| 8 | PEPE/USD | 70.817 | 3.92e-06 | -0.58% | 2.68x |
| 9 | SOL/USD | 67.564 | 74.93 | -0.05% | 1.34x |
| 10 | ETH/USD | 67.377 | 1806.21 | -0.14% | 1.51x |
| 11 | XBT/USD | 64.588 | 63847.9 | -0.01% | 2.42x |
| 12 | QNT/USD | 56.362 | 154.36 | -0.70% | 5.62x |

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

- Persisted scans: 792; predictions: 6648; observations: 479076.
- Matured sampled outcomes across 1/6/24/48h: 6671; gap abstentions: 15073. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44543417520 · **Generation:** 792 · **Legacy run:** 44543417520
**Main quote time:** 2026-11-19T14:25:29.394423+00:00 · **Legacy report time:** 2026-11-19T14:26:07.519955+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002744 | 96.94 | +0.15% | 4.64x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | VVV/USD | 23.21 | 89.74 | +0.41% | 0.09x | STRONG 75/100 | VERY_HIGH 70/100 | Watch |
| 3 | TAO/USD | 198.8374 | 82.95 | -0.05% | 1.70x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 4 | PEPE/USD | 3.92e-06 | 82.90 | -0.58% | 2.68x | STRONG 71/100 | HIGH 61/100 | Watch |
| 5 | XBT/USD | 63847.9 | 78.80 | -0.01% | 2.42x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 6 | ETH/USD | 1806.21 | 71.76 | -0.14% | 1.51x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 7 | SOL/USD | 74.93 | 70.68 | -0.05% | 1.34x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 8 | ZEC/USD | 942.41 | 70.39 | -0.22% | 0.40x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 9 | QNT/USD | 154.36 | 67.86 | -0.70% | 5.62x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 10 | XRP/USD | 0.98998 | 67.19 | +0.00% | 0.55x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 11 | GRASS/USD | 0.4438 | 65.58 | -0.31% | 0.54x | WEAK 33/100 | EXTREME 87/100 | Do nothing |
| 12 | AKT/USD | 0.5534 | 63.83 | +0.09% | 0.23x | MODERATE 47/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002743 | 87.40 | +0.15% | 4.64x | 4889 | STRONG 94/100 | HIGH 61/100 | Watch |

**Same-run overlap:** PUMP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
