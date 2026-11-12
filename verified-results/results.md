# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T20:40:33.064829+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43302244496
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 35f9dbc740ef83ff726d49c15dc3ffb2df80e5ec
**Ledger generation:** 346 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 16.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | JUP/USD | 0.26866 | 67.383 | 62.018 | +5.29% | +1.22% | 0.93x | 17.1 | 2026-11-12T20:40:26.649241+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | XLM/USD | 0.14896 | 66.114 | 59.546 | +1.34% | +0.54% | 1.39x | 0.3 | 2026-11-12T20:40:26.649241+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | XDC/USD | 0.0298 | 60.427 | 51.339 | +2.55% | +0.03% | 1.89x | 13.4 | 2026-11-12T20:40:26.649241+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | TIA/USD | 0.428 | 57.305 | 58.527 | +3.28% | +0.61% | 0.57x | 2.3 | 2026-11-12T20:40:26.649241+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | MON/USD | 0.01738 | 51.371 | 58.144 | +4.32% | -0.17% | 0.41x | 11.5 | 2026-11-12T20:40:26.649241+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | USELESS/USD | 0.13083 | 46.784 | 43.289 | +2.78% | -0.50% | 1.60x | 28.3 | 2026-11-12T20:40:26.649241+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | BAT/USD | 0.12187 | 46.742 | 49.644 | +3.52% | -0.39% | 0.91x | 16.4 | 2026-11-12T20:40:26.649241+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | POL/USD | 0.08781 | 44.311 | 35.015 | +0.70% | +0.49% | 1.68x | 5.7 | 2026-11-12T20:40:26.649241+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 346; predictions: 3200; observations: 207992.
- Matured sampled outcomes across 1/6/24/48h: 2868; gap abstentions: 8468. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
