# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T18:10:10.751616+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43276533427
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** c6fd06375d26196b6f254adb3158353f3fcdeb89
**Ledger generation:** 340 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 15.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.01752 | 65.217 | 64.152 | +5.16% | +0.00% | 1.11x | 11.4 | 2026-11-12T18:10:05.576286+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | TIA/USD | 0.4155 | 54.028 | 37.338 | +0.27% | +0.34% | 5.82x | 2.4 | 2026-11-12T18:10:05.576286+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | TON/USD | 1.206 | 48.835 | 56.294 | +2.81% | -2.27% | 1.39x | 16.6 | 2026-11-12T18:10:05.576286+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | BAT/USD | 0.12109 | 47.592 | 50.751 | +2.85% | +0.98% | 0.20x | 5.0 | 2026-11-12T18:10:05.576286+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | JUP/USD | 0.26217 | 41.879 | 44.565 | +2.74% | +0.54% | 0.46x | 15.3 | 2026-11-12T18:10:05.576286+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | MEGA/USD | 0.04594 | 35.465 | 40.977 | +2.54% | +0.31% | 0.30x | 17.5 | 2026-11-12T18:10:05.576286+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | XDC/USD | 0.02941 | 33.529 | 42.172 | +1.20% | -0.07% | 0.17x | 13.6 | 2026-11-12T18:10:05.576286+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ATOM/USD | 1.4128 | 32.705 | 37.396 | +1.39% | -0.25% | 0.65x | 9.2 | 2026-11-12T18:10:05.576286+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 340; predictions: 3157; observations: 204356.
- Matured sampled outcomes across 1/6/24/48h: 2810; gap abstentions: 8358. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
