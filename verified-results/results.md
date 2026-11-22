# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T22:04:38.318896+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45075340872
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 3316db37129327dcbc34d419042d0a06090e5432 (atomic ledger/results publication)
**Ledger generation:** 1342 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.37436 | 88.934 | 84.447 | +11.68% | +0.18% | 1.36x | 9.1 | 2026-11-22T22:04:29.987875+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04912 | 84.504 | 88.458 | +10.93% | +0.20% | 0.50x | 10.2 | 2026-11-22T22:04:29.987875+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | PUMP/USD | 0.002568 | 83.374 | 80.805 | +9.56% | +0.08% | 1.22x | 11.7 | 2026-11-22T22:04:29.987875+00:00 | Not calibrated | MODERATE 62/100 | HIGH 68/100 | Watch | WATCH |
| 4 | ZEC/USD | 794.52 | 73.253 | 67.692 | +2.10% | +0.42% | 1.34x | 4.0 | 2026-11-22T22:04:29.987875+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 5 | VVV/USD | 25.964 | 72.860 | 81.251 | +4.27% | -0.60% | 0.46x | 7.3 | 2026-11-22T22:04:29.987875+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | NEAR/USD | 2.9912 | 71.837 | 78.433 | +3.63% | -0.30% | 0.49x | 4.0 | 2026-11-22T22:04:29.987875+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | ETH/USD | 1712.34 | 65.064 | 67.479 | +1.79% | -0.30% | 0.91x | 0.1 | 2026-11-22T22:04:29.987875+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 8 | HYPE/USD | 62.51 | 63.194 | 67.916 | +2.07% | -0.16% | 0.61x | 3.2 | 2026-11-22T22:04:29.987875+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | XBT/USD | 60768.1 | 58.690 | 62.892 | +1.13% | -0.19% | 0.67x | 0.0 | 2026-11-22T22:04:29.987875+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | BNB/USD | 555.88 | 55.918 | 47.404 | +1.55% | -0.14% | 1.92x | 1.4 | 2026-11-22T22:04:29.987875+00:00 | Not calibrated | MODERATE 48/100 | HIGH 61/100 | Watch | WATCH |
| 11 | SUI/USD | 0.6545 | 54.246 | 61.924 | +1.11% | -0.15% | 0.31x | 1.5 | 2026-11-22T22:04:29.987875+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | DOT/USD | 0.6592 | 52.746 | 39.031 | +0.95% | -0.26% | 7.35x | 1.5 | 2026-11-22T22:04:29.987875+00:00 | Not calibrated | MODERATE 56/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 88.458 | 0.04912 | +0.20% | 0.50x |
| 2 | DRV/USD | 84.447 | 0.37436 | +0.18% | 1.36x |
| 3 | VVV/USD | 81.251 | 25.964 | -0.60% | 0.46x |
| 4 | PUMP/USD | 80.805 | 0.002568 | +0.08% | 1.22x |
| 5 | NEAR/USD | 78.433 | 2.9912 | -0.30% | 0.49x |
| 6 | HYPE/USD | 67.916 | 62.51 | -0.16% | 0.61x |
| 7 | ZEC/USD | 67.692 | 794.52 | +0.42% | 1.34x |
| 8 | ETH/USD | 67.479 | 1712.34 | -0.30% | 0.91x |
| 9 | XBT/USD | 62.892 | 60768.1 | -0.19% | 0.67x |
| 10 | SUI/USD | 61.924 | 0.6545 | -0.15% | 0.31x |
| 11 | BNB/USD | 47.404 | 555.88 | -0.14% | 1.92x |
| 12 | DOT/USD | 39.031 | 0.6592 | -0.26% | 7.35x |

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

- Persisted scans: 1342; predictions: 11023; observations: 812386.
- Matured sampled outcomes across 1/6/24/48h: 16881; gap abstentions: 22369. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
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

**Writer:** 45075340872 · **Generation:** 1342 · **Legacy run:** 45075340872
**Main quote time:** 2026-11-22T22:04:38.318896+00:00 · **Legacy report time:** 2026-11-22T22:05:22.569289+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.37436 | 88.93 | +0.18% | 1.36x | STRONG 79/100 | HIGH 55/100 | Watch |
| 2 | NIGHT/USD | 0.04912 | 84.50 | +0.20% | 0.50x | MODERATE 67/100 | VERY_HIGH 76/100 | Watch |
| 3 | PUMP/USD | 0.002568 | 83.37 | +0.08% | 1.22x | MODERATE 62/100 | HIGH 68/100 | Watch |
| 4 | ZEC/USD ⭐ | 794.52 | 73.25 | +0.42% | 1.34x | STRONG 92/100 | HIGH 55/100 | Watch |
| 5 | VVV/USD | 25.964 | 72.86 | -0.60% | 0.46x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 6 | NEAR/USD | 2.9912 | 71.84 | -0.30% | 0.49x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 7 | ETH/USD | 1712.34 | 65.06 | -0.30% | 0.91x | WEAK 38/100 | HIGH 68/100 | Watch |
| 8 | HYPE/USD | 62.51 | 63.19 | -0.16% | 0.61x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 9 | XBT/USD | 60768.1 | 58.69 | -0.19% | 0.67x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | BNB/USD | 555.88 | 55.92 | -0.14% | 1.92x | MODERATE 48/100 | HIGH 61/100 | Watch |
| 11 | SUI/USD | 0.6545 | 54.25 | -0.15% | 0.31x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | DOT/USD | 0.6592 | 52.75 | -0.26% | 7.35x | MODERATE 56/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 793.76 | 74.79 | +0.07% | 1.33x | 18697 | STRONG 82/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
