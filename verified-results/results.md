# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T05:26:26.715181+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42761968418
**Source SHA:** 44f0ae518ad7c7318e1bf279b01df30dfc630b65
**Ledger commit:** 0c8fbf09bdf42cccfe3b6f02b76a0699199059f6
**Ledger generation:** 226 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 529; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04228 | 83.592 | 64.298 | +4.45% | +0.86% | 3.80x | 11.8 | 2026-11-10T05:26:19.886037+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 5.252e-06 | 58.670 | 70.863 | +2.54% | -0.77% | 0.17x | 3.8 | 2026-11-10T05:26:19.886037+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | XDC/USD | 0.0299 | 53.103 | 43.172 | +1.46% | +0.03% | 1.98x | 6.7 | 2026-11-10T05:26:19.886037+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | HBAR/USD | 0.06694 | 51.565 | 38.054 | +0.31% | -0.30% | 3.69x | 3.0 | 2026-11-10T05:26:19.886037+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ADA/USD | 0.178074 | 45.941 | 55.819 | +0.46% | -0.23% | 0.13x | 0.1 | 2026-11-10T05:26:19.886037+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | CAP/USD | 0.101106 | 38.203 | 45.173 | +2.27% | -0.45% | 0.53x | 6.1 | 2026-11-10T05:26:19.886037+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 226; predictions: 2067; observations: 135885.
- Matured sampled outcomes across 1/6/24/48h: 1189; gap abstentions: 5654. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 18; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
