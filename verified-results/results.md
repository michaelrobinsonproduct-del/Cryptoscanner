# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T08:44:49.772501+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42588075767
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** 2fd4c44e7ba4dfe68a199119b3b16f66963d373c
**Ledger generation:** 187 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.106e-06 | 88.092 | 74.559 | +3.21% | -0.29% | 4.57x | 5.9 | 2026-11-09T08:44:41.720155+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AAVE/USD | 129.59 | 79.876 | 63.601 | +2.89% | +0.26% | 10.39x | 4.6 | 2026-11-09T08:44:41.720155+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | RSR/USD | 0.001759 | 78.596 | 64.419 | +6.35% | +1.62% | 1.61x | 22.9 | 2026-11-09T08:44:41.720155+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | QNT/USD | 199.39 | 77.300 | 58.306 | +2.33% | +0.80% | 3.29x | 5.0 | 2026-11-09T08:44:41.720155+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | RENDER/USD | 1.573 | 63.194 | 47.133 | +3.15% | +0.58% | 2.32x | 19.1 | 2026-11-09T08:44:41.720155+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | GBP/USD | 1.3411 | 62.212 | 57.664 | +0.41% | +0.00% | 1.45x | 0.4 | 2026-11-09T08:44:41.720155+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | CAP/USD | 0.102131 | 60.357 | 44.928 | +2.21% | +0.09% | 3.91x | 5.7 | 2026-11-09T08:44:41.720155+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | PAXG/USD | 4087.01 | 58.057 | 42.622 | +0.99% | +0.09% | 3.47x | 1.5 | 2026-11-09T08:44:41.720155+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | LTC/USD | 50.56 | 55.310 | 50.920 | +0.98% | -0.24% | 1.56x | 4.0 | 2026-11-09T08:44:41.720155+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | ENA/USD | 0.1492 | 50.224 | 54.949 | +0.47% | -0.13% | 0.59x | 6.7 | 2026-11-09T08:44:41.720155+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | TIA/USD | 0.4159 | 49.739 | 36.301 | +1.02% | -0.31% | 5.55x | 4.8 | 2026-11-09T08:44:41.720155+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | AUD/USD | 0.68998 | 44.825 | 42.777 | +0.46% | +0.05% | 1.18x | 1.7 | 2026-11-09T08:44:41.720155+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 187; predictions: 1649; observations: 113030.
- Matured sampled outcomes across 1/6/24/48h: 951; gap abstentions: 4604. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
