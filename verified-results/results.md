# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-13T17:31:08.436388+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43473490990
**Source SHA:** 9df68d00c09d9e96abd2a328b39d1b6b7c76a7bb
**Previous ledger commit:** 21d7c432749ae547923248a6c305249ee70ff5bf (atomic ledger/results publication)
**Ledger generation:** 363 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 21.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 8.129 | 91.115 | 94.452 | +8.97% | -0.09% | 0.71x | 11.1 | 2026-11-13T17:31:00.832634+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ZBCN/USD | 0.001849 | 89.862 | 73.961 | +8.26% | +0.87% | 2.15x | 5.4 | 2026-11-13T17:31:00.832634+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NEAR/USD | 3.5096 | 71.257 | 71.367 | +2.62% | -0.05% | 1.01x | 4.0 | 2026-11-13T17:31:00.832634+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | GRT/USD | 0.01798 | 56.301 | 32.826 | +2.22% | +1.69% | 2.76x | 27.9 | 2026-11-13T17:31:00.832634+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | TAO/USD | 214.8712 | 55.655 | 61.223 | +1.40% | -0.19% | 0.54x | 7.1 | 2026-11-13T17:31:00.832634+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | UAI/USD | 0.03814 | 52.541 | 64.047 | +5.74% | -2.49% | 1.10x | 15.8 | 2026-11-13T17:31:00.832634+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ZEUS/USD | 0.00603 | 50.777 | 60.446 | +8.65% | -1.47% | 0.77x | 33.3 | 2026-11-13T17:31:00.832634+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | Q/USD | 0.029903 | 49.933 | 41.892 | +3.85% | -0.33% | 1.97x | 37.0 | 2026-11-13T17:31:00.832634+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | UP/USD | 0.05567 | 49.150 | 31.309 | +1.03% | +0.61% | 2.48x | 14.4 | 2026-11-13T17:31:00.832634+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | PEARL/USD | 1.4706 | 44.762 | 46.579 | +3.03% | -0.41% | 1.02x | 10.9 | 2026-11-13T17:31:00.832634+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | CT/USD | 0.1104 | 27.072 | 32.259 | +2.13% | -0.63% | 0.80x | 27.3 | 2026-11-13T17:31:00.832634+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 363; predictions: 3358; observations: 218297.
- Matured sampled outcomes across 1/6/24/48h: 2938; gap abstentions: 9550. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
