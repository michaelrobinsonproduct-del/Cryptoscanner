# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T06:33:27.759734+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43168685645
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** f572ecc0d3caf040a5ca2bafb787a7fe10283466
**Ledger generation:** 317 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 16.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 983.56 | 77.358 | 69.504 | +2.24% | +0.15% | 1.71x | 2.3 | 2026-11-12T06:33:23.126809+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AVAX/USD | 8.594 | 76.572 | 60.000 | +0.96% | +0.31% | 3.39x | 3.5 | 2026-11-12T06:33:23.126809+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | PEPE/USD | 4.549e-06 | 74.607 | 59.168 | +0.91% | +0.09% | 4.69x | 4.4 | 2026-11-12T06:33:23.126809+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | DOT/USD | 0.8419 | 52.804 | 36.793 | +0.39% | +0.20% | 2.65x | 3.6 | 2026-11-12T06:33:23.126809+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | TON/USD | 1.181 | 45.743 | 45.009 | +0.68% | -0.50% | 1.33x | 8.5 | 2026-11-12T06:33:23.126809+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | BAT/USD | 0.11993 | 39.455 | 43.276 | +1.87% | +0.92% | 0.16x | 5.0 | 2026-11-12T06:33:23.126809+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | HBAR/USD | 0.06555 | 34.495 | 35.821 | +0.28% | +0.46% | 0.64x | 3.1 | 2026-11-12T06:33:23.126809+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 317; predictions: 3016; observations: 190419.
- Matured sampled outcomes across 1/6/24/48h: 2481; gap abstentions: 7939. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
