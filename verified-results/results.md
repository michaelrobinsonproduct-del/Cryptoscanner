# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T11:22:52.163215+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45603381978
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** dc6571ae33946622e785800dc8581d72e4d1b4fe (atomic ledger/results publication)
**Ledger generation:** 1711 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.3373 | 81.848 | 77.080 | +7.32% | -0.61% | 1.78x | 11.9 | 2026-11-25T11:22:46.549684+00:00 | Not calibrated | MODERATE 56/100 | HIGH 67/100 | Watch | WATCH |
| 2 | VVV/USD | 25.058 | 67.992 | 62.217 | +2.12% | +0.47% | 1.34x | 15.2 | 2026-11-25T11:22:46.549684+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 3 | MON/USD | 0.0099 | 62.061 | 70.566 | +4.54% | -1.10% | 0.70x | 20.2 | 2026-11-25T11:22:46.549684+00:00 | Not calibrated | WEAK 26/100 | EXTREME 92/100 | Do nothing | WATCH |
| 4 | BABY/USD | 0.00853 | 33.236 | 42.655 | +3.27% | -0.35% | 0.23x | 23.4 | 2026-11-25T11:22:46.549684+00:00 | Not calibrated | WEAK 12/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 77.080 | 0.3373 | -0.61% | 1.78x |
| 2 | MON/USD | 70.566 | 0.0099 | -1.10% | 0.70x |
| 3 | VVV/USD | 62.217 | 25.058 | +0.47% | 1.34x |
| 4 | BABY/USD | 42.655 | 0.00853 | -0.35% | 0.23x |

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

- Persisted scans: 1711; predictions: 14473; observations: 1037073.
- Matured sampled outcomes across 1/6/24/48h: 31478; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45603381978 · **Generation:** 1711 · **Legacy run:** 45603381978
**Main quote time:** 2026-11-25T11:22:52.163215+00:00 · **Legacy report time:** 2026-11-25T11:24:07.435551+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.3373 | 81.85 | -0.61% | 1.78x | MODERATE 56/100 | HIGH 67/100 | Watch |
| 2 | VVV/USD ⭐ | 25.058 | 67.99 | +0.47% | 1.34x | STRONG 84/100 | HIGH 61/100 | Watch |
| 3 | MON/USD | 0.0099 | 62.06 | -1.10% | 0.70x | WEAK 26/100 | EXTREME 92/100 | Do nothing |
| 4 | BABY/USD | 0.00853 | 33.24 | -0.35% | 0.23x | WEAK 12/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 24.968 | 60.80 | +0.47% | 1.34x | 13129 | STRONG 85/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
