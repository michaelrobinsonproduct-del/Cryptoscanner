# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-13T03:29:28.674580+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43358925106
**Source SHA:** 3ef9e2b4e56117c883f066848eacfa8505a522fa
**Ledger commit:** 7eb27f01b67b33b09c219093bedf4e5f5cebe4a9
**Ledger generation:** 350 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 1s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 5.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | PAXG/USD | 3906.22 | 53.859 | 47.198 | +0.74% | -0.14% | 1.73x | 0.0 | 2026-11-13T03:29:27.257776+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 4.561e-06 | 52.045 | 57.121 | +0.77% | -0.22% | 0.60x | 6.6 | 2026-11-13T03:29:27.257776+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | XAUT/USD | 3904.3 | 47.065 | 41.723 | +0.73% | -0.15% | 1.61x | 0.3 | 2026-11-13T03:29:27.257776+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | QNT/USD | 164.37 | 44.322 | 46.484 | +0.46% | +0.17% | 0.70x | 5.5 | 2026-11-13T03:29:27.257776+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 350; predictions: 3230; observations: 210416.
- Matured sampled outcomes across 1/6/24/48h: 2926; gap abstentions: 8851. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 1; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
