# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T14:34:01.494256+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43039338245
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 26ed02193f62b9d0e33d1fb03506ef4a7697175b
**Ledger generation:** 284 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 605; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04522 | 85.703 | 85.796 | +7.87% | +0.24% | 0.87x | 6.6 | 2026-11-11T14:33:52.409127+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NEAR/USD | 3.7464 | 82.735 | 84.487 | +4.54% | -0.17% | 0.91x | 4.5 | 2026-11-11T14:33:52.409127+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | XMR/USD | 583.29 | 81.939 | 72.103 | +3.67% | +0.10% | 1.93x | 17.2 | 2026-11-11T14:33:52.409127+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | XLM/USD | 0.148349 | 73.817 | 64.564 | +2.60% | -1.15% | 2.73x | 4.9 | 2026-11-11T14:33:52.409127+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | TON/USD | 1.217 | 70.948 | 81.634 | +6.85% | -1.55% | 0.71x | 16.5 | 2026-11-11T14:33:52.409127+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | SUI/USD | 0.8318 | 66.428 | 62.055 | +1.09% | -0.24% | 1.56x | 1.2 | 2026-11-11T14:33:52.409127+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ADA/USD | 0.176831 | 63.485 | 64.802 | +1.74% | -0.24% | 0.99x | 4.8 | 2026-11-11T14:33:52.409127+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | AVAX/USD | 8.512 | 60.242 | 64.863 | +1.75% | -0.11% | 0.59x | 4.7 | 2026-11-11T14:33:52.409127+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | TAO/USD | 221.3515 | 59.273 | 63.775 | +1.46% | +0.02% | 0.54x | 2.9 | 2026-11-11T14:33:52.409127+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | HYPE/USD | 72.69 | 57.309 | 58.179 | +0.65% | -0.44% | 1.13x | 2.8 | 2026-11-11T14:33:52.409127+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | DOT/USD | 0.8628 | 54.609 | 53.909 | +2.41% | -0.40% | 1.27x | 2.3 | 2026-11-11T14:33:52.409127+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | LINK/USD | 10.32144 | 54.597 | 44.467 | +0.36% | -0.27% | 2.15x | 8.5 | 2026-11-11T14:33:52.409127+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 284; predictions: 2676; observations: 170433.
- Matured sampled outcomes across 1/6/24/48h: 1956; gap abstentions: 7074. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
