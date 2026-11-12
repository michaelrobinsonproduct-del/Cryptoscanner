# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T04:07:30.362453+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43152434465
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 3f67fbe17af9ba4ff238409458dd22e12f6c226d
**Ledger generation:** 312 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AVAX/USD | 8.598 | 75.792 | 60.327 | +1.01% | +0.09% | 6.48x | 3.5 | 2026-11-12T04:07:23.474794+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | HYPE/USD | 72.27 | 71.226 | 56.240 | +0.38% | +0.32% | 2.34x | 2.8 | 2026-11-12T04:07:23.474794+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ZEC/USD | 986.89 | 65.254 | 71.322 | +2.59% | +0.35% | 0.22x | 3.5 | 2026-11-12T04:07:23.474794+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | PUMP/USD | 0.003476 | 56.323 | 40.458 | +0.43% | +0.17% | 5.09x | 8.7 | 2026-11-12T04:07:23.474794+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | PEPE/USD | 4.573e-06 | 54.445 | 61.808 | +1.44% | -0.02% | 0.27x | 6.6 | 2026-11-12T04:07:23.474794+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | INJ/USD | 7.606 | 47.861 | 49.873 | +0.92% | +0.96% | 0.32x | 10.5 | 2026-11-12T04:07:23.474794+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | KAS/USD | 0.02934 | 38.395 | 38.275 | +0.93% | +0.00% | 1.01x | 13.7 | 2026-11-12T04:07:23.474794+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | DOT/USD | 0.8434 | 30.017 | 38.654 | +0.57% | +0.13% | 0.07x | 2.4 | 2026-11-12T04:07:23.474794+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | HBAR/USD | 0.06555 | 27.624 | 35.194 | +0.28% | +0.20% | 0.14x | 4.6 | 2026-11-12T04:07:23.474794+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | ICNT/USD | 0.281 | 24.466 | 26.362 | +0.29% | +0.43% | 0.60x | 14.2 | 2026-11-12T04:07:23.474794+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 312; predictions: 2986; observations: 187389.
- Matured sampled outcomes across 1/6/24/48h: 2377; gap abstentions: 7860. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
