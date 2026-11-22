# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T13:41:13.261086+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45028629845
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 6a8fb8793deda01cd551619fc085e6af2aacf0a5 (atomic ledger/results publication)
**Ledger generation:** 1290 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.0304 | 107.739 | 87.636 | +4.99% | +1.02% | 3.15x | 4.6 | 2026-11-22T13:41:05.238513+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NIGHT/USD | 0.04815 | 96.794 | 84.591 | +8.74% | +1.77% | 1.34x | 12.5 | 2026-11-22T13:41:05.238513+00:00 | Not calibrated | STRONG 88/100 | HIGH 61/100 | Watch | WATCH |
| 3 | DRV/USD | 0.36518 | 89.003 | 86.978 | +8.94% | +1.43% | 0.49x | 0.3 | 2026-11-22T13:41:05.238513+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | INJ/USD | 6.269 | 79.264 | 74.136 | +4.96% | -0.05% | 1.54x | 6.4 | 2026-11-22T13:41:05.238513+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 5 | LINK/USD | 8.771 | 76.248 | 61.240 | +2.05% | +0.00% | 4.47x | 0.0 | 2026-11-22T13:41:05.238513+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 6 | ETH/USD | 1706.22 | 68.706 | 64.170 | +1.42% | +0.10% | 1.40x | 1.6 | 2026-11-22T13:41:05.238513+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 7 | TAO/USD | 191.4981 | 62.747 | 70.974 | +3.11% | +0.12% | 0.12x | 4.6 | 2026-11-22T13:41:05.238513+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XBT/USD | 60778.7 | 61.898 | 63.016 | +1.15% | +0.23% | 0.77x | 0.0 | 2026-11-22T13:41:05.238513+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 9 | HYPE/USD | 62.69 | 61.576 | 70.776 | +2.37% | -0.25% | 0.21x | 1.6 | 2026-11-22T13:41:05.238513+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6593 | 60.924 | 66.459 | +1.85% | +0.12% | 0.39x | 3.0 | 2026-11-22T13:41:05.238513+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ZEC/USD | 793.97 | 60.772 | 67.763 | +2.03% | -0.09% | 0.34x | 2.9 | 2026-11-22T13:41:05.238513+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | BNB/USD | 554.95 | 54.049 | 47.076 | +1.38% | +0.11% | 1.64x | 1.8 | 2026-11-22T13:41:05.238513+00:00 | Not calibrated | MODERATE 62/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 87.636 | 3.0304 | +1.02% | 3.15x |
| 2 | DRV/USD | 86.978 | 0.36518 | +1.43% | 0.49x |
| 3 | NIGHT/USD | 84.591 | 0.04815 | +1.77% | 1.34x |
| 4 | INJ/USD | 74.136 | 6.269 | -0.05% | 1.54x |
| 5 | TAO/USD | 70.974 | 191.4981 | +0.12% | 0.12x |
| 6 | HYPE/USD | 70.776 | 62.69 | -0.25% | 0.21x |
| 7 | ZEC/USD | 67.763 | 793.97 | -0.09% | 0.34x |
| 8 | SUI/USD | 66.459 | 0.6593 | +0.12% | 0.39x |
| 9 | ETH/USD | 64.170 | 1706.22 | +0.10% | 1.40x |
| 10 | XBT/USD | 63.016 | 60778.7 | +0.23% | 0.77x |
| 11 | LINK/USD | 61.240 | 8.771 | +0.00% | 4.47x |
| 12 | BNB/USD | 47.076 | 554.95 | +0.11% | 1.64x |

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

- Persisted scans: 1290; predictions: 10400; observations: 780719.
- Matured sampled outcomes across 1/6/24/48h: 15102; gap abstentions: 22262. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 60 (sampled only; not a success-rate estimate).
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

**Writer:** 45028629845 · **Generation:** 1290 · **Legacy run:** 45028629845
**Main quote time:** 2026-11-22T13:41:13.261086+00:00 · **Legacy report time:** 2026-11-22T13:42:17.042609+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.0304 | 107.74 | +1.02% | 3.15x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NIGHT/USD ⭐ | 0.04815 | 96.79 | +1.77% | 1.34x | STRONG 98/100 | HIGH 61/100 | Watch |
| 3 | DRV/USD | 0.36518 | 89.00 | +1.43% | 0.49x | STRONG 75/100 | VERY_HIGH 70/100 | Watch |
| 4 | INJ/USD | 6.269 | 79.26 | -0.05% | 1.54x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 5 | LINK/USD | 8.771 | 76.25 | +0.00% | 4.47x | STRONG 83/100 | HIGH 55/100 | Watch |
| 6 | ETH/USD ⭐ | 1706.22 | 68.71 | +0.10% | 1.40x | STRONG 79/100 | HIGH 55/100 | Watch |
| 7 | TAO/USD | 191.4981 | 62.75 | +0.12% | 0.12x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 8 | XBT/USD | 60778.7 | 61.90 | +0.23% | 0.77x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 9 | HYPE/USD | 62.69 | 61.58 | -0.25% | 0.21x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 10 | SUI/USD | 0.6593 | 60.92 | +0.12% | 0.39x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 11 | ZEC/USD | 793.97 | 60.77 | -0.09% | 0.34x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | BNB/USD | 554.95 | 54.05 | +0.11% | 1.64x | MODERATE 62/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.026 | 100.00 | +1.02% | 3.15x | 13386 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NIGHT/USD ⭐ | 0.04806 | 86.12 | +1.77% | 1.34x | 9364 | STRONG 88/100 | HIGH 67/100 | Watch |
| 3 | ETH/USD ⭐ | 1705 | 70.01 | +0.10% | 1.40x | 42668 | STRONG 80/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NEAR/USD, NIGHT/USD, ETH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
