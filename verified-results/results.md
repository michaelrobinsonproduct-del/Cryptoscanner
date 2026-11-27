# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T13:01:51.973238+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46003237397
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8c8c0d8779efb39ff1c2b2ffe03704ccc83f63d9 (atomic ledger/results publication)
**Ledger generation:** 2011 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 65.97 | 113.563 | 96.430 | +6.03% | +0.43% | 3.30x | 1.5 | 2026-11-27T13:01:44.052169+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 27.446 | 94.860 | 80.742 | +4.82% | +0.78% | 2.02x | 10.6 | 2026-11-27T13:01:44.052169+00:00 | Not calibrated | STRONG 97/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | ZEC/USD | 761.54 | 91.238 | 96.843 | +11.72% | +0.45% | 0.21x | 6.3 | 2026-11-27T13:01:44.052169+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | SOL/USD | 73.06 | 90.988 | 75.235 | +2.99% | +0.15% | 4.05x | 1.4 | 2026-11-27T13:01:44.052169+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 5 | LINK/USD | 9.48681 | 85.169 | 71.488 | +2.36% | -0.26% | 58.30x | 0.0 | 2026-11-27T13:01:44.052169+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 6 | ETH/USD | 1722.52 | 78.675 | 69.422 | +2.06% | +0.13% | 1.86x | 0.1 | 2026-11-27T13:01:44.052169+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 7 | XRP/USD | 0.97255 | 77.966 | 76.561 | +3.16% | +0.23% | 1.02x | 1.1 | 2026-11-27T13:01:44.052169+00:00 | Not calibrated | STRONG 74/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0585603 | 76.574 | 72.746 | +3.88% | -0.15% | 1.46x | 2.2 | 2026-11-27T13:01:44.052169+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 9 | PEPE/USD | 3.639e-06 | 74.129 | 72.192 | +4.63% | -0.11% | 1.25x | 8.3 | 2026-11-27T13:01:44.052169+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6865 | 72.052 | 73.252 | +2.82% | +0.09% | 0.84x | 2.9 | 2026-11-27T13:01:44.052169+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 11 | KNTQ/USD | 0.22214 | 66.594 | 73.450 | +5.89% | +0.42% | 0.11x | 0.5 | 2026-11-27T13:01:44.052169+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 12 | XBT/USD | 61523.2 | 64.730 | 66.854 | +1.69% | +0.16% | 0.71x | 0.0 | 2026-11-27T13:01:44.052169+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 96.843 | 761.54 | +0.45% | 0.21x |
| 2 | HYPE/USD | 96.430 | 65.97 | +0.43% | 3.30x |
| 3 | VVV/USD | 80.742 | 27.446 | +0.78% | 2.02x |
| 4 | XRP/USD | 76.561 | 0.97255 | +0.23% | 1.02x |
| 5 | SOL/USD | 75.235 | 73.06 | +0.15% | 4.05x |
| 6 | KNTQ/USD | 73.450 | 0.22214 | +0.42% | 0.11x |
| 7 | SUI/USD | 73.252 | 0.6865 | +0.09% | 0.84x |
| 8 | XDG/USD | 72.746 | 0.0585603 | -0.15% | 1.46x |
| 9 | PEPE/USD | 72.192 | 3.639e-06 | -0.11% | 1.25x |
| 10 | LINK/USD | 71.488 | 9.48681 | -0.26% | 58.30x |
| 11 | ETH/USD | 69.422 | 1722.52 | +0.13% | 1.86x |
| 12 | XBT/USD | 66.854 | 61523.2 | +0.16% | 0.71x |

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

- Persisted scans: 2011; predictions: 17834; observations: 1217782.
- Matured sampled outcomes across 1/6/24/48h: 39713; gap abstentions: 25848. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46003237397 · **Generation:** 2011 · **Legacy run:** 46003237397
**Main quote time:** 2026-11-27T13:01:51.973238+00:00 · **Legacy report time:** 2026-11-27T13:02:29.558027+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 65.97 | 113.56 | +0.43% | 3.30x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 27.446 | 94.86 | +0.78% | 2.02x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | ZEC/USD | 761.54 | 91.24 | +0.45% | 0.21x | STRONG 76/100 | VERY_HIGH 70/100 | Watch |
| 4 | SOL/USD ⭐ | 73.06 | 90.99 | +0.15% | 4.05x | STRONG 100/100 | HIGH 55/100 | Watch |
| 5 | LINK/USD | 9.48681 | 85.17 | -0.26% | 58.30x | STRONG 73/100 | HIGH 61/100 | Watch |
| 6 | ETH/USD ⭐ | 1722.52 | 78.67 | +0.13% | 1.86x | STRONG 84/100 | HIGH 55/100 | Watch |
| 7 | XRP/USD ⭐ | 0.97255 | 77.97 | +0.23% | 1.02x | STRONG 84/100 | HIGH 62/100 | Watch |
| 8 | XDG/USD | 0.0585603 | 76.57 | -0.15% | 1.46x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 9 | PEPE/USD | 3.639e-06 | 74.13 | -0.11% | 1.25x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 10 | SUI/USD | 0.6865 | 72.05 | +0.09% | 0.84x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 11 | KNTQ/USD | 0.22214 | 66.59 | +0.42% | 0.11x | MODERATE 63/100 | VERY_HIGH 75/100 | Watch |
| 12 | XBT/USD | 61523.2 | 64.73 | +0.16% | 0.71x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 65.94 | 100.00 | +0.43% | 3.30x | 15704 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SOL/USD ⭐ | 73.05 | 93.41 | +0.15% | 4.05x | 33969 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | VVV/USD ⭐ | 27.466 | 89.79 | +0.78% | 2.02x | 9364 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | XRP/USD ⭐ | 0.9719 | 87.84 | +0.23% | 1.02x | 27179 | STRONG 89/100 | HIGH 62/100 | Watch |
| 5 | ETH/USD ⭐ | 1721.05 | 79.44 | +0.13% | 1.86x | 36000 | STRONG 85/100 | HIGH 55/100 | Watch |

**Same-run overlap:** HYPE/USD, VVV/USD, SOL/USD, ETH/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
