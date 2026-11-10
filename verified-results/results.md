# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T04:49:45.450681+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=20,50 * * * *, intended UTC minute=20,50; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42758167270
**Source SHA:** 477d6c2f4cab0daab12aee798826c72cad7caa79
**Ledger commit:** 6ce882a76bff7441a651b410814f040d87414c98
**Ledger generation:** 225 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 521; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.239e-06 | 81.629 | 70.035 | +2.28% | -0.68% | 2.94x | 1.9 | 2026-11-10T04:49:38.632341+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ADA/USD | 0.178136 | 65.218 | 54.030 | +0.49% | -0.07% | 2.16x | 4.0 | 2026-11-10T04:49:38.632341+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | TON/USD | 1.077 | 56.137 | 55.240 | +3.56% | -0.09% | 1.14x | 9.3 | 2026-11-10T04:49:38.632341+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ATOM/USD | 1.3915 | 51.289 | 35.823 | +1.51% | +0.09% | 4.81x | 12.2 | 2026-11-10T04:49:38.632341+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | NIGHT/USD | 0.04139 | 42.887 | 48.478 | +2.25% | +0.02% | 0.43x | 12.1 | 2026-11-10T04:49:38.632341+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | HBAR/USD | 0.06709 | 34.826 | 39.717 | +0.54% | -0.12% | 0.57x | 3.0 | 2026-11-10T04:49:38.632341+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | PENGU/USD | 0.006334 | 24.669 | 31.373 | +0.32% | -0.22% | 0.44x | 4.7 | 2026-11-10T04:49:38.632341+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 225; predictions: 2061; observations: 135356.
- Matured sampled outcomes across 1/6/24/48h: 1189; gap abstentions: 5627. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 17; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
