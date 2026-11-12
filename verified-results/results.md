# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T08:35:17.771094+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43183831426
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 829e3aaac7adeca2b9b4dd1b28e81da98bbc7979
**Ledger generation:** 321 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 13.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AVAX/USD | 8.604 | 74.081 | 60.241 | +1.08% | -0.23% | 3.74x | 4.7 | 2026-11-12T08:35:13.019185+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ZEC/USD | 985.4 | 69.460 | 70.744 | +2.43% | -0.09% | 0.92x | 2.5 | 2026-11-12T08:35:13.019185+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | TON/USD | 1.217 | 64.586 | 63.408 | +3.75% | +1.50% | 0.37x | 16.5 | 2026-11-12T08:35:13.019185+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | XDC/USD | 0.03044 | 60.710 | 66.878 | +4.75% | -0.46% | 0.61x | 13.2 | 2026-11-12T08:35:13.019185+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | MEGA/USD | 0.04595 | 55.560 | 32.123 | +2.57% | +1.69% | 14.10x | 34.8 | 2026-11-12T08:35:13.019185+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ATOM/USD | 1.3975 | 41.821 | 26.785 | +0.29% | +0.01% | 8.42x | 13.6 | 2026-11-12T08:35:13.019185+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | HBAR/USD | 0.06577 | 37.293 | 38.258 | +0.61% | +0.09% | 0.86x | 3.0 | 2026-11-12T08:35:13.019185+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | BAT/USD | 0.12067 | 36.136 | 45.059 | +2.50% | +0.09% | 0.06x | 10.8 | 2026-11-12T08:35:13.019185+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 321; predictions: 3042; observations: 192843.
- Matured sampled outcomes across 1/6/24/48h: 2553; gap abstentions: 7992. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
