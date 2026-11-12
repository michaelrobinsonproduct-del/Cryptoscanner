# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-12T14:04:38.022170+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43232953603
**Source SHA:** 21b4cf643df9f7a7adfddc959660920dd467c70b
**Ledger commit:** 390e5961a17565dbe7816dc27e0bcdad012c7830
**Ledger generation:** 332 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 2s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 624; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 606; valid market observations: 606; OHLC screened: 6.

## Top WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | Confidence / risk | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | TON/USD | 1.235 | 64.689 | 75.839 | +5.29% | -0.80% | 0.29x | 8.1 | 2026-11-12T14:04:36.123276+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 2 | BAT/USD | 0.12236 | 50.402 | 50.678 | +3.93% | -0.40% | 1.17x | 19.7 | 2026-11-12T14:04:36.123276+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 3 | XDC/USD | 0.02945 | 40.616 | 45.330 | +1.34% | -0.98% | 1.02x | 10.2 | 2026-11-12T14:04:36.123276+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 4 | MEGA/USD | 0.04617 | 28.638 | 34.864 | +3.06% | +0.61% | 0.07x | 36.9 | 2026-11-12T14:04:36.123276+00:00 | NOT CALIBRATED / HIGH | WATCH |
| 5 | MON/USD | 0.01671 | 15.095 | 28.845 | +0.30% | -0.95% | 0.10x | 12.0 | 2026-11-12T14:04:36.123276+00:00 | NOT CALIBRATED / HIGH | WATCH |

**Confidence:** uncalibrated research heuristics, NOT validated probabilities. **BUY:** none authorized. Numerical baseline/challenger scores are uncalibrated paper-only ranking values, not probabilities or validated improvement.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 332; predictions: 3104; observations: 199508.
- Matured sampled outcomes across 1/6/24/48h: 2710; gap abstentions: 8167. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 1; details in immutable scan JSON artifact.
- Storage: checksum-sealed ledger pushed non-force and read back before this report. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
