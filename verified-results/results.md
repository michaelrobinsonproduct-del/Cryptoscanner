# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T19:12:14.003609+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46054691820
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c9afe87d42d23a990808a7958c128f3c26e6f668 (atomic ledger/results publication)
**Ledger generation:** 2048 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 745.67 | 99.651 | 98.725 | +9.39% | +0.01% | 1.09x | 2.5 | 2026-11-27T19:12:06.936946+00:00 | Not calibrated | STRONG 75/100 | HIGH 62/100 | Watch | WATCH |
| 2 | UNI/USD | 4.8163 | 90.374 | 75.395 | +3.57% | -0.00% | 2.78x | 4.2 | 2026-11-27T19:12:06.936946+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XDG/USD | 0.0578194 | 89.010 | 72.846 | +2.56% | +0.23% | 2.65x | 0.2 | 2026-11-27T19:12:06.936946+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | HYPE/USD | 63.77 | 87.443 | 70.870 | +2.49% | +0.31% | 2.65x | 3.1 | 2026-11-27T19:12:06.936946+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | NIGHT/USD | 0.04999 | 70.713 | 74.954 | +3.14% | +0.30% | 0.43x | 4.0 | 2026-11-27T19:12:06.936946+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | PEPE/USD | 3.532e-06 | 69.177 | 55.138 | +1.55% | +0.45% | 2.18x | 2.8 | 2026-11-27T19:12:06.936946+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SOL/USD | 71.96 | 65.816 | 64.370 | +1.44% | +0.04% | 1.12x | 1.4 | 2026-11-27T19:12:06.936946+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 8 | PAXG/USD | 3631.51 | 65.442 | 57.352 | +2.10% | -0.01% | 1.82x | 0.0 | 2026-11-27T19:12:06.936946+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 9 | LINK/USD | 9.38609 | 63.148 | 62.218 | +1.27% | -0.06% | 1.12x | 3.3 | 2026-11-27T19:12:06.936946+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 10 | FET/USD | 0.1265 | 62.899 | 60.772 | +5.07% | +0.48% | 0.97x | 23.7 | 2026-11-27T19:12:06.936946+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 11 | XRP/USD | 0.95 | 62.112 | 60.331 | +0.77% | +0.15% | 1.10x | 0.1 | 2026-11-27T19:12:06.936946+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 12 | LTC/USD | 43.85 | 60.104 | 54.478 | +0.25% | -0.05% | 1.59x | 4.6 | 2026-11-27T19:12:06.936946+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.725 | 745.67 | +0.01% | 1.09x |
| 2 | UNI/USD | 75.395 | 4.8163 | -0.00% | 2.78x |
| 3 | NIGHT/USD | 74.954 | 0.04999 | +0.30% | 0.43x |
| 4 | XDG/USD | 72.846 | 0.0578194 | +0.23% | 2.65x |
| 5 | HYPE/USD | 70.870 | 63.77 | +0.31% | 2.65x |
| 6 | SOL/USD | 64.370 | 71.96 | +0.04% | 1.12x |
| 7 | LINK/USD | 62.218 | 9.38609 | -0.06% | 1.12x |
| 8 | FET/USD | 60.772 | 0.1265 | +0.48% | 0.97x |
| 9 | XRP/USD | 60.331 | 0.95 | +0.15% | 1.10x |
| 10 | PAXG/USD | 57.352 | 3631.51 | -0.01% | 1.82x |
| 11 | PEPE/USD | 55.138 | 3.532e-06 | +0.45% | 2.18x |
| 12 | LTC/USD | 54.478 | 43.85 | -0.05% | 1.59x |

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

- Persisted scans: 2048; predictions: 18278; observations: 1240149.
- Matured sampled outcomes across 1/6/24/48h: 41195; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
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

**Writer:** 46054691820 · **Generation:** 2048 · **Legacy run:** 46054691820
**Main quote time:** 2026-11-27T19:12:14.003609+00:00 · **Legacy report time:** 2026-11-27T19:12:52.268316+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 745.67 | 99.65 | +0.01% | 1.09x | STRONG 75/100 | HIGH 62/100 | Watch |
| 2 | UNI/USD | 4.8163 | 90.37 | -0.00% | 2.78x | STRONG 75/100 | HIGH 61/100 | Watch |
| 3 | XDG/USD ⭐ | 0.0578194 | 89.01 | +0.23% | 2.65x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | HYPE/USD ⭐ | 63.77 | 87.44 | +0.31% | 2.65x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | NIGHT/USD | 0.04999 | 70.71 | +0.30% | 0.43x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 6 | PEPE/USD | 3.532e-06 | 69.18 | +0.45% | 2.18x | STRONG 90/100 | HIGH 55/100 | Watch |
| 7 | SOL/USD | 71.96 | 65.82 | +0.04% | 1.12x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 8 | PAXG/USD | 3631.51 | 65.44 | -0.01% | 1.82x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 9 | LINK/USD | 9.38609 | 63.15 | -0.06% | 1.12x | WEAK 42/100 | HIGH 68/100 | Watch |
| 10 | FET/USD | 0.1265 | 62.90 | +0.48% | 0.97x | MODERATE 51/100 | VERY_HIGH 74/100 | Watch |
| 11 | XRP/USD | 0.95 | 62.11 | +0.15% | 1.10x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 12 | LTC/USD | 43.85 | 60.10 | -0.05% | 1.59x | MODERATE 50/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XDG/USD ⭐ | 0.0578194 | 89.23 | +0.23% | 2.65x | 13135 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HYPE/USD ⭐ | 63.77 | 86.29 | +0.31% | 2.65x | 20893 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ENA/USD | 0.1038 | 75.93 | +0.39% | 2.71x | 2658 | STRONG 93/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XDG/USD, HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
