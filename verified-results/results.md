# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-14T03:54:45.384511+00:00
**GitHub trigger:** authenticated on-demand scan request (verified event=push; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43553980524
**Source SHA:** c99059ab38afa899eea337921e39efae1387e63e
**Previous ledger commit:** 61aca2385539389ba5e559c8be14d7e702f42d7f (atomic ledger/results publication)
**Ledger generation:** 381 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 1s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 5.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKE/USD | 0.01248608 | 78.969 | 58.180 | +1.10% | +7.06% | 0.58x | 9.1 | 2026-11-14T03:54:44.030627+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 2 | UAI/USD | 0.04165 | 62.210 | 70.713 | +7.37% | -2.68% | 1.49x | 14.5 | 2026-11-14T03:54:44.030627+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 3 | CAP/USD | 0.107681 | 46.355 | 34.673 | +0.61% | +0.81% | 1.76x | 14.2 | 2026-11-14T03:54:44.030627+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ICNT/USD | 0.2571 | 30.258 | 27.614 | +0.35% | +0.04% | 1.24x | 11.7 | 2026-11-14T03:54:44.030627+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 80/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UAI/USD | 70.713 | 0.04165 | -2.68% | 1.49x |
| 2 | AKE/USD | 58.180 | 0.01248608 | +7.06% | 0.58x |
| 3 | CAP/USD | 34.673 | 0.107681 | +0.81% | 1.76x |
| 4 | ICNT/USD | 27.614 | 0.2571 | +0.04% | 1.24x |

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

- Persisted scans: 381; predictions: 3474; observations: 229222.
- Matured sampled outcomes across 1/6/24/48h: 2993; gap abstentions: 10050. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 1; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.
