# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T15:01:11.286579+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45035783845
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 5502f8b881c6ab49a48fc1bdda1b748d20cfbf2b (atomic ledger/results publication)
**Ledger generation:** 1298 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 62.92 | 90.480 | 73.407 | +2.74% | +0.41% | 6.32x | 1.6 | 2026-11-22T15:01:05.239257+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NEAR/USD | 3.0293 | 85.839 | 87.696 | +4.95% | -0.80% | 1.21x | 4.0 | 2026-11-22T15:01:05.239257+00:00 | Not calibrated | MODERATE 53/100 | HIGH 68/100 | Watch | WATCH |
| 3 | ZEC/USD | 795.99 | 83.547 | 68.516 | +2.29% | +0.01% | 8.32x | 5.0 | 2026-11-22T15:01:05.239257+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04856 | 81.108 | 82.856 | +9.67% | +0.47% | 0.59x | 18.5 | 2026-11-22T15:01:05.239257+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | XBT/USD | 60829.5 | 78.214 | 63.608 | +1.23% | -0.08% | 2.70x | 0.0 | 2026-11-22T15:01:05.239257+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 6 | ETH/USD | 1709.68 | 74.682 | 66.372 | +1.63% | -0.14% | 1.90x | 0.1 | 2026-11-22T15:01:05.239257+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6583 | 73.159 | 66.135 | +1.70% | -0.14% | 1.77x | 1.5 | 2026-11-22T15:01:05.239257+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 8 | LINK/USD | 8.77955 | 72.594 | 58.431 | +2.15% | -0.17% | 2.64x | 1.2 | 2026-11-22T15:01:05.239257+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 9 | AVAX/USD | 6.676 | 66.112 | 51.561 | +1.72% | -0.09% | 8.39x | 4.5 | 2026-11-22T15:01:05.239257+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 10 | TAO/USD | 191.1528 | 61.062 | 66.258 | +2.92% | -0.21% | 0.59x | 7.1 | 2026-11-22T15:01:05.239257+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | VVV/USD | 25.51 | 58.616 | 68.228 | +2.45% | -0.27% | 0.18x | 7.8 | 2026-11-22T15:01:05.239257+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | BNB/USD | 557.12 | 56.870 | 48.792 | +1.77% | +0.10% | 1.76x | 1.8 | 2026-11-22T15:01:05.239257+00:00 | Not calibrated | MODERATE 63/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 87.696 | 3.0293 | -0.80% | 1.21x |
| 2 | NIGHT/USD | 82.856 | 0.04856 | +0.47% | 0.59x |
| 3 | HYPE/USD | 73.407 | 62.92 | +0.41% | 6.32x |
| 4 | ZEC/USD | 68.516 | 795.99 | +0.01% | 8.32x |
| 5 | VVV/USD | 68.228 | 25.51 | -0.27% | 0.18x |
| 6 | ETH/USD | 66.372 | 1709.68 | -0.14% | 1.90x |
| 7 | TAO/USD | 66.258 | 191.1528 | -0.21% | 0.59x |
| 8 | SUI/USD | 66.135 | 0.6583 | -0.14% | 1.77x |
| 9 | XBT/USD | 63.608 | 60829.5 | -0.08% | 2.70x |
| 10 | LINK/USD | 58.431 | 8.77955 | -0.17% | 2.64x |
| 11 | AVAX/USD | 51.561 | 6.676 | -0.09% | 8.39x |
| 12 | BNB/USD | 48.792 | 557.12 | +0.10% | 1.76x |

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

- Persisted scans: 1298; predictions: 10495; observations: 785591.
- Matured sampled outcomes across 1/6/24/48h: 15333; gap abstentions: 22290. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
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

**Writer:** 45035783845 · **Generation:** 1298 · **Legacy run:** 45035783845
**Main quote time:** 2026-11-22T15:01:11.286579+00:00 · **Legacy report time:** 2026-11-22T15:01:57.129111+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 62.92 | 90.48 | +0.41% | 6.32x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NEAR/USD | 3.0293 | 85.84 | -0.80% | 1.21x | MODERATE 53/100 | HIGH 68/100 | Watch |
| 3 | ZEC/USD | 795.99 | 83.55 | +0.01% | 8.32x | STRONG 87/100 | HIGH 55/100 | Watch |
| 4 | NIGHT/USD | 0.04856 | 81.11 | +0.47% | 0.59x | MODERATE 66/100 | VERY_HIGH 76/100 | Watch |
| 5 | XBT/USD | 60829.5 | 78.21 | -0.08% | 2.70x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 6 | ETH/USD | 1709.68 | 74.68 | -0.14% | 1.90x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 7 | SUI/USD | 0.6583 | 73.16 | -0.14% | 1.77x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 8 | LINK/USD | 8.77955 | 72.59 | -0.17% | 2.64x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 9 | AVAX/USD | 6.676 | 66.11 | -0.09% | 8.39x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 10 | TAO/USD | 191.1528 | 61.06 | -0.21% | 0.59x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 11 | VVV/USD | 25.51 | 58.62 | -0.27% | 0.18x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | BNB/USD | 557.12 | 56.87 | +0.10% | 1.76x | MODERATE 63/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 62.87 | 90.00 | +0.41% | 6.32x | 11195 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZBCN/USD | 0.001943 | 75.29 | +1.04% | 1.01x | 4785 | MODERATE 58/100 | EXTREME 89/100 | Do nothing |

**Same-run overlap:** HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
