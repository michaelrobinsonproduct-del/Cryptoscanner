# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T01:57:06.149259+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=10,40 * * * *, intended UTC minute=10,40; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42548133177
**Source SHA:** d46d8e77dc3cd1f97a6b375aaf3270b763ec3c09
**Ledger commit:** fedf97fd30e0fb1d537cb81365a3b308fbb6cdba
**Ledger generation:** 176 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.186e-06 | 113.139 | 85.925 | +4.83% | +2.44% | 2.53x | 5.8 | 2026-11-09T01:56:59.697088+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | SOL/USD | 87.8 | 80.321 | 65.362 | +1.56% | +0.55% | 2.22x | 1.1 | 2026-11-09T01:56:59.697088+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | USELESS/USD | 0.12866 | 79.625 | 61.310 | +4.49% | +2.00% | 1.83x | 17.1 | 2026-11-09T01:56:59.697088+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ENA/USD | 0.1526 | 71.121 | 71.048 | +2.76% | +0.53% | 0.74x | 6.6 | 2026-11-09T01:56:59.697088+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | SUI/USD | 0.8391 | 66.934 | 69.764 | +2.28% | +0.52% | 0.46x | 2.4 | 2026-11-09T01:56:59.697088+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | HYPE/USD | 74.92 | 63.926 | 58.563 | +0.60% | +0.56% | 1.25x | 1.3 | 2026-11-09T01:56:59.697088+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ZEC/USD | 1238.65 | 63.855 | 65.711 | +2.16% | +0.70% | 0.46x | 8.9 | 2026-11-09T01:56:59.697088+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | XDG/USD | 0.0698323 | 63.677 | 62.725 | +1.39% | +0.67% | 0.76x | 4.0 | 2026-11-09T01:56:59.697088+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | XLM/USD | 0.148043 | 62.966 | 63.839 | +1.27% | +0.65% | 0.59x | 0.1 | 2026-11-09T01:56:59.697088+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | UNI/USD | 6.9623 | 59.605 | 62.726 | +2.63% | +0.80% | 0.29x | 4.3 | 2026-11-09T01:56:59.697088+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | NEAR/USD | 3.631 | 59.108 | 62.659 | +1.53% | +0.77% | 0.26x | 6.1 | 2026-11-09T01:56:59.697088+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | UAI/USD | 0.06578 | 58.393 | 67.007 | +7.26% | -2.05% | 1.16x | 32.0 | 2026-11-09T01:56:59.697088+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 176; predictions: 1520; observations: 106364.
- Matured sampled outcomes across 1/6/24/48h: 819; gap abstentions: 4383. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
