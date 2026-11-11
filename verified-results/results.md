# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T01:33:16.973782+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42939573684
**Source SHA:** 9c182729094d97cd83095218ec2e91b55a348672
**Ledger commit:** 4e44c018109d68cdd2e84084e5742c8eb4e631fa
**Ledger generation:** 258 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 600; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | SUI/USD | 0.8319 | 79.449 | 60.938 | +1.11% | +0.70% | 23.17x | 3.6 | 2026-11-11T01:33:08.048038+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | ARB/USD | 0.1644 | 78.649 | 56.241 | +2.49% | +1.48% | 59.47x | 12.2 | 2026-11-11T01:33:08.048038+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | XDG/USD | 0.0685058 | 76.980 | 60.117 | +0.83% | +0.37% | 2.76x | 1.4 | 2026-11-11T01:33:08.048038+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | AVAX/USD | 8.449 | 76.900 | 58.387 | +0.99% | +0.70% | 6.17x | 7.1 | 2026-11-11T01:33:08.048038+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | NEAR/USD | 3.6801 | 72.407 | 67.287 | +2.69% | +1.52% | 0.75x | 13.0 | 2026-11-11T01:33:08.048038+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | LINK/USD | 10.39255 | 62.747 | 54.272 | +1.06% | +0.60% | 1.55x | 3.8 | 2026-11-11T01:33:08.048038+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | LTC/USD | 50.99 | 62.255 | 49.115 | +0.57% | +0.43% | 2.10x | 3.9 | 2026-11-11T01:33:08.048038+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ENA/USD | 0.1533 | 61.898 | 65.248 | +2.47% | +0.92% | 0.20x | 6.5 | 2026-11-11T01:33:08.048038+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | PEPE/USD | 5.485e-06 | 60.725 | 62.153 | +2.07% | +0.96% | 0.38x | 14.6 | 2026-11-11T01:33:08.048038+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | HBAR/USD | 0.06646 | 59.295 | 48.471 | +1.42% | +0.64% | 1.76x | 4.5 | 2026-11-11T01:33:08.048038+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | SOL/USD | 83.49 | 57.531 | 56.504 | +0.30% | +0.53% | 0.84x | 1.2 | 2026-11-11T01:33:08.048038+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | TAO/USD | 220.2786 | 57.130 | 58.499 | +0.97% | +0.63% | 0.55x | 6.5 | 2026-11-11T01:33:08.048038+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 258; predictions: 2373; observations: 154760.
- Matured sampled outcomes across 1/6/24/48h: 1566; gap abstentions: 6519. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
