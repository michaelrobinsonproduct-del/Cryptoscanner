# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T12:48:38.670243+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42818660864
**Source SHA:** 46df1627878352d4e4822ef888168ae0fa7d40b6
**Ledger commit:** 54de83e40ae96bf97668c32b80d9a6e16640d06e
**Ledger generation:** 232 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 583; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.281e-06 | 88.989 | 75.783 | +3.10% | -0.36% | 3.60x | 1.9 | 2026-11-10T12:48:30.509769+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | TON/USD | 1.107 | 79.475 | 66.056 | +6.44% | +1.01% | 1.83x | 27.2 | 2026-11-10T12:48:30.509769+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NIGHT/USD | 0.04205 | 65.534 | 62.281 | +3.88% | +0.38% | 1.13x | 7.1 | 2026-11-10T12:48:30.509769+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | XDC/USD | 0.0309 | 65.060 | 68.054 | +4.85% | -0.51% | 0.96x | 9.7 | 2026-11-10T12:48:30.509769+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | CAP/USD | 0.10268 | 59.350 | 56.263 | +3.87% | +0.07% | 1.27x | 6.1 | 2026-11-10T12:48:30.509769+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | UAI/USD | 0.04109 | 54.203 | 61.375 | +6.56% | -0.99% | 0.78x | 34.1 | 2026-11-10T12:48:30.509769+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ENA/USD | 0.1535 | 51.112 | 41.546 | +0.26% | -0.13% | 2.02x | 6.5 | 2026-11-10T12:48:30.509769+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | TRX/USD | 0.318601 | 34.097 | 40.004 | +0.39% | -0.01% | 0.41x | 1.1 | 2026-11-10T12:48:30.509769+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ATOM/USD | 1.3807 | 26.515 | 30.805 | +0.72% | -0.12% | 0.63x | 10.9 | 2026-11-10T12:48:30.509769+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | STABLE/USD | 0.0291 | 9.693 | 19.577 | +0.34% | -0.44% | 0.23x | 27.5 | 2026-11-10T12:48:30.509769+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 232; predictions: 2121; observations: 139254.
- Matured sampled outcomes across 1/6/24/48h: 1189; gap abstentions: 6010. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
