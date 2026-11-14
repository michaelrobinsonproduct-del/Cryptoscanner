# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-14T05:23:14.124123+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43561251820
**Source SHA:** 22d700ffdd5cf951d00938d39bb83942c82176e3
**Previous ledger commit:** b84ecc82818e1e233d2092a56ab55101d8322046 (atomic ledger/results publication)
**Ledger generation:** 384 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 8.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | UAI/USD | 0.04186 | 78.741 | 68.651 | +7.91% | +2.82% | 0.60x | 19.1 | 2026-11-14T05:23:11.594080+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 2 | BMT/USD | 0.0242 | 56.020 | 59.345 | +7.60% | +1.00% | 0.17x | 33.2 | 2026-11-14T05:23:11.594080+00:00 | Not calibrated | MODERATE 48/100 | EXTREME 94/100 | Do nothing | WATCH |
| 3 | INJ/USD | 8.092 | 52.081 | 54.514 | +0.37% | +0.76% | 0.38x | 6.2 | 2026-11-14T05:23:11.594080+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | PIEVERSE/USD | 1.7208 | 43.760 | 46.510 | +5.04% | +0.15% | 0.65x | 39.9 | 2026-11-14T05:23:11.594080+00:00 | Not calibrated | WEAK 27/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UAI/USD | 68.651 | 0.04186 | +2.82% | 0.60x |
| 2 | BMT/USD | 59.345 | 0.0242 | +1.00% | 0.17x |
| 3 | INJ/USD | 54.514 | 8.092 | +0.76% | 0.38x |
| 4 | PIEVERSE/USD | 46.510 | 1.7208 | +0.15% | 0.65x |

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

- Persisted scans: 384; predictions: 3481; observations: 231043.
- Matured sampled outcomes across 1/6/24/48h: 3003; gap abstentions: 10088. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
