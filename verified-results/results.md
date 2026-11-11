# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T21:40:18.477465+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43104675876
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 3319ba16d228ead28d00c48b9918ae01a661b7b8
**Ledger generation:** 298 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 585.57 | 79.081 | 79.343 | +4.08% | +0.28% | 0.83x | 8.4 | 2026-11-11T21:40:11.943363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AVAX/USD | 8.623 | 74.358 | 75.344 | +3.07% | +0.02% | 0.89x | 2.3 | 2026-11-11T21:40:11.943363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | LINK/USD | 10.42677 | 68.679 | 52.274 | +1.39% | +0.28% | 9.23x | 3.7 | 2026-11-11T21:40:11.943363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ADA/USD | 0.177207 | 66.183 | 67.055 | +1.96% | -0.18% | 1.00x | 3.3 | 2026-11-11T21:40:11.943363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | NEAR/USD | 3.6778 | 63.914 | 71.592 | +2.62% | -0.20% | 0.33x | 3.5 | 2026-11-11T21:40:11.943363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | SOL/USD | 84.72 | 61.987 | 66.856 | +1.78% | -0.19% | 0.61x | 1.2 | 2026-11-11T21:40:11.943363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ETH/USD | 2075.86 | 60.771 | 63.581 | +1.23% | -0.11% | 0.77x | 0.0 | 2026-11-11T21:40:11.943363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | SUI/USD | 0.8353 | 59.281 | 65.035 | +1.52% | -0.19% | 0.52x | 1.2 | 2026-11-11T21:40:11.943363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | XBT/USD | 74493.3 | 58.125 | 62.534 | +1.08% | -0.15% | 0.64x | 0.0 | 2026-11-11T21:40:11.943363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | XLM/USD | 0.149142 | 57.536 | 68.168 | +3.15% | -0.50% | 0.18x | 3.0 | 2026-11-11T21:40:11.943363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | TAO/USD | 219.6621 | 55.624 | 57.775 | +0.68% | +0.08% | 0.75x | 4.0 | 2026-11-11T21:40:11.943363+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | HYPE/USD | 72.94 | 55.470 | 60.607 | +1.00% | -0.10% | 0.53x | 2.7 | 2026-11-11T21:40:11.943363+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 298; predictions: 2844; observations: 178905.
- Matured sampled outcomes across 1/6/24/48h: 2243; gap abstentions: 7430. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
