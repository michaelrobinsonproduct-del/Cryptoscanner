# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T00:36:45.460487+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42932471675
**Source SHA:** 9c182729094d97cd83095218ec2e91b55a348672
**Ledger commit:** f9db0384a6f15d8ac111052f48a2b2a84fcd1743
**Ledger generation:** 256 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 600; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.447e-06 | 81.949 | 61.752 | +1.36% | +1.04% | 4.97x | 5.5 | 2026-11-11T00:36:37.120558+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NEAR/USD | 3.6372 | 81.728 | 61.853 | +1.49% | +0.97% | 4.54x | 7.2 | 2026-11-11T00:36:37.120558+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | XDG/USD | 0.0683173 | 73.911 | 58.861 | +0.56% | +0.01% | 3.32x | 0.1 | 2026-11-11T00:36:37.120558+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ENA/USD | 0.1533 | 70.848 | 61.904 | +2.47% | +0.59% | 1.60x | 13.0 | 2026-11-11T00:36:37.120558+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ADA/USD | 0.174528 | 70.551 | 56.299 | +0.41% | -0.15% | 4.00x | 3.2 | 2026-11-11T00:36:37.120558+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | AAVE/USD | 123.95 | 68.678 | 53.477 | +0.46% | +0.04% | 2.85x | 0.8 | 2026-11-11T00:36:37.120558+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | LTC/USD | 50.88 | 63.156 | 49.236 | +0.35% | -0.22% | 2.57x | 2.0 | 2026-11-11T00:36:37.120558+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | LINK/USD | 10.34704 | 59.323 | 52.098 | +0.61% | -0.10% | 1.77x | 2.2 | 2026-11-11T00:36:37.120558+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | AVAX/USD | 8.396 | 57.914 | 55.133 | +0.36% | -0.36% | 1.46x | 4.8 | 2026-11-11T00:36:37.120558+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | HBAR/USD | 0.06581 | 57.408 | 42.712 | +0.43% | -0.06% | 6.89x | 3.0 | 2026-11-11T00:36:37.120558+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | UNI/USD | 6.7174 | 54.624 | 57.493 | +0.79% | +0.36% | 0.53x | 6.1 | 2026-11-11T00:36:37.120558+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | SUI/USD | 0.8266 | 52.513 | 57.629 | +0.46% | -0.06% | 0.52x | 1.2 | 2026-11-11T00:36:37.120558+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 256; predictions: 2349; observations: 153560.
- Matured sampled outcomes across 1/6/24/48h: 1528; gap abstentions: 6480. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
