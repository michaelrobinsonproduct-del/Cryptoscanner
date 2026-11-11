# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T23:06:11.043272+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43116803216
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 6cad2c25c6d3ba13ff091651a59986696f3c100d
**Ledger generation:** 301 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 21.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.178 | 80.925 | 64.996 | +3.42% | +0.25% | 2.47x | 8.5 | 2026-11-11T23:06:03.528851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEAQ/USD | 0.02759 | 77.784 | 61.147 | +4.87% | +0.33% | 6.09x | 7.3 | 2026-11-11T23:06:03.528851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | AVAX/USD | 8.499 | 77.641 | 64.362 | +1.59% | +0.32% | 2.17x | 3.5 | 2026-11-11T23:06:03.528851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | XMR/USD | 583.3 | 73.725 | 74.694 | +3.67% | +0.13% | 0.84x | 12.0 | 2026-11-11T23:06:03.528851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | NEAR/USD | 3.6033 | 72.406 | 56.587 | +0.54% | +0.16% | 12.64x | 4.4 | 2026-11-11T23:06:03.528851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XLM/USD | 0.147103 | 67.027 | 56.840 | +1.74% | +0.37% | 1.84x | 6.9 | 2026-11-11T23:06:03.528851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ADA/USD | 0.174695 | 62.911 | 55.396 | +0.51% | +0.38% | 1.56x | 6.4 | 2026-11-11T23:06:03.528851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ICP/USD | 2.611 | 61.290 | 53.710 | +3.00% | +0.97% | 1.27x | 7.7 | 2026-11-11T23:06:03.528851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | FET/USD | 0.1479 | 59.474 | 43.797 | +2.00% | +0.14% | 3.61x | 6.8 | 2026-11-11T23:06:03.528851+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | VVV/USD | 19.628 | 49.902 | 43.586 | +1.68% | +0.08% | 1.59x | 9.7 | 2026-11-11T23:06:03.528851+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 301; predictions: 2878; observations: 180723.
- Matured sampled outcomes across 1/6/24/48h: 2255; gap abstentions: 7555. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
