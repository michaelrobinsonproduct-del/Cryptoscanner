# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T11:21:18.458359+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45016751677
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 3c4336bd48f6f22cde312e7e2afc0ebda4afdb54 (atomic ledger/results publication)
**Ledger generation:** 1275 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PUMP/USD | 0.002489 | 99.050 | 79.591 | +6.19% | +0.89% | 2.53x | 12.0 | 2026-11-22T11:21:10.192653+00:00 | Not calibrated | STRONG 100/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | NEAR/USD | 2.9993 | 82.105 | 79.399 | +3.92% | -0.38% | 1.46x | 6.0 | 2026-11-22T11:21:10.192653+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LINK/USD | 8.82423 | 73.747 | 68.622 | +2.67% | +0.25% | 1.39x | 5.4 | 2026-11-22T11:21:10.192653+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 4 | CRV/USD | 0.18556 | 72.561 | 68.444 | +4.04% | +0.20% | 1.31x | 10.2 | 2026-11-22T11:21:10.192653+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ETH/USD | 1705.01 | 71.810 | 63.871 | +1.35% | -0.12% | 1.85x | 1.2 | 2026-11-22T11:21:10.192653+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 6 | ZEC/USD | 798.13 | 70.211 | 69.130 | +2.56% | +0.40% | 0.91x | 7.7 | 2026-11-22T11:21:10.192653+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 7 | HYPE/USD | 62.51 | 66.161 | 68.716 | +2.07% | +0.16% | 0.66x | 1.6 | 2026-11-22T11:21:10.192653+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XBT/USD | 60792 | 65.210 | 63.171 | +1.17% | +0.04% | 1.18x | 0.0 | 2026-11-22T11:21:10.192653+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 9 | SOL/USD | 70.65 | 63.775 | 58.373 | +0.68% | +0.09% | 1.50x | 2.8 | 2026-11-22T11:21:10.192653+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 10 | INJ/USD | 6.252 | 62.976 | 70.751 | +4.67% | +0.08% | 0.18x | 8.0 | 2026-11-22T11:21:10.192653+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | TAO/USD | 190.7265 | 62.658 | 70.551 | +2.69% | +0.09% | 0.17x | 6.6 | 2026-11-22T11:21:10.192653+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | SUI/USD | 0.6607 | 62.122 | 68.734 | +2.07% | +0.18% | 0.25x | 1.5 | 2026-11-22T11:21:10.192653+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PUMP/USD | 79.591 | 0.002489 | +0.89% | 2.53x |
| 2 | NEAR/USD | 79.399 | 2.9993 | -0.38% | 1.46x |
| 3 | INJ/USD | 70.751 | 6.252 | +0.08% | 0.18x |
| 4 | TAO/USD | 70.551 | 190.7265 | +0.09% | 0.17x |
| 5 | ZEC/USD | 69.130 | 798.13 | +0.40% | 0.91x |
| 6 | SUI/USD | 68.734 | 0.6607 | +0.18% | 0.25x |
| 7 | HYPE/USD | 68.716 | 62.51 | +0.16% | 0.66x |
| 8 | LINK/USD | 68.622 | 8.82423 | +0.25% | 1.39x |
| 9 | CRV/USD | 68.444 | 0.18556 | +0.20% | 1.31x |
| 10 | ETH/USD | 63.871 | 1705.01 | -0.12% | 1.85x |
| 11 | XBT/USD | 63.171 | 60792 | +0.04% | 1.18x |
| 12 | SOL/USD | 58.373 | 70.65 | +0.09% | 1.50x |

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

- Persisted scans: 1275; predictions: 10220; observations: 771584.
- Matured sampled outcomes across 1/6/24/48h: 14743; gap abstentions: 22203. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 60 (sampled only; not a success-rate estimate).
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

**Writer:** 45016751677 · **Generation:** 1275 · **Legacy run:** 45016751677
**Main quote time:** 2026-11-22T11:21:18.458359+00:00 · **Legacy report time:** 2026-11-22T11:22:22.576904+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002489 | 99.05 | +0.89% | 2.53x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | NEAR/USD | 2.9993 | 82.10 | -0.38% | 1.46x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 3 | LINK/USD ⭐ | 8.82423 | 73.75 | +0.25% | 1.39x | STRONG 92/100 | HIGH 55/100 | Watch |
| 4 | CRV/USD ⭐ | 0.18556 | 72.56 | +0.20% | 1.31x | STRONG 76/100 | HIGH 61/100 | Watch |
| 5 | ETH/USD | 1705.01 | 71.81 | -0.12% | 1.85x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 6 | ZEC/USD | 798.13 | 70.21 | +0.40% | 0.91x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 7 | HYPE/USD | 62.51 | 66.16 | +0.16% | 0.66x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 8 | XBT/USD | 60792 | 65.21 | +0.04% | 1.18x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 9 | SOL/USD | 70.65 | 63.78 | +0.09% | 1.50x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 10 | INJ/USD | 6.252 | 62.98 | +0.08% | 0.18x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 11 | TAO/USD | 190.7265 | 62.66 | +0.09% | 0.17x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 12 | SUI/USD | 0.6607 | 62.12 | +0.18% | 0.25x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002503 | 86.25 | +0.89% | 2.53x | 4686 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | CRV/USD ⭐ | 0.18569 | 81.04 | +0.20% | 1.31x | 6840 | STRONG 81/100 | HIGH 61/100 | Watch |
| 3 | LINK/USD ⭐ | 8.82587 | 73.65 | +0.25% | 1.39x | 6284 | STRONG 92/100 | HIGH 55/100 | Watch |
| 4 | ENA/USD | 0.1028 | 73.51 | +0.29% | 1.18x | 2406 | MODERATE 67/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** PUMP/USD, LINK/USD, CRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
