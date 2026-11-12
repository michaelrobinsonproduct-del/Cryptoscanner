# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T00:37:10.670688+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43128349629
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 6b4f1b536c2a0c03f7ca4f6f2ae8f1d9c4079d15
**Ledger generation:** 304 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AVAX/USD | 8.563 | 69.063 | 56.277 | +0.60% | +0.29% | 2.13x | 5.8 | 2026-11-12T00:37:02.361282+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ADA/USD | 0.174808 | 66.348 | 55.764 | +0.38% | +0.06% | 2.03x | 3.8 | 2026-11-12T00:37:02.361282+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ZEC/USD | 991.22 | 66.187 | 73.523 | +3.04% | +0.43% | 0.05x | 5.4 | 2026-11-12T00:37:02.361282+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | TAO/USD | 216.6436 | 64.638 | 54.316 | +0.39% | -0.13% | 2.10x | 6.9 | 2026-11-12T00:37:02.361282+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | NEAR/USD | 3.5972 | 54.501 | 55.871 | +0.38% | -0.10% | 0.91x | 3.6 | 2026-11-12T00:37:02.361282+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | PEPE/USD | 4.545e-06 | 53.184 | 57.444 | +0.82% | -0.90% | 1.02x | 6.6 | 2026-11-12T00:37:02.361282+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | XRP/USD | 1.05372 | 52.587 | 56.642 | +0.26% | -0.15% | 0.67x | 0.3 | 2026-11-12T00:37:02.361282+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | NIGHT/USD | 0.04775 | 52.191 | 47.256 | +0.74% | +0.44% | 1.27x | 10.5 | 2026-11-12T00:37:02.361282+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | DOT/USD | 0.8437 | 51.415 | 37.658 | +0.61% | -0.25% | 7.01x | 5.9 | 2026-11-12T00:37:02.361282+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | SOL/USD | 83.51 | 50.344 | 56.579 | +0.40% | -0.20% | 0.48x | 2.4 | 2026-11-12T00:37:02.361282+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | ETH/USD | 2059.33 | 50.324 | 56.891 | +0.27% | +0.12% | 0.28x | 0.0 | 2026-11-12T00:37:02.361282+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | STX/USD | 0.3114 | 48.760 | 38.111 | +1.40% | +0.97% | 1.58x | 6.4 | 2026-11-12T00:37:02.361282+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 304; predictions: 2910; observations: 182541.
- Matured sampled outcomes across 1/6/24/48h: 2291; gap abstentions: 7703. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
