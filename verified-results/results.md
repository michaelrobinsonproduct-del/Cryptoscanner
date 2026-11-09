# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T22:22:45.281167+00:00
**GitHub trigger:** authenticated issue heartbeat (verified event=issue_comment; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42711104214
**Source SHA:** 47efb405551d493df87bca8b2583b5611396f1fa
**Ledger commit:** c8f0f4453e3384d759b265d3705957e5414dd53b
**Ledger generation:** 213 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 602; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AVAX/USD | 8.601 | 91.113 | 97.675 | +8.48% | -0.29% | 0.49x | 4.7 | 2026-11-09T22:22:38.731354+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ONDO/USD | 0.37207 | 90.331 | 93.153 | +5.83% | +0.35% | 0.54x | 1.6 | 2026-11-09T22:22:38.731354+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | VVV/USD | 21.911 | 86.255 | 80.544 | +9.23% | +0.87% | 1.13x | 1.4 | 2026-11-09T22:22:38.731354+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | UNI/USD | 7.0176 | 73.902 | 77.617 | +3.44% | -0.05% | 0.65x | 3.0 | 2026-11-09T22:22:38.731354+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | SUI/USD | 0.8416 | 73.183 | 72.495 | +2.58% | +0.15% | 0.99x | 1.2 | 2026-11-09T22:22:38.731354+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XDG/USD | 0.0697482 | 67.811 | 63.852 | +1.27% | +0.12% | 1.34x | 0.0 | 2026-11-09T22:22:38.731354+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | XLM/USD | 0.14693 | 67.015 | 58.543 | +0.51% | +0.19% | 1.75x | 0.1 | 2026-11-09T22:22:38.731354+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | HBAR/USD | 0.0669 | 66.695 | 51.022 | +2.00% | +0.13% | 2.98x | 1.5 | 2026-11-09T22:22:38.731354+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | NEAR/USD | 3.6392 | 63.321 | 66.330 | +1.76% | +0.19% | 0.61x | 1.9 | 2026-11-09T22:22:38.731354+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | TAO/USD | 222.1094 | 63.288 | 71.912 | +2.47% | +0.08% | 0.10x | 0.7 | 2026-11-09T22:22:38.731354+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | AUD/USD | 0.69256 | 59.382 | 43.977 | +0.84% | +0.08% | 10.29x | 1.4 | 2026-11-09T22:22:38.731354+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | XBT/USD | 74932 | 59.284 | 56.769 | +0.25% | +0.04% | 1.23x | 0.0 | 2026-11-09T22:22:38.731354+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 213; predictions: 1959; observations: 128769.
- Matured sampled outcomes across 1/6/24/48h: 1105; gap abstentions: 5219. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
