# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T03:17:38.584688+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42555484260
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** c41775a0137698c9d7a9da302d8e562c09381c30
**Ledger generation:** 178 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.075e-06 | 62.801 | 70.156 | +2.59% | -0.67% | 0.60x | 5.9 | 2026-11-09T03:17:30.059371+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PAXG/USD | 4102.73 | 58.941 | 44.328 | +1.38% | -0.08% | 2.60x | 0.2 | 2026-11-09T03:17:30.059371+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ETH/USD | 2138.15 | 57.950 | 59.371 | +0.63% | -0.28% | 1.00x | 0.0 | 2026-11-09T03:17:30.059371+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ZEC/USD | 1228.6 | 57.841 | 61.414 | +1.34% | -0.65% | 0.97x | 5.9 | 2026-11-09T03:17:30.059371+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | UNI/USD | 6.8994 | 56.185 | 55.719 | +1.70% | -0.76% | 1.43x | 5.8 | 2026-11-09T03:17:30.059371+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ENA/USD | 0.152 | 56.090 | 64.911 | +2.36% | -0.26% | 0.25x | 13.2 | 2026-11-09T03:17:30.059371+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | XDG/USD | 0.0693505 | 55.659 | 59.457 | +0.69% | -0.95% | 1.10x | 0.7 | 2026-11-09T03:17:30.059371+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | SOL/USD | 87.33 | 55.313 | 61.553 | +1.02% | -0.71% | 0.73x | 1.1 | 2026-11-09T03:17:30.059371+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | SUI/USD | 0.8316 | 54.075 | 63.354 | +1.37% | -0.78% | 0.46x | 2.4 | 2026-11-09T03:17:30.059371+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | XBT/USD | 74935.5 | 52.983 | 56.802 | +0.26% | -0.34% | 0.79x | 0.0 | 2026-11-09T03:17:30.059371+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | XLM/USD | 0.146836 | 50.463 | 57.855 | +0.45% | -0.88% | 0.70x | 0.5 | 2026-11-09T03:17:30.059371+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | LTC/USD | 50.66 | 47.763 | 51.939 | +1.18% | -0.55% | 0.86x | 3.9 | 2026-11-09T03:17:30.059371+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 178; predictions: 1544; observations: 107576.
- Matured sampled outcomes across 1/6/24/48h: 867; gap abstentions: 4436. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
