# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-14T11:21:46.445567+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43589377261
**Source SHA:** 736b465e7542c5a8e4b7a0fb1f100f55d439f0be
**Previous ledger commit:** ce27d4d9f21994c13fce60bea1b66a23e68b0e7e (atomic ledger/results publication)
**Ledger generation:** 396 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 606; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 534.6 | 68.618 | 52.077 | +1.07% | +0.31% | 4.52x | 20.8 | 2026-11-14T11:21:41.824098+00:00 | Not calibrated | STRONG 79/100 | HIGH 67/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04718 | 62.736 | 45.008 | +0.64% | +1.07% | 2.24x | 14.8 | 2026-11-14T11:21:41.824098+00:00 | Not calibrated | STRONG 81/100 | HIGH 61/100 | Watch | WATCH |
| 3 | PIEVERSE/USD | 1.7615 | 52.458 | 62.433 | +7.53% | -0.43% | 0.22x | 28.4 | 2026-11-14T11:21:41.824098+00:00 | Not calibrated | WEAK 21/100 | EXTREME 100/100 | Do nothing | WATCH |
| 4 | TON/USD | 1.106 | 49.230 | 39.198 | +1.37% | +0.00% | 2.00x | 18.1 | 2026-11-14T11:21:41.824098+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 5 | TRX/USD | 0.31292 | 33.022 | 39.066 | +0.37% | +0.03% | 0.38x | 1.3 | 2026-11-14T11:21:41.824098+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PIEVERSE/USD | 62.433 | 1.7615 | -0.43% | 0.22x |
| 2 | XMR/USD | 52.077 | 534.6 | +0.31% | 4.52x |
| 3 | NIGHT/USD | 45.008 | 0.04718 | +1.07% | 2.24x |
| 4 | TON/USD | 39.198 | 1.106 | +0.00% | 2.00x |
| 5 | TRX/USD | 39.066 | 0.31292 | +0.03% | 0.38x |

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

- Persisted scans: 396; predictions: 3528; observations: 238318.
- Matured sampled outcomes across 1/6/24/48h: 3117; gap abstentions: 10222. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
