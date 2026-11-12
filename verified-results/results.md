# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T11:07:14.382091+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43205886405
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 3eefd66655ba885df1ba04c7fb5ea5b83f2b87b9
**Ledger generation:** 326 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 21.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.236 | 73.562 | 77.073 | +5.37% | -0.40% | 0.85x | 8.1 | 2026-11-12T11:07:08.404810+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ZEC/USD | 991.74 | 72.897 | 75.415 | +3.09% | +0.46% | 0.52x | 2.4 | 2026-11-12T11:07:08.404810+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | XDC/USD | 0.02988 | 68.908 | 53.406 | +2.82% | +0.10% | 11.53x | 13.4 | 2026-11-12T11:07:08.404810+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | AKE/USD | 0.00263737 | 55.832 | 63.309 | +6.46% | -0.31% | 0.40x | 30.4 | 2026-11-12T11:07:08.404810+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | JUP/USD | 0.25782 | 40.653 | 32.905 | +1.04% | +0.58% | 1.48x | 14.4 | 2026-11-12T11:07:08.404810+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | CAP/USD | 0.102359 | 39.148 | 41.645 | +1.88% | +0.84% | 0.33x | 6.1 | 2026-11-12T11:07:08.404810+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | HBAR/USD | 0.0658 | 31.928 | 37.725 | +0.66% | -0.27% | 0.56x | 4.6 | 2026-11-12T11:07:08.404810+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 326; predictions: 3076; observations: 195873.
- Matured sampled outcomes across 1/6/24/48h: 2636; gap abstentions: 8058. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
