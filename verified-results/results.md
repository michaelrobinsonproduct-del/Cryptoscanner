# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T17:05:00.045855+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42860883538
**Source SHA:** 3774b902ccb4e4fd5507499dc7c96ebbb4185329
**Ledger commit:** 1fa4e7783a9a541ac68dee39854a47f4f1fe6810
**Ledger generation:** 241 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 597; OHLC screened: 9.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.181e-06 | 57.355 | 61.133 | +1.15% | -0.37% | 0.81x | 3.9 | 2026-11-10T17:04:57.138379+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | UAI/USD | 0.04095 | 53.152 | 60.852 | +6.20% | -1.08% | 0.77x | 31.8 | 2026-11-10T17:04:57.138379+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | LIGHTER/USD | 3.325 | 50.871 | 47.331 | +2.85% | -0.36% | 1.53x | 15.0 | 2026-11-10T17:04:57.138379+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | TON/USD | 1.097 | 46.226 | 54.361 | +5.48% | -0.63% | 0.50x | 36.5 | 2026-11-10T17:04:57.138379+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | NIGHT/USD | 0.04099 | 42.052 | 48.579 | +1.26% | -1.25% | 0.97x | 7.3 | 2026-11-10T17:04:57.138379+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XDC/USD | 0.02991 | 39.816 | 47.078 | +1.49% | -0.77% | 0.66x | 6.7 | 2026-11-10T17:04:57.138379+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | PLAY/USD | 0.008501 | 39.164 | 41.474 | +3.51% | +0.53% | 0.50x | 28.3 | 2026-11-10T17:04:57.138379+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 241; predictions: 2213; observations: 144565.
- Matured sampled outcomes across 1/6/24/48h: 1259; gap abstentions: 6200. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
