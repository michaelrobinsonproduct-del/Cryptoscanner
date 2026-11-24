# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T14:11:50.865750+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45410982591
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 939fa6a701cbd7d00a1239821faa7eccddeea6da (atomic ledger/results publication)
**Ledger generation:** 1584 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 496.96 | 81.974 | 66.226 | +2.25% | +0.15% | 2.62x | 9.1 | 2026-11-24T14:11:48.032909+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 2 | LUNA/USD | 4.589e-05 | 81.636 | 64.231 | +5.57% | +0.48% | 7.48x | 13.1 | 2026-11-24T14:11:48.032909+00:00 | Not calibrated | STRONG 91/100 | HIGH 66/100 | Consider small entry | WATCH |
| 3 | VVV/USD | 25.573 | 76.782 | 82.713 | +4.60% | +0.14% | 0.34x | 9.0 | 2026-11-24T14:11:48.032909+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | 2Z/USD | 0.01622 | 59.333 | 50.090 | +3.64% | +1.12% | 1.36x | 12.3 | 2026-11-24T14:11:48.032909+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | GBP/USD | 1.30961 | 56.622 | 58.034 | +0.49% | +0.03% | 0.84x | 0.8 | 2026-11-24T14:11:48.032909+00:00 | Not calibrated | MODERATE 48/100 | HIGH 62/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.04831 | 53.556 | 42.388 | +0.33% | -0.27% | 2.25x | 12.4 | 2026-11-24T14:11:48.032909+00:00 | Not calibrated | MODERATE 52/100 | HIGH 67/100 | Watch | WATCH |
| 7 | Q/USD | 0.026888 | 34.632 | 38.377 | +3.94% | +0.79% | 0.23x | 39.8 | 2026-11-24T14:11:48.032909+00:00 | Not calibrated | WEAK 32/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 82.713 | 25.573 | +0.14% | 0.34x |
| 2 | XMR/USD | 66.226 | 496.96 | +0.15% | 2.62x |
| 3 | LUNA/USD | 64.231 | 4.589e-05 | +0.48% | 7.48x |
| 4 | GBP/USD | 58.034 | 1.30961 | +0.03% | 0.84x |
| 5 | 2Z/USD | 50.090 | 0.01622 | +1.12% | 1.36x |
| 6 | NIGHT/USD | 42.388 | 0.04831 | -0.27% | 2.25x |
| 7 | Q/USD | 38.377 | 0.026888 | +0.79% | 0.23x |

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

- Persisted scans: 1584; predictions: 13660; observations: 959753.
- Matured sampled outcomes across 1/6/24/48h: 26812; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45410982591 · **Generation:** 1584 · **Legacy run:** 45410982591
**Main quote time:** 2026-11-24T14:11:50.865750+00:00 · **Legacy report time:** 2026-11-24T14:12:41.700654+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 496.96 | 81.97 | +0.15% | 2.62x | STRONG 96/100 | HIGH 55/100 | Watch |
| 2 | LUNA/USD ⭐ | 4.589e-05 | 81.64 | +0.48% | 7.48x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 3 | VVV/USD | 25.573 | 76.78 | +0.14% | 0.34x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 4 | 2Z/USD ⭐ | 0.01622 | 59.33 | +1.12% | 1.36x | STRONG 80/100 | VERY_HIGH 73/100 | Watch |
| 5 | GBP/USD | 1.30961 | 56.62 | +0.03% | 0.84x | MODERATE 48/100 | HIGH 62/100 | Watch |
| 6 | NIGHT/USD | 0.04831 | 53.56 | -0.27% | 2.25x | MODERATE 52/100 | HIGH 67/100 | Watch |
| 7 | Q/USD | 0.026888 | 34.63 | +0.79% | 0.23x | WEAK 32/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.589e-05 | 72.89 | +0.48% | 7.48x | 1724 | STRONG 91/100 | VERY_HIGH 72/100 | Watch |
| 2 | XMR/USD ⭐ | 497.48 | 72.21 | +0.15% | 2.62x | 10386 | STRONG 91/100 | HIGH 55/100 | Watch |
| 3 | 2Z/USD ⭐ | 0.01626 | 65.80 | +1.12% | 1.36x | 1327 | STRONG 88/100 | HIGH 67/100 | Watch |

**Same-run overlap:** XMR/USD, LUNA/USD, 2Z/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
