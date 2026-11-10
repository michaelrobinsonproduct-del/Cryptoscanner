# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-10T05:30:03.533058+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42762329340
**Source SHA:** c86831bd1c7157bee5fef4ed53347615491fbb76
**Ledger commit:** 97de2fac846d04d74255e27fc8730b7dcdf17e50
**Ledger generation:** 227 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 529; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04228 | 84.827 | 65.533 | +4.45% | +0.86% | 3.80x | 9.5 | 2026-11-10T05:29:54.719424+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 5.262e-06 | 60.040 | 72.233 | +2.73% | -0.77% | 0.17x | 3.8 | 2026-11-10T05:29:54.719424+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | XDC/USD | 0.02993 | 55.550 | 45.618 | +1.56% | +0.03% | 1.98x | 3.3 | 2026-11-10T05:29:54.719424+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | HBAR/USD | 0.06696 | 51.029 | 37.519 | +0.34% | -0.30% | 3.69x | 4.5 | 2026-11-10T05:29:54.719424+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ADA/USD | 0.17802 | 43.661 | 53.540 | +0.43% | -0.23% | 0.13x | 4.2 | 2026-11-10T05:29:54.719424+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | CAP/USD | 0.10098 | 37.312 | 44.282 | +2.15% | -0.45% | 0.53x | 6.1 | 2026-11-10T05:29:54.719424+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 227; predictions: 2073; observations: 136414.
- Matured sampled outcomes across 1/6/24/48h: 1189; gap abstentions: 5678. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 18; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
