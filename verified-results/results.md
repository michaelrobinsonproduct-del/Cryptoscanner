# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T21:46:50.889072+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44953179441
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** cdcba71cd48765b318288cae3e5fa43527a44381 (atomic ledger/results publication)
**Ledger generation:** 1190 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UNI/USD | 4.7204 | 108.395 | 92.769 | +5.67% | +0.13% | 3.43x | 3.8 | 2026-11-21T21:46:42.085002+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | XMR/USD | 492.26 | 105.981 | 97.460 | +7.88% | +0.53% | 1.59x | 5.1 | 2026-11-21T21:46:42.085002+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ZEC/USD | 792.55 | 101.237 | 85.921 | +4.57% | +0.06% | 3.89x | 2.1 | 2026-11-21T21:46:42.085002+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 4 | PEARL/USD | 1.99 | 84.940 | 89.216 | +8.84% | -0.59% | 0.87x | 0.5 | 2026-11-21T21:46:42.085002+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04491 | 84.765 | 90.180 | +6.37% | +0.31% | 0.30x | 6.7 | 2026-11-21T21:46:42.085002+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | ETH/USD | 1684.6 | 80.713 | 83.190 | +4.03% | -0.02% | 0.76x | 0.1 | 2026-11-21T21:46:42.085002+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 7 | SOL/USD | 70.34 | 79.921 | 70.895 | +2.37% | -0.16% | 1.98x | 1.4 | 2026-11-21T21:46:42.085002+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XBT/USD | 60313.1 | 72.954 | 72.927 | +2.56% | -0.04% | 1.03x | 0.0 | 2026-11-21T21:46:42.085002+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 9 | XRP/USD | 0.92851 | 69.180 | 69.768 | +2.18% | -0.09% | 0.99x | 1.0 | 2026-11-21T21:46:42.085002+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 10 | XDG/USD | 0.055084 | 66.856 | 65.271 | +1.49% | -0.16% | 1.24x | 0.3 | 2026-11-21T21:46:42.085002+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 11 | TAO/USD | 185.7178 | 63.968 | 71.898 | +2.89% | +0.14% | 0.14x | 6.6 | 2026-11-21T21:46:42.085002+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | BNB/USD | 548.11 | 59.715 | 55.451 | +1.57% | -0.13% | 1.49x | 1.5 | 2026-11-21T21:46:42.085002+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 97.460 | 492.26 | +0.53% | 1.59x |
| 2 | UNI/USD | 92.769 | 4.7204 | +0.13% | 3.43x |
| 3 | NIGHT/USD | 90.180 | 0.04491 | +0.31% | 0.30x |
| 4 | PEARL/USD | 89.216 | 1.99 | -0.59% | 0.87x |
| 5 | ZEC/USD | 85.921 | 792.55 | +0.06% | 3.89x |
| 6 | ETH/USD | 83.190 | 1684.6 | -0.02% | 0.76x |
| 7 | XBT/USD | 72.927 | 60313.1 | -0.04% | 1.03x |
| 8 | TAO/USD | 71.898 | 185.7178 | +0.14% | 0.14x |
| 9 | SOL/USD | 70.895 | 70.34 | -0.16% | 1.98x |
| 10 | XRP/USD | 69.768 | 0.92851 | -0.09% | 0.99x |
| 11 | XDG/USD | 65.271 | 0.055084 | -0.16% | 1.24x |
| 12 | BNB/USD | 55.451 | 548.11 | -0.13% | 1.49x |

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

- Persisted scans: 1190; predictions: 9589; observations: 719879.
- Matured sampled outcomes across 1/6/24/48h: 12820; gap abstentions: 21479. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44953179441 · **Generation:** 1190 · **Legacy run:** 44953179441
**Main quote time:** 2026-11-21T21:46:50.889072+00:00 · **Legacy report time:** 2026-11-21T21:47:34.757080+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.7204 | 108.40 | +0.13% | 3.43x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | XMR/USD ⭐ | 492.26 | 105.98 | +0.53% | 1.59x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ZEC/USD ⭐ | 792.55 | 101.24 | +0.06% | 3.89x | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | PEARL/USD | 1.99 | 84.94 | -0.59% | 0.87x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 5 | NIGHT/USD | 0.04491 | 84.76 | +0.31% | 0.30x | STRONG 72/100 | VERY_HIGH 70/100 | Watch |
| 6 | ETH/USD | 1684.6 | 80.71 | -0.02% | 0.76x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 7 | SOL/USD | 70.34 | 79.92 | -0.16% | 1.98x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 8 | XBT/USD | 60313.1 | 72.95 | -0.04% | 1.03x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 9 | XRP/USD | 0.92851 | 69.18 | -0.09% | 0.99x | WEAK 40/100 | HIGH 68/100 | Watch |
| 10 | XDG/USD | 0.055084 | 66.86 | -0.16% | 1.24x | WEAK 43/100 | HIGH 68/100 | Watch |
| 11 | TAO/USD | 185.7178 | 63.97 | +0.14% | 0.14x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 12 | BNB/USD | 548.11 | 59.72 | -0.13% | 1.49x | MODERATE 50/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 4.7204 | 100.00 | +0.13% | 3.43x | 10848 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD ⭐ | 792.56 | 100.00 | +0.06% | 3.89x | 40415 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | XMR/USD ⭐ | 491.97 | 88.94 | +0.53% | 1.59x | 12028 | STRONG 94/100 | HIGH 61/100 | Consider small entry |
| 4 | PIEVERSE/USD | 3.4313 | 75.16 | +0.50% | 1.02x | 2636 | STRONG 73/100 | HIGH 67/100 | Watch |

**Same-run overlap:** UNI/USD, XMR/USD, ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
