# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T11:18:11.329863+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42607797730
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** 44b6ad0d3ac0a0ddfaef5fe1751f12957fd65902
**Ledger generation:** 192 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKE/USD | 0.00561815 | 88.220 | 66.651 | +7.22% | +2.92% | 1.70x | 26.4 | 2026-11-09T11:18:03.217479+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 5.103e-06 | 78.109 | 72.168 | +3.15% | -0.26% | 1.72x | 9.8 | 2026-11-09T11:18:03.217479+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ARB/USD | 0.1792 | 74.179 | 79.057 | +8.02% | +0.34% | 0.34x | 11.1 | 2026-11-09T11:18:03.217479+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ENA/USD | 0.1527 | 73.267 | 71.519 | +2.83% | -0.13% | 1.24x | 6.6 | 2026-11-09T11:18:03.217479+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | AAVE/USD | 131.92 | 72.627 | 74.718 | +4.74% | -0.31% | 0.94x | 11.4 | 2026-11-09T11:18:03.217479+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | SUI/USD | 0.8303 | 62.623 | 61.039 | +1.21% | -0.22% | 1.27x | 4.8 | 2026-11-09T11:18:03.217479+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | RSR/USD | 0.001794 | 62.085 | 62.567 | +8.46% | -1.86% | 1.88x | 27.9 | 2026-11-09T11:18:03.217479+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | TAO/USD | 219.6872 | 57.759 | 61.042 | +1.35% | +0.13% | 0.61x | 6.8 | 2026-11-09T11:18:03.217479+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | HBAR/USD | 0.06747 | 54.783 | 57.499 | +2.87% | -0.25% | 0.86x | 4.5 | 2026-11-09T11:18:03.217479+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | GBP/USD | 1.34231 | 54.459 | 58.410 | +0.50% | +0.03% | 0.59x | 0.2 | 2026-11-09T11:18:03.217479+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | SOL/USD | 86.77 | 52.575 | 56.438 | +0.37% | -0.06% | 0.64x | 2.3 | 2026-11-09T11:18:03.217479+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | PUMP/USD | 0.00364 | 51.291 | 61.395 | +3.67% | -0.50% | 0.24x | 19.2 | 2026-11-09T11:18:03.217479+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 192; predictions: 1707; observations: 116060.
- Matured sampled outcomes across 1/6/24/48h: 963; gap abstentions: 4688. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
