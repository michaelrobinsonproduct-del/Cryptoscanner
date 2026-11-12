# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T02:04:00.887505+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43138538614
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** c4d31af5579f3ca6d7baaab137a0c6c5a22d1c7c
**Ledger generation:** 307 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 19.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 990.9 | 85.599 | 72.127 | +3.00% | +0.20% | 2.25x | 7.8 | 2026-11-12T02:03:53.763831+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AVAX/USD | 8.536 | 69.160 | 54.630 | +0.28% | -0.09% | 5.92x | 4.7 | 2026-11-12T02:03:53.763831+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | PEPE/USD | 4.555e-06 | 54.350 | 60.102 | +1.04% | +0.42% | 0.22x | 4.4 | 2026-11-12T02:03:53.763831+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | TON/USD | 1.188 | 47.366 | 45.144 | +1.28% | +0.08% | 1.18x | 16.9 | 2026-11-12T02:03:53.763831+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | JUP/USD | 0.256 | 41.520 | 27.164 | +0.33% | -0.13% | 2.79x | 16.1 | 2026-11-12T02:03:53.763831+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | DOT/USD | 0.8422 | 35.417 | 38.283 | +0.43% | -0.32% | 0.87x | 1.2 | 2026-11-12T02:03:53.763831+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | PUMP/USD | 0.003474 | 34.171 | 39.049 | +0.38% | -0.03% | 0.53x | 11.5 | 2026-11-12T02:03:53.763831+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ICNT/USD | 0.2821 | 27.434 | 29.115 | +0.68% | +0.97% | 0.35x | 14.3 | 2026-11-12T02:03:53.763831+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 307; predictions: 2942; observations: 184359.
- Matured sampled outcomes across 1/6/24/48h: 2321; gap abstentions: 7768. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
