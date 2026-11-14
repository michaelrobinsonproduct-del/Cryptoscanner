# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-14T21:16:09.121751+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43641868290
**Source SHA:** 0b3881628c9c1e66f0c8c6a8a50d1c27d78caa90
**Previous ledger commit:** f595fd7647a4cbe2b8bf0097bd16485ea62a1409 (atomic ledger/results publication)
**Ledger generation:** 416 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 1s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 4.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CAP/USD | 0.108462 | 53.048 | 43.704 | +1.34% | -0.79% | 2.33x | 4.3 | 2026-11-14T21:16:07.650525+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |
| 2 | PROMPT/USD | 0.01392 | 45.428 | 53.679 | +3.73% | -1.69% | 1.02x | 7.2 | 2026-11-14T21:16:07.650525+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 84/100 | Do nothing | WATCH |
| 3 | MEGA/USD | 0.04522 | 5.869 | 20.663 | +0.85% | -1.37% | 0.20x | 33.1 | 2026-11-14T21:16:07.650525+00:00 | Not calibrated | WEAK 0/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PROMPT/USD | 53.679 | 0.01392 | -1.69% | 1.02x |
| 2 | CAP/USD | 43.704 | 0.108462 | -0.79% | 2.33x |
| 3 | MEGA/USD | 20.663 | 0.04522 | -1.37% | 0.20x |

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

- Persisted scans: 416; predictions: 3592; observations: 250439.
- Matured sampled outcomes across 1/6/24/48h: 3154; gap abstentions: 10553. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 1; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
