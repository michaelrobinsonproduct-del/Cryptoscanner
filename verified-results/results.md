# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T14:34:03.429125+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42635707392
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** 76bb6c53c68981675ae477ba596debcd4aada957
**Ledger generation:** 198 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.17e-06 | 101.942 | 85.588 | +4.51% | +0.27% | 5.02x | 1.9 | 2026-11-09T14:33:55.352209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AVAX/USD | 8.774 | 87.465 | 97.150 | +10.66% | -1.06% | 0.56x | 5.7 | 2026-11-09T14:33:55.352209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | SUI/USD | 0.85 | 85.538 | 79.084 | +3.61% | +0.16% | 1.56x | 2.3 | 2026-11-09T14:33:55.352209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ARB/USD | 0.1821 | 81.373 | 81.347 | +9.76% | -0.17% | 1.09x | 11.0 | 2026-11-09T14:33:55.352209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | AAVE/USD | 132.57 | 77.727 | 83.471 | +5.26% | +0.06% | 0.40x | 4.5 | 2026-11-09T14:33:55.352209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XDG/USD | 0.0695767 | 70.886 | 61.097 | +1.02% | +0.16% | 1.90x | 2.0 | 2026-11-09T14:33:55.352209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | LTC/USD | 51.67 | 70.749 | 69.229 | +3.20% | +0.12% | 1.09x | 3.9 | 2026-11-09T14:33:55.352209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | SOL/USD | 87.09 | 70.569 | 59.608 | +0.74% | +0.20% | 2.00x | 1.1 | 2026-11-09T14:33:55.352209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ENA/USD | 0.1533 | 68.709 | 74.373 | +3.23% | -0.13% | 0.50x | 6.5 | 2026-11-09T14:33:55.352209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | GBP/USD | 1.34128 | 67.702 | 57.945 | +0.43% | +0.01% | 1.97x | 0.1 | 2026-11-09T14:33:55.352209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | WLD/USD | 0.3226 | 66.376 | 62.237 | +3.46% | -0.47% | 1.65x | 3.1 | 2026-11-09T14:33:55.352209+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | TAO/USD | 222.4777 | 65.371 | 69.370 | +2.64% | -0.00% | 0.60x | 8.2 | 2026-11-09T14:33:55.352209+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 198; predictions: 1779; observations: 119695.
- Matured sampled outcomes across 1/6/24/48h: 1021; gap abstentions: 4821. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
