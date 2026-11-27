# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T06:01:40.117953+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45949036110
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d0cd4eba9fed9c550e58a2ec312714f2beb0e44f (atomic ledger/results publication)
**Ledger generation:** 1968 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 602; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 66.13 | 111.219 | 98.233 | +6.28% | +0.11% | 2.25x | 1.5 | 2026-11-27T06:01:32.217721+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | ZEC/USD | 762.54 | 87.692 | 96.521 | +11.87% | -0.21% | 0.22x | 7.0 | 2026-11-27T06:01:32.217721+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | XRP/USD | 0.97006 | 84.550 | 75.226 | +2.90% | +0.26% | 1.80x | 0.1 | 2026-11-27T06:01:32.217721+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | LINK/USD | 9.6763 | 79.499 | 82.733 | +4.40% | -0.07% | 0.71x | 6.1 | 2026-11-27T06:01:32.217721+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | XBT/USD | 61719.1 | 78.331 | 69.121 | +2.02% | +0.04% | 1.90x | 0.0 | 2026-11-27T06:01:32.217721+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 6 | SUI/USD | 0.6866 | 75.470 | 73.614 | +2.83% | +0.26% | 1.05x | 1.5 | 2026-11-27T06:01:32.217721+00:00 | Not calibrated | STRONG 73/100 | HIGH 62/100 | Watch | WATCH |
| 7 | ETH/USD | 1740.21 | 73.691 | 76.759 | +3.11% | -0.11% | 0.75x | 0.1 | 2026-11-27T06:01:32.217721+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | NEAR/USD | 3.13 | 73.493 | 72.418 | +2.69% | +0.35% | 0.93x | 2.9 | 2026-11-27T06:01:32.217721+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 9 | SOL/USD | 73.02 | 73.094 | 74.840 | +2.93% | -0.08% | 0.87x | 1.4 | 2026-11-27T06:01:32.217721+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 10 | W/USD | 0.00978 | 67.127 | 73.062 | +11.01% | -1.32% | 1.07x | 10.2 | 2026-11-27T06:01:32.217721+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 11 | ADA/USD | 0.152922 | 66.993 | 71.963 | +3.01% | +0.31% | 0.35x | 3.7 | 2026-11-27T06:01:32.217721+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | VVV/USD | 27.012 | 63.523 | 72.353 | +3.17% | -1.00% | 0.62x | 9.6 | 2026-11-27T06:01:32.217721+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | HYPE/USD | 98.233 | 66.13 | +0.11% | 2.25x |
| 2 | ZEC/USD | 96.521 | 762.54 | -0.21% | 0.22x |
| 3 | LINK/USD | 82.733 | 9.6763 | -0.07% | 0.71x |
| 4 | ETH/USD | 76.759 | 1740.21 | -0.11% | 0.75x |
| 5 | XRP/USD | 75.226 | 0.97006 | +0.26% | 1.80x |
| 6 | SOL/USD | 74.840 | 73.02 | -0.08% | 0.87x |
| 7 | SUI/USD | 73.614 | 0.6866 | +0.26% | 1.05x |
| 8 | W/USD | 73.062 | 0.00978 | -1.32% | 1.07x |
| 9 | NEAR/USD | 72.418 | 3.13 | +0.35% | 0.93x |
| 10 | VVV/USD | 72.353 | 27.012 | -1.00% | 0.62x |
| 11 | ADA/USD | 71.963 | 0.152922 | +0.31% | 0.35x |
| 12 | XBT/USD | 69.121 | 61719.1 | +0.04% | 1.90x |

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

- Persisted scans: 1968; predictions: 17318; observations: 1191858.
- Matured sampled outcomes across 1/6/24/48h: 38220; gap abstentions: 25560. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45949036110 · **Generation:** 1968 · **Legacy run:** 45949036110
**Main quote time:** 2026-11-27T06:01:40.117953+00:00 · **Legacy report time:** 2026-11-27T06:02:17.869413+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 66.13 | 111.22 | +0.11% | 2.25x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD | 762.54 | 87.69 | -0.21% | 0.22x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |
| 3 | XRP/USD ⭐ | 0.97006 | 84.55 | +0.26% | 1.80x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 4 | LINK/USD | 9.6763 | 79.50 | -0.07% | 0.71x | MODERATE 45/100 | VERY_HIGH 76/100 | Watch |
| 5 | XBT/USD | 61719.1 | 78.33 | +0.04% | 1.90x | STRONG 74/100 | HIGH 55/100 | Watch |
| 6 | SUI/USD ⭐ | 0.6866 | 75.47 | +0.26% | 1.05x | STRONG 83/100 | HIGH 62/100 | Watch |
| 7 | ETH/USD | 1740.21 | 73.69 | -0.11% | 0.75x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 8 | NEAR/USD | 3.13 | 73.49 | +0.35% | 0.93x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 9 | SOL/USD | 73.02 | 73.09 | -0.08% | 0.87x | WEAK 42/100 | HIGH 68/100 | Watch |
| 10 | W/USD | 0.00978 | 67.13 | -1.32% | 1.07x | WEAK 39/100 | VERY_HIGH 83/100 | Do nothing |
| 11 | ADA/USD | 0.152922 | 66.99 | +0.31% | 0.35x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 12 | VVV/USD | 27.012 | 63.52 | -1.00% | 0.62x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 66.12 | 100.00 | +0.11% | 2.25x | 15688 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | XRP/USD ⭐ | 0.96958 | 87.05 | +0.26% | 1.80x | 21666 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 3 | WLD/USD | 0.2519 | 83.92 | +0.12% | 1.92x | 2660 | STRONG 77/100 | HIGH 60/100 | Watch |
| 4 | SUI/USD ⭐ | 0.6873 | 82.15 | +0.26% | 1.05x | 5186 | STRONG 86/100 | HIGH 62/100 | Watch |
| 5 | LTC/USD | 44.75 | 75.44 | +0.09% | 1.04x | 14483 | MODERATE 63/100 | HIGH 62/100 | Watch |

**Same-run overlap:** HYPE/USD, XRP/USD, SUI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
