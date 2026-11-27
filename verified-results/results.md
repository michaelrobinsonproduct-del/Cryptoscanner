# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T05:51:39.572140+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45948087251
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4a2245da81d266d36de565a32cbad8f0fa3c0f16 (atomic ledger/results publication)
**Ledger generation:** 1967 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 602; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 65.82 | 93.339 | 94.741 | +5.79% | -0.32% | 1.02x | 1.5 | 2026-11-27T05:51:33.286927+00:00 | Not calibrated | MODERATE 57/100 | HIGH 68/100 | Watch | WATCH |
| 2 | ZEC/USD | 759.65 | 91.933 | 97.959 | +11.44% | -0.01% | 0.40x | 4.1 | 2026-11-27T05:51:33.286927+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | XRP/USD | 0.96868 | 89.667 | 74.202 | +2.75% | +0.09% | 3.89x | 0.1 | 2026-11-27T05:51:33.286927+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SUI/USD | 0.6857 | 86.381 | 72.543 | +2.70% | -0.12% | 2.44x | 1.5 | 2026-11-27T05:51:33.286927+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 5 | LINK/USD | 9.64804 | 81.752 | 80.827 | +4.10% | -0.38% | 1.28x | 5.7 | 2026-11-27T05:51:33.286927+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XBT/USD | 61651.9 | 78.211 | 68.343 | +1.91% | -0.15% | 2.06x | 0.0 | 2026-11-27T05:51:33.286927+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 7 | SOL/USD | 73.08 | 75.362 | 75.432 | +3.02% | -0.29% | 1.14x | 1.4 | 2026-11-27T05:51:33.286927+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 8 | ETH/USD | 1738.71 | 74.366 | 75.878 | +3.02% | -0.26% | 0.98x | 0.6 | 2026-11-27T05:51:33.286927+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 9 | NEAR/USD | 3.1169 | 73.532 | 69.082 | +2.26% | -0.10% | 1.49x | 3.5 | 2026-11-27T05:51:33.286927+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 10 | VVV/USD | 27.007 | 68.282 | 72.950 | +3.15% | -1.27% | 1.17x | 8.2 | 2026-11-27T05:51:33.286927+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 11 | UNI/USD | 4.8486 | 67.208 | 70.438 | +4.27% | -0.56% | 0.95x | 4.5 | 2026-11-27T05:51:33.286927+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 12 | QNT/USD | 150.05 | 64.081 | 51.566 | +1.59% | -0.50% | 6.84x | 1.3 | 2026-11-27T05:51:33.286927+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.959 | 759.65 | -0.01% | 0.40x |
| 2 | HYPE/USD | 94.741 | 65.82 | -0.32% | 1.02x |
| 3 | LINK/USD | 80.827 | 9.64804 | -0.38% | 1.28x |
| 4 | ETH/USD | 75.878 | 1738.71 | -0.26% | 0.98x |
| 5 | SOL/USD | 75.432 | 73.08 | -0.29% | 1.14x |
| 6 | XRP/USD | 74.202 | 0.96868 | +0.09% | 3.89x |
| 7 | VVV/USD | 72.950 | 27.007 | -1.27% | 1.17x |
| 8 | SUI/USD | 72.543 | 0.6857 | -0.12% | 2.44x |
| 9 | UNI/USD | 70.438 | 4.8486 | -0.56% | 0.95x |
| 10 | NEAR/USD | 69.082 | 3.1169 | -0.10% | 1.49x |
| 11 | XBT/USD | 68.343 | 61651.9 | -0.15% | 2.06x |
| 12 | QNT/USD | 51.566 | 150.05 | -0.50% | 6.84x |

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

- Persisted scans: 1967; predictions: 17306; observations: 1191256.
- Matured sampled outcomes across 1/6/24/48h: 38186; gap abstentions: 25553. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 1; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45948087251 · **Generation:** 1967 · **Legacy run:** 45948087251
**Main quote time:** 2026-11-27T05:51:39.572140+00:00 · **Legacy report time:** 2026-11-27T05:52:24.372253+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 65.82 | 93.34 | -0.32% | 1.02x | MODERATE 57/100 | HIGH 68/100 | Watch |
| 2 | ZEC/USD | 759.65 | 91.93 | -0.01% | 0.40x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 3 | XRP/USD ⭐ | 0.96868 | 89.67 | +0.09% | 3.89x | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | SUI/USD | 0.6857 | 86.38 | -0.12% | 2.44x | STRONG 73/100 | HIGH 61/100 | Watch |
| 5 | LINK/USD | 9.64804 | 81.75 | -0.38% | 1.28x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 6 | XBT/USD | 61651.9 | 78.21 | -0.15% | 2.06x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 7 | SOL/USD | 73.08 | 75.36 | -0.29% | 1.14x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 8 | ETH/USD | 1738.71 | 74.37 | -0.26% | 0.98x | WEAK 42/100 | HIGH 68/100 | Watch |
| 9 | NEAR/USD | 3.1169 | 73.53 | -0.10% | 1.49x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 10 | VVV/USD | 27.007 | 68.28 | -1.27% | 1.17x | WEAK 44/100 | VERY_HIGH 72/100 | Do nothing |
| 11 | UNI/USD | 4.8486 | 67.21 | -0.56% | 0.95x | WEAK 39/100 | HIGH 68/100 | Watch |
| 12 | QNT/USD | 150.05 | 64.08 | -0.50% | 6.84x | MODERATE 62/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.96871 | 93.12 | +0.09% | 3.89x | 21567 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | TIA/USD | 0.3478 | 81.28 | +0.17% | 11.69x | 2604 | STRONG 86/100 | HIGH 67/100 | Watch |

**Same-run overlap:** XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
