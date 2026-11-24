# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T06:16:55.432209+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45339037580
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 0e238d9ab4cab8663565a4245fd801ba09255de2 (atomic ledger/results publication)
**Ledger generation:** 1536 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEPE/USD | 3.561e-06 | 87.330 | 76.230 | +4.06% | -0.78% | 2.75x | 5.6 | 2026-11-24T06:16:49.225333+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 2 | VVV/USD | 25.382 | 83.411 | 77.604 | +3.82% | +0.94% | 1.11x | 8.3 | 2026-11-24T06:16:49.225333+00:00 | Not calibrated | STRONG 77/100 | HIGH 62/100 | Watch | WATCH |
| 3 | BAT/USD | 0.08047 | 73.280 | 59.639 | +4.28% | -0.27% | 7.88x | 5.0 | 2026-11-24T06:16:49.225333+00:00 | Not calibrated | MODERATE 67/100 | HIGH 66/100 | Watch | WATCH |
| 4 | ICNT/USD | 0.3316 | 66.150 | 69.835 | +7.28% | +0.52% | 0.37x | 15.1 | 2026-11-24T06:16:49.225333+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04941 | 65.589 | 64.064 | +2.62% | +0.67% | 0.82x | 8.1 | 2026-11-24T06:16:49.225333+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.0362 | 65.085 | 66.099 | +1.84% | -0.50% | 1.15x | 3.6 | 2026-11-24T06:16:49.225333+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 7 | XRP/USD | 0.95109 | 56.805 | 63.666 | +1.25% | -0.37% | 0.50x | 0.1 | 2026-11-24T06:16:49.225333+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | LINK/USD | 9.10121 | 54.126 | 60.181 | +1.07% | -0.19% | 0.49x | 4.6 | 2026-11-24T06:16:49.225333+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | XMR/USD | 494.24 | 53.875 | 61.479 | +1.69% | -0.37% | 0.42x | 10.7 | 2026-11-24T06:16:49.225333+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 10 | LTC/USD | 41.78 | 53.749 | 59.886 | +0.87% | -0.26% | 0.52x | 2.4 | 2026-11-24T06:16:49.225333+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | XDG/USD | 0.0565877 | 51.358 | 58.151 | +0.50% | -0.22% | 0.43x | 0.7 | 2026-11-24T06:16:49.225333+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | HYPE/USD | 64.12 | 49.709 | 59.499 | +0.75% | -0.23% | 0.14x | 1.6 | 2026-11-24T06:16:49.225333+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 77.604 | 25.382 | +0.94% | 1.11x |
| 2 | PEPE/USD | 76.230 | 3.561e-06 | -0.78% | 2.75x |
| 3 | ICNT/USD | 69.835 | 0.3316 | +0.52% | 0.37x |
| 4 | NEAR/USD | 66.099 | 3.0362 | -0.50% | 1.15x |
| 5 | NIGHT/USD | 64.064 | 0.04941 | +0.67% | 0.82x |
| 6 | XRP/USD | 63.666 | 0.95109 | -0.37% | 0.50x |
| 7 | XMR/USD | 61.479 | 494.24 | -0.37% | 0.42x |
| 8 | LINK/USD | 60.181 | 9.10121 | -0.19% | 0.49x |
| 9 | LTC/USD | 59.886 | 41.78 | -0.26% | 0.52x |
| 10 | BAT/USD | 59.639 | 0.08047 | -0.27% | 7.88x |
| 11 | HYPE/USD | 59.499 | 64.12 | -0.23% | 0.14x |
| 12 | XDG/USD | 58.151 | 0.0565877 | -0.22% | 0.43x |

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

- Persisted scans: 1536; predictions: 13165; observations: 930522.
- Matured sampled outcomes across 1/6/24/48h: 24704; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 137 (sampled only; not a success-rate estimate).
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

**Writer:** 45339037580 · **Generation:** 1536 · **Legacy run:** 45339037580
**Main quote time:** 2026-11-24T06:16:55.432209+00:00 · **Legacy report time:** 2026-11-24T06:18:04.639361+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 3.561e-06 | 87.33 | -0.78% | 2.75x | STRONG 74/100 | HIGH 61/100 | Watch |
| 2 | VVV/USD ⭐ | 25.382 | 83.41 | +0.94% | 1.11x | STRONG 87/100 | HIGH 62/100 | Watch |
| 3 | BAT/USD | 0.08047 | 73.28 | -0.27% | 7.88x | MODERATE 67/100 | HIGH 66/100 | Watch |
| 4 | ICNT/USD | 0.3316 | 66.15 | +0.52% | 0.37x | MODERATE 58/100 | VERY_HIGH 81/100 | Watch |
| 5 | NIGHT/USD | 0.04941 | 65.59 | +0.67% | 0.82x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 6 | NEAR/USD | 3.0362 | 65.09 | -0.50% | 1.15x | WEAK 43/100 | HIGH 68/100 | Watch |
| 7 | XRP/USD | 0.95109 | 56.80 | -0.37% | 0.50x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | LINK/USD | 9.10121 | 54.13 | -0.19% | 0.49x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | XMR/USD | 494.24 | 53.88 | -0.37% | 0.42x | WEAK 27/100 | VERY_HIGH 82/100 | Do nothing |
| 10 | LTC/USD | 41.78 | 53.75 | -0.26% | 0.52x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | XDG/USD | 0.0565877 | 51.36 | -0.22% | 0.43x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | HYPE/USD | 64.12 | 49.71 | -0.23% | 0.14x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.326 | 83.36 | +0.94% | 1.11x | 12413 | STRONG 87/100 | HIGH 62/100 | Watch |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
