# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T02:50:50.137034+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46099794800
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 87e136d64a540d003eb8293737eae9f23974eef6 (atomic ledger/results publication)
**Ledger generation:** 2095 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 21.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 64.33 | 76.330 | 63.484 | +1.32% | +0.09% | 2.24x | 1.6 | 2026-11-28T02:50:42.570999+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 2 | XMR/USD | 411.93 | 60.196 | 57.177 | +1.14% | +0.69% | 0.96x | 11.7 | 2026-11-28T02:50:42.570999+00:00 | Not calibrated | MODERATE 55/100 | HIGH 68/100 | Watch | WATCH |
| 3 | ZEC/USD | 749.21 | 58.631 | 66.283 | +1.99% | -0.76% | 0.61x | 5.3 | 2026-11-28T02:50:42.570999+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | CC/USD | 0.07524 | 54.065 | 42.102 | +1.47% | +0.55% | 1.92x | 5.3 | 2026-11-28T02:50:42.570999+00:00 | Not calibrated | STRONG 72/100 | HIGH 60/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.0454 | 53.203 | 59.338 | +0.90% | +0.00% | 0.38x | 3.9 | 2026-11-28T02:50:42.570999+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | VVV/USD | 26.092 | 49.776 | 52.287 | +1.33% | -0.02% | 0.76x | 8.1 | 2026-11-28T02:50:42.570999+00:00 | Not calibrated | WEAK 30/100 | HIGH 68/100 | Do nothing | WATCH |
| 7 | BCH/USD | 208.74 | 48.529 | 40.426 | +0.84% | -0.22% | 1.92x | 5.7 | 2026-11-28T02:50:42.570999+00:00 | Not calibrated | WEAK 44/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ONDO/USD | 0.28786 | 48.445 | 33.948 | +0.26% | -0.10% | 2.61x | 6.3 | 2026-11-28T02:50:42.570999+00:00 | Not calibrated | MODERATE 54/100 | HIGH 66/100 | Watch | WATCH |
| 9 | SPX/USD | 0.2734 | 41.600 | 27.148 | +0.37% | -0.11% | 20.34x | 14.7 | 2026-11-28T02:50:42.570999+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 10 | SENT/USD | 0.024035 | 35.734 | 36.180 | +1.35% | -0.21% | 1.06x | 8.3 | 2026-11-28T02:50:42.570999+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 80/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 66.283 | 749.21 | -0.76% | 0.61x |
| 2 | HYPE/USD | 63.484 | 64.33 | +0.09% | 2.24x |
| 3 | NEAR/USD | 59.338 | 3.0454 | +0.00% | 0.38x |
| 4 | XMR/USD | 57.177 | 411.93 | +0.69% | 0.96x |
| 5 | VVV/USD | 52.287 | 26.092 | -0.02% | 0.76x |
| 6 | CC/USD | 42.102 | 0.07524 | +0.55% | 1.92x |
| 7 | BCH/USD | 40.426 | 208.74 | -0.22% | 1.92x |
| 8 | SENT/USD | 36.180 | 0.024035 | -0.21% | 1.06x |
| 9 | ONDO/USD | 33.948 | 0.28786 | -0.10% | 2.61x |
| 10 | SPX/USD | 27.148 | 0.2734 | -0.11% | 20.34x |

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

- Persisted scans: 2095; predictions: 18801; observations: 1268616.
- Matured sampled outcomes across 1/6/24/48h: 43346; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46099794800 · **Generation:** 2095 · **Legacy run:** 46099794800
**Main quote time:** 2026-11-28T02:50:50.137034+00:00 · **Legacy report time:** 2026-11-28T02:51:47.221646+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 64.33 | 76.33 | +0.09% | 2.24x | STRONG 93/100 | HIGH 55/100 | Watch |
| 2 | XMR/USD | 411.93 | 60.20 | +0.69% | 0.96x | MODERATE 55/100 | HIGH 68/100 | Watch |
| 3 | ZEC/USD | 749.21 | 58.63 | -0.76% | 0.61x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | CC/USD ⭐ | 0.07524 | 54.06 | +0.55% | 1.92x | STRONG 82/100 | HIGH 60/100 | Consider small entry |
| 5 | NEAR/USD | 3.0454 | 53.20 | +0.00% | 0.38x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 6 | VVV/USD | 26.092 | 49.78 | -0.02% | 0.76x | WEAK 30/100 | HIGH 68/100 | Do nothing |
| 7 | BCH/USD | 208.74 | 48.53 | -0.22% | 1.92x | WEAK 44/100 | HIGH 61/100 | Watch |
| 8 | ONDO/USD | 0.28786 | 48.44 | -0.10% | 2.61x | MODERATE 54/100 | HIGH 66/100 | Watch |
| 9 | SPX/USD | 0.2734 | 41.60 | -0.11% | 20.34x | MODERATE 46/100 | VERY_HIGH 72/100 | Watch |
| 10 | SENT/USD | 0.024035 | 35.73 | -0.21% | 1.06x | WEAK 28/100 | VERY_HIGH 80/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 64.35 | 67.27 | +0.09% | 2.24x | 18767 | STRONG 89/100 | HIGH 55/100 | Watch |
| 2 | CC/USD ⭐ | 0.07524 | 52.01 | +0.55% | 1.92x | 5226 | STRONG 81/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** HYPE/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
