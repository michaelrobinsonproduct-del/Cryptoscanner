# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T06:51:01.942577+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44995458578
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 4d4e4309117d0b5802af0b3ef5023e802fb8a053 (atomic ledger/results publication)
**Ledger generation:** 1247 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 787.17 | 57.095 | 62.207 | +1.16% | +0.53% | 0.22x | 1.8 | 2026-11-22T06:50:57.095545+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04444 | 46.087 | 43.629 | +0.36% | -0.07% | 1.28x | 6.8 | 2026-11-22T06:50:57.095545+00:00 | Not calibrated | WEAK 33/100 | HIGH 61/100 | Do nothing | WATCH |
| 3 | ICNT/USD | 0.3502 | 45.523 | 30.600 | +0.81% | +1.42% | 1.78x | 17.2 | 2026-11-22T06:50:57.095545+00:00 | Not calibrated | MODERATE 63/100 | HIGH 66/100 | Watch | WATCH |
| 4 | SPX/USD | 0.2812 | 45.029 | 26.094 | +0.64% | +0.79% | 3.78x | 21.4 | 2026-11-22T06:50:57.095545+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | PEARL/USD | 1.9751 | 42.785 | 40.700 | +1.38% | +0.17% | 1.12x | 22.3 | 2026-11-22T06:50:57.095545+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 6 | TRUMP/USD | 0.891 | 34.781 | 32.752 | +0.56% | -0.22% | 1.31x | 11.2 | 2026-11-22T06:50:57.095545+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 72/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 62.207 | 787.17 | +0.53% | 0.22x |
| 2 | NIGHT/USD | 43.629 | 0.04444 | -0.07% | 1.28x |
| 3 | PEARL/USD | 40.700 | 1.9751 | +0.17% | 1.12x |
| 4 | TRUMP/USD | 32.752 | 0.891 | -0.22% | 1.31x |
| 5 | ICNT/USD | 30.600 | 0.3502 | +1.42% | 1.78x |
| 6 | SPX/USD | 26.094 | 0.2812 | +0.79% | 3.78x |

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

- Persisted scans: 1247; predictions: 9949; observations: 754534.
- Matured sampled outcomes across 1/6/24/48h: 14260; gap abstentions: 22010. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 55 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44995458578 · **Generation:** 1247 · **Legacy run:** 44995458578
**Main quote time:** 2026-11-22T06:51:01.942577+00:00 · **Legacy report time:** 2026-11-22T06:51:47.779603+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 787.17 | 57.09 | +0.53% | 0.22x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 2 | NIGHT/USD | 0.04444 | 46.09 | -0.07% | 1.28x | WEAK 33/100 | HIGH 61/100 | Do nothing |
| 3 | ICNT/USD ⭐ | 0.3502 | 45.52 | +1.42% | 1.78x | STRONG 73/100 | HIGH 66/100 | Watch |
| 4 | SPX/USD | 0.2812 | 45.03 | +0.79% | 3.78x | MODERATE 68/100 | VERY_HIGH 72/100 | Watch |
| 5 | PEARL/USD ⭐ | 1.9751 | 42.78 | +0.17% | 1.12x | MODERATE 46/100 | VERY_HIGH 74/100 | Watch |
| 6 | TRUMP/USD | 0.891 | 34.78 | -0.22% | 1.31x | WEAK 32/100 | VERY_HIGH 72/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AUD/USD | 0.66123 | 49.07 | +0.10% | 2.81x | 3629 | STRONG 70/100 | HIGH 55/100 | Watch |
| 2 | PEARL/USD ⭐ | 1.9755 | 47.11 | +0.17% | 1.12x | 8622 | MODERATE 49/100 | VERY_HIGH 74/100 | Watch |
| 3 | ICNT/USD ⭐ | 0.3486 | 35.61 | +1.42% | 1.78x | 3226 | MODERATE 63/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** ICNT/USD, PEARL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
