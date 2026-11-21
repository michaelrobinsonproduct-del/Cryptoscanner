# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T18:10:58.043491+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44933964018
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** da022284dbfb09431823f5158ff7eee7ea9432a0 (atomic ledger/results publication)
**Ledger generation:** 1168 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 143.51 | 87.362 | 76.176 | +3.42% | +0.24% | 2.00x | 5.6 | 2026-11-21T18:10:49.206741+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XMR/USD | 480.78 | 85.988 | 89.868 | +5.37% | +0.22% | 0.50x | 5.4 | 2026-11-21T18:10:49.206741+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | PEARL/USD | 1.9761 | 84.267 | 73.034 | +8.08% | +0.75% | 1.75x | 37.2 | 2026-11-21T18:10:49.206741+00:00 | Not calibrated | STRONG 72/100 | HIGH 67/100 | Watch | WATCH |
| 4 | UNI/USD | 4.7125 | 82.686 | 91.528 | +5.49% | -0.42% | 0.33x | 3.8 | 2026-11-21T18:10:49.206741+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | ETH/USD | 1680.16 | 78.733 | 81.270 | +3.76% | +0.06% | 0.72x | 0.1 | 2026-11-21T18:10:49.206741+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.04585 | 75.195 | 78.321 | +8.60% | -0.72% | 1.05x | 28.4 | 2026-11-21T18:10:49.206741+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 7 | AVAX/USD | 6.602 | 75.134 | 62.910 | +1.48% | -0.12% | 2.28x | 3.0 | 2026-11-21T18:10:49.206741+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ZEC/USD | 786.14 | 72.705 | 79.610 | +3.72% | +0.17% | 0.22x | 2.9 | 2026-11-21T18:10:49.206741+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XBT/USD | 60009.9 | 70.284 | 69.317 | +2.05% | +0.16% | 1.02x | 0.0 | 2026-11-21T18:10:49.206741+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 10 | USELESS/USD | 0.08203 | 69.283 | 78.752 | +10.11% | -0.13% | 0.12x | 11.0 | 2026-11-21T18:10:49.206741+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 11 | SOL/USD | 70.6 | 69.176 | 73.547 | +2.75% | +0.00% | 0.56x | 1.4 | 2026-11-21T18:10:49.206741+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | TAO/USD | 186.043 | 67.801 | 73.879 | +3.07% | -0.08% | 0.43x | 5.2 | 2026-11-21T18:10:49.206741+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UNI/USD | 91.528 | 4.7125 | -0.42% | 0.33x |
| 2 | XMR/USD | 89.868 | 480.78 | +0.22% | 0.50x |
| 3 | ETH/USD | 81.270 | 1680.16 | +0.06% | 0.72x |
| 4 | ZEC/USD | 79.610 | 786.14 | +0.17% | 0.22x |
| 5 | USELESS/USD | 78.752 | 0.08203 | -0.13% | 0.12x |
| 6 | NIGHT/USD | 78.321 | 0.04585 | -0.72% | 1.05x |
| 7 | QNT/USD | 76.176 | 143.51 | +0.24% | 2.00x |
| 8 | TAO/USD | 73.879 | 186.043 | -0.08% | 0.43x |
| 9 | SOL/USD | 73.547 | 70.6 | +0.00% | 0.56x |
| 10 | PEARL/USD | 73.034 | 1.9761 | +0.75% | 1.75x |
| 11 | XBT/USD | 69.317 | 60009.9 | +0.16% | 1.02x |
| 12 | AVAX/USD | 62.910 | 6.602 | -0.12% | 2.28x |

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

- Persisted scans: 1168; predictions: 9325; observations: 706503.
- Matured sampled outcomes across 1/6/24/48h: 12292; gap abstentions: 21044. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44933964018 · **Generation:** 1168 · **Legacy run:** 44933964018
**Main quote time:** 2026-11-21T18:10:58.043491+00:00 · **Legacy report time:** 2026-11-21T18:11:52.406628+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 143.51 | 87.36 | +0.24% | 2.00x | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD | 480.78 | 85.99 | +0.22% | 0.50x | STRONG 73/100 | VERY_HIGH 70/100 | Watch |
| 3 | PEARL/USD ⭐ | 1.9761 | 84.27 | +0.75% | 1.75x | STRONG 82/100 | HIGH 67/100 | Consider small entry |
| 4 | UNI/USD | 4.7125 | 82.69 | -0.42% | 0.33x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 5 | ETH/USD | 1680.16 | 78.73 | +0.06% | 0.72x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 6 | NIGHT/USD | 0.04585 | 75.20 | -0.72% | 1.05x | WEAK 38/100 | VERY_HIGH 80/100 | Watch |
| 7 | AVAX/USD | 6.602 | 75.13 | -0.12% | 2.28x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 8 | ZEC/USD | 786.14 | 72.71 | +0.17% | 0.22x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 9 | XBT/USD ⭐ | 60009.9 | 70.28 | +0.16% | 1.02x | STRONG 70/100 | HIGH 62/100 | Watch |
| 10 | USELESS/USD | 0.08203 | 69.28 | -0.13% | 0.12x | WEAK 35/100 | VERY_HIGH 82/100 | Watch |
| 11 | SOL/USD | 70.6 | 69.18 | +0.00% | 0.56x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 12 | TAO/USD | 186.043 | 67.80 | -0.08% | 0.43x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 1.9594 | 85.13 | +0.75% | 1.75x | 12641 | STRONG 88/100 | HIGH 67/100 | Consider small entry |
| 2 | WINGS/USD | 0.001836 | 82.13 | +0.88% | 1.91x | 9670 | STRONG 86/100 | HIGH 60/100 | Consider small entry |
| 3 | QNT/USD ⭐ | 143.43 | 82.11 | +0.24% | 2.00x | 11174 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 4 | XBT/USD ⭐ | 60022.2 | 77.32 | +0.16% | 1.02x | 239804 | STRONG 74/100 | HIGH 62/100 | Watch |

**Same-run overlap:** QNT/USD, PEARL/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
