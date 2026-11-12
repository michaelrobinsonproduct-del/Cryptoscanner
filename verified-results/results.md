# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T21:02:48.415060+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43305737594
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 0efe32144aa5a50a185cbde13e3014fd85eb1a7e
**Ledger generation:** 347 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 18.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD | 0.148904 | 72.702 | 58.534 | +1.30% | -0.17% | 2.68x | 2.6 | 2026-11-12T21:02:42.068835+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | CAP/USD | 0.104643 | 72.385 | 52.107 | +4.15% | +1.06% | 3.07x | 17.3 | 2026-11-12T21:02:42.068835+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | MON/USD | 0.01739 | 71.687 | 58.602 | +4.38% | +0.06% | 2.28x | 11.5 | 2026-11-12T21:02:42.068835+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | AKE/USD | 0.00274208 | 64.315 | 63.135 | +10.69% | +1.45% | 0.39x | 32.5 | 2026-11-12T21:02:42.068835+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | JUP/USD | 0.26547 | 62.858 | 55.361 | +4.04% | -1.50% | 5.69x | 13.2 | 2026-11-12T21:02:42.068835+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | PEPE/USD | 4.54e-06 | 58.745 | 57.767 | +0.71% | +0.07% | 1.06x | 4.4 | 2026-11-12T21:02:42.068835+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | XDC/USD | 0.02972 | 58.415 | 49.307 | +2.27% | -0.03% | 1.93x | 13.4 | 2026-11-12T21:02:42.068835+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | USELESS/USD | 0.13066 | 55.087 | 48.063 | +2.65% | -0.58% | 1.99x | 17.5 | 2026-11-12T21:02:42.068835+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | BAT/USD | 0.12233 | 50.163 | 57.301 | +3.91% | +0.25% | 0.16x | 4.9 | 2026-11-12T21:02:42.068835+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | POL/USD | 0.08781 | 43.428 | 33.388 | +0.70% | -0.36% | 2.19x | 9.1 | 2026-11-12T21:02:42.068835+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | ATOM/USD | 1.4157 | 35.948 | 38.339 | +1.59% | -0.08% | 0.80x | 10.6 | 2026-11-12T21:02:42.068835+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 347; predictions: 3211; observations: 208598.
- Matured sampled outcomes across 1/6/24/48h: 2885; gap abstentions: 8486. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
