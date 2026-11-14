# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-14T12:52:40.767374+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43596633156
**Source SHA:** c72deb0ead45d5d5949a96d65395c87f208d57f2
**Previous ledger commit:** e4808a87dac895a50475677f7f3010cfe65f94d6 (atomic ledger/results publication)
**Ledger generation:** 399 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 606; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04837 | 75.433 | 70.331 | +3.18% | -0.68% | 1.85x | 2.1 | 2026-11-14T12:52:37.118180+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XMR/USD | 532.97 | 44.447 | 45.846 | +0.76% | -0.57% | 1.15x | 28.9 | 2026-11-14T12:52:37.118180+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 3 | TRX/USD | 0.31269 | 43.539 | 38.379 | +0.30% | -0.04% | 1.54x | 0.7 | 2026-11-14T12:52:37.118180+00:00 | Not calibrated | WEAK 42/100 | HIGH 66/100 | Watch | WATCH |
| 4 | TON/USD | 1.1 | 38.032 | 39.634 | +0.82% | -0.27% | 0.98x | 9.1 | 2026-11-14T12:52:37.118180+00:00 | Not calibrated | WEAK 24/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 70.331 | 0.04837 | -0.68% | 1.85x |
| 2 | XMR/USD | 45.846 | 532.97 | -0.57% | 1.15x |
| 3 | TON/USD | 39.634 | 1.1 | -0.27% | 0.98x |
| 4 | TRX/USD | 38.379 | 0.31269 | -0.04% | 1.54x |

The baseline ordering is over this same confirmed WATCH pool, not an independent full-market baseline scan.
The separate legacy-inspired scanner publishes its own WATCH signals in a later, read-only GitHub artifact linked by this paper run ID.

**30%+ in 48h probability:** NOT CALIBRATED. The separate signal-confidence index (0–100) expresses current setup strength, NOT odds of a gain. Risk varies by spread, momentum and volume; every candidate remains speculative. The action is a research consideration, not an executed or authorized trade. A more substantial entry requires independently qualified held-out calibration.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 399; predictions: 3543; observations: 240136.
- Matured sampled outcomes across 1/6/24/48h: 3117; gap abstentions: 10271. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
