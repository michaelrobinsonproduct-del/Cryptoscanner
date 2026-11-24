# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T14:52:07.467148+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45418420646
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 9eeef0b24ca36ffb5818147d96db49a1f5afe4f1 (atomic ledger/results publication)
**Ledger generation:** 1588 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.656 | 104.359 | 87.638 | +4.94% | +0.34% | 2.87x | 3.9 | 2026-11-24T14:52:01.671882+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NIGHT/USD | 0.0489 | 69.627 | 51.315 | +1.56% | +0.66% | 3.50x | 6.1 | 2026-11-24T14:52:01.671882+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 3 | PEPE/USD | 3.432e-06 | 65.893 | 47.202 | +0.29% | +0.74% | 8.69x | 2.9 | 2026-11-24T14:52:01.671882+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 4 | 2Z/USD | 0.01641 | 63.529 | 61.702 | +4.86% | +0.68% | 0.84x | 6.1 | 2026-11-24T14:52:01.671882+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 5 | ICNT/USD | 0.3329 | 60.724 | 67.483 | +7.70% | -0.21% | 0.43x | 21.0 | 2026-11-24T14:52:01.671882+00:00 | Not calibrated | WEAK 25/100 | EXTREME 93/100 | Do nothing | WATCH |
| 6 | XMR/USD | 497.09 | 58.802 | 66.930 | +2.28% | -0.07% | 0.22x | 8.0 | 2026-11-24T14:52:01.671882+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | GBP/USD | 1.31122 | 57.954 | 59.166 | +0.61% | +0.06% | 0.85x | 0.2 | 2026-11-24T14:52:01.671882+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 8 | BAT/USD | 0.07761 | 42.296 | 32.688 | +0.57% | +0.80% | 1.56x | 7.7 | 2026-11-24T14:52:01.671882+00:00 | Not calibrated | MODERATE 66/100 | HIGH 60/100 | Watch | WATCH |
| 9 | AUD/USD | 0.66532 | 41.597 | 43.840 | +0.41% | +0.11% | 0.72x | 1.4 | 2026-11-24T14:52:01.671882+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 87.638 | 25.656 | +0.34% | 2.87x |
| 2 | ICNT/USD | 67.483 | 0.3329 | -0.21% | 0.43x |
| 3 | XMR/USD | 66.930 | 497.09 | -0.07% | 0.22x |
| 4 | 2Z/USD | 61.702 | 0.01641 | +0.68% | 0.84x |
| 5 | GBP/USD | 59.166 | 1.31122 | +0.06% | 0.85x |
| 6 | NIGHT/USD | 51.315 | 0.0489 | +0.66% | 3.50x |
| 7 | PEPE/USD | 47.202 | 3.432e-06 | +0.74% | 8.69x |
| 8 | AUD/USD | 43.840 | 0.66532 | +0.11% | 0.72x |
| 9 | BAT/USD | 32.688 | 0.07761 | +0.80% | 1.56x |

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

- Persisted scans: 1588; predictions: 13690; observations: 962187.
- Matured sampled outcomes across 1/6/24/48h: 26991; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45418420646 · **Generation:** 1588 · **Legacy run:** 45418420646
**Main quote time:** 2026-11-24T14:52:07.467148+00:00 · **Legacy report time:** 2026-11-24T14:53:01.080688+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.656 | 104.36 | +0.34% | 2.87x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NIGHT/USD ⭐ | 0.0489 | 69.63 | +0.66% | 3.50x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | PEPE/USD | 3.432e-06 | 65.89 | +0.74% | 8.69x | STRONG 88/100 | HIGH 55/100 | Watch |
| 4 | 2Z/USD | 0.01641 | 63.53 | +0.68% | 0.84x | MODERATE 62/100 | VERY_HIGH 74/100 | Watch |
| 5 | ICNT/USD | 0.3329 | 60.72 | -0.21% | 0.43x | WEAK 25/100 | EXTREME 93/100 | Do nothing |
| 6 | XMR/USD | 497.09 | 58.80 | -0.07% | 0.22x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | GBP/USD | 1.31122 | 57.95 | +0.06% | 0.85x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 8 | BAT/USD ⭐ | 0.07761 | 42.30 | +0.80% | 1.56x | STRONG 76/100 | HIGH 60/100 | Consider small entry |
| 9 | AUD/USD | 0.66532 | 41.60 | +0.11% | 0.72x | WEAK 41/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.572 | 93.51 | +0.34% | 2.87x | 12847 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NIGHT/USD ⭐ | 0.04887 | 68.58 | +0.66% | 3.50x | 10319 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 3 | BAT/USD ⭐ | 0.07766 | 35.80 | +0.80% | 1.56x | 4029 | MODERATE 63/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** VVV/USD, NIGHT/USD, BAT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
