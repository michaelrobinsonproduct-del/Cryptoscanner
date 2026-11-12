# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T20:08:26.429378+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43296849316
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** a0c60ddd0b39880903b6870bc8418952696104a1
**Ledger generation:** 345 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 15.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | JUP/USD | 0.2653 | 69.431 | 54.661 | +3.97% | +0.01% | 2.47x | 13.2 | 2026-11-12T20:08:20.979248+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | BAT/USD | 0.1226 | 56.934 | 60.150 | +4.14% | -0.79% | 1.07x | 4.1 | 2026-11-12T20:08:20.979248+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | MON/USD | 0.01744 | 56.603 | 60.840 | +4.68% | -0.29% | 0.72x | 11.5 | 2026-11-12T20:08:20.979248+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | TIA/USD | 0.4243 | 53.604 | 51.013 | +2.39% | +0.38% | 1.07x | 4.7 | 2026-11-12T20:08:20.979248+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | XDC/USD | 0.02978 | 52.646 | 52.581 | +2.48% | -0.03% | 1.02x | 10.1 | 2026-11-12T20:08:20.979248+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XLM/USD | 0.14737 | 50.080 | 50.565 | +0.26% | +0.26% | 0.82x | 3.2 | 2026-11-12T20:08:20.979248+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | USELESS/USD | 0.12999 | 46.814 | 48.591 | +2.12% | +0.69% | 0.48x | 7.7 | 2026-11-12T20:08:20.979248+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 345; predictions: 3192; observations: 207386.
- Matured sampled outcomes across 1/6/24/48h: 2854; gap abstentions: 8449. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
