# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T08:12:38.191687+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43180773475
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 9fb41e10bda1c0a9e15236eafefc3d6bf1ff76e5
**Ledger generation:** 320 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 16.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | XDC/USD | 0.03055 | 78.374 | 69.767 | +5.13% | +0.79% | 1.46x | 13.1 | 2026-11-12T08:12:32.788951+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ZEC/USD | 984.56 | 69.476 | 70.283 | +2.34% | +0.07% | 0.89x | 2.2 | 2026-11-12T08:12:32.788951+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | AVAX/USD | 8.596 | 62.662 | 59.580 | +0.99% | -0.44% | 1.53x | 4.7 | 2026-11-12T08:12:32.788951+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | TON/USD | 1.2 | 59.753 | 56.961 | +2.30% | -0.58% | 1.57x | 8.3 | 2026-11-12T08:12:32.788951+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | BAT/USD | 0.12038 | 44.258 | 46.212 | +2.25% | +0.30% | 0.65x | 5.0 | 2026-11-12T08:12:32.788951+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | DOT/USD | 0.8414 | 38.371 | 37.334 | +0.33% | +0.33% | 0.94x | 1.2 | 2026-11-12T08:12:32.788951+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | HBAR/USD | 0.06567 | 29.488 | 37.252 | +0.46% | -0.11% | 0.28x | 3.0 | 2026-11-12T08:12:32.788951+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 320; predictions: 3034; observations: 192237.
- Matured sampled outcomes across 1/6/24/48h: 2534; gap abstentions: 7980. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
