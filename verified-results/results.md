# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-09T09:41:49.387426+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=09,39 * * * *, intended UTC minute=09,39; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/42595242935
**Source SHA:** bba6177fd9f7dcbc32e4a40002747091c0abb5e2
**Ledger commit:** 971bd2beb8f7c2dd7db6b829d79ac59b19e5b170
**Ledger generation:** 189 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 24.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | AAVE/USD | 131.08 | 91.343 | 71.504 | +4.07% | +0.97% | 7.20x | 7.6 | 2026-11-09T09:41:41.310406+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | PEPE/USD | 5.156e-06 | 87.723 | 78.746 | +4.22% | +0.94% | 1.43x | 11.7 | 2026-11-09T09:41:41.310406+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | ARB/USD | 0.1767 | 83.534 | 78.442 | +6.51% | +0.74% | 1.14x | 11.4 | 2026-11-09T09:41:41.310406+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | ZAMA/USD | 0.06673 | 68.615 | 62.772 | +5.99% | +1.33% | 0.92x | 21.0 | 2026-11-09T09:41:41.310406+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | LTC/USD | 51.03 | 64.347 | 58.926 | +1.92% | +0.41% | 1.34x | 2.0 | 2026-11-09T09:41:41.310406+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 6 | RENDER/USD | 1.611 | 62.555 | 65.255 | +5.64% | +0.56% | 0.45x | 18.7 | 2026-11-09T09:41:41.310406+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 7 | SOL/USD | 86.75 | 58.932 | 55.700 | +0.35% | +0.21% | 1.22x | 3.5 | 2026-11-09T09:41:41.310406+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 8 | ZEC/USD | 1217 | 58.932 | 54.160 | +0.38% | +0.29% | 1.33x | 7.0 | 2026-11-09T09:41:41.310406+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 9 | XDG/USD | 0.0693565 | 55.820 | 58.069 | +0.70% | +0.34% | 0.60x | 3.6 | 2026-11-09T09:41:41.310406+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 10 | AUD/USD | 0.69011 | 54.826 | 43.671 | +0.48% | -0.21% | 2.22x | 1.0 | 2026-11-09T09:41:41.310406+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 11 | SUI/USD | 0.8263 | 51.465 | 58.824 | +0.72% | +0.24% | 0.14x | 2.4 | 2026-11-09T09:41:41.310406+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 12 | GBP/USD | 1.34122 | 50.411 | 57.876 | +0.42% | +0.02% | 0.24x | 0.1 | 2026-11-09T09:41:41.310406+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 189; predictions: 1673; observations: 114242.
- Matured sampled outcomes across 1/6/24/48h: 951; gap abstentions: 4631. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
