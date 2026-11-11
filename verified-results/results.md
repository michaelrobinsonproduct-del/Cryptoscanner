# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T07:00:03.491308+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42976090397
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** e1fb4d4c7acdd8620dad800d94476fbaea84bcae
**Ledger generation:** 269 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 602; OHLC screened: 21.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 564.53 | 69.558 | 56.908 | +0.34% | -0.47% | 10.45x | 0.9 | 2026-11-11T06:59:54.970418+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | INJ/USD | 8.211 | 66.622 | 54.114 | +2.57% | -0.50% | 2.75x | 12.2 | 2026-11-11T06:59:54.970418+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NEAR/USD | 3.6018 | 62.065 | 55.600 | +0.50% | -0.60% | 1.95x | 5.8 | 2026-11-11T06:59:54.970418+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | AVAX/USD | 8.451 | 53.775 | 59.743 | +1.02% | -0.54% | 0.67x | 4.7 | 2026-11-11T06:59:54.970418+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | PYTH/USD | 0.06788 | 53.394 | 50.267 | +3.70% | -0.98% | 1.80x | 16.2 | 2026-11-11T06:59:54.970418+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | KAS/USD | 0.02992 | 50.659 | 35.993 | +1.15% | -0.07% | 7.56x | 13.4 | 2026-11-11T06:59:54.970418+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | TON/USD | 1.144 | 45.429 | 30.991 | +0.44% | +0.53% | 2.18x | 17.5 | 2026-11-11T06:59:54.970418+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | NIGHT/USD | 0.04272 | 42.923 | 48.071 | +1.91% | -0.02% | 0.50x | 16.4 | 2026-11-11T06:59:54.970418+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ZRO/USD | 1.548 | 41.629 | 43.331 | +0.91% | -0.45% | 1.06x | 12.9 | 2026-11-11T06:59:54.970418+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | SPX/USD | 0.367 | 32.868 | 43.049 | +1.55% | -0.51% | 0.24x | 10.9 | 2026-11-11T06:59:54.970418+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | CC/USD | 0.08975 | 28.032 | 32.983 | +0.30% | +0.34% | 0.34x | 11.2 | 2026-11-11T06:59:54.970418+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 269; predictions: 2500; observations: 161381.
- Matured sampled outcomes across 1/6/24/48h: 1781; gap abstentions: 6690. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
