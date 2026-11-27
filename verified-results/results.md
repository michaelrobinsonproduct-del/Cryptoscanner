# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T02:21:26.661596+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45927648909
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 5eaa94b1020e1e594b074dc94fd6f43d2fcbc895 (atomic ledger/results publication)
**Ledger generation:** 1945 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 724.92 | 124.462 | 96.386 | +6.35% | +2.62% | 4.17x | 6.1 | 2026-11-27T02:21:19.854227+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | UNI/USD | 4.8391 | 97.459 | 65.966 | +4.06% | +3.30% | 4.01x | 8.3 | 2026-11-27T02:21:19.854227+00:00 | Not calibrated | STRONG 100/100 | HIGH 65/100 | Consider small entry | WATCH |
| 3 | HYPE/USD | 63.92 | 95.757 | 72.561 | +2.73% | +1.64% | 16.92x | 3.1 | 2026-11-27T02:21:19.854227+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | VVV/USD | 26.611 | 88.511 | 62.498 | +1.63% | +2.20% | 4.04x | 7.9 | 2026-11-27T02:21:19.854227+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | NEAR/USD | 3.1084 | 87.123 | 66.804 | +1.99% | +1.06% | 3.74x | 4.2 | 2026-11-27T02:21:19.854227+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | ETH/USD | 1712.13 | 84.225 | 65.112 | +1.45% | +0.82% | 6.90x | 0.1 | 2026-11-27T02:21:19.854227+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | XRP/USD | 0.955 | 82.404 | 63.572 | +1.30% | +0.77% | 3.00x | 1.0 | 2026-11-27T02:21:19.854227+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | ADA/USD | 0.15082 | 81.506 | 61.056 | +1.59% | +1.09% | 3.71x | 4.9 | 2026-11-27T02:21:19.854227+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | XBT/USD | 61132 | 80.766 | 62.328 | +1.05% | +0.69% | 3.54x | 0.0 | 2026-11-27T02:21:19.854227+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 10 | LINK/USD | 9.429 | 80.334 | 65.430 | +1.73% | +1.20% | 1.89x | 3.4 | 2026-11-27T02:21:19.854227+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Consider small entry | WATCH |
| 11 | SOL/USD | 71.98 | 80.064 | 64.568 | +1.47% | +0.69% | 2.21x | 1.4 | 2026-11-27T02:21:19.854227+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 12 | LTC/USD | 44.35 | 76.332 | 61.368 | +1.39% | +0.75% | 2.12x | 4.5 | 2026-11-27T02:21:19.854227+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 96.386 | 724.92 | +2.62% | 4.17x |
| 2 | HYPE/USD | 72.561 | 63.92 | +1.64% | 16.92x |
| 3 | NEAR/USD | 66.804 | 3.1084 | +1.06% | 3.74x |
| 4 | UNI/USD | 65.966 | 4.8391 | +3.30% | 4.01x |
| 5 | LINK/USD | 65.430 | 9.429 | +1.20% | 1.89x |
| 6 | ETH/USD | 65.112 | 1712.13 | +0.82% | 6.90x |
| 7 | SOL/USD | 64.568 | 71.98 | +0.69% | 2.21x |
| 8 | XRP/USD | 63.572 | 0.955 | +0.77% | 3.00x |
| 9 | VVV/USD | 62.498 | 26.611 | +2.20% | 4.04x |
| 10 | XBT/USD | 62.328 | 61132 | +0.69% | 3.54x |
| 11 | LTC/USD | 61.368 | 44.35 | +0.75% | 2.12x |
| 12 | ADA/USD | 61.056 | 0.15082 | +1.09% | 3.71x |

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

- Persisted scans: 1945; predictions: 17042; observations: 1178030.
- Matured sampled outcomes across 1/6/24/48h: 37394; gap abstentions: 25455. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45927648909 · **Generation:** 1945 · **Legacy run:** 45927648909
**Main quote time:** 2026-11-27T02:21:26.661596+00:00 · **Legacy report time:** 2026-11-27T02:22:19.778776+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 724.92 | 124.46 | +2.62% | 4.17x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UNI/USD ⭐ | 4.8391 | 97.46 | +3.30% | 4.01x | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 3 | HYPE/USD ⭐ | 63.92 | 95.76 | +1.64% | 16.92x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | VVV/USD ⭐ | 26.611 | 88.51 | +2.20% | 4.04x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | NEAR/USD ⭐ | 3.1084 | 87.12 | +1.06% | 3.74x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | ETH/USD ⭐ | 1712.13 | 84.23 | +0.82% | 6.90x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | XRP/USD ⭐ | 0.955 | 82.40 | +0.77% | 3.00x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | ADA/USD ⭐ | 0.15082 | 81.51 | +1.09% | 3.71x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | XBT/USD ⭐ | 61132 | 80.77 | +0.69% | 3.54x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 10 | LINK/USD ⭐ | 9.429 | 80.33 | +1.20% | 1.89x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 11 | SOL/USD ⭐ | 71.98 | 80.06 | +0.69% | 2.21x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 12 | LTC/USD ⭐ | 44.35 | 76.33 | +0.75% | 2.12x | STRONG 100/100 | HIGH 55/100 | Consider small entry |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 733.13 | 100.00 | +2.62% | 4.17x | 35571 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HYPE/USD ⭐ | 64.06 | 94.16 | +1.64% | 16.92x | 13059 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | UNI/USD ⭐ | 4.861 | 93.04 | +3.30% | 4.01x | 6097 | STRONG 100/100 | VERY_HIGH 71/100 | Watch |
| 4 | NEAR/USD ⭐ | 3.1166 | 81.90 | +1.06% | 3.74x | 13491 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | ETH/USD ⭐ | 1714.62 | 81.51 | +0.82% | 6.90x | 30190 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | XRP/USD ⭐ | 0.95641 | 76.97 | +0.77% | 3.00x | 20659 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | XBT/USD ⭐ | 61218.2 | 76.32 | +0.69% | 3.54x | 131207 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | SOL/USD ⭐ | 72.04 | 74.72 | +0.69% | 2.21x | 33034 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | VVV/USD ⭐ | 26.663 | 73.61 | +2.20% | 4.04x | 17800 | STRONG 97/100 | HIGH 61/100 | Consider small entry |
| 10 | ADA/USD ⭐ | 0.150691 | 71.35 | +1.09% | 3.71x | 9917 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 11 | LTC/USD ⭐ | 44.37 | 70.86 | +0.75% | 2.12x | 14196 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 12 | LINK/USD ⭐ | 9.43667 | 68.83 | +1.20% | 1.89x | 7155 | STRONG 89/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ZEC/USD, UNI/USD, HYPE/USD, VVV/USD, NEAR/USD, ETH/USD, XRP/USD, ADA/USD, XBT/USD, LINK/USD, SOL/USD, LTC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
