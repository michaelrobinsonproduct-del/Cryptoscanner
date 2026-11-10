# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T19:36:42.696234+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42886673899
**Source SHA:** a401ca9b3fa5588c6780befb93e5eb91f2431f0f
**Ledger commit:** 558a66f413be623fab8a56ed5a551b28ffd2197f
**Ledger generation:** 246 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 599; OHLC screened: 14.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 5.246e-06 | 65.771 | 70.993 | +2.42% | -0.06% | 0.51x | 1.9 | 2026-11-10T19:36:38.499523+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | CAP/USD | 0.102693 | 56.232 | 52.420 | +3.88% | -0.16% | 1.46x | 27.0 | 2026-11-10T19:36:38.499523+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NIGHT/USD | 0.0415 | 45.541 | 55.348 | +2.52% | -0.50% | 0.27x | 12.1 | 2026-11-10T19:36:38.499523+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | LIGHTER/USD | 3.324 | 43.115 | 42.587 | +2.81% | -0.36% | 1.23x | 24.1 | 2026-11-10T19:36:38.499523+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | PLUME/USD | 0.01296 | 39.786 | 31.689 | +1.25% | +0.00% | 1.81x | 15.5 | 2026-11-10T19:36:38.499523+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | MEGA/USD | 0.05012 | 33.454 | 17.254 | +0.66% | +0.24% | 3.08x | 40.1 | 2026-11-10T19:36:38.499523+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | TRUMP/USD | 1.128 | 24.744 | 33.940 | +0.71% | -0.62% | 0.39x | 8.9 | 2026-11-10T19:36:38.499523+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 246; predictions: 2263; observations: 147560.
- Matured sampled outcomes across 1/6/24/48h: 1330; gap abstentions: 6278. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
