# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T18:35:08.107674+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42876452494
**Source SHA:** a401ca9b3fa5588c6780befb93e5eb91f2431f0f
**Ledger commit:** cc3e54a889124b8c1de2b5a81021b85ef6f1e8cb
**Ledger generation:** 244 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 599; OHLC screened: 23.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.297e-06 | 73.433 | 77.029 | +3.42% | +0.68% | 0.30x | 3.8 | 2026-11-10T18:35:00.078676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NIGHT/USD | 0.04204 | 73.349 | 68.592 | +3.85% | +0.48% | 1.24x | 4.8 | 2026-11-10T18:35:00.078676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | TON/USD | 1.104 | 63.084 | 73.161 | +6.15% | -0.45% | 0.22x | 9.1 | 2026-11-10T18:35:00.078676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | XDC/USD | 0.0301 | 57.731 | 53.609 | +2.14% | +0.40% | 1.21x | 3.3 | 2026-11-10T18:35:00.078676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | CAP/USD | 0.103017 | 54.563 | 60.473 | +4.21% | -0.85% | 0.83x | 15.4 | 2026-11-10T18:35:00.078676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | UAI/USD | 0.04035 | 44.552 | 48.383 | +4.64% | -0.10% | 0.67x | 34.8 | 2026-11-10T18:35:00.078676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | LIGHTER/USD | 3.354 | 43.631 | 50.643 | +3.74% | +0.03% | 0.28x | 20.9 | 2026-11-10T18:35:00.078676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ZRO/USD | 1.484 | 39.144 | 38.698 | +0.54% | +1.57% | 0.26x | 20.3 | 2026-11-10T18:35:00.078676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | SYRUP/USD | 0.1364 | 38.724 | 27.338 | +0.67% | +0.64% | 1.82x | 16.9 | 2026-11-10T18:35:00.078676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | MEGA/USD | 0.05112 | 35.774 | 35.644 | +2.67% | +0.83% | 0.60x | 31.4 | 2026-11-10T18:35:00.078676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | STX/USD | 0.3149 | 33.948 | 31.222 | +0.86% | +1.12% | 0.71x | 12.7 | 2026-11-10T18:35:00.078676+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | KAS/USD | 0.02997 | 30.800 | 32.152 | +0.77% | +0.88% | 0.43x | 13.4 | 2026-11-10T18:35:00.078676+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 244; predictions: 2244; observations: 146362.
- Matured sampled outcomes across 1/6/24/48h: 1294; gap abstentions: 6258. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
