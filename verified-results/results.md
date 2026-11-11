# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T19:08:09.600178+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43084065512
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 2280824013cfdee4cbfba63de585497556b72a4f
**Ledger generation:** 294 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 605; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.6958 | 79.026 | 74.035 | +3.13% | -0.93% | 1.97x | 5.7 | 2026-11-11T19:08:01.452636+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | TON/USD | 1.221 | 78.222 | 79.277 | +7.20% | -0.33% | 1.06x | 24.6 | 2026-11-11T19:08:01.452636+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | HYPE/USD | 72.97 | 73.721 | 61.584 | +1.04% | -0.48% | 2.45x | 1.4 | 2026-11-11T19:08:01.452636+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | SUI/USD | 0.8349 | 73.089 | 64.695 | +1.47% | -0.60% | 2.14x | 1.2 | 2026-11-11T19:08:01.452636+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | SOL/USD | 84.67 | 72.763 | 66.435 | +1.72% | -0.53% | 1.90x | 1.2 | 2026-11-11T19:08:01.452636+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XMR/USD | 586.22 | 71.229 | 76.991 | +4.19% | -0.30% | 0.57x | 14.7 | 2026-11-11T19:08:01.452636+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ETH/USD | 2075.83 | 70.436 | 63.571 | +1.23% | -0.46% | 1.91x | 0.0 | 2026-11-11T19:08:01.452636+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | XBT/USD | 74279.9 | 69.606 | 60.507 | +0.79% | -0.22% | 2.02x | 0.0 | 2026-11-11T19:08:01.452636+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | XRP/USD | 1.05869 | 66.938 | 56.666 | +0.34% | -0.95% | 2.57x | 1.4 | 2026-11-11T19:08:01.452636+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | XLM/USD | 0.148958 | 63.479 | 67.843 | +3.02% | -0.45% | 0.79x | 4.0 | 2026-11-11T19:08:01.452636+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | AVAX/USD | 8.563 | 61.392 | 69.731 | +2.35% | -0.42% | 0.38x | 3.5 | 2026-11-11T19:08:01.452636+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | XDG/USD | 0.0685047 | 61.203 | 48.607 | +0.83% | -0.48% | 7.68x | 0.0 | 2026-11-11T19:08:01.452636+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 294; predictions: 2796; observations: 176483.
- Matured sampled outcomes across 1/6/24/48h: 2171; gap abstentions: 7276. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
