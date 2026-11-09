# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T19:46:29.766159+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42686318137
**Source SHA:** 69b32fce88f9296ad7d9292e14e64b61178763c7
**Ledger commit:** e4b19d7e61f61b0dde2f143be00ddf34409cf30c
**Ledger generation:** 207 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AVAX/USD | 8.552 | 115.029 | 95.906 | +7.86% | +0.82% | 2.80x | 8.2 | 2026-11-09T19:46:22.791229+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ENA/USD | 0.1566 | 107.158 | 89.989 | +5.45% | +1.36% | 2.04x | 6.4 | 2026-11-09T19:46:22.791229+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ONDO/USD | 0.37652 | 106.843 | 99.867 | +7.09% | +1.25% | 1.07x | 0.3 | 2026-11-09T19:46:22.791229+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | PEPE/USD | 5.142e-06 | 100.244 | 81.620 | +3.94% | +0.72% | 2.60x | 1.9 | 2026-11-09T19:46:22.791229+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | UNI/USD | 7.0893 | 99.866 | 84.326 | +4.50% | +1.34% | 1.88x | 4.4 | 2026-11-09T19:46:22.791229+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ARB/USD | 0.1778 | 99.545 | 82.854 | +7.17% | +0.34% | 8.65x | 11.3 | 2026-11-09T19:46:22.791229+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | TAO/USD | 224.8775 | 99.013 | 81.207 | +3.74% | +0.56% | 2.62x | 0.0 | 2026-11-09T19:46:22.791229+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | SUI/USD | 0.8526 | 92.951 | 81.888 | +3.92% | +0.83% | 1.69x | 1.2 | 2026-11-09T19:46:22.791229+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | PAXG/USD | 4110.8 | 83.327 | 65.988 | +1.58% | +0.47% | 3.06x | 0.1 | 2026-11-09T19:46:22.791229+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | XDG/USD | 0.0701568 | 78.863 | 68.005 | +1.86% | +0.73% | 1.72x | 0.0 | 2026-11-09T19:46:22.791229+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | ETH/USD | 2131.85 | 76.057 | 57.296 | +0.33% | +0.75% | 4.67x | 0.0 | 2026-11-09T19:46:22.791229+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | MON/USD | 0.01694 | 74.580 | 79.429 | +7.90% | +0.65% | 0.19x | 5.9 | 2026-11-09T19:46:22.791229+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 207; predictions: 1887; observations: 125149.
- Matured sampled outcomes across 1/6/24/48h: 1081; gap abstentions: 5085. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
