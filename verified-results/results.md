# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-14T02:55:24.325036+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43548868582
**Source SHA:** 7857a48ba7d84b8ebc4a711f2cdbbc5515ea9cd1
**Previous ledger commit:** 6fc0d4c47d86e1b6f46a8ec7aa1a1b78020fec54 (atomic ledger/results publication)
**Ledger generation:** 379 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 8.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZAMA/USD | 0.05859 | 50.421 | 37.343 | +1.21% | +1.17% | 1.72x | 6.8 | 2026-11-14T02:55:21.620107+00:00 | Not calibrated | STRONG 70/100 | HIGH 60/100 | Watch | WATCH |
| 2 | XDC/USD | 0.02891 | 48.524 | 32.311 | +0.31% | +0.24% | 2.70x | 10.4 | 2026-11-14T02:55:21.620107+00:00 | Not calibrated | STRONG 74/100 | HIGH 66/100 | Watch | WATCH |
| 3 | MEGA/USD | 0.04576 | 48.444 | 26.577 | +2.05% | +1.37% | 7.78x | 37.2 | 2026-11-14T02:55:21.620107+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | ZRO/USD | 1.581 | 40.722 | 33.581 | +0.25% | +0.32% | 1.56x | 19.0 | 2026-11-14T02:55:21.620107+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 5 | PROMPT/USD | 0.01385 | 40.647 | 42.374 | +3.20% | +1.09% | 0.28x | 21.5 | 2026-11-14T02:55:21.620107+00:00 | Not calibrated | WEAK 40/100 | EXTREME 94/100 | Do nothing | WATCH |
| 6 | ICNT/USD | 0.258 | 21.212 | 30.096 | +0.70% | -0.89% | 0.55x | 11.6 | 2026-11-14T02:55:21.620107+00:00 | Not calibrated | WEAK 11/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PROMPT/USD | 42.374 | 0.01385 | +1.09% | 0.28x |
| 2 | ZAMA/USD | 37.343 | 0.05859 | +1.17% | 1.72x |
| 3 | ZRO/USD | 33.581 | 1.581 | +0.32% | 1.56x |
| 4 | XDC/USD | 32.311 | 0.02891 | +0.24% | 2.70x |
| 5 | ICNT/USD | 30.096 | 0.258 | -0.89% | 0.55x |
| 6 | MEGA/USD | 26.577 | 0.04576 | +1.37% | 7.78x |

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

- Persisted scans: 379; predictions: 3468; observations: 228008.
- Matured sampled outcomes across 1/6/24/48h: 2979; gap abstentions: 10017. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
