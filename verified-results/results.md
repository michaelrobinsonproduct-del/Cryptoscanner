# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-13T12:01:42.557268+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43421671558
**Source SHA:** 8aeef60280dc5ad603844a3cdf110b67a2160ee2
**Previous ledger commit:** 1e4d68e244ae6f13782ef2535bf98ed7b78b9dd3 (atomic ledger/results publication)
**Ledger generation:** 358 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.551 | 93.910 | 80.566 | +3.83% | -0.33% | 7.78x | 2.5 | 2026-11-13T12:01:35.784006+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ZEC/USD | 958.79 | 68.784 | 55.865 | +0.30% | -0.29% | 2.44x | 2.5 | 2026-11-13T12:01:35.784006+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | INJ/USD | 7.746 | 66.082 | 73.279 | +3.83% | -0.54% | 0.55x | 7.8 | 2026-11-13T12:01:35.784006+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | HYPE/USD | 73.88 | 61.707 | 65.302 | +1.67% | +0.14% | 0.57x | 2.7 | 2026-11-13T12:01:35.784006+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | VVV/USD | 19.15 | 58.757 | 43.285 | +0.83% | +0.09% | 3.98x | 7.3 | 2026-11-13T12:01:35.784006+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ZRO/USD | 1.6 | 50.147 | 54.767 | +3.03% | -0.06% | 0.57x | 12.5 | 2026-11-13T12:01:35.784006+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | AVAX/USD | 8.395 | 49.565 | 58.261 | +0.55% | -0.27% | 0.27x | 1.2 | 2026-11-13T12:01:35.784006+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | RENDER/USD | 1.528 | 46.949 | 31.622 | +0.39% | +0.07% | 19.22x | 13.1 | 2026-11-13T12:01:35.784006+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ICNT/USD | 0.2867 | 46.176 | 53.862 | +3.99% | -0.10% | 0.28x | 10.5 | 2026-11-13T12:01:35.784006+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | CAP/USD | 0.108103 | 45.133 | 49.283 | +4.38% | +0.84% | 0.16x | 32.3 | 2026-11-13T12:01:35.784006+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | ICP/USD | 2.598 | 43.041 | 36.767 | +0.93% | +0.27% | 1.49x | 11.6 | 2026-11-13T12:01:35.784006+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | TON/USD | 1.151 | 41.976 | 48.916 | +0.96% | +0.00% | 0.31x | 8.7 | 2026-11-13T12:01:35.784006+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 358; predictions: 3302; observations: 215264.
- Matured sampled outcomes across 1/6/24/48h: 2926; gap abstentions: 9252. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
