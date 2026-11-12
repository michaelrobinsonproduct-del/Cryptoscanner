# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T10:34:50.841800+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43201242567
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 352edfc61e91218dd76d9054a1177b69ffbcf557
**Ledger generation:** 325 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 21.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.256 | 96.684 | 85.955 | +7.08% | +2.21% | 0.97x | 8.0 | 2026-11-12T10:34:42.876857+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ZEC/USD | 990.87 | 82.998 | 73.772 | +3.00% | +1.09% | 1.38x | 4.4 | 2026-11-12T10:34:42.876857+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | AVAX/USD | 8.576 | 66.708 | 59.097 | +0.75% | -0.27% | 1.89x | 2.3 | 2026-11-12T10:34:42.876857+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | BAT/USD | 0.12329 | 54.776 | 61.527 | +4.72% | -0.24% | 0.45x | 8.9 | 2026-11-12T10:34:42.876857+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | JUP/USD | 0.25622 | 49.934 | 30.151 | +0.41% | +0.96% | 6.70x | 10.9 | 2026-11-12T10:34:42.876857+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XDC/USD | 0.02983 | 47.879 | 55.113 | +2.65% | +0.13% | 0.21x | 6.7 | 2026-11-12T10:34:42.876857+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | HBAR/USD | 0.06604 | 40.413 | 39.568 | +1.02% | +0.09% | 1.04x | 6.1 | 2026-11-12T10:34:42.876857+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | MON/USD | 0.01683 | 28.541 | 36.048 | +1.02% | -0.06% | 0.28x | 5.9 | 2026-11-12T10:34:42.876857+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 325; predictions: 3069; observations: 195267.
- Matured sampled outcomes across 1/6/24/48h: 2621; gap abstentions: 8046. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
