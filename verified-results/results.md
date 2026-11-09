# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T04:14:21.367767+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42560576117
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** 4c9f08f5afdf6c8ad91b9d54fbeef321ec118e34
**Ledger generation:** 180 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ENA/USD | 0.1535 | 79.337 | 75.310 | +3.37% | +0.52% | 1.14x | 6.5 | 2026-11-09T04:14:15.113076+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | LTC/USD | 51.08 | 72.414 | 58.995 | +2.02% | +0.20% | 2.24x | 2.0 | 2026-11-09T04:14:15.113076+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | PEPE/USD | 5.072e-06 | 70.309 | 68.747 | +2.53% | -0.35% | 1.33x | 7.9 | 2026-11-09T04:14:15.113076+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | HBAR/USD | 0.06694 | 68.212 | 52.239 | +2.06% | +0.19% | 2.63x | 3.0 | 2026-11-09T04:14:15.113076+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ZEC/USD | 1232.66 | 66.200 | 64.663 | +1.67% | -0.22% | 1.26x | 4.1 | 2026-11-09T04:14:15.113076+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | SUI/USD | 0.8355 | 65.286 | 67.285 | +1.84% | +0.20% | 0.70x | 1.2 | 2026-11-09T04:14:15.113076+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | NEAR/USD | 3.6241 | 61.202 | 62.957 | +1.33% | +0.33% | 0.66x | 2.8 | 2026-11-09T04:14:15.113076+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | XLM/USD | 0.14749 | 61.167 | 60.547 | +0.89% | +0.22% | 0.95x | 1.4 | 2026-11-09T04:14:15.113076+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | XDG/USD | 0.0696835 | 59.739 | 63.194 | +1.17% | +0.23% | 0.54x | 0.0 | 2026-11-09T04:14:15.113076+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | SOL/USD | 87.59 | 58.046 | 63.660 | +1.32% | -0.02% | 0.45x | 1.1 | 2026-11-09T04:14:15.113076+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | LINK/USD | 10.60134 | 55.240 | 61.958 | +1.92% | +0.10% | 0.28x | 3.7 | 2026-11-09T04:14:15.113076+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | XBT/USD | 74941.2 | 53.444 | 56.855 | +0.27% | +0.08% | 0.62x | 0.0 | 2026-11-09T04:14:15.113076+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 180; predictions: 1568; observations: 108788.
- Matured sampled outcomes across 1/6/24/48h: 867; gap abstentions: 4466. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
