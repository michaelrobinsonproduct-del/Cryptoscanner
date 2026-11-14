# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-14T15:51:39.586019+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43612162246
**Source SHA:** 36c0409ea72f3e76429e8e5b76fa2b43315f4918
**Previous ledger commit:** 9dd3df04dd92940d49699e16e87981eecd59d7d9 (atomic ledger/results publication)
**Ledger generation:** 404 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 2s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 606; OHLC screened: 7.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05001 | 84.958 | 90.014 | +6.68% | -0.85% | 0.92x | 20.0 | 2026-11-14T15:51:37.849617+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | AKE/USD | 0.01297398 | 79.776 | 79.844 | +5.05% | +0.28% | 0.86x | 21.1 | 2026-11-14T15:51:37.849617+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | CAP/USD | 0.109078 | 43.651 | 50.074 | +1.91% | +0.22% | 0.25x | 1.9 | 2026-11-14T15:51:37.849617+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 90.014 | 0.05001 | -0.85% | 0.92x |
| 2 | AKE/USD | 79.844 | 0.01297398 | +0.28% | 0.86x |
| 3 | CAP/USD | 50.074 | 0.109078 | +0.22% | 0.25x |

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

- Persisted scans: 404; predictions: 3554; observations: 243166.
- Matured sampled outcomes across 1/6/24/48h: 3133; gap abstentions: 10366. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
