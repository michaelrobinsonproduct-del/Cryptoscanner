# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T00:41:57.722043+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45298947852
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c5ab1c281e5d510ad5acb43f56f0efe390570b65 (atomic ledger/results publication)
**Ledger generation:** 1502 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LINK/USD | 9.0748 | 75.521 | 58.860 | +0.78% | +0.33% | 5.15x | 3.1 | 2026-11-24T00:41:48.369851+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XRP/USD | 0.94318 | 73.218 | 57.188 | +0.40% | +0.21% | 3.57x | 1.3 | 2026-11-24T00:41:48.369851+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | XDG/USD | 0.0565921 | 72.145 | 58.524 | +0.51% | +0.19% | 2.27x | 0.1 | 2026-11-24T00:41:48.369851+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 4 | UNI/USD | 4.8774 | 69.113 | 54.298 | +0.81% | -0.04% | 6.89x | 5.7 | 2026-11-24T00:41:48.369851+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ADA/USD | 0.149181 | 65.680 | 57.422 | +0.49% | +0.07% | 1.79x | 2.1 | 2026-11-24T00:41:48.369851+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XLM/USD | 0.131353 | 64.439 | 60.262 | +1.05% | +0.50% | 1.17x | 4.1 | 2026-11-24T00:41:48.369851+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 7 | LTC/USD | 41.66 | 59.063 | 57.856 | +0.58% | +0.07% | 1.08x | 2.4 | 2026-11-24T00:41:48.369851+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 8 | BNB/USD | 556.95 | 56.506 | 42.099 | +0.29% | -0.05% | 2.46x | 2.0 | 2026-11-24T00:41:48.369851+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 9 | PEARL/USD | 2.3113 | 55.296 | 48.735 | +0.28% | +0.81% | 1.25x | 16.5 | 2026-11-24T00:41:48.369851+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 10 | VVV/USD | 24.687 | 55.280 | 57.990 | +0.98% | +0.56% | 0.45x | 7.7 | 2026-11-24T00:41:48.369851+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | PAXG/USD | 3645.1 | 55.280 | 52.693 | +0.67% | +0.26% | 1.13x | 1.6 | 2026-11-24T00:41:48.369851+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 12 | NEAR/USD | 2.9937 | 54.992 | 55.260 | +0.42% | -0.52% | 1.23x | 5.4 | 2026-11-24T00:41:48.369851+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XLM/USD | 60.262 | 0.131353 | +0.50% | 1.17x |
| 2 | LINK/USD | 58.860 | 9.0748 | +0.33% | 5.15x |
| 3 | XDG/USD | 58.524 | 0.0565921 | +0.19% | 2.27x |
| 4 | VVV/USD | 57.990 | 24.687 | +0.56% | 0.45x |
| 5 | LTC/USD | 57.856 | 41.66 | +0.07% | 1.08x |
| 6 | ADA/USD | 57.422 | 0.149181 | +0.07% | 1.79x |
| 7 | XRP/USD | 57.188 | 0.94318 | +0.21% | 3.57x |
| 8 | NEAR/USD | 55.260 | 2.9937 | -0.52% | 1.23x |
| 9 | UNI/USD | 54.298 | 4.8774 | -0.04% | 6.89x |
| 10 | PAXG/USD | 52.693 | 3645.1 | +0.26% | 1.13x |
| 11 | PEARL/USD | 48.735 | 2.3113 | +0.81% | 1.25x |
| 12 | BNB/USD | 42.099 | 556.95 | -0.05% | 2.46x |

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

- Persisted scans: 1502; predictions: 12781; observations: 909820.
- Matured sampled outcomes across 1/6/24/48h: 23512; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45298947852 · **Generation:** 1502 · **Legacy run:** 45298947852
**Main quote time:** 2026-11-24T00:41:57.722043+00:00 · **Legacy report time:** 2026-11-24T00:43:10.865397+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD ⭐ | 9.0748 | 75.52 | +0.33% | 5.15x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.94318 | 73.22 | +0.21% | 3.57x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XDG/USD ⭐ | 0.0565921 | 72.14 | +0.19% | 2.27x | STRONG 91/100 | HIGH 55/100 | Watch |
| 4 | UNI/USD | 4.8774 | 69.11 | -0.04% | 6.89x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 5 | ADA/USD ⭐ | 0.149181 | 65.68 | +0.07% | 1.79x | STRONG 78/100 | HIGH 55/100 | Watch |
| 6 | XLM/USD ⭐ | 0.131353 | 64.44 | +0.50% | 1.17x | STRONG 77/100 | HIGH 62/100 | Watch |
| 7 | LTC/USD ⭐ | 41.66 | 59.06 | +0.07% | 1.08x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 8 | BNB/USD | 556.95 | 56.51 | -0.05% | 2.46x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 9 | PEARL/USD | 2.3113 | 55.30 | +0.81% | 1.25x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 10 | VVV/USD | 24.687 | 55.28 | +0.56% | 0.45x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 11 | PAXG/USD ⭐ | 3645.1 | 55.28 | +0.26% | 1.13x | STRONG 73/100 | HIGH 62/100 | Watch |
| 12 | NEAR/USD | 2.9937 | 54.99 | -0.52% | 1.23x | WEAK 37/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD ⭐ | 9.06451 | 64.32 | +0.33% | 5.15x | 8681 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.94262 | 63.47 | +0.21% | 3.57x | 44192 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 3 | XDG/USD ⭐ | 0.0565702 | 57.63 | +0.19% | 2.27x | 10368 | STRONG 84/100 | HIGH 55/100 | Watch |
| 4 | XLM/USD ⭐ | 0.131315 | 57.37 | +0.50% | 1.17x | 17851 | STRONG 74/100 | HIGH 62/100 | Watch |
| 5 | PAXG/USD ⭐ | 3648.17 | 57.25 | +0.26% | 1.13x | 6097 | STRONG 74/100 | HIGH 62/100 | Watch |
| 6 | ADA/USD ⭐ | 0.149114 | 55.00 | +0.07% | 1.79x | 14259 | STRONG 72/100 | HIGH 55/100 | Watch |
| 7 | LTC/USD ⭐ | 41.64 | 49.32 | +0.07% | 1.08x | 12854 | MODERATE 60/100 | HIGH 62/100 | Watch |

**Same-run overlap:** LINK/USD, XRP/USD, XDG/USD, ADA/USD, XLM/USD, LTC/USD, PAXG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
