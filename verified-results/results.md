# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T06:35:11.852954+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44252351825
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** ab6cb5fc413960689f963cb732480aacbe1ef90f (atomic ledger/results publication)
**Ledger generation:** 556 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.3018 | 82.036 | 65.156 | +9.31% | +4.50% | 0.44x | 26.5 | 2026-11-18T06:35:04.215845+00:00 | Not calibrated | MODERATE 61/100 | EXTREME 97/100 | Do nothing | WATCH |
| 2 | CC/USD | 0.08417 | 58.822 | 49.520 | +2.48% | -0.43% | 2.14x | 7.1 | 2026-11-18T06:35:04.215845+00:00 | Not calibrated | MODERATE 59/100 | HIGH 66/100 | Watch | WATCH |
| 3 | SENT/USD | 0.019662 | 55.252 | 61.817 | +5.32% | -0.67% | 0.68x | 12.7 | 2026-11-18T06:35:04.215845+00:00 | Not calibrated | WEAK 28/100 | EXTREME 94/100 | Do nothing | WATCH |
| 4 | PEARL/USD | 1.849 | 51.716 | 46.913 | +2.13% | +0.26% | 1.35x | 5.4 | 2026-11-18T06:35:04.215845+00:00 | Not calibrated | STRONG 71/100 | HIGH 60/100 | Watch | WATCH |
| 5 | MNT/USD | 0.3775 | 38.480 | 36.771 | +1.13% | -0.29% | 1.32x | 7.9 | 2026-11-18T06:35:04.215845+00:00 | Not calibrated | WEAK 39/100 | HIGH 66/100 | Watch | WATCH |
| 6 | AKE/USD | 0.01008587 | 37.711 | 32.900 | +1.02% | -2.04% | 5.32x | 17.3 | 2026-11-18T06:35:04.215845+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | AKT/USD | 0.5144 | 29.544 | 37.479 | +1.00% | +0.12% | 0.15x | 3.9 | 2026-11-18T06:35:04.215845+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ICNT/USD | 65.156 | 0.3018 | +4.50% | 0.44x |
| 2 | SENT/USD | 61.817 | 0.019662 | -0.67% | 0.68x |
| 3 | CC/USD | 49.520 | 0.08417 | -0.43% | 2.14x |
| 4 | PEARL/USD | 46.913 | 1.849 | +0.26% | 1.35x |
| 5 | AKT/USD | 37.479 | 0.5144 | +0.12% | 0.15x |
| 6 | MNT/USD | 36.771 | 0.3775 | -0.29% | 1.32x |
| 7 | AKE/USD | 32.900 | 0.01008587 | -2.04% | 5.32x |

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

- Persisted scans: 556; predictions: 4691; observations: 335611.
- Matured sampled outcomes across 1/6/24/48h: 3991; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44252351825 · **Generation:** 556 · **Legacy run:** 44252351825
**Main quote time:** 2026-11-18T06:35:11.852954+00:00 · **Legacy report time:** 2026-11-18T06:35:29.504159+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD | 0.3018 | 82.04 | +4.50% | 0.44x | MODERATE 61/100 | EXTREME 97/100 | Do nothing |
| 2 | CC/USD | 0.08417 | 58.82 | -0.43% | 2.14x | MODERATE 59/100 | HIGH 66/100 | Watch |
| 3 | SENT/USD | 0.019662 | 55.25 | -0.67% | 0.68x | WEAK 28/100 | EXTREME 94/100 | Do nothing |
| 4 | PEARL/USD ⭐ | 1.849 | 51.72 | +0.26% | 1.35x | STRONG 81/100 | HIGH 60/100 | Watch |
| 5 | MNT/USD | 0.3775 | 38.48 | -0.29% | 1.32x | WEAK 39/100 | HIGH 66/100 | Watch |
| 6 | AKE/USD | 0.01008587 | 37.71 | -2.04% | 5.32x | WEAK 44/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | AKT/USD | 0.5144 | 29.54 | +0.12% | 0.15x | WEAK 35/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 1.849 | 64.29 | +0.26% | 1.35x | 3775 | STRONG 87/100 | HIGH 60/100 | Watch |
| 2 | TRX/USD | 0.308376 | 51.69 | +0.28% | 2.46x | 4089 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** PEARL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
