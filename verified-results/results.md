# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-15T20:09:41.665965+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43756422119
**Source SHA:** 885b4a0465f5c74a8a87db5ca921c3c0a00021af
**Previous ledger commit:** a55cb20b8cd1ac3f192f07b20f88843cfc0c7500 (atomic ledger/results publication)
**Ledger generation:** 443 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 155.11 | 104.109 | 94.201 | +8.23% | -1.02% | 4.21x | 11.6 | 2026-11-15T20:09:35.018531+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 71/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.05004 | 99.327 | 87.201 | +5.46% | +0.12% | 2.15x | 12.0 | 2026-11-15T20:09:35.018531+00:00 | Not calibrated | STRONG 90/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XMR/USD | 500.56 | 98.747 | 99.900 | +6.46% | +0.08% | 0.84x | 0.2 | 2026-11-15T20:09:35.018531+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 4 | UNI/USD | 5.1645 | 96.878 | 92.423 | +5.78% | -0.28% | 1.59x | 5.8 | 2026-11-15T20:09:35.018531+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ASTER/USD | 0.54829 | 94.078 | 82.006 | +9.53% | -0.12% | 2.27x | 5.8 | 2026-11-15T20:09:35.018531+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.1592 | 90.352 | 83.373 | +4.30% | -0.17% | 1.78x | 3.5 | 2026-11-15T20:09:35.018531+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ADA/USD | 0.153752 | 83.032 | 82.176 | +4.13% | -0.28% | 1.23x | 3.4 | 2026-11-15T20:09:35.018531+00:00 | Not calibrated | MODERATE 52/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XRP/USD | 0.95656 | 81.927 | 87.301 | +4.68% | -0.37% | 0.65x | 0.9 | 2026-11-15T20:09:35.018531+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | CC/USD | 0.08301 | 80.243 | 86.864 | +6.96% | -0.02% | 0.35x | 6.0 | 2026-11-15T20:09:35.018531+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | AAVE/USD | 108.01 | 79.301 | 87.749 | +7.42% | +0.21% | 0.05x | 4.6 | 2026-11-15T20:09:35.018531+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | HYPE/USD | 67.15 | 77.382 | 84.425 | +4.42% | -0.28% | 0.44x | 3.0 | 2026-11-15T20:09:35.018531+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | ETH/USD | 1819.62 | 74.143 | 75.341 | +2.91% | -0.37% | 1.07x | 0.1 | 2026-11-15T20:09:35.018531+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 99.900 | 500.56 | +0.08% | 0.84x |
| 2 | QNT/USD | 94.201 | 155.11 | -1.02% | 4.21x |
| 3 | UNI/USD | 92.423 | 5.1645 | -0.28% | 1.59x |
| 4 | AAVE/USD | 87.749 | 108.01 | +0.21% | 0.05x |
| 5 | XRP/USD | 87.301 | 0.95656 | -0.37% | 0.65x |
| 6 | NIGHT/USD | 87.201 | 0.05004 | +0.12% | 2.15x |
| 7 | CC/USD | 86.864 | 0.08301 | -0.02% | 0.35x |
| 8 | HYPE/USD | 84.425 | 67.15 | -0.28% | 0.44x |
| 9 | NEAR/USD | 83.373 | 3.1592 | -0.17% | 1.78x |
| 10 | ADA/USD | 82.176 | 0.153752 | -0.28% | 1.23x |
| 11 | ASTER/USD | 82.006 | 0.54829 | -0.12% | 2.27x |
| 12 | ETH/USD | 75.341 | 1819.62 | -0.37% | 1.07x |

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

- Persisted scans: 443; predictions: 3832; observations: 266816.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 11135. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 43756422119 · **Generation:** 443 · **Legacy run:** 43756422119
**Main quote time:** 2026-11-15T20:09:41.665965+00:00 · **Legacy report time:** 2026-11-15T20:09:54.977418+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 155.11 | 104.11 | -1.02% | 4.21x | STRONG 75/100 | VERY_HIGH 71/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.05004 | 99.33 | +0.12% | 2.15x | STRONG 100/100 | HIGH 61/100 | Watch |
| 3 | XMR/USD | 500.56 | 98.75 | +0.08% | 0.84x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 4 | UNI/USD | 5.1645 | 96.88 | -0.28% | 1.59x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 5 | ASTER/USD | 0.54829 | 94.08 | -0.12% | 2.27x | STRONG 77/100 | HIGH 61/100 | Watch |
| 6 | NEAR/USD | 3.1592 | 90.35 | -0.17% | 1.78x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 7 | ADA/USD | 0.153752 | 83.03 | -0.28% | 1.23x | MODERATE 52/100 | HIGH 68/100 | Watch |
| 8 | XRP/USD | 0.95656 | 81.93 | -0.37% | 0.65x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 9 | CC/USD | 0.08301 | 80.24 | -0.02% | 0.35x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 10 | AAVE/USD | 108.01 | 79.30 | +0.21% | 0.05x | STRONG 70/100 | VERY_HIGH 70/100 | Watch |
| 11 | HYPE/USD | 67.15 | 77.38 | -0.28% | 0.44x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 12 | ETH/USD | 1819.62 | 74.14 | -0.37% | 1.07x | MODERATE 47/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04991 | 89.97 | +0.12% | 2.15x | 18977 | STRONG 90/100 | HIGH 67/100 | Watch |

**Same-run overlap:** NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
