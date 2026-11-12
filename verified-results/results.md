# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T02:33:40.547840+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43141960533
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 9b675e6e6bfb7289eda3a7390fb1083c61dc2dec
**Ledger generation:** 308 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 4.578e-06 | 74.840 | 63.684 | +1.55% | +0.68% | 1.77x | 4.4 | 2026-11-12T02:33:31.203249+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ZEC/USD | 995.63 | 74.740 | 76.742 | +3.49% | -0.44% | 1.02x | 5.4 | 2026-11-12T02:33:31.203249+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | HYPE/USD | 72.38 | 73.975 | 58.003 | +0.53% | +0.19% | 5.05x | 1.4 | 2026-11-12T02:33:31.203249+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | XRP/USD | 1.0543 | 73.481 | 56.839 | +0.31% | +0.33% | 3.36x | 0.7 | 2026-11-12T02:33:31.203249+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ADA/USD | 0.174703 | 72.966 | 55.541 | +0.32% | +0.48% | 5.25x | 3.4 | 2026-11-12T02:33:31.203249+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | NEAR/USD | 3.6065 | 71.954 | 58.105 | +0.64% | -0.23% | 8.94x | 2.8 | 2026-11-12T02:33:31.203249+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | XDG/USD | 0.0676601 | 60.050 | 46.223 | +0.38% | +0.37% | 2.20x | 0.5 | 2026-11-12T02:33:31.203249+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | AVAX/USD | 8.618 | 59.403 | 61.976 | +1.25% | +0.68% | 0.40x | 3.5 | 2026-11-12T02:33:31.203249+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | XLM/USD | 0.148178 | 57.728 | 51.770 | +0.81% | +0.17% | 1.51x | 3.2 | 2026-11-12T02:33:31.203249+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | SOL/USD | 83.51 | 55.217 | 56.579 | +0.40% | +0.12% | 0.80x | 2.4 | 2026-11-12T02:33:31.203249+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | HBAR/USD | 0.0658 | 54.249 | 38.028 | +0.66% | +0.24% | 3.07x | 4.6 | 2026-11-12T02:33:31.203249+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | TIA/USD | 0.4164 | 49.120 | 33.638 | +0.48% | +0.10% | 8.25x | 2.4 | 2026-11-12T02:33:31.203249+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 308; predictions: 2954; observations: 184965.
- Matured sampled outcomes across 1/6/24/48h: 2333; gap abstentions: 7802. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
