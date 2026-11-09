# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T11:42:16.735830+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42610977052
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** 0ec7c7a33d6d1a7024bdbfda3a5cc285a95bf7f7
**Ledger generation:** 193 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ARB/USD | 0.178 | 97.501 | 82.221 | +7.29% | +0.06% | 4.49x | 5.6 | 2026-11-09T11:42:09.408312+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AAVE/USD | 131.5 | 91.103 | 75.570 | +4.41% | +0.11% | 4.45x | 5.3 | 2026-11-09T11:42:09.408312+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | QNT/USD | 201.82 | 82.033 | 67.380 | +3.58% | -0.07% | 6.75x | 7.9 | 2026-11-09T11:42:09.408312+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | PUMP/USD | 0.00364 | 81.142 | 65.454 | +3.67% | +0.14% | 5.26x | 11.0 | 2026-11-09T11:42:09.408312+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | AKE/USD | 0.00569525 | 76.984 | 69.981 | +8.69% | +0.91% | 1.25x | 20.2 | 2026-11-09T11:42:09.408312+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | PEPE/USD | 5.035e-06 | 76.906 | 64.471 | +1.78% | -0.51% | 2.69x | 6.0 | 2026-11-09T11:42:09.408312+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | LINK/USD | 10.51926 | 76.859 | 60.675 | +1.13% | +0.24% | 6.29x | 4.5 | 2026-11-09T11:42:09.408312+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ENA/USD | 0.151 | 71.568 | 63.471 | +1.68% | -0.20% | 1.91x | 6.6 | 2026-11-09T11:42:09.408312+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | SUI/USD | 0.8277 | 66.041 | 60.017 | +0.89% | -0.07% | 1.64x | 2.4 | 2026-11-09T11:42:09.408312+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | PAXG/USD | 4096.86 | 60.965 | 44.890 | +1.23% | +0.22% | 2.53x | 3.3 | 2026-11-09T11:42:09.408312+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | HBAR/USD | 0.06732 | 56.032 | 55.920 | +2.64% | +0.16% | 0.93x | 4.5 | 2026-11-09T11:42:09.408312+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | GBP/USD | 1.3418 | 54.525 | 58.106 | +0.47% | +0.01% | 0.64x | 0.3 | 2026-11-09T11:42:09.408312+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 193; predictions: 1719; observations: 116666.
- Matured sampled outcomes across 1/6/24/48h: 963; gap abstentions: 4716. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
