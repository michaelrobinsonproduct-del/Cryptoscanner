# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T11:06:56.789513+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43008893253
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** b45c8b9290858c3b1e288fc729da8d6a2c185e9f
**Ledger generation:** 277 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 603; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AVAX/USD | 8.651 | 80.222 | 76.534 | +3.41% | -0.40% | 1.57x | 4.6 | 2026-11-11T11:06:50.785913+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | XLM/USD | 0.147431 | 74.802 | 61.768 | +1.97% | -0.39% | 11.70x | 2.7 | 2026-11-11T11:06:50.785913+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | PUMP/USD | 0.003577 | 68.292 | 57.911 | +1.85% | +0.08% | 2.00x | 14.0 | 2026-11-11T11:06:50.785913+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | NIGHT/USD | 0.04414 | 67.275 | 76.986 | +5.30% | -0.29% | 0.18x | 9.1 | 2026-11-11T11:06:50.785913+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | SOL/USD | 83.69 | 64.375 | 58.187 | +0.54% | +0.17% | 1.54x | 1.2 | 2026-11-11T11:06:50.785913+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XMR/USD | 576.62 | 62.471 | 69.357 | +2.48% | -0.06% | 0.34x | 6.1 | 2026-11-11T11:06:50.785913+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ETH/USD | 2057 | 60.229 | 57.143 | +0.31% | +0.10% | 1.26x | 0.0 | 2026-11-11T11:06:50.785913+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | XRP/USD | 1.06088 | 59.904 | 57.932 | +0.55% | -0.00% | 1.20x | 1.8 | 2026-11-11T11:06:50.785913+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | NEAR/USD | 3.643 | 58.939 | 62.581 | +1.65% | +0.28% | 0.50x | 8.0 | 2026-11-11T11:06:50.785913+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | TON/USD | 1.191 | 58.820 | 59.952 | +4.57% | -0.83% | 1.30x | 25.3 | 2026-11-11T11:06:50.785913+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | HYPE/USD | 72.48 | 58.045 | 56.830 | +0.36% | +0.04% | 1.10x | 1.4 | 2026-11-11T11:06:50.785913+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | ADA/USD | 0.176083 | 54.933 | 62.264 | +1.31% | -0.18% | 0.36x | 3.8 | 2026-11-11T11:06:50.785913+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 277; predictions: 2592; observations: 166204.
- Matured sampled outcomes across 1/6/24/48h: 1873; gap abstentions: 6883. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
