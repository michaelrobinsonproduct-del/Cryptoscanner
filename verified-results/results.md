# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T04:43:03.832925+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42563248481
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** 2d6c3e2bb2663aa2126b19c1a5ced9d94de90e21
**Ledger generation:** 181 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | USELESS/USD | 0.1283 | 87.880 | 63.261 | +4.20% | +1.92% | 3.39x | 10.1 | 2026-11-09T04:42:55.552656+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | SOL/USD | 87.29 | 77.431 | 61.229 | +0.97% | +0.24% | 2.54x | 1.1 | 2026-11-09T04:42:55.552656+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | LINK/USD | 10.56882 | 75.505 | 59.611 | +1.61% | +0.18% | 5.64x | 4.6 | 2026-11-09T04:42:55.552656+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ENA/USD | 0.1526 | 71.101 | 71.046 | +2.76% | +0.39% | 0.81x | 6.6 | 2026-11-09T04:42:55.552656+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | PEPE/USD | 5.033e-06 | 67.478 | 64.189 | +1.74% | +0.34% | 1.16x | 6.0 | 2026-11-09T04:42:55.552656+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | SUI/USD | 0.8317 | 66.080 | 63.439 | +1.38% | +0.08% | 1.22x | 2.4 | 2026-11-09T04:42:55.552656+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ETH/USD | 2135.57 | 63.677 | 58.521 | +0.51% | -0.06% | 1.54x | 0.0 | 2026-11-09T04:42:55.552656+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ZEC/USD | 1228.82 | 62.191 | 61.625 | +1.35% | +0.51% | 0.80x | 5.7 | 2026-11-09T04:42:55.552656+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | XDG/USD | 0.0695034 | 61.925 | 61.364 | +0.91% | +0.11% | 1.00x | 0.0 | 2026-11-09T04:42:55.552656+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | AVAX/USD | 8 | 61.568 | 45.133 | +0.90% | +0.29% | 2.68x | 2.5 | 2026-11-09T04:42:55.552656+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | XLM/USD | 0.146804 | 57.983 | 57.940 | +0.42% | +0.08% | 0.97x | 0.1 | 2026-11-09T04:42:55.552656+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | TAO/USD | 217.378 | 56.651 | 54.741 | +0.28% | +0.49% | 0.95x | 4.5 | 2026-11-09T04:42:55.552656+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 181; predictions: 1580; observations: 109394.
- Matured sampled outcomes across 1/6/24/48h: 879; gap abstentions: 4471. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
