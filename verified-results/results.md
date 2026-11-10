# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T11:02:51.653256+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42804029208
**Source SHA:** 47e99644e7d7ff00dca3e241f2bbbf508d9a3b56
**Ledger commit:** 7a15765ac74289dd571723649abab08bb8f9b1f4
**Ledger generation:** 230 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 577; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.098 | 76.412 | 64.605 | +5.58% | +1.20% | 1.58x | 18.2 | 2026-11-10T11:02:43.252617+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 5.266e-06 | 71.097 | 70.876 | +2.81% | +0.06% | 0.99x | 7.6 | 2026-11-10T11:02:43.252617+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NIGHT/USD | 0.04222 | 61.517 | 63.312 | +4.30% | -0.05% | 0.84x | 11.8 | 2026-11-10T11:02:43.252617+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | CAP/USD | 0.100341 | 57.748 | 41.952 | +1.50% | +0.25% | 2.45x | 1.5 | 2026-11-10T11:02:43.252617+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | TRX/USD | 0.318876 | 43.540 | 41.886 | +0.48% | -0.02% | 1.17x | 2.9 | 2026-11-10T11:02:43.252617+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | STABLE/USD | 0.02998 | 37.683 | 41.168 | +3.38% | -0.69% | 1.00x | 26.7 | 2026-11-10T11:02:43.252617+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ATOM/USD | 1.3775 | 36.075 | 28.940 | +0.49% | +0.20% | 1.61x | 11.6 | 2026-11-10T11:02:43.252617+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | FET/USD | 0.1442 | 19.906 | 26.889 | +0.28% | +0.07% | 0.27x | 13.9 | 2026-11-10T11:02:43.252617+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 230; predictions: 2101; observations: 138092.
- Matured sampled outcomes across 1/6/24/48h: 1189; gap abstentions: 5930. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 16; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
