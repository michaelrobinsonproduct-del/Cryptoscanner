# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T10:33:25.712373+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43004270724
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 04372c335e047744eb9503b38ecbf5539e3c1a19
**Ledger generation:** 276 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 603; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04448 | 100.696 | 81.590 | +6.11% | +0.82% | 4.81x | 11.3 | 2026-11-11T10:33:16.697642+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AVAX/USD | 8.707 | 91.103 | 80.659 | +4.08% | +0.65% | 1.72x | 5.7 | 2026-11-11T10:33:16.697642+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | TON/USD | 1.2 | 86.865 | 68.531 | +5.36% | +0.67% | 2.66x | 16.7 | 2026-11-11T10:33:16.697642+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | XMR/USD | 575.25 | 82.445 | 66.774 | +2.24% | +0.13% | 4.15x | 7.8 | 2026-11-11T10:33:16.697642+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ADA/USD | 0.176763 | 81.915 | 64.640 | +1.70% | +0.46% | 10.20x | 4.5 | 2026-11-11T10:33:16.697642+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | HYPE/USD | 72.68 | 76.826 | 58.770 | +0.64% | +0.61% | 11.44x | 1.4 | 2026-11-11T10:33:16.697642+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ZRO/USD | 1.575 | 76.281 | 60.962 | +2.67% | +0.06% | 3.71x | 6.4 | 2026-11-11T10:33:16.697642+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | NEAR/USD | 3.6469 | 73.130 | 64.989 | +1.76% | +0.39% | 1.62x | 4.7 | 2026-11-11T10:33:16.697642+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | SOL/USD | 83.87 | 72.561 | 59.702 | +0.76% | +0.50% | 2.03x | 1.2 | 2026-11-11T10:33:16.697642+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | XBT/USD | 73991.6 | 68.430 | 57.769 | +0.40% | +0.37% | 1.88x | 0.0 | 2026-11-11T10:33:16.697642+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | LTC/USD | 51.06 | 66.247 | 50.070 | +0.71% | +0.24% | 2.60x | 2.0 | 2026-11-11T10:33:16.697642+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | SUI/USD | 0.8327 | 64.089 | 62.221 | +1.20% | +0.50% | 0.94x | 2.4 | 2026-11-11T10:33:16.697642+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 276; predictions: 2580; observations: 165601.
- Matured sampled outcomes across 1/6/24/48h: 1861; gap abstentions: 6859. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
