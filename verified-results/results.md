# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T11:44:49.273104+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44076697545
**Source SHA:** 51cf90dde69583431478c570c3fd0bfd47a88250
**Previous ledger commit:** 3c992e5e44323c446e4e732a943f892ec8cfd949 (atomic ledger/results publication)
**Ledger generation:** 453 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INJ/USD | 7.53 | 115.033 | 91.461 | +9.15% | +1.74% | 2.49x | 4.0 | 2026-11-17T11:44:42.343713+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 945.12 | 103.908 | 82.242 | +4.57% | +1.33% | 7.58x | 9.5 | 2026-11-17T11:44:42.343713+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | NEAR/USD | 3.2762 | 94.082 | 80.788 | +3.75% | +1.17% | 1.75x | 0.9 | 2026-11-17T11:44:42.343713+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | SOL/USD | 73.34 | 91.388 | 72.131 | +2.54% | +0.85% | 2.73x | 1.4 | 2026-11-17T11:44:42.343713+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | VVV/USD | 21.587 | 90.967 | 87.516 | +7.14% | +1.47% | 0.61x | 4.6 | 2026-11-17T11:44:42.343713+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | SUI/USD | 0.7338 | 84.122 | 66.442 | +2.00% | +0.54% | 2.66x | 1.4 | 2026-11-17T11:44:42.343713+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | JUP/USD | 0.2601 | 84.009 | 74.401 | +8.12% | +1.84% | 1.04x | 10.7 | 2026-11-17T11:44:42.343713+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | XMR/USD | 514.1 | 83.681 | 75.343 | +4.16% | +0.35% | 1.66x | 17.5 | 2026-11-17T11:44:42.343713+00:00 | Not calibrated | STRONG 82/100 | HIGH 61/100 | Consider small entry | WATCH |
| 9 | UNI/USD | 5.3402 | 81.037 | 65.977 | +3.47% | +0.98% | 2.02x | 5.2 | 2026-11-17T11:44:42.343713+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 10 | BAT/USD | 0.10017 | 75.768 | 68.889 | +5.75% | +0.32% | 1.53x | 5.0 | 2026-11-17T11:44:42.343713+00:00 | Not calibrated | STRONG 83/100 | HIGH 67/100 | Consider small entry | WATCH |
| 11 | XDG/USD | 0.059273 | 71.608 | 59.041 | +0.66% | +0.51% | 2.00x | 1.1 | 2026-11-17T11:44:42.343713+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 12 | XRP/USD | 0.96935 | 70.871 | 65.129 | +1.53% | +0.48% | 1.34x | 1.1 | 2026-11-17T11:44:42.343713+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 91.461 | 7.53 | +1.74% | 2.49x |
| 2 | VVV/USD | 87.516 | 21.587 | +1.47% | 0.61x |
| 3 | ZEC/USD | 82.242 | 945.12 | +1.33% | 7.58x |
| 4 | NEAR/USD | 80.788 | 3.2762 | +1.17% | 1.75x |
| 5 | XMR/USD | 75.343 | 514.1 | +0.35% | 1.66x |
| 6 | JUP/USD | 74.401 | 0.2601 | +1.84% | 1.04x |
| 7 | SOL/USD | 72.131 | 73.34 | +0.85% | 2.73x |
| 8 | BAT/USD | 68.889 | 0.10017 | +0.32% | 1.53x |
| 9 | SUI/USD | 66.442 | 0.7338 | +0.54% | 2.66x |
| 10 | UNI/USD | 65.977 | 5.3402 | +0.98% | 2.02x |
| 11 | XRP/USD | 65.129 | 0.96935 | +0.48% | 1.34x |
| 12 | XDG/USD | 59.041 | 0.059273 | +0.51% | 2.00x |

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

- Persisted scans: 453; predictions: 3917; observations: 272886.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12143. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44076697545 · **Generation:** 453 · **Legacy run:** 44076697545
**Main quote time:** 2026-11-17T11:44:49.273104+00:00 · **Legacy report time:** 2026-11-17T11:45:00.284241+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 7.53 | 115.03 | +1.74% | 2.49x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 945.12 | 103.91 | +1.33% | 7.58x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD ⭐ | 3.2762 | 94.08 | +1.17% | 1.75x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SOL/USD ⭐ | 73.34 | 91.39 | +0.85% | 2.73x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | VVV/USD | 21.587 | 90.97 | +1.47% | 0.61x | STRONG 75/100 | VERY_HIGH 70/100 | Watch |
| 6 | SUI/USD ⭐ | 0.7338 | 84.12 | +0.54% | 2.66x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | JUP/USD ⭐ | 0.2601 | 84.01 | +1.84% | 1.04x | STRONG 82/100 | VERY_HIGH 73/100 | Watch |
| 8 | XMR/USD ⭐ | 514.1 | 83.68 | +0.35% | 1.66x | STRONG 92/100 | HIGH 61/100 | Consider small entry |
| 9 | UNI/USD ⭐ | 5.3402 | 81.04 | +0.98% | 2.02x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 10 | BAT/USD ⭐ | 0.10017 | 75.77 | +0.32% | 1.53x | STRONG 93/100 | HIGH 67/100 | Consider small entry |
| 11 | XDG/USD | 0.059273 | 71.61 | +0.51% | 2.00x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 12 | XRP/USD ⭐ | 0.96935 | 70.87 | +0.48% | 1.34x | STRONG 90/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.2773 | 100.00 | +1.17% | 1.75x | 13362 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | INJ/USD ⭐ | 7.522 | 99.26 | +1.74% | 2.49x | 7997 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ZEC/USD ⭐ | 947.89 | 97.00 | +1.33% | 7.58x | 29150 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 4 | SOL/USD ⭐ | 73.32 | 88.94 | +0.85% | 2.73x | 35595 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | XMR/USD ⭐ | 514.73 | 88.69 | +0.35% | 1.66x | 11522 | STRONG 94/100 | HIGH 61/100 | Consider small entry |
| 6 | ZAMA/USD | 0.05947 | 88.53 | +1.18% | 6.82x | 3192 | STRONG 99/100 | HIGH 60/100 | Consider small entry |
| 7 | AKE/USD | 0.0108919 | 81.78 | +1.91% | 1.83x | 6149 | STRONG 71/100 | VERY_HIGH 82/100 | Watch |
| 8 | UNI/USD ⭐ | 5.3402 | 81.49 | +0.98% | 2.02x | 6262 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | JUP/USD ⭐ | 0.2601 | 78.54 | +1.84% | 1.04x | 3203 | STRONG 79/100 | VERY_HIGH 73/100 | Watch |
| 10 | SUI/USD ⭐ | 0.7341 | 78.21 | +0.54% | 2.66x | 6755 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 11 | BAT/USD ⭐ | 0.10017 | 76.75 | +0.32% | 1.53x | 2643 | STRONG 93/100 | HIGH 67/100 | Consider small entry |
| 12 | XRP/USD ⭐ | 0.96938 | 72.94 | +0.48% | 1.34x | 30909 | STRONG 91/100 | HIGH 55/100 | Watch |

**Same-run overlap:** INJ/USD, ZEC/USD, NEAR/USD, SOL/USD, SUI/USD, JUP/USD, XMR/USD, UNI/USD, BAT/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
