# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T00:57:53.344886+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=20,50 * * * *, intended UTC minute=20,50; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42935161242
**Source SHA:** 9c182729094d97cd83095218ec2e91b55a348672
**Ledger commit:** 02149c2b1813f480c44c7944fe33747abc8cb3e1
**Ledger generation:** 257 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 600; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.6231 | 72.151 | 59.914 | +1.10% | -0.47% | 2.46x | 5.5 | 2026-11-11T00:57:46.573650+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | UNI/USD | 6.6996 | 69.239 | 56.957 | +0.53% | -0.54% | 28.99x | 3.4 | 2026-11-11T00:57:46.573650+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ENA/USD | 0.1519 | 66.812 | 58.950 | +1.54% | -1.43% | 6.96x | 6.6 | 2026-11-11T00:57:46.573650+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | AAVE/USD | 124.09 | 66.246 | 54.429 | +0.58% | -0.13% | 2.25x | 0.8 | 2026-11-11T00:57:46.573650+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | XDG/USD | 0.0682252 | 59.549 | 57.934 | +0.42% | -0.28% | 1.30x | 0.0 | 2026-11-11T00:57:46.573650+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ADA/USD | 0.174709 | 55.416 | 56.772 | +0.52% | -0.05% | 0.89x | 3.7 | 2026-11-11T00:57:46.573650+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | SUI/USD | 0.8262 | 55.328 | 57.287 | +0.41% | -0.40% | 1.00x | 1.2 | 2026-11-11T00:57:46.573650+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | AVAX/USD | 8.416 | 49.837 | 56.807 | +0.60% | -0.27% | 0.44x | 4.8 | 2026-11-11T00:57:46.573650+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | LINK/USD | 10.32891 | 49.287 | 50.264 | +0.44% | -0.24% | 1.02x | 3.4 | 2026-11-11T00:57:46.573650+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | PEPE/USD | 5.402e-06 | 46.658 | 56.796 | +0.52% | -0.53% | 0.25x | 3.7 | 2026-11-11T00:57:46.573650+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | HBAR/USD | 0.06589 | 42.255 | 43.531 | +0.55% | -0.09% | 0.92x | 3.0 | 2026-11-11T00:57:46.573650+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | ARB/USD | 0.1614 | 41.754 | 41.715 | +0.62% | +0.25% | 0.88x | 6.2 | 2026-11-11T00:57:46.573650+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 257; predictions: 2361; observations: 154160.
- Matured sampled outcomes across 1/6/24/48h: 1547; gap abstentions: 6480. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
