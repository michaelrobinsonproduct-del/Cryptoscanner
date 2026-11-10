# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T15:05:59.663536+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42840584810
**Source SHA:** 3774b902ccb4e4fd5507499dc7c96ebbb4185329
**Ledger commit:** ec296ae7ad468f0af7dd149536809303a39dd967
**Ledger generation:** 237 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 590; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.557e-06 | 121.793 | 98.199 | +8.49% | +1.72% | 3.36x | 3.6 | 2026-11-10T15:05:51.017850+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | LIGHTER/USD | 3.433 | 95.980 | 69.806 | +6.19% | +2.23% | 2.59x | 14.6 | 2026-11-10T15:05:51.017850+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NEAR/USD | 3.7342 | 94.964 | 74.390 | +3.11% | +1.11% | 4.94x | 4.8 | 2026-11-10T15:05:51.017850+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | NIGHT/USD | 0.04324 | 93.505 | 80.146 | +6.82% | +1.72% | 1.48x | 11.6 | 2026-11-10T15:05:51.017850+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | TON/USD | 1.102 | 87.853 | 66.885 | +5.96% | +1.19% | 4.00x | 18.2 | 2026-11-10T15:05:51.017850+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ENA/USD | 0.1575 | 83.187 | 60.450 | +2.87% | +1.55% | 3.47x | 12.7 | 2026-11-10T15:05:51.017850+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ZEC/USD | 1187.9 | 82.418 | 68.924 | +2.19% | +0.59% | 2.05x | 2.8 | 2026-11-10T15:05:51.017850+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ONDO/USD | 0.37936 | 80.747 | 57.710 | +1.56% | +1.61% | 9.28x | 9.2 | 2026-11-10T15:05:51.017850+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | UNI/USD | 7.1301 | 80.519 | 59.964 | +2.29% | +1.11% | 3.22x | 9.0 | 2026-11-10T15:05:51.017850+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | ADA/USD | 0.177903 | 71.296 | 52.624 | +0.36% | +0.73% | 8.72x | 9.7 | 2026-11-10T15:05:51.017850+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | XDC/USD | 0.031 | 67.164 | 72.957 | +5.19% | -0.26% | 0.55x | 6.5 | 2026-11-10T15:05:51.017850+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | RENDER/USD | 1.608 | 58.304 | 38.291 | +1.07% | +1.00% | 5.01x | 6.2 | 2026-11-10T15:05:51.017850+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 237; predictions: 2171; observations: 142189.
- Matured sampled outcomes across 1/6/24/48h: 1218; gap abstentions: 6106. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
