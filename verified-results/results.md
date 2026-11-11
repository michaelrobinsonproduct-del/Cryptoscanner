# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T22:10:19.529321+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43109138822
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** b7561825593b6ae86db11233b3c841b3d8221d58
**Ledger generation:** 299 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.6882 | 90.795 | 73.357 | +2.91% | +0.49% | 4.51x | 4.1 | 2026-11-11T22:10:10.706722+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | XLM/USD | 0.149359 | 86.538 | 69.787 | +3.30% | +0.35% | 5.12x | 2.5 | 2026-11-11T22:10:10.706722+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | SUI/USD | 0.835 | 80.680 | 64.781 | +1.48% | +0.18% | 2.67x | 1.2 | 2026-11-11T22:10:10.706722+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | XMR/USD | 586.06 | 77.204 | 78.509 | +4.16% | +0.16% | 0.79x | 11.3 | 2026-11-11T22:10:10.706722+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | XBT/USD | 74393.7 | 76.851 | 61.588 | +0.94% | +0.05% | 2.72x | 0.0 | 2026-11-11T22:10:10.706722+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | HYPE/USD | 72.73 | 74.875 | 59.256 | +0.71% | +0.12% | 7.56x | 1.4 | 2026-11-11T22:10:10.706722+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | AVAX/USD | 8.61 | 68.894 | 74.835 | +2.92% | -0.06% | 0.43x | 1.2 | 2026-11-11T22:10:10.706722+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | TON/USD | 1.182 | 68.872 | 67.791 | +3.78% | +1.11% | 0.55x | 8.5 | 2026-11-11T22:10:10.706722+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | TAO/USD | 219.6595 | 64.833 | 58.058 | +0.68% | +0.25% | 1.55x | 3.4 | 2026-11-11T22:10:10.706722+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | SOL/USD | 84.55 | 62.563 | 65.425 | +1.57% | -0.01% | 0.72x | 1.2 | 2026-11-11T22:10:10.706722+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | ETH/USD | 2069.52 | 61.270 | 61.417 | +0.92% | -0.10% | 1.04x | 0.0 | 2026-11-11T22:10:10.706722+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | ADA/USD | 0.177038 | 58.711 | 65.245 | +1.86% | +0.25% | 0.22x | 5.5 | 2026-11-11T22:10:10.706722+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 299; predictions: 2856; observations: 179511.
- Matured sampled outcomes across 1/6/24/48h: 2243; gap abstentions: 7462. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
