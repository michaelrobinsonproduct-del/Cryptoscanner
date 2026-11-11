# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T19:32:40.048627+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43087880584
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 645d5707e61f160232a56800c208862adf44fa5a
**Ledger generation:** 295 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 605; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.6987 | 92.228 | 76.090 | +3.21% | +0.23% | 3.15x | 2.7 | 2026-11-11T19:32:31.119084+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | XMR/USD | 588.33 | 89.614 | 80.668 | +4.57% | +0.41% | 1.69x | 12.6 | 2026-11-11T19:32:31.119084+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | AVAX/USD | 8.562 | 85.289 | 69.647 | +2.34% | +0.13% | 5.35x | 3.5 | 2026-11-11T19:32:31.119084+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | XLM/USD | 0.14883 | 84.009 | 67.804 | +2.93% | +0.24% | 2.95x | 3.1 | 2026-11-11T19:32:31.119084+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | ADA/USD | 0.177007 | 83.026 | 66.362 | +1.84% | +0.33% | 3.23x | 3.1 | 2026-11-11T19:32:31.119084+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | TAO/USD | 221.4516 | 77.763 | 64.780 | +1.50% | -0.40% | 85.86x | 1.5 | 2026-11-11T19:32:31.119084+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | HYPE/USD | 72.98 | 72.486 | 61.680 | +1.05% | +0.27% | 1.94x | 1.4 | 2026-11-11T19:32:31.119084+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | SHX/USD | 0.00431 | 70.619 | 60.922 | +4.48% | +0.09% | 1.92x | 2.3 | 2026-11-11T19:32:31.119084+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | ETH/USD | 2077.35 | 70.141 | 64.090 | +1.30% | +0.37% | 1.42x | 0.0 | 2026-11-11T19:32:31.119084+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | TON/USD | 1.213 | 68.848 | 70.930 | +6.50% | +0.08% | 0.75x | 41.3 | 2026-11-11T19:32:31.119084+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | SOL/USD | 84.67 | 67.408 | 66.435 | +1.72% | +0.34% | 0.93x | 1.2 | 2026-11-11T19:32:31.119084+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | SUI/USD | 0.8353 | 65.218 | 65.036 | +1.52% | +0.40% | 0.82x | 1.2 | 2026-11-11T19:32:31.119084+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 295; predictions: 2808; observations: 177088.
- Matured sampled outcomes across 1/6/24/48h: 2195; gap abstentions: 7300. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
