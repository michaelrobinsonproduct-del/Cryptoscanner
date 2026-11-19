# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T01:45:31.110729+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44439181451
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 72c99e8bc06017d32878ce131b731cf14b07b279 (atomic ledger/results publication)
**Ledger generation:** 722 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.021707 | 72.911 | 62.232 | +5.35% | +2.68% | 0.73x | 13.4 | 2026-11-19T01:45:23.291122+00:00 | Not calibrated | MODERATE 61/100 | EXTREME 88/100 | Do nothing | WATCH |
| 2 | CRV/USD | 0.19938 | 48.071 | 30.905 | +0.26% | +0.43% | 3.10x | 13.1 | 2026-11-19T01:45:23.291122+00:00 | Not calibrated | STRONG 74/100 | HIGH 66/100 | Watch | WATCH |
| 3 | MEGA/USD | 0.05753 | 45.746 | 42.504 | +2.73% | -0.21% | 1.43x | 15.7 | 2026-11-19T01:45:23.291122+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | DRV/USD | 0.26621 | 45.445 | 31.102 | +0.57% | -0.13% | 4.41x | 12.4 | 2026-11-19T01:45:23.291122+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | PYTH/USD | 0.05359 | 38.543 | 33.407 | +1.57% | +0.53% | 1.25x | 18.7 | 2026-11-19T01:45:23.291122+00:00 | Not calibrated | MODERATE 49/100 | HIGH 66/100 | Watch | WATCH |
| 6 | PAXG/USD | 3743.91 | 37.967 | 43.896 | +0.34% | +0.21% | 0.30x | 1.7 | 2026-11-19T01:45:23.291122+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | TRX/USD | 0.310314 | 37.240 | 40.321 | +0.33% | +0.12% | 0.63x | 1.1 | 2026-11-19T01:45:23.291122+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | CC/USD | 0.08215 | 33.542 | 36.431 | +0.33% | +0.33% | 0.55x | 2.4 | 2026-11-19T01:45:23.291122+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | ATOM/USD | 1.3032 | 32.271 | 30.636 | +0.35% | +0.24% | 1.04x | 10.8 | 2026-11-19T01:45:23.291122+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 10 | BAT/USD | 0.09359 | 28.851 | 26.224 | +0.61% | +0.26% | 1.13x | 18.2 | 2026-11-19T01:45:23.291122+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 80/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 62.232 | 0.021707 | +2.68% | 0.73x |
| 2 | PAXG/USD | 43.896 | 3743.91 | +0.21% | 0.30x |
| 3 | MEGA/USD | 42.504 | 0.05753 | -0.21% | 1.43x |
| 4 | TRX/USD | 40.321 | 0.310314 | +0.12% | 0.63x |
| 5 | CC/USD | 36.431 | 0.08215 | +0.33% | 0.55x |
| 6 | PYTH/USD | 33.407 | 0.05359 | +0.53% | 1.25x |
| 7 | DRV/USD | 31.102 | 0.26621 | -0.13% | 4.41x |
| 8 | CRV/USD | 30.905 | 0.19938 | +0.43% | 3.10x |
| 9 | ATOM/USD | 30.636 | 1.3032 | +0.24% | 1.04x |
| 10 | BAT/USD | 26.224 | 0.09359 | +0.26% | 1.13x |

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

- Persisted scans: 722; predictions: 5856; observations: 436705.
- Matured sampled outcomes across 1/6/24/48h: 5775; gap abstentions: 13460. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44439181451 · **Generation:** 722 · **Legacy run:** 44439181451
**Main quote time:** 2026-11-19T01:45:31.110729+00:00 · **Legacy report time:** 2026-11-19T01:46:15.237484+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.021707 | 72.91 | +2.68% | 0.73x | MODERATE 61/100 | EXTREME 88/100 | Do nothing |
| 2 | CRV/USD | 0.19938 | 48.07 | +0.43% | 3.10x | STRONG 74/100 | HIGH 66/100 | Watch |
| 3 | MEGA/USD | 0.05753 | 45.75 | -0.21% | 1.43x | WEAK 38/100 | VERY_HIGH 79/100 | Watch |
| 4 | DRV/USD | 0.26621 | 45.45 | -0.13% | 4.41x | MODERATE 48/100 | VERY_HIGH 72/100 | Watch |
| 5 | PYTH/USD ⭐ | 0.05359 | 38.54 | +0.53% | 1.25x | MODERATE 59/100 | HIGH 66/100 | Watch |
| 6 | PAXG/USD | 3743.91 | 37.97 | +0.21% | 0.30x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 7 | TRX/USD | 0.310314 | 37.24 | +0.12% | 0.63x | WEAK 39/100 | VERY_HIGH 70/100 | Watch |
| 8 | CC/USD | 0.08215 | 33.54 | +0.33% | 0.55x | MODERATE 47/100 | VERY_HIGH 75/100 | Watch |
| 9 | ATOM/USD | 1.3032 | 32.27 | +0.24% | 1.04x | MODERATE 46/100 | VERY_HIGH 73/100 | Watch |
| 10 | BAT/USD | 0.09359 | 28.85 | +0.26% | 1.13x | WEAK 44/100 | VERY_HIGH 80/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD | 1776.75 | 53.97 | +0.13% | 1.54x | 58858 | MODERATE 62/100 | HIGH 55/100 | Watch |
| 2 | LTC/USD | 44.12 | 46.37 | +0.30% | 2.19x | 11742 | STRONG 78/100 | HIGH 55/100 | Watch |
| 3 | PYTH/USD ⭐ | 0.05376 | 42.55 | +0.53% | 1.25x | 1943 | MODERATE 56/100 | VERY_HIGH 72/100 | Watch |
| 4 | PROS/USD | 0.6752 | 38.34 | +1.60% | 1.57x | 2475 | MODERATE 54/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** PYTH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
