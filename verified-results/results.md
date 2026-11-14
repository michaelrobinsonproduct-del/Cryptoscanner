# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-14T20:25:25.777343+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43637374086
**Source SHA:** f195c4f1b4775bd72c0888a411731047be2157ff
**Previous ledger commit:** 761f8e3fbdef462208725564655789efa6926d17 (atomic ledger/results publication)
**Ledger generation:** 413 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 2s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 606; OHLC screened: 8.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PIEVERSE/USD | 1.8202 | 64.378 | 65.648 | +11.11% | -0.36% | 1.05x | 23.7 | 2026-11-14T20:25:23.609165+00:00 | Not calibrated | WEAK 32/100 | EXTREME 85/100 | Do nothing | WATCH |
| 2 | PROMPT/USD | 0.01438 | 60.405 | 62.215 | +7.15% | +1.20% | 0.22x | 27.9 | 2026-11-14T20:25:23.609165+00:00 | Not calibrated | MODERATE 50/100 | EXTREME 94/100 | Do nothing | WATCH |
| 3 | NIGHT/USD | 0.0474 | 50.465 | 58.538 | +1.11% | -0.77% | 0.58x | 8.5 | 2026-11-14T20:25:23.609165+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | CAP/USD | 0.109879 | 49.802 | 52.107 | +2.66% | +0.27% | 0.63x | 6.1 | 2026-11-14T20:25:23.609165+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 5 | AKE/USD | 0.0125075 | 41.745 | 46.908 | +1.28% | -1.57% | 1.27x | 34.1 | 2026-11-14T20:25:23.609165+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 77/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PIEVERSE/USD | 65.648 | 1.8202 | -0.36% | 1.05x |
| 2 | PROMPT/USD | 62.215 | 0.01438 | +1.20% | 0.22x |
| 3 | NIGHT/USD | 58.538 | 0.0474 | -0.77% | 0.58x |
| 4 | CAP/USD | 52.107 | 0.109879 | +0.27% | 0.63x |
| 5 | AKE/USD | 46.908 | 0.0125075 | -1.57% | 1.27x |

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

- Persisted scans: 413; predictions: 3583; observations: 248620.
- Matured sampled outcomes across 1/6/24/48h: 3145; gap abstentions: 10514. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
