# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T02:48:51.043152+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42552879029
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** 3c1f0c11a9c9a430248bfc4c6ef31d8da167800d
**Ledger generation:** 177 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ENA/USD | 0.1531 | 85.013 | 73.413 | +3.10% | +0.07% | 2.13x | 6.5 | 2026-11-09T02:48:43.984189+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | XDG/USD | 0.0700595 | 82.261 | 66.573 | +1.72% | +0.14% | 3.41x | 0.9 | 2026-11-09T02:48:43.984189+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NEAR/USD | 3.6446 | 79.830 | 65.461 | +1.91% | -0.13% | 6.49x | 5.8 | 2026-11-09T02:48:43.984189+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | SUI/USD | 0.8394 | 78.329 | 70.615 | +2.32% | +0.05% | 1.75x | 1.2 | 2026-11-09T02:48:43.984189+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ZEC/USD | 1235.33 | 77.912 | 66.168 | +1.89% | -0.31% | 2.33x | 4.1 | 2026-11-09T02:48:43.984189+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XBT/USD | 75226.4 | 73.769 | 59.526 | +0.65% | -0.15% | 6.00x | 0.0 | 2026-11-09T02:48:43.984189+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | XLM/USD | 0.14831 | 72.133 | 63.802 | +1.46% | +0.11% | 1.78x | 2.8 | 2026-11-09T02:48:43.984189+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | PEPE/USD | 5.103e-06 | 67.474 | 73.153 | +3.15% | -0.25% | 0.56x | 7.8 | 2026-11-09T02:48:43.984189+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | USELESS/USD | 0.13 | 66.837 | 71.847 | +5.58% | +0.66% | 0.17x | 12.4 | 2026-11-09T02:48:43.984189+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | ETH/USD | 2148.42 | 64.126 | 62.755 | +1.11% | -0.05% | 1.16x | 0.0 | 2026-11-09T02:48:43.984189+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | AERO/USD | 0.5819 | 61.112 | 46.455 | +1.73% | -0.07% | 118.05x | 1.7 | 2026-11-09T02:48:43.984189+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | SOL/USD | 88.02 | 60.564 | 66.576 | +1.82% | +0.03% | 0.38x | 2.3 | 2026-11-09T02:48:43.984189+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 177; predictions: 1532; observations: 106970.
- Matured sampled outcomes across 1/6/24/48h: 867; gap abstentions: 4394. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
