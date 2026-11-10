# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T20:03:30.752982+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42891117306
**Source SHA:** 9c182729094d97cd83095218ec2e91b55a348672
**Ledger commit:** 6ee6118bc1037ae992bd7ff9aee10aa6105ce94b
**Ledger generation:** 247 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 600; OHLC screened: 17.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.222e-06 | 67.595 | 65.793 | +1.95% | -0.15% | 1.26x | 5.7 | 2026-11-10T20:03:26.009849+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | NIGHT/USD | 0.04135 | 56.721 | 57.322 | +2.15% | +0.39% | 0.75x | 2.4 | 2026-11-10T20:03:26.009849+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | TRUMP/USD | 1.133 | 50.307 | 37.166 | +1.16% | +0.89% | 1.87x | 8.8 | 2026-11-10T20:03:26.009849+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | CAP/USD | 0.101 | 44.707 | 53.691 | +2.17% | -0.52% | 0.36x | 0.2 | 2026-11-10T20:03:26.009849+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ICP/USD | 2.413 | 29.793 | 32.934 | +0.63% | +0.79% | 0.29x | 8.3 | 2026-11-10T20:03:26.009849+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | MEGA/USD | 0.05034 | 22.634 | 25.500 | +1.10% | +0.56% | 0.43x | 29.8 | 2026-11-10T20:03:26.009849+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 247; predictions: 2269; observations: 148160.
- Matured sampled outcomes across 1/6/24/48h: 1349; gap abstentions: 6284. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
