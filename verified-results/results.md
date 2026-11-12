# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T19:15:42.457611+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=20,50 * * * *, intended UTC minute=20,50; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43287795230
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 506b85569cd30383ad8621f6c32c9cd6aede54b6
**Ledger generation:** 343 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 12.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.01739 | 70.207 | 58.677 | +4.38% | +0.81% | 1.75x | 11.5 | 2026-11-12T19:15:38.270251+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | BAT/USD | 0.12383 | 63.392 | 64.665 | +5.18% | +0.58% | 0.58x | 9.7 | 2026-11-12T19:15:38.270251+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | TIA/USD | 0.4233 | 52.057 | 49.501 | +2.15% | +0.62% | 0.95x | 4.7 | 2026-11-12T19:15:38.270251+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | JUP/USD | 0.26537 | 52.000 | 55.285 | +4.00% | +0.47% | 0.43x | 11.7 | 2026-11-12T19:15:38.270251+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | XDC/USD | 0.02963 | 37.673 | 47.581 | +1.96% | -0.10% | 0.06x | 13.5 | 2026-11-12T19:15:38.270251+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ATOM/USD | 1.4091 | 35.754 | 36.345 | +1.12% | -0.21% | 1.05x | 7.8 | 2026-11-12T19:15:38.270251+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 343; predictions: 3178; observations: 206174.
- Matured sampled outcomes across 1/6/24/48h: 2831; gap abstentions: 8401. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
