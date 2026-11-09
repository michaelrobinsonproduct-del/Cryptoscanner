# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T00:52:35.264221+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42542467553
**Source SHA:** 9f804965dcd9160d6e3cd3448395ca97d0a35c94
**Ledger commit:** c06daa8ce8c9a8691623d1b6e4f4363329d3ae58
**Ledger generation:** 173 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.6176 | 78.563 | 61.128 | +1.15% | +0.49% | 6.76x | 3.9 | 2026-11-09T00:52:26.670159+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | XDG/USD | 0.069416 | 70.706 | 60.476 | +0.78% | +0.05% | 2.00x | 0.0 | 2026-11-09T00:52:26.670159+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ZEC/USD | 1232.63 | 66.229 | 64.281 | +1.67% | +0.19% | 1.10x | 4.8 | 2026-11-09T00:52:26.670159+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | PEPE/USD | 5.083e-06 | 63.379 | 70.299 | +2.75% | +0.18% | 0.22x | 7.9 | 2026-11-09T00:52:26.670159+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | SUI/USD | 0.8353 | 61.118 | 67.115 | +1.82% | +0.46% | 0.17x | 1.2 | 2026-11-09T00:52:26.670159+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ENA/USD | 0.1515 | 60.700 | 65.843 | +2.02% | +0.33% | 0.32x | 6.6 | 2026-11-09T00:52:26.670159+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | XLM/USD | 0.14746 | 58.408 | 59.657 | +0.87% | -0.05% | 0.90x | 2.9 | 2026-11-09T00:52:26.670159+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | SOL/USD | 87.36 | 58.260 | 61.796 | +1.05% | +0.07% | 0.61x | 1.1 | 2026-11-09T00:52:26.670159+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ETH/USD | 2142.95 | 55.878 | 60.953 | +0.85% | +0.04% | 0.47x | 0.0 | 2026-11-09T00:52:26.670159+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | HYPE/USD | 75.02 | 54.896 | 59.504 | +0.74% | -0.07% | 0.57x | 1.3 | 2026-11-09T00:52:26.670159+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | XRP/USD | 1.11971 | 53.954 | 59.790 | +0.69% | -0.09% | 0.46x | 0.1 | 2026-11-09T00:52:26.670159+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | XBT/USD | 75129 | 49.584 | 58.614 | +0.52% | +0.04% | 0.08x | 0.0 | 2026-11-09T00:52:26.670159+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 173; predictions: 1484; observations: 104546.
- Matured sampled outcomes across 1/6/24/48h: 814; gap abstentions: 4371. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
