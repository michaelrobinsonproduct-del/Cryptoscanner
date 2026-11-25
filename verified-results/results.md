# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T19:36:39.207619+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45686552738
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a24baded84b0227b721c1f297c7b38ebae706cb2 (atomic ledger/results publication)
**Ledger generation:** 1757 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LTC/USD | 42.55 | 99.727 | 82.956 | +4.16% | +0.35% | 7.80x | 2.4 | 2026-11-25T19:36:31.064805+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XPL/USD | 0.0486 | 90.171 | 72.065 | +10.45% | +0.62% | 3.33x | 20.6 | 2026-11-25T19:36:31.064805+00:00 | Not calibrated | STRONG 90/100 | HIGH 67/100 | Consider small entry | WATCH |
| 3 | XRP/USD | 0.9426 | 84.292 | 69.021 | +2.06% | +0.05% | 2.73x | 0.7 | 2026-11-25T19:36:31.064805+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 4 | XLM/USD | 0.12797 | 80.038 | 64.113 | +3.16% | +0.19% | 4.37x | 5.0 | 2026-11-25T19:36:31.064805+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 5 | SOL/USD | 70.48 | 78.141 | 63.141 | +1.26% | +0.00% | 2.71x | 1.4 | 2026-11-25T19:36:31.064805+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 6 | ETH/USD | 1688.72 | 74.496 | 59.031 | +0.66% | +0.09% | 2.60x | 1.1 | 2026-11-25T19:36:31.064805+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 7 | XBT/USD | 60057.4 | 73.484 | 58.696 | +0.53% | +0.03% | 2.46x | 0.0 | 2026-11-25T19:36:31.064805+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6658 | 73.330 | 72.530 | +2.83% | +0.56% | 0.80x | 4.5 | 2026-11-25T19:36:31.064805+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 9 | HYPE/USD | 61.54 | 70.280 | 72.899 | +2.79% | +0.51% | 0.48x | 3.3 | 2026-11-25T19:36:31.064805+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XMR/USD | 518.58 | 69.283 | 62.993 | +1.76% | -0.58% | 1.92x | 8.7 | 2026-11-25T19:36:31.064805+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 11 | ZEC/USD | 759.73 | 68.339 | 71.912 | +2.82% | +0.65% | 0.32x | 5.7 | 2026-11-25T19:36:31.064805+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0559038 | 68.083 | 52.744 | +1.21% | +0.07% | 4.13x | 1.5 | 2026-11-25T19:36:31.064805+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 82.956 | 42.55 | +0.35% | 7.80x |
| 2 | HYPE/USD | 72.899 | 61.54 | +0.51% | 0.48x |
| 3 | SUI/USD | 72.530 | 0.6658 | +0.56% | 0.80x |
| 4 | XPL/USD | 72.065 | 0.0486 | +0.62% | 3.33x |
| 5 | ZEC/USD | 71.912 | 759.73 | +0.65% | 0.32x |
| 6 | XRP/USD | 69.021 | 0.9426 | +0.05% | 2.73x |
| 7 | XLM/USD | 64.113 | 0.12797 | +0.19% | 4.37x |
| 8 | SOL/USD | 63.141 | 70.48 | +0.00% | 2.71x |
| 9 | XMR/USD | 62.993 | 518.58 | -0.58% | 1.92x |
| 10 | ETH/USD | 59.031 | 1688.72 | +0.09% | 2.60x |
| 11 | XBT/USD | 58.696 | 60057.4 | +0.03% | 2.46x |
| 12 | XDG/USD | 52.744 | 0.0559038 | +0.07% | 4.13x |

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

- Persisted scans: 1757; predictions: 14828; observations: 1065057.
- Matured sampled outcomes across 1/6/24/48h: 32582; gap abstentions: 22845. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45686552738 · **Generation:** 1757 · **Legacy run:** 45686552738
**Main quote time:** 2026-11-25T19:36:39.207619+00:00 · **Legacy report time:** 2026-11-25T19:37:40.522538+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD ⭐ | 42.55 | 99.73 | +0.35% | 7.80x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XPL/USD ⭐ | 0.0486 | 90.17 | +0.62% | 3.33x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 3 | XRP/USD ⭐ | 0.9426 | 84.29 | +0.05% | 2.73x | STRONG 97/100 | HIGH 55/100 | Watch |
| 4 | XLM/USD ⭐ | 0.12797 | 80.04 | +0.19% | 4.37x | STRONG 95/100 | HIGH 55/100 | Watch |
| 5 | SOL/USD | 70.48 | 78.14 | +0.00% | 2.71x | STRONG 84/100 | HIGH 55/100 | Watch |
| 6 | ETH/USD | 1688.72 | 74.50 | +0.09% | 2.60x | STRONG 82/100 | HIGH 55/100 | Watch |
| 7 | XBT/USD | 60057.4 | 73.48 | +0.03% | 2.46x | STRONG 82/100 | HIGH 55/100 | Watch |
| 8 | SUI/USD | 0.6658 | 73.33 | +0.56% | 0.80x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 9 | HYPE/USD | 61.54 | 70.28 | +0.51% | 0.48x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 10 | XMR/USD | 518.58 | 69.28 | -0.58% | 1.92x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 11 | ZEC/USD | 759.73 | 68.34 | +0.65% | 0.32x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 12 | XDG/USD | 0.0559038 | 68.08 | +0.07% | 4.13x | STRONG 79/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD ⭐ | 42.61 | 100.00 | +0.35% | 7.80x | 13379 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD | 27.574 | 89.47 | +1.47% | 1.02x | 11621 | STRONG 70/100 | VERY_HIGH 74/100 | Watch |
| 3 | XLM/USD ⭐ | 0.128036 | 86.23 | +0.19% | 4.37x | 8200 | STRONG 98/100 | HIGH 55/100 | Watch |
| 4 | CC/USD | 0.07818 | 82.62 | +0.45% | 3.08x | 5327 | STRONG 91/100 | HIGH 66/100 | Consider small entry |
| 5 | XPL/USD ⭐ | 0.0484 | 81.87 | +0.62% | 3.33x | 2352 | STRONG 96/100 | HIGH 67/100 | Consider small entry |
| 6 | XRP/USD ⭐ | 0.94351 | 81.34 | +0.05% | 2.73x | 38748 | STRONG 96/100 | HIGH 55/100 | Watch |
| 7 | HBAR/USD | 0.05189 | 79.45 | +0.29% | 1.70x | 5929 | STRONG 85/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** LTC/USD, XPL/USD, XRP/USD, XLM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
