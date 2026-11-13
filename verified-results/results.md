# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-13T06:32:38.299118+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43379379133
**Source SHA:** fb88270f7a672ac90f7335bb9ebeb22e9e09b88d
**Previous ledger commit:** 2428f95efc0b300a6c2cd2df2637cfc61da148f2 (atomic ledger/results publication)
**Ledger generation:** 352 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 13.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 4.603e-06 | 72.558 | 65.820 | +1.70% | +1.19% | 1.08x | 2.2 | 2026-11-13T06:32:33.038563+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ZRO/USD | 1.58 | 72.448 | 43.294 | +1.74% | +2.83% | 4.99x | 12.7 | 2026-11-13T06:32:33.038563+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | UAI/USD | 0.03672 | 71.517 | 31.517 | +1.80% | +5.58% | 5.76x | 24.6 | 2026-11-13T06:32:33.038563+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | NEAR/USD | 3.4467 | 60.092 | 57.728 | +0.78% | +1.79% | 0.34x | 5.5 | 2026-11-13T06:32:33.038563+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ICNT/USD | 0.2828 | 54.245 | 41.976 | +2.58% | +1.79% | 1.33x | 14.2 | 2026-11-13T06:32:33.038563+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | CAP/USD | 0.103882 | 48.120 | 31.667 | +0.30% | +0.29% | 3.91x | 5.2 | 2026-11-13T06:32:33.038563+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | TON/USD | 1.151 | 42.686 | 45.532 | +0.96% | +1.05% | 0.19x | 17.4 | 2026-11-13T06:32:33.038563+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 352; predictions: 3239; observations: 211628.
- Matured sampled outcomes across 1/6/24/48h: 2926; gap abstentions: 8999. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
