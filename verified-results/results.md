# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-14T07:46:29.485290+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43572625955
**Source SHA:** e71dc258e8aeedc5fa1b851544587c4166e8df63
**Previous ledger commit:** cfff70262a07a5d069a7feb431379de7507828b4 (atomic ledger/results publication)
**Ledger generation:** 389 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 2s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 606; OHLC screened: 7.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKE/USD | 0.01270315 | 75.918 | 58.560 | +2.86% | +0.47% | 4.87x | 32.9 | 2026-11-14T07:46:27.263539+00:00 | Not calibrated | STRONG 83/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | UAI/USD | 0.04125 | 60.666 | 70.200 | +6.34% | -1.24% | 0.67x | 17.1 | 2026-11-14T07:46:27.263539+00:00 | Not calibrated | WEAK 30/100 | EXTREME 91/100 | Do nothing | WATCH |
| 3 | PIEVERSE/USD | 1.701 | 50.987 | 45.996 | +3.83% | -0.16% | 1.58x | 24.2 | 2026-11-14T07:46:27.263539+00:00 | Not calibrated | WEAK 35/100 | EXTREME 85/100 | Do nothing | WATCH |
| 4 | ICNT/USD | 0.258 | 31.337 | 31.908 | +0.70% | +0.31% | 0.79x | 7.7 | 2026-11-14T07:46:27.263539+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 74/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UAI/USD | 70.200 | 0.04125 | -1.24% | 0.67x |
| 2 | AKE/USD | 58.560 | 0.01270315 | +0.47% | 4.87x |
| 3 | PIEVERSE/USD | 45.996 | 1.701 | -0.16% | 1.58x |
| 4 | ICNT/USD | 31.908 | 0.258 | +0.31% | 0.79x |

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

- Persisted scans: 389; predictions: 3502; observations: 234075.
- Matured sampled outcomes across 1/6/24/48h: 3057; gap abstentions: 10127. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
