# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T00:08:31.246057+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43124718472
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 48123cf50702603d3233fc85ab894d22330b35d8
**Ledger generation:** 303 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 20.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 974.54 | 63.071 | 60.863 | +1.30% | +1.25% | 0.60x | 6.5 | 2026-11-12T00:08:24.261773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 4.539e-06 | 54.463 | 57.607 | +0.69% | +0.22% | 0.58x | 4.4 | 2026-11-12T00:08:24.261773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | QNT/USD | 171.28 | 49.718 | 50.767 | +0.35% | +0.92% | 0.43x | 7.6 | 2026-11-12T00:08:24.261773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | TON/USD | 1.177 | 48.085 | 43.025 | +0.34% | +0.34% | 1.34x | 8.5 | 2026-11-12T00:08:24.261773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | NIGHT/USD | 0.04768 | 44.407 | 47.235 | +0.59% | +0.61% | 0.41x | 8.4 | 2026-11-12T00:08:24.261773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | PUMP/USD | 0.003498 | 42.988 | 46.465 | +1.07% | +0.90% | 0.20x | 8.6 | 2026-11-12T00:08:24.261773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ARB/USD | 0.1524 | 37.810 | 43.278 | +0.66% | +0.46% | 0.22x | 6.6 | 2026-11-12T00:08:24.261773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | USELESS/USD | 0.12853 | 36.583 | 35.376 | +0.97% | +1.84% | 0.20x | 14.8 | 2026-11-12T00:08:24.261773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ENA/USD | 0.1462 | 35.417 | 40.100 | +0.34% | +0.76% | 0.15x | 6.9 | 2026-11-12T00:08:24.261773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | DOT/USD | 0.841 | 27.729 | 36.222 | +0.29% | +0.18% | 0.06x | 3.6 | 2026-11-12T00:08:24.261773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | STRK/USD | 0.03684 | 22.276 | 31.314 | +0.60% | +0.03% | 0.08x | 8.2 | 2026-11-12T00:08:24.261773+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | SYRUP/USD | 0.13193 | 18.378 | 24.143 | +0.28% | +0.24% | 0.31x | 17.4 | 2026-11-12T00:08:24.261773+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 303; predictions: 2898; observations: 181935.
- Matured sampled outcomes across 1/6/24/48h: 2291; gap abstentions: 7648. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
