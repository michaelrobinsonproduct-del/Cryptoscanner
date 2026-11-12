# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T15:41:04.544156+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43249896519
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 8525b59064e878f2eb39609fea84cc2b7dbec450
**Ledger generation:** 335 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 8.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.255 | 80.920 | 85.390 | +6.99% | +0.80% | 0.15x | 7.9 | 2026-11-12T15:41:01.777393+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | XDC/USD | 0.0294 | 58.256 | 43.596 | +1.17% | -0.07% | 2.74x | 10.2 | 2026-11-12T15:41:01.777393+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | MON/USD | 0.01689 | 52.670 | 39.761 | +1.38% | -0.24% | 2.41x | 5.9 | 2026-11-12T15:41:01.777393+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | BAT/USD | 0.1193 | 33.733 | 36.437 | +1.33% | +0.20% | 0.63x | 11.8 | 2026-11-12T15:41:01.777393+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | CAP/USD | 0.101995 | 31.856 | 38.860 | +1.51% | +0.22% | 0.19x | 6.1 | 2026-11-12T15:41:01.777393+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 335; predictions: 3124; observations: 201326.
- Matured sampled outcomes across 1/6/24/48h: 2744; gap abstentions: 8232. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
