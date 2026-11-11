# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-11T20:01:56.107502+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43092328797
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** bef5925a653f4c71ebc95ee9f974f37475829ddb
**Ledger generation:** 296 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 605; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AVAX/USD | 8.6 | 76.779 | 72.835 | +2.80% | +0.32% | 1.24x | 3.5 | 2026-11-11T20:01:48.208823+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | XMR/USD | 589.69 | 76.530 | 80.778 | +4.81% | -0.06% | 0.61x | 15.8 | 2026-11-11T20:01:48.208823+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | NEAR/USD | 3.714 | 71.489 | 77.742 | +3.63% | +0.60% | 0.07x | 5.4 | 2026-11-11T20:01:48.208823+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | TON/USD | 1.209 | 67.994 | 77.138 | +6.15% | -0.66% | 0.41x | 24.9 | 2026-11-11T20:01:48.208823+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | SOL/USD | 84.88 | 65.879 | 68.202 | +1.97% | +0.17% | 0.69x | 1.2 | 2026-11-11T20:01:48.208823+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | XLM/USD | 0.149366 | 64.482 | 70.418 | +3.30% | +0.20% | 0.31x | 2.8 | 2026-11-11T20:01:48.208823+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | ADA/USD | 0.177645 | 63.215 | 68.543 | +2.21% | +0.27% | 0.33x | 3.8 | 2026-11-11T20:01:48.208823+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ETH/USD | 2078.86 | 62.328 | 64.606 | +1.38% | -0.11% | 0.83x | 0.0 | 2026-11-11T20:01:48.208823+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | SUI/USD | 0.8366 | 62.226 | 65.546 | +1.68% | +0.16% | 0.59x | 2.4 | 2026-11-11T20:01:48.208823+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | HBAR/USD | 0.06641 | 62.103 | 45.905 | +1.34% | +0.29% | 2.48x | 3.0 | 2026-11-11T20:01:48.208823+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | XBT/USD | 74406.7 | 58.562 | 61.711 | +0.96% | -0.08% | 0.72x | 0.0 | 2026-11-11T20:01:48.208823+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | HYPE/USD | 73.22 | 56.048 | 63.327 | +1.38% | +0.32% | 0.11x | 2.7 | 2026-11-11T20:01:48.208823+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 296; predictions: 2820; observations: 177693.
- Matured sampled outcomes across 1/6/24/48h: 2219; gap abstentions: 7312. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
