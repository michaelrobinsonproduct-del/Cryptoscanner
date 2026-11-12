# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T12:08:02.527373+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43214828176
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** cc8025bd4c0707bbc15d63bef7fa70440fd1199d
**Ledger generation:** 328 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 605; OHLC screened: 10.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.238 | 69.781 | 69.913 | +5.54% | -0.32% | 1.15x | 24.3 | 2026-11-12T12:07:59.053421+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | BAT/USD | 0.1219 | 65.449 | 49.424 | +3.54% | +0.21% | 8.93x | 16.5 | 2026-11-12T12:07:59.053421+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ZEC/USD | 965.39 | 60.690 | 54.552 | +0.35% | -0.66% | 1.94x | 5.8 | 2026-11-12T12:07:59.053421+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | JUP/USD | 0.25914 | 50.330 | 36.283 | +1.56% | +0.51% | 2.15x | 15.1 | 2026-11-12T12:07:59.053421+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | CAP/USD | 0.101078 | 26.898 | 32.591 | +0.60% | -0.93% | 0.90x | 6.1 | 2026-11-12T12:07:59.053421+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 328; predictions: 3085; observations: 197084.
- Matured sampled outcomes across 1/6/24/48h: 2661; gap abstentions: 8090. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
