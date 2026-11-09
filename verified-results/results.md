# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T01:30:50.248633+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42545850104
**Source SHA:** d46d8e77dc3cd1f97a6b375aaf3270b763ec3c09
**Ledger commit:** b149ce795a8dcfccf55c7da2baf631bda726d088
**Ledger generation:** 175 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | UAI/USD | 0.06502 | 88.473 | 68.922 | +6.02% | +2.74% | 1.58x | 23.1 | 2026-11-09T01:30:43.246573+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ENA/USD | 0.1512 | 78.101 | 64.420 | +1.82% | -0.26% | 2.51x | 6.6 | 2026-11-09T01:30:43.246573+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | SUI/USD | 0.8321 | 72.324 | 63.781 | +1.43% | -0.29% | 2.00x | 2.4 | 2026-11-09T01:30:43.246573+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | NEAR/USD | 3.5902 | 63.656 | 54.219 | +0.39% | -0.55% | 2.22x | 7.0 | 2026-11-09T01:30:43.246573+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | AAVE/USD | 127.86 | 60.643 | 50.827 | +1.52% | -0.28% | 2.12x | 5.5 | 2026-11-09T01:30:43.246573+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | PEPE/USD | 5.038e-06 | 59.221 | 63.907 | +1.84% | -0.75% | 0.91x | 7.9 | 2026-11-09T01:30:43.246573+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | SOL/USD | 86.96 | 57.811 | 58.555 | +0.59% | -0.39% | 1.12x | 1.1 | 2026-11-09T01:30:43.246573+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | XLM/USD | 0.146668 | 57.215 | 55.789 | +0.33% | -0.07% | 1.18x | 3.1 | 2026-11-09T01:30:43.246573+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ZEC/USD | 1225.05 | 55.980 | 59.727 | +1.04% | -0.52% | 0.88x | 5.1 | 2026-11-09T01:30:43.246573+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | UNI/USD | 6.8858 | 55.507 | 54.597 | +1.50% | -0.40% | 1.29x | 4.5 | 2026-11-09T01:30:43.246573+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | XDG/USD | 0.06916 | 52.364 | 57.874 | +0.41% | -0.29% | 0.60x | 0.0 | 2026-11-09T01:30:43.246573+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | DOT/USD | 0.8657 | 49.644 | 35.566 | +0.48% | -0.18% | 3.58x | 1.2 | 2026-11-09T01:30:43.246573+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 175; predictions: 1508; observations: 105758.
- Matured sampled outcomes across 1/6/24/48h: 819; gap abstentions: 4382. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
