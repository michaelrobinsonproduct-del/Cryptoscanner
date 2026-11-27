# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T01:01:27.642556+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45919949573
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** cf0b607ebe3ae384d329394ed3b782f323cea591 (atomic ledger/results publication)
**Ledger generation:** 1937 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.0812 | 75.634 | 61.025 | +1.09% | -0.08% | 2.66x | 3.2 | 2026-11-27T01:01:19.726671+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 2 | VVV/USD | 26.49 | 75.542 | 59.236 | +1.17% | +0.26% | 2.93x | 7.9 | 2026-11-27T01:01:19.726671+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ETH/USD | 1701.33 | 70.242 | 60.632 | +0.81% | +0.10% | 1.91x | 0.1 | 2026-11-27T01:01:19.726671+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ADA/USD | 0.149457 | 69.944 | 56.533 | +0.67% | +0.07% | 2.31x | 3.6 | 2026-11-27T01:01:19.726671+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 5 | ZEC/USD | 704.12 | 68.399 | 74.584 | +3.29% | +0.40% | 0.18x | 7.0 | 2026-11-27T01:01:19.726671+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | LTC/USD | 44.11 | 65.605 | 59.788 | +0.85% | -0.09% | 1.63x | 2.3 | 2026-11-27T01:01:19.726671+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 7 | HYPE/USD | 63.05 | 64.978 | 62.751 | +1.33% | -0.06% | 1.25x | 3.2 | 2026-11-27T01:01:19.726671+00:00 | Not calibrated | WEAK 42/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XMR/USD | 465.26 | 63.911 | 63.534 | +1.82% | +0.39% | 0.84x | 8.4 | 2026-11-27T01:01:19.726671+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 9 | LINK/USD | 9.34077 | 60.437 | 57.507 | +0.78% | -0.10% | 1.34x | 5.9 | 2026-11-27T01:01:19.726671+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 10 | SOL/USD | 71.26 | 58.941 | 57.456 | +0.45% | -0.18% | 1.24x | 1.4 | 2026-11-27T01:01:19.726671+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 11 | XRP/USD | 0.94668 | 52.193 | 56.809 | +0.42% | +0.00% | 0.54x | 2.2 | 2026-11-27T01:01:19.726671+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | DOT/USD | 0.6763 | 51.311 | 35.496 | +0.57% | +0.16% | 20.54x | 1.5 | 2026-11-27T01:01:19.726671+00:00 | Not calibrated | STRONG 71/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 74.584 | 704.12 | +0.40% | 0.18x |
| 2 | XMR/USD | 63.534 | 465.26 | +0.39% | 0.84x |
| 3 | HYPE/USD | 62.751 | 63.05 | -0.06% | 1.25x |
| 4 | NEAR/USD | 61.025 | 3.0812 | -0.08% | 2.66x |
| 5 | ETH/USD | 60.632 | 1701.33 | +0.10% | 1.91x |
| 6 | LTC/USD | 59.788 | 44.11 | -0.09% | 1.63x |
| 7 | VVV/USD | 59.236 | 26.49 | +0.26% | 2.93x |
| 8 | LINK/USD | 57.507 | 9.34077 | -0.10% | 1.34x |
| 9 | SOL/USD | 57.456 | 71.26 | -0.18% | 1.24x |
| 10 | XRP/USD | 56.809 | 0.94668 | +0.00% | 0.54x |
| 11 | ADA/USD | 56.533 | 0.149457 | +0.07% | 2.31x |
| 12 | DOT/USD | 35.496 | 0.6763 | +0.16% | 20.54x |

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

- Persisted scans: 1937; predictions: 16946; observations: 1173222.
- Matured sampled outcomes across 1/6/24/48h: 37137; gap abstentions: 25416. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45919949573 · **Generation:** 1937 · **Legacy run:** 45919949573
**Main quote time:** 2026-11-27T01:01:27.642556+00:00 · **Legacy report time:** 2026-11-27T01:02:09.230985+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.0812 | 75.63 | -0.08% | 2.66x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 2 | VVV/USD ⭐ | 26.49 | 75.54 | +0.26% | 2.93x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ETH/USD ⭐ | 1701.33 | 70.24 | +0.10% | 1.91x | STRONG 80/100 | HIGH 55/100 | Watch |
| 4 | ADA/USD ⭐ | 0.149457 | 69.94 | +0.07% | 2.31x | STRONG 90/100 | HIGH 55/100 | Watch |
| 5 | ZEC/USD | 704.12 | 68.40 | +0.40% | 0.18x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 6 | LTC/USD | 44.11 | 65.60 | -0.09% | 1.63x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 7 | HYPE/USD | 63.05 | 64.98 | -0.06% | 1.25x | WEAK 42/100 | HIGH 61/100 | Watch |
| 8 | XMR/USD | 465.26 | 63.91 | +0.39% | 0.84x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 9 | LINK/USD | 9.34077 | 60.44 | -0.10% | 1.34x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 10 | SOL/USD | 71.26 | 58.94 | -0.18% | 1.24x | WEAK 39/100 | HIGH 68/100 | Watch |
| 11 | XRP/USD | 0.94668 | 52.19 | +0.00% | 0.54x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 12 | DOT/USD | 0.6763 | 51.31 | +0.16% | 20.54x | STRONG 71/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.42 | 66.82 | +0.26% | 2.93x | 18535 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 2 | ETH/USD ⭐ | 1700.88 | 65.21 | +0.10% | 1.91x | 29398 | STRONG 78/100 | HIGH 55/100 | Watch |
| 3 | ADA/USD ⭐ | 0.149489 | 56.38 | +0.07% | 2.31x | 10134 | STRONG 83/100 | HIGH 55/100 | Watch |
| 4 | PEPE/USD | 3.517e-06 | 53.66 | +0.09% | 1.75x | 5337 | MODERATE 62/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD, ETH/USD, ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
