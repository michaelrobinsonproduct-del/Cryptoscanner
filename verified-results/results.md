# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T07:40:36.522428+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43176718430
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** b4c1f2710d81d00bf7a84eefacd8e6d8bf1c2de6
**Ledger generation:** 319 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 15.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 986.44 | 76.107 | 71.350 | +2.54% | -0.12% | 1.54x | 2.8 | 2026-11-12T07:40:30.829038+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | TON/USD | 1.202 | 67.017 | 53.669 | +2.47% | -0.33% | 3.86x | 16.6 | 2026-11-12T07:40:30.829038+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | AVAX/USD | 8.65 | 63.328 | 64.613 | +1.62% | +0.06% | 0.84x | 3.5 | 2026-11-12T07:40:30.829038+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | BAT/USD | 0.12069 | 55.007 | 40.090 | +2.51% | -0.02% | 10.29x | 20.7 | 2026-11-12T07:40:30.829038+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | HBAR/USD | 0.06565 | 46.658 | 36.274 | +0.43% | -0.18% | 2.13x | 4.6 | 2026-11-12T07:40:30.829038+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 319; predictions: 3027; observations: 191631.
- Matured sampled outcomes across 1/6/24/48h: 2517; gap abstentions: 7969. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
