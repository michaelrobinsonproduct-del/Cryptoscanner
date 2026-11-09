# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T12:18:11.401854+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42615685342
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** 3eb13feb1f0769058d51a73acd8f9a3ba10dd065
**Ledger generation:** 194 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD | 0.003662 | 89.250 | 71.900 | +4.30% | +0.47% | 2.99x | 8.2 | 2026-11-09T12:18:02.477060+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AAVE/USD | 132.04 | 76.372 | 79.509 | +4.84% | +0.80% | 0.29x | 3.8 | 2026-11-09T12:18:02.477060+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | LINK/USD | 10.58631 | 70.912 | 65.921 | +1.78% | +0.50% | 1.25x | 3.1 | 2026-11-09T12:18:02.477060+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | USELESS/USD | 0.13653 | 70.589 | 69.847 | +10.88% | +0.70% | 0.73x | 27.9 | 2026-11-09T12:18:02.477060+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | PEPE/USD | 5.049e-06 | 63.210 | 68.443 | +2.06% | +0.22% | 0.37x | 2.0 | 2026-11-09T12:18:02.477060+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | LTC/USD | 51 | 62.246 | 59.661 | +1.86% | +0.39% | 1.06x | 2.0 | 2026-11-09T12:18:02.477060+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | RENDER/USD | 1.602 | 62.246 | 64.656 | +5.05% | +0.44% | 0.54x | 12.5 | 2026-11-09T12:18:02.477060+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | QNT/USD | 202.16 | 62.112 | 68.769 | +3.75% | -0.23% | 0.45x | 8.9 | 2026-11-09T12:18:02.477060+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ENA/USD | 0.1519 | 61.826 | 64.444 | +2.29% | +0.40% | 0.54x | 13.2 | 2026-11-09T12:18:02.477060+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | XLM/USD | 0.14657 | 55.999 | 54.464 | +0.26% | +0.43% | 0.94x | 4.8 | 2026-11-09T12:18:02.477060+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | XDG/USD | 0.0691711 | 54.260 | 57.373 | +0.43% | +0.42% | 0.48x | 1.2 | 2026-11-09T12:18:02.477060+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | GBP/USD | 1.34103 | 53.572 | 57.702 | +0.41% | +0.00% | 0.59x | 0.3 | 2026-11-09T12:18:02.477060+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 194; predictions: 1731; observations: 117272.
- Matured sampled outcomes across 1/6/24/48h: 963; gap abstentions: 4745. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
