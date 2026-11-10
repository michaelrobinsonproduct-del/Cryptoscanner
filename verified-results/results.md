# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T15:37:48.720122+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42846066070
**Source SHA:** 3774b902ccb4e4fd5507499dc7c96ebbb4185329
**Ledger commit:** acf5cb95641e8bee094702b72cfc4f5292ab2989
**Ledger generation:** 238 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 591; OHLC screened: 16.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PLAY/USD | 0.008555 | 62.567 | 53.761 | +4.16% | -1.24% | 5.78x | 12.9 | 2026-11-10T15:37:42.256676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | XDC/USD | 0.03062 | 58.590 | 62.231 | +3.90% | -0.35% | 0.81x | 9.8 | 2026-11-10T15:37:42.256676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | PEPE/USD | 5.269e-06 | 52.311 | 68.448 | +2.87% | -1.90% | 0.34x | 13.3 | 2026-11-10T15:37:42.256676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | TON/USD | 1.092 | 48.621 | 60.085 | +5.00% | -1.44% | 0.57x | 18.3 | 2026-11-10T15:37:42.256676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | NIGHT/USD | 0.04181 | 44.936 | 60.295 | +3.29% | -2.28% | 0.60x | 7.2 | 2026-11-10T15:37:42.256676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | LIGHTER/USD | 3.326 | 43.261 | 48.494 | +2.88% | -1.79% | 1.37x | 12.0 | 2026-11-10T15:37:42.256676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | PLUME/USD | 0.01308 | 39.246 | 30.623 | +2.19% | -1.28% | 12.57x | 30.8 | 2026-11-10T15:37:42.256676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | TRX/USD | 0.318965 | 37.886 | 42.449 | +0.51% | -0.09% | 0.59x | 0.1 | 2026-11-10T15:37:42.256676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | XPL/USD | 0.0527 | 29.372 | 34.663 | +1.74% | -0.93% | 0.94x | 19.0 | 2026-11-10T15:37:42.256676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | ZRO/USD | 1.499 | 27.824 | 41.534 | +1.56% | -2.00% | 0.63x | 20.0 | 2026-11-10T15:37:42.256676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | KAS/USD | 0.02986 | 24.610 | 29.026 | +0.40% | -1.37% | 1.25x | 13.4 | 2026-11-10T15:37:42.256676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | UAI/USD | 0.03938 | 24.587 | 30.416 | +2.13% | -1.49% | 1.16x | 35.9 | 2026-11-10T15:37:42.256676+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 238; predictions: 2183; observations: 142780.
- Matured sampled outcomes across 1/6/24/48h: 1223; gap abstentions: 6135. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
