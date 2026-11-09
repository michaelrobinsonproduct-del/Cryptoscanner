# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T03:41:38.452399+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42557689415
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** 173cc46951bc095f739e148016bacfa8b0ca402b
**Ledger generation:** 179 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AAVE/USD | 129.58 | 73.851 | 59.929 | +2.88% | -0.22% | 3.85x | 6.2 | 2026-11-09T03:41:30.268290+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 5.096e-06 | 72.061 | 73.140 | +3.01% | +0.71% | 0.54x | 5.9 | 2026-11-09T03:41:30.268290+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ENA/USD | 0.1525 | 68.620 | 70.579 | +2.69% | +0.33% | 0.64x | 6.6 | 2026-11-09T03:41:30.268290+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | SUI/USD | 0.8344 | 65.849 | 65.748 | +1.71% | +0.08% | 0.97x | 2.4 | 2026-11-09T03:41:30.268290+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ETH/USD | 2141.71 | 65.631 | 60.544 | +0.80% | -0.02% | 1.52x | 0.0 | 2026-11-09T03:41:30.268290+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | UNI/USD | 6.9424 | 65.418 | 63.007 | +2.34% | +0.32% | 1.08x | 0.6 | 2026-11-09T03:41:30.268290+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | SOL/USD | 87.65 | 65.124 | 64.146 | +1.39% | +0.07% | 1.06x | 1.1 | 2026-11-09T03:41:30.268290+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | LINK/USD | 10.5713 | 63.627 | 60.190 | +1.63% | +0.29% | 1.20x | 3.0 | 2026-11-09T03:41:30.268290+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | PAXG/USD | 4105.12 | 59.908 | 45.114 | +1.44% | -0.04% | 3.94x | 0.6 | 2026-11-09T03:41:30.268290+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | XLM/USD | 0.147254 | 59.714 | 60.094 | +0.73% | +0.18% | 0.87x | 0.1 | 2026-11-09T03:41:30.268290+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | ZEC/USD | 1232.63 | 59.364 | 65.255 | +1.67% | +0.20% | 0.31x | 2.8 | 2026-11-09T03:41:30.268290+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | LTC/USD | 50.93 | 57.674 | 56.752 | +1.72% | +0.20% | 0.99x | 2.0 | 2026-11-09T03:41:30.268290+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 179; predictions: 1556; observations: 108182.
- Matured sampled outcomes across 1/6/24/48h: 867; gap abstentions: 4449. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
