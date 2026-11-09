# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T07:51:13.132011+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42581796436
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** 540f93d10193e492eec6936878280bb5ab6839b5
**Ledger generation:** 186 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 17.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.021e-06 | 70.232 | 61.484 | +1.50% | +0.77% | 1.49x | 8.0 | 2026-11-09T07:51:07.211590+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PAXG/USD | 4075.28 | 54.830 | 40.662 | +0.70% | -0.17% | 3.77x | 0.7 | 2026-11-09T07:51:07.211590+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | BAT/USD | 0.12205 | 50.322 | 52.005 | +3.37% | -0.09% | 0.88x | 6.6 | 2026-11-09T07:51:07.211590+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ARB/USD | 0.1708 | 46.693 | 52.913 | +2.95% | -0.12% | 0.44x | 11.7 | 2026-11-09T07:51:07.211590+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | AAVE/USD | 127.58 | 44.635 | 50.197 | +1.29% | +0.28% | 0.30x | 6.3 | 2026-11-09T07:51:07.211590+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | HBAR/USD | 0.06579 | 38.865 | 39.251 | +0.30% | +0.27% | 0.82x | 4.6 | 2026-11-09T07:51:07.211590+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | MEGA/USD | 0.05055 | 36.439 | 34.137 | +1.59% | +0.80% | 0.83x | 15.8 | 2026-11-09T07:51:07.211590+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | RENDER/USD | 1.531 | 21.017 | 27.362 | +0.39% | +0.07% | 0.33x | 19.6 | 2026-11-09T07:51:07.211590+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | CAP/USD | 0.100755 | 18.530 | 22.373 | +0.84% | +0.15% | 0.54x | 31.4 | 2026-11-09T07:51:07.211590+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 186; predictions: 1637; observations: 112424.
- Matured sampled outcomes across 1/6/24/48h: 951; gap abstentions: 4537. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
