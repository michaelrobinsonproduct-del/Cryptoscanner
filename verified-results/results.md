# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T03:13:15.812362+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=20,50 * * * *, intended UTC minute=20,50; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43146380110
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 084f3c2750a73d9c826b84737ce2946759e1fad5
**Ledger generation:** 310 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 23.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 4.6e-06 | 65.317 | 67.111 | +2.04% | -0.39% | 1.02x | 4.3 | 2026-11-12T03:13:07.449666+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ZEC/USD | 986.89 | 63.528 | 71.728 | +2.59% | -0.06% | 0.21x | 2.7 | 2026-11-12T03:13:07.449666+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | TON/USD | 1.194 | 59.232 | 52.949 | +1.79% | +0.51% | 1.38x | 8.4 | 2026-11-12T03:13:07.449666+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | AVAX/USD | 8.561 | 47.620 | 56.695 | +0.58% | -0.23% | 0.21x | 4.7 | 2026-11-12T03:13:07.449666+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | CC/USD | 0.09119 | 39.725 | 39.591 | +0.64% | -0.12% | 1.07x | 4.4 | 2026-11-12T03:13:07.449666+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | DOT/USD | 0.8446 | 35.132 | 38.482 | +0.72% | +0.02% | 0.65x | 4.7 | 2026-11-12T03:13:07.449666+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 310; predictions: 2969; observations: 186177.
- Matured sampled outcomes across 1/6/24/48h: 2345; gap abstentions: 7832. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 17; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
