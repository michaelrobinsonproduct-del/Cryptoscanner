# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T03:04:05.507658+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42950024799
**Source SHA:** 9c182729094d97cd83095218ec2e91b55a348672
**Ledger commit:** 87301f510808b10195c9e010b8ef7172bdc0e7b6
**Ledger generation:** 261 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 602; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.6816 | 85.104 | 71.933 | +2.73% | -0.37% | 5.26x | 4.3 | 2026-11-11T03:03:57.158458+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AVAX/USD | 8.473 | 73.081 | 62.184 | +1.28% | -0.82% | 5.31x | 3.5 | 2026-11-11T03:03:57.158458+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | INJ/USD | 8.323 | 65.656 | 64.686 | +3.97% | -0.16% | 1.18x | 10.8 | 2026-11-11T03:03:57.158458+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | UNI/USD | 6.6899 | 64.478 | 55.339 | +0.38% | -1.17% | 3.11x | 4.6 | 2026-11-11T03:03:57.158458+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | XMR/USD | 564.54 | 61.370 | 54.617 | +0.34% | +0.20% | 1.58x | 5.5 | 2026-11-11T03:03:57.158458+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ADA/USD | 0.175536 | 55.926 | 60.739 | +0.99% | -0.32% | 0.68x | 2.4 | 2026-11-11T03:03:57.158458+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | AAVE/USD | 124.4 | 54.735 | 54.153 | +0.83% | -0.33% | 1.22x | 4.8 | 2026-11-11T03:03:57.158458+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ARB/USD | 0.1661 | 53.928 | 68.578 | +3.55% | -1.19% | 0.13x | 6.0 | 2026-11-11T03:03:57.158458+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | XRP/USD | 1.05838 | 52.394 | 57.122 | +0.31% | -0.33% | 0.69x | 0.1 | 2026-11-11T03:03:57.158458+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | TAO/USD | 218.9721 | 52.304 | 54.864 | +0.37% | -0.33% | 0.91x | 5.4 | 2026-11-11T03:03:57.158458+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | ETH/USD | 2058.63 | 50.486 | 57.700 | +0.39% | -0.15% | 0.35x | 0.0 | 2026-11-11T03:03:57.158458+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | XDG/USD | 0.068337 | 50.070 | 58.421 | +0.58% | -0.37% | 0.35x | 1.3 | 2026-11-11T03:03:57.158458+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 261; predictions: 2409; observations: 156565.
- Matured sampled outcomes across 1/6/24/48h: 1617; gap abstentions: 6583. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
