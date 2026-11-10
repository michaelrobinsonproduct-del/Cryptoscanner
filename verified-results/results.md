# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T13:06:28.684128+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=20,50 * * * *, intended UTC minute=20,50; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42821288249
**Source SHA:** 46df1627878352d4e4822ef888168ae0fa7d40b6
**Ledger commit:** ae9da63e02865480c55cc1c686127c701454aab5
**Ledger generation:** 233 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 584; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | CAP/USD | 0.106163 | 85.461 | 68.568 | +7.39% | +2.53% | 1.42x | 17.7 | 2026-11-10T13:06:20.093766+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NEAR/USD | 3.6344 | 72.880 | 56.000 | +0.36% | +0.38% | 2.50x | 3.0 | 2026-11-10T13:06:20.093766+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NIGHT/USD | 0.04237 | 69.980 | 64.400 | +4.67% | +0.69% | 1.21x | 14.2 | 2026-11-10T13:06:20.093766+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | PEPE/USD | 5.297e-06 | 69.655 | 77.028 | +3.42% | +0.32% | 0.10x | 3.8 | 2026-11-10T13:06:20.093766+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | XDC/USD | 0.03098 | 63.018 | 66.765 | +5.12% | +0.16% | 0.54x | 16.1 | 2026-11-10T13:06:20.093766+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | TRX/USD | 0.3185 | 54.971 | 40.191 | +0.36% | -0.04% | 3.81x | 0.3 | 2026-11-10T13:06:20.093766+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | TON/USD | 1.096 | 53.429 | 58.449 | +5.38% | -0.09% | 0.54x | 27.4 | 2026-11-10T13:06:20.093766+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ENA/USD | 0.1545 | 42.404 | 43.006 | +0.91% | +0.32% | 0.78x | 13.0 | 2026-11-10T13:06:20.093766+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | SYRUP/USD | 0.13671 | 24.432 | 31.898 | +0.90% | -0.43% | 0.47x | 10.2 | 2026-11-10T13:06:20.093766+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 233; predictions: 2130; observations: 139838.
- Matured sampled outcomes across 1/6/24/48h: 1189; gap abstentions: 6031. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
