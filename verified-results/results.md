# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T14:01:23.024650+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42829617605
**Source SHA:** 3774b902ccb4e4fd5507499dc7c96ebbb4185329
**Ledger commit:** 0c9b6f6e75bcc946dfb7e57a24cd28131d8a88eb
**Ledger generation:** 235 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 589; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.323e-06 | 100.431 | 80.590 | +3.92% | +0.97% | 12.98x | 3.8 | 2026-11-10T14:01:13.551057+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | CAP/USD | 0.109555 | 92.034 | 74.915 | +10.82% | +0.42% | 6.19x | 6.0 | 2026-11-10T14:01:13.551057+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NIGHT/USD | 0.04247 | 88.490 | 70.762 | +4.92% | +0.55% | 4.75x | 7.1 | 2026-11-10T14:01:13.551057+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | XDC/USD | 0.0311 | 87.185 | 69.923 | +5.53% | +0.45% | 15.71x | 16.1 | 2026-11-10T14:01:13.551057+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | UAI/USD | 0.04179 | 79.876 | 60.516 | +8.38% | +0.87% | 2.79x | 36.0 | 2026-11-10T14:01:13.551057+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | NEAR/USD | 3.6364 | 74.603 | 56.525 | +0.41% | +0.62% | 10.05x | 2.7 | 2026-11-10T14:01:13.551057+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ZEC/USD | 1168.75 | 72.235 | 52.229 | +0.54% | +1.00% | 8.15x | 13.1 | 2026-11-10T14:01:13.551057+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ENA/USD | 0.1539 | 65.392 | 46.793 | +0.52% | +0.72% | 12.02x | 6.5 | 2026-11-10T14:01:13.551057+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | UNI/USD | 6.998 | 63.374 | 46.295 | +0.40% | +0.42% | 43.33x | 6.7 | 2026-11-10T14:01:13.551057+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | TON/USD | 1.1 | 59.470 | 56.365 | +5.77% | +0.83% | 0.90x | 36.4 | 2026-11-10T14:01:13.551057+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | PLAY/USD | 0.008654 | 53.177 | 53.020 | +5.37% | +1.16% | 0.44x | 31.2 | 2026-11-10T14:01:13.551057+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | KAS/USD | 0.02999 | 50.043 | 33.871 | +0.84% | +0.23% | 4.41x | 10.0 | 2026-11-10T14:01:13.551057+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 235; predictions: 2147; observations: 141010.
- Matured sampled outcomes across 1/6/24/48h: 1199; gap abstentions: 6071. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
