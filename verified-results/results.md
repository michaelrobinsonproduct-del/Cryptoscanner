# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T09:29:29.952789+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42593655799
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** 17077e2f8af3133cbf17a3812511da20e6602739
**Ledger generation:** 188 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | ARB/USD | 0.1774 | 92.168 | 78.307 | +6.93% | -0.23% | 3.45x | 11.3 | 2026-11-09T09:29:21.742824+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | AAVE/USD | 130.6 | 80.837 | 68.740 | +3.69% | -0.58% | 38.77x | 7.6 | 2026-11-09T09:29:21.742824+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | RENDER/USD | 1.612 | 70.416 | 68.862 | +5.70% | -0.81% | 1.56x | 12.4 | 2026-11-09T09:29:21.742824+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | SUI/USD | 0.8248 | 70.350 | 58.150 | +0.54% | -0.53% | 2.49x | 1.2 | 2026-11-09T09:29:21.742824+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ENA/USD | 0.1511 | 69.779 | 63.951 | +1.75% | -0.79% | 1.98x | 6.6 | 2026-11-09T09:29:21.742824+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | PEPE/USD | 5.13e-06 | 68.431 | 76.998 | +3.70% | -1.18% | 0.73x | 7.8 | 2026-11-09T09:29:21.742824+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | QNT/USD | 200.18 | 64.057 | 56.747 | +2.74% | -1.10% | 2.28x | 15.0 | 2026-11-09T09:29:21.742824+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ZEC/USD | 1217.22 | 55.397 | 54.327 | +0.40% | -1.12% | 1.67x | 6.9 | 2026-11-09T09:29:21.742824+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | XDG/USD | 0.0692087 | 55.226 | 55.257 | +0.48% | -0.50% | 1.25x | 6.2 | 2026-11-09T09:29:21.742824+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | LINK/USD | 10.44313 | 54.837 | 54.840 | +0.40% | -0.31% | 1.15x | 5.4 | 2026-11-09T09:29:21.742824+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | LTC/USD | 50.93 | 53.749 | 56.480 | +1.72% | -0.35% | 0.90x | 3.9 | 2026-11-09T09:29:21.742824+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | AUD/USD | 0.68989 | 52.567 | 43.008 | +0.45% | +0.26% | 1.82x | 1.6 | 2026-11-09T09:29:21.742824+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 188; predictions: 1661; observations: 113636.
- Matured sampled outcomes across 1/6/24/48h: 951; gap abstentions: 4606. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
