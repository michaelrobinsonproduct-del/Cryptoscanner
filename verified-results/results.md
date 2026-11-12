# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T14:33:53.361969+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43237955499
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 6cb2ce562bee7017526c0c0d7b3895366e32cb44
**Ledger generation:** 333 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 9.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.226 | 75.499 | 70.958 | +4.52% | -0.89% | 1.90x | 8.2 | 2026-11-12T14:33:50.723775+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ZEC/USD | 968.06 | 66.207 | 56.193 | +0.63% | -1.00% | 5.52x | 6.4 | 2026-11-12T14:33:50.723775+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | BAT/USD | 0.1215 | 56.612 | 49.684 | +3.20% | +0.67% | 1.36x | 11.5 | 2026-11-12T14:33:50.723775+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | CAP/USD | 0.10119 | 44.724 | 33.816 | +0.71% | +0.22% | 1.98x | 4.8 | 2026-11-12T14:33:50.723775+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | XDC/USD | 0.0293 | 40.536 | 38.183 | +0.83% | +0.37% | 1.05x | 17.1 | 2026-11-12T14:33:50.723775+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | MON/USD | 0.01675 | 38.788 | 30.634 | +0.54% | -1.37% | 2.82x | 12.0 | 2026-11-12T14:33:50.723775+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | MEGA/USD | 0.04547 | 38.481 | 29.166 | +1.50% | -0.26% | 2.06x | 26.4 | 2026-11-12T14:33:50.723775+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ATOM/USD | 1.3992 | 27.725 | 31.990 | +0.41% | +0.11% | 0.52x | 5.7 | 2026-11-12T14:33:50.723775+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | JUP/USD | 0.25587 | 19.753 | 26.663 | +0.27% | -0.63% | 0.63x | 17.2 | 2026-11-12T14:33:50.723775+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 333; predictions: 3113; observations: 200114.
- Matured sampled outcomes across 1/6/24/48h: 2722; gap abstentions: 8184. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 0; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
