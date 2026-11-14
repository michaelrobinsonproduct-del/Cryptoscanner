# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-14T07:19:00.371829+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43570486670
**Source SHA:** ec76c938f48a010193e354b23caf7274390bbeee
**Previous ledger commit:** 901f0574367df73b5d32112ceeef4d5505ed3729 (atomic ledger/results publication)
**Ledger generation:** 388 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 606; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKE/USD | 0.01282991 | 66.459 | 69.802 | +3.89% | +0.53% | 0.40x | 24.8 | 2026-11-14T07:18:57.121804+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | UAI/USD | 0.04199 | 54.891 | 70.908 | +8.25% | -11.18% | 1.90x | 16.7 | 2026-11-14T07:18:57.121804+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 3 | CAP/USD | 0.108752 | 36.249 | 35.975 | +1.61% | -0.15% | 1.10x | 27.8 | 2026-11-14T07:18:57.121804+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 4 | TRX/USD | 0.312561 | 36.098 | 39.149 | +0.26% | -0.01% | 0.70x | 0.0 | 2026-11-14T07:18:57.121804+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | ICNT/USD | 0.2571 | 34.026 | 31.428 | +0.35% | +0.31% | 1.10x | 3.9 | 2026-11-14T07:18:57.121804+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 6 | PIEVERSE/USD | 1.7066 | 27.650 | 38.850 | +4.18% | -1.82% | 0.79x | 43.3 | 2026-11-14T07:18:57.121804+00:00 | Not calibrated | WEAK 4/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UAI/USD | 70.908 | 0.04199 | -11.18% | 1.90x |
| 2 | AKE/USD | 69.802 | 0.01282991 | +0.53% | 0.40x |
| 3 | TRX/USD | 39.149 | 0.312561 | -0.01% | 0.70x |
| 4 | PIEVERSE/USD | 38.850 | 1.7066 | -1.82% | 0.79x |
| 5 | CAP/USD | 35.975 | 0.108752 | -0.15% | 1.10x |
| 6 | ICNT/USD | 31.428 | 0.2571 | +0.31% | 1.10x |

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

- Persisted scans: 388; predictions: 3498; observations: 233469.
- Matured sampled outcomes across 1/6/24/48h: 3039; gap abstentions: 10127. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
