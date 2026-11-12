# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T05:09:04.621481+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43159122744
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** bffe1aac7899332b9759f7ee7d7fdf3e9eb2df01
**Ledger generation:** 314 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 19.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 979.82 | 71.175 | 66.165 | +1.85% | -0.27% | 1.64x | 3.6 | 2026-11-12T05:08:59.282886+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AVAX/USD | 8.578 | 63.237 | 58.094 | +0.78% | -0.15% | 1.59x | 4.7 | 2026-11-12T05:08:59.282886+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | PEPE/USD | 4.564e-06 | 56.961 | 60.409 | +1.24% | -0.20% | 0.75x | 6.6 | 2026-11-12T05:08:59.282886+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | DOT/USD | 0.8445 | 35.527 | 40.143 | +0.70% | +0.07% | 0.50x | 1.2 | 2026-11-12T05:08:59.282886+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | AKE/USD | 0.00251645 | 6.534 | 37.493 | +1.58% | -5.51% | 0.40x | 11.4 | 2026-11-12T05:08:59.282886+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 314; predictions: 2997; observations: 188601.
- Matured sampled outcomes across 1/6/24/48h: 2440; gap abstentions: 7884. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
