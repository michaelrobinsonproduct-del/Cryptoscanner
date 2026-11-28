# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T01:22:19.878860+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46092524586
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4a1d679b6526b807d665028501124aa0e9245442 (atomic ledger/results publication)
**Ledger generation:** 2086 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 748.3 | 87.551 | 65.947 | +1.87% | +1.32% | 2.66x | 4.3 | 2026-11-28T01:22:12.167161+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | SOL/USD | 72.01 | 75.683 | 58.314 | +0.57% | +0.47% | 3.22x | 1.4 | 2026-11-28T01:22:12.167161+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | NEAR/USD | 3.0436 | 71.356 | 58.425 | +0.84% | +1.06% | 1.76x | 4.9 | 2026-11-28T01:22:12.167161+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | XBT/USD | 60091.3 | 70.070 | 57.652 | +0.38% | +0.33% | 2.08x | 0.0 | 2026-11-28T01:22:12.167161+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | HYPE/USD | 64.23 | 69.772 | 62.380 | +1.17% | +0.77% | 1.36x | 1.6 | 2026-11-28T01:22:12.167161+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0579393 | 63.884 | 58.189 | +0.46% | +0.31% | 1.42x | 0.1 | 2026-11-28T01:22:12.167161+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 7 | ETH/USD | 1666.42 | 62.489 | 57.292 | +0.33% | +0.29% | 1.38x | 0.1 | 2026-11-28T01:22:12.167161+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 8 | TAO/USD | 189.0163 | 61.645 | 59.812 | +1.10% | +0.43% | 0.97x | 5.8 | 2026-11-28T01:22:12.167161+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 9 | LINK/USD | 9.40008 | 61.125 | 56.572 | +0.34% | +0.28% | 1.32x | 1.7 | 2026-11-28T01:22:12.167161+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 10 | AVAX/USD | 6.635 | 60.214 | 43.173 | +0.45% | +0.41% | 6.56x | 1.5 | 2026-11-28T01:22:12.167161+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 11 | XRP/USD | 0.95197 | 55.871 | 57.842 | +0.41% | +0.25% | 0.68x | 0.1 | 2026-11-28T01:22:12.167161+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XLM/USD | 0.127083 | 53.157 | 48.928 | +0.29% | +0.21% | 1.32x | 2.3 | 2026-11-28T01:22:12.167161+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 65.947 | 748.3 | +1.32% | 2.66x |
| 2 | HYPE/USD | 62.380 | 64.23 | +0.77% | 1.36x |
| 3 | TAO/USD | 59.812 | 189.0163 | +0.43% | 0.97x |
| 4 | NEAR/USD | 58.425 | 3.0436 | +1.06% | 1.76x |
| 5 | SOL/USD | 58.314 | 72.01 | +0.47% | 3.22x |
| 6 | XDG/USD | 58.189 | 0.0579393 | +0.31% | 1.42x |
| 7 | XRP/USD | 57.842 | 0.95197 | +0.25% | 0.68x |
| 8 | XBT/USD | 57.652 | 60091.3 | +0.33% | 2.08x |
| 9 | ETH/USD | 57.292 | 1666.42 | +0.29% | 1.38x |
| 10 | LINK/USD | 56.572 | 9.40008 | +0.28% | 1.32x |
| 11 | XLM/USD | 48.928 | 0.127083 | +0.21% | 1.32x |
| 12 | AVAX/USD | 43.173 | 6.635 | +0.41% | 6.56x |

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

- Persisted scans: 2086; predictions: 18695; observations: 1263162.
- Matured sampled outcomes across 1/6/24/48h: 42965; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46092524586 · **Generation:** 2086 · **Legacy run:** 46092524586
**Main quote time:** 2026-11-28T01:22:19.878860+00:00 · **Legacy report time:** 2026-11-28T01:22:57.829867+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 748.3 | 87.55 | +1.32% | 2.66x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SOL/USD ⭐ | 72.01 | 75.68 | +0.47% | 3.22x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD ⭐ | 3.0436 | 71.36 | +1.06% | 1.76x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 4 | XBT/USD ⭐ | 60091.3 | 70.07 | +0.33% | 2.08x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | HYPE/USD ⭐ | 64.23 | 69.77 | +0.77% | 1.36x | STRONG 90/100 | HIGH 55/100 | Watch |
| 6 | XDG/USD ⭐ | 0.0579393 | 63.88 | +0.31% | 1.42x | STRONG 87/100 | HIGH 55/100 | Watch |
| 7 | ETH/USD ⭐ | 1666.42 | 62.49 | +0.29% | 1.38x | STRONG 86/100 | HIGH 55/100 | Watch |
| 8 | TAO/USD | 189.0163 | 61.64 | +0.43% | 0.97x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 9 | LINK/USD ⭐ | 9.40008 | 61.13 | +0.28% | 1.32x | STRONG 86/100 | HIGH 55/100 | Watch |
| 10 | AVAX/USD | 6.635 | 60.21 | +0.41% | 6.56x | STRONG 85/100 | HIGH 55/100 | Watch |
| 11 | XRP/USD | 0.95197 | 55.87 | +0.25% | 0.68x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 12 | XLM/USD ⭐ | 0.127083 | 53.16 | +0.21% | 1.32x | STRONG 82/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 752.48 | 83.08 | +1.32% | 2.66x | 33576 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SOL/USD ⭐ | 72.06 | 66.36 | +0.47% | 3.22x | 45104 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 3 | HYPE/USD ⭐ | 64.27 | 64.25 | +0.77% | 1.36x | 20000 | STRONG 87/100 | HIGH 55/100 | Watch |
| 4 | NEAR/USD ⭐ | 3.0453 | 62.44 | +1.06% | 1.76x | 14282 | STRONG 86/100 | HIGH 55/100 | Consider small entry |
| 5 | SENT/USD | 0.024349 | 62.35 | +2.19% | 1.30x | 3646 | MODERATE 61/100 | VERY_HIGH 73/100 | Watch |
| 6 | XBT/USD ⭐ | 60088.1 | 61.76 | +0.33% | 2.08x | 166906 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 7 | XDG/USD ⭐ | 0.0579501 | 60.24 | +0.31% | 1.42x | 13509 | STRONG 85/100 | HIGH 55/100 | Watch |
| 8 | ETH/USD ⭐ | 1667.51 | 59.01 | +0.29% | 1.38x | 46812 | STRONG 85/100 | HIGH 55/100 | Watch |
| 9 | XLM/USD ⭐ | 0.127083 | 52.44 | +0.21% | 1.32x | 8693 | STRONG 81/100 | HIGH 55/100 | Watch |
| 10 | LINK/USD ⭐ | 9.40057 | 51.90 | +0.28% | 1.32x | 9265 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD, SOL/USD, NEAR/USD, XBT/USD, HYPE/USD, XDG/USD, ETH/USD, LINK/USD, XLM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
