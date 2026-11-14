# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-14T06:20:19.680568+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43565795361
**Source SHA:** 939757530139ad3582f41f5fd3376a66acca455d
**Previous ledger commit:** 3e0c2b6bf0a02fd40b971a77dda7949dfdb61778 (atomic ledger/results publication)
**Ledger generation:** 386 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INJ/USD | 8.214 | 79.850 | 63.934 | +1.89% | +0.95% | 2.12x | 8.5 | 2026-11-14T06:20:13.652086+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XMR/USD | 530.86 | 52.095 | 53.759 | +0.36% | +0.42% | 0.63x | 7.5 | 2026-11-14T06:20:13.652086+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | ZRO/USD | 1.586 | 43.622 | 41.637 | +0.57% | +1.28% | 0.56x | 12.6 | 2026-11-14T06:20:13.652086+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | ICNT/USD | 0.2603 | 43.179 | 30.663 | +1.60% | -0.50% | 4.24x | 23.1 | 2026-11-14T06:20:13.652086+00:00 | Not calibrated | WEAK 42/100 | EXTREME 85/100 | Do nothing | WATCH |
| 5 | TRX/USD | 0.312813 | 38.151 | 40.283 | +0.34% | +0.06% | 0.76x | 0.0 | 2026-11-14T06:20:13.652086+00:00 | Not calibrated | WEAK 39/100 | HIGH 62/100 | Watch | WATCH |
| 6 | CAP/USD | 0.107344 | 28.174 | 33.559 | +0.29% | +0.33% | 0.30x | 13.7 | 2026-11-14T06:20:13.652086+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 63.934 | 8.214 | +0.95% | 2.12x |
| 2 | XMR/USD | 53.759 | 530.86 | +0.42% | 0.63x |
| 3 | ZRO/USD | 41.637 | 1.586 | +1.28% | 0.56x |
| 4 | TRX/USD | 40.283 | 0.312813 | +0.06% | 0.76x |
| 5 | CAP/USD | 33.559 | 0.107344 | +0.33% | 0.30x |
| 6 | ICNT/USD | 30.663 | 0.2603 | -0.50% | 4.24x |

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

- Persisted scans: 386; predictions: 3489; observations: 232257.
- Matured sampled outcomes across 1/6/24/48h: 3021; gap abstentions: 10106. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
