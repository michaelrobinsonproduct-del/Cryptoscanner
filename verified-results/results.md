# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T03:01:50.115513+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43145123373
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 817cd55be58d458d12216c9d76389d2aa2160775
**Ledger generation:** 309 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 4.603e-06 | 68.691 | 68.665 | +2.11% | +0.07% | 0.97x | 2.2 | 2026-11-12T03:01:41.535607+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ZEC/USD | 991.11 | 66.830 | 74.906 | +3.02% | -0.22% | 0.30x | 2.5 | 2026-11-12T03:01:41.535607+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | AVAX/USD | 8.576 | 51.793 | 57.932 | +0.75% | +0.02% | 0.37x | 4.7 | 2026-11-12T03:01:41.535607+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | NIGHT/USD | 0.04758 | 50.388 | 43.306 | +0.38% | +0.08% | 1.67x | 12.6 | 2026-11-12T03:01:41.535607+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | TON/USD | 1.189 | 46.480 | 45.736 | +1.36% | -0.59% | 1.37x | 16.8 | 2026-11-12T03:01:41.535607+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | DOT/USD | 0.8465 | 39.966 | 41.256 | +0.94% | -0.28% | 1.01x | 2.4 | 2026-11-12T03:01:41.535607+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | AKE/USD | 0.00260215 | 39.097 | 46.507 | +5.04% | +0.17% | 0.18x | 41.5 | 2026-11-12T03:01:41.535607+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | CC/USD | 0.09111 | 31.636 | 37.844 | +0.55% | -0.23% | 0.49x | 6.6 | 2026-11-12T03:01:41.535607+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ICP/USD | 2.596 | 30.793 | 36.286 | +0.39% | +0.00% | 0.45x | 3.9 | 2026-11-12T03:01:41.535607+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 309; predictions: 2963; observations: 185571.
- Matured sampled outcomes across 1/6/24/48h: 2345; gap abstentions: 7832. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
