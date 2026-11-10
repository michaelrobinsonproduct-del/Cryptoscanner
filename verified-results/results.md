# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T06:33:15.247794+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42769087659
**Source SHA:** 5485350d2a97636b4030746c73b926c2745740e1
**Ledger commit:** 3a263e38d054621485309ce98858418283b63ff0
**Ledger generation:** 228 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 540; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04294 | 76.206 | 79.832 | +6.08% | +0.78% | 0.25x | 4.7 | 2026-11-10T06:33:08.446201+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 5.295e-06 | 75.314 | 76.752 | +3.38% | +0.63% | 0.54x | 3.8 | 2026-11-10T06:33:08.446201+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | TON/USD | 1.093 | 69.644 | 66.144 | +5.10% | +0.28% | 1.21x | 9.2 | 2026-11-10T06:33:08.446201+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | XLM/USD | 0.14817 | 64.223 | 56.611 | +0.58% | +0.38% | 1.57x | 2.0 | 2026-11-10T06:33:08.446201+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | XDC/USD | 0.03083 | 62.223 | 67.501 | +4.61% | -0.45% | 0.70x | 6.5 | 2026-11-10T06:33:08.446201+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | TIA/USD | 0.4368 | 59.165 | 41.754 | +1.63% | +0.48% | 3.18x | 2.3 | 2026-11-10T06:33:08.446201+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ADA/USD | 0.178742 | 55.578 | 57.215 | +0.83% | +0.22% | 0.73x | 2.9 | 2026-11-10T06:33:08.446201+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ENA/USD | 0.1543 | 48.220 | 48.473 | +0.78% | +0.59% | 0.68x | 6.5 | 2026-11-10T06:33:08.446201+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | PENGU/USD | 0.006348 | 39.995 | 32.918 | +0.54% | +0.27% | 1.57x | 4.7 | 2026-11-10T06:33:08.446201+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | CAP/USD | 0.100663 | 33.671 | 42.250 | +1.83% | +0.16% | 0.06x | 6.1 | 2026-11-10T06:33:08.446201+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 228; predictions: 2083; observations: 136954.
- Matured sampled outcomes across 1/6/24/48h: 1189; gap abstentions: 5752. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
