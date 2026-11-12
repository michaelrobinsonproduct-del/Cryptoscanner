# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T19:02:31.940880+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43285480417
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** e77ac19f176b344d705de82faf823aa6eb55ba33
**Ledger generation:** 342 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 12.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | BAT/USD | 0.12321 | 64.149 | 58.130 | +4.65% | +0.54% | 1.33x | 15.4 | 2026-11-12T19:02:28.503494+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | XDC/USD | 0.02966 | 58.660 | 46.743 | +2.06% | +0.30% | 2.04x | 16.9 | 2026-11-12T19:02:28.503494+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | MON/USD | 0.01716 | 49.073 | 51.806 | +3.00% | -0.40% | 0.93x | 5.8 | 2026-11-12T19:02:28.503494+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | TIA/USD | 0.4191 | 37.157 | 42.291 | +1.13% | +0.53% | 0.22x | 4.8 | 2026-11-12T19:02:28.503494+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | JUP/USD | 0.26226 | 36.023 | 45.313 | +2.78% | -0.33% | 0.24x | 14.5 | 2026-11-12T19:02:28.503494+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | ATOM/USD | 1.4078 | 31.025 | 35.681 | +1.03% | -0.28% | 0.67x | 7.8 | 2026-11-12T19:02:28.503494+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 342; predictions: 3172; observations: 205568.
- Matured sampled outcomes across 1/6/24/48h: 2831; gap abstentions: 8401. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
