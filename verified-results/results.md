# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T13:01:06.719914+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45025102456
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 329566dce513697da13e55f235c00603d62070ac (atomic ledger/results publication)
**Ledger generation:** 1286 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TAO/USD | 191.5556 | 86.786 | 70.550 | +3.14% | +0.25% | 3.08x | 9.0 | 2026-11-22T13:01:00.129063+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | DRV/USD | 0.36787 | 81.476 | 80.145 | +9.75% | +0.97% | 0.65x | 13.9 | 2026-11-22T13:01:00.129063+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | PUMP/USD | 0.002495 | 76.691 | 81.840 | +6.44% | +0.69% | 0.14x | 12.0 | 2026-11-22T13:01:00.129063+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | HYPE/USD | 62.97 | 75.118 | 73.186 | +2.83% | +0.61% | 0.89x | 3.2 | 2026-11-22T13:01:00.129063+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04677 | 74.690 | 77.129 | +5.62% | -0.28% | 0.89x | 15.0 | 2026-11-22T13:01:00.129063+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 6 | INJ/USD | 6.249 | 68.120 | 71.782 | +4.62% | +0.22% | 0.52x | 6.4 | 2026-11-22T13:01:00.129063+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | NEAR/USD | 2.9836 | 67.467 | 76.252 | +3.37% | -0.17% | 0.21x | 4.7 | 2026-11-22T13:01:00.129063+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6582 | 61.172 | 66.028 | +1.68% | +0.00% | 0.51x | 1.5 | 2026-11-22T13:01:00.129063+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | ZEC/USD | 791.23 | 60.677 | 65.484 | +1.68% | +0.14% | 0.45x | 2.5 | 2026-11-22T13:01:00.129063+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | ETH/USD | 1704.93 | 57.707 | 64.395 | +1.35% | +0.09% | 0.29x | 0.1 | 2026-11-22T13:01:00.129063+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XBT/USD | 60775.8 | 56.275 | 62.982 | +1.14% | +0.17% | 0.24x | 0.0 | 2026-11-22T13:01:00.129063+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | ADA/USD | 0.145286 | 38.950 | 48.081 | +0.80% | -0.04% | 0.10x | 2.6 | 2026-11-22T13:01:00.129063+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PUMP/USD | 81.840 | 0.002495 | +0.69% | 0.14x |
| 2 | DRV/USD | 80.145 | 0.36787 | +0.97% | 0.65x |
| 3 | NIGHT/USD | 77.129 | 0.04677 | -0.28% | 0.89x |
| 4 | NEAR/USD | 76.252 | 2.9836 | -0.17% | 0.21x |
| 5 | HYPE/USD | 73.186 | 62.97 | +0.61% | 0.89x |
| 6 | INJ/USD | 71.782 | 6.249 | +0.22% | 0.52x |
| 7 | TAO/USD | 70.550 | 191.5556 | +0.25% | 3.08x |
| 8 | SUI/USD | 66.028 | 0.6582 | +0.00% | 0.51x |
| 9 | ZEC/USD | 65.484 | 791.23 | +0.14% | 0.45x |
| 10 | ETH/USD | 64.395 | 1704.93 | +0.09% | 0.29x |
| 11 | XBT/USD | 62.982 | 60775.8 | +0.17% | 0.24x |
| 12 | ADA/USD | 48.081 | 0.145286 | -0.04% | 0.10x |

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

- Persisted scans: 1286; predictions: 10352; observations: 778283.
- Matured sampled outcomes across 1/6/24/48h: 14977; gap abstentions: 22251. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 60 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45025102456 · **Generation:** 1286 · **Legacy run:** 45025102456
**Main quote time:** 2026-11-22T13:01:06.719914+00:00 · **Legacy report time:** 2026-11-22T13:02:08.968677+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD ⭐ | 191.5556 | 86.79 | +0.25% | 3.08x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | DRV/USD | 0.36787 | 81.48 | +0.97% | 0.65x | MODERATE 66/100 | VERY_HIGH 76/100 | Watch |
| 3 | PUMP/USD | 0.002495 | 76.69 | +0.69% | 0.14x | MODERATE 63/100 | VERY_HIGH 76/100 | Watch |
| 4 | HYPE/USD | 62.97 | 75.12 | +0.61% | 0.89x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 5 | NIGHT/USD | 0.04677 | 74.69 | -0.28% | 0.89x | WEAK 37/100 | VERY_HIGH 74/100 | Watch |
| 6 | INJ/USD | 6.249 | 68.12 | +0.22% | 0.52x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 7 | NEAR/USD | 2.9836 | 67.47 | -0.17% | 0.21x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 8 | SUI/USD | 0.6582 | 61.17 | +0.00% | 0.51x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 9 | ZEC/USD | 791.23 | 60.68 | +0.14% | 0.45x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 10 | ETH/USD | 1704.93 | 57.71 | +0.09% | 0.29x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 11 | XBT/USD | 60775.8 | 56.28 | +0.17% | 0.24x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 12 | ADA/USD | 0.145286 | 38.95 | -0.04% | 0.10x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD ⭐ | 191.7557 | 83.55 | +0.25% | 3.08x | 6712 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** TAO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
