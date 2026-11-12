# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T07:03:57.189487+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43172169068
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 7d324ffd05392226a79fa904517809fdc394ccdb
**Ledger generation:** 318 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 16.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 987.46 | 65.620 | 71.384 | +2.64% | +0.05% | 0.40x | 4.3 | 2026-11-12T07:03:52.801141+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AVAX/USD | 8.617 | 61.415 | 61.895 | +1.23% | -0.16% | 1.03x | 3.5 | 2026-11-12T07:03:52.801141+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | TON/USD | 1.182 | 57.631 | 41.356 | +0.77% | +0.25% | 2.72x | 16.9 | 2026-11-12T07:03:52.801141+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | HBAR/USD | 0.06565 | 52.055 | 36.979 | +0.43% | +0.02% | 12.28x | 3.0 | 2026-11-12T07:03:52.801141+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | DOT/USD | 0.8423 | 46.298 | 37.690 | +0.44% | +0.29% | 1.72x | 2.4 | 2026-11-12T07:03:52.801141+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | BAT/USD | 0.11857 | 32.880 | 32.605 | +0.71% | -0.88% | 1.47x | 10.1 | 2026-11-12T07:03:52.801141+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 318; predictions: 3022; observations: 191025.
- Matured sampled outcomes across 1/6/24/48h: 2498; gap abstentions: 7951. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
