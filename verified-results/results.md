# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T07:01:33.188027+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45127895071
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 87921de37c9c4e3f6355548a89f322689652bcb0 (atomic ledger/results publication)
**Ledger generation:** 1396 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XDC/USD | 0.02744 | 81.396 | 59.957 | +4.89% | +1.29% | 4.35x | 14.6 | 2026-11-23T07:01:26.474741+00:00 | Not calibrated | STRONG 91/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | NIGHT/USD | 0.05025 | 72.330 | 62.634 | +2.20% | -0.08% | 2.01x | 8.0 | 2026-11-23T07:01:26.474741+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 3 | JUP/USD | 0.23843 | 65.758 | 72.418 | +6.17% | -0.33% | 0.50x | 10.5 | 2026-11-23T07:01:26.474741+00:00 | Not calibrated | WEAK 33/100 | EXTREME 87/100 | Do nothing | WATCH |
| 4 | GBP/USD | 1.3125 | 63.889 | 56.709 | +0.27% | +0.00% | 1.72x | 0.3 | 2026-11-23T07:01:26.474741+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 5 | AI/USD | 0.01633 | 63.123 | 73.165 | +11.70% | -0.54% | 0.27x | 6.1 | 2026-11-23T07:01:26.474741+00:00 | Not calibrated | WEAK 37/100 | EXTREME 88/100 | Do nothing | WATCH |
| 6 | SOL/USD | 71.93 | 61.227 | 66.493 | +1.84% | +0.22% | 0.36x | 2.8 | 2026-11-23T07:01:26.474741+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6639 | 61.186 | 63.000 | +1.25% | -0.27% | 0.95x | 1.5 | 2026-11-23T07:01:26.474741+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 8 | CC/USD | 0.07635 | 60.885 | 61.463 | +4.20% | +0.35% | 0.77x | 6.5 | 2026-11-23T07:01:26.474741+00:00 | Not calibrated | MODERATE 60/100 | HIGH 67/100 | Watch | WATCH |
| 9 | XBT/USD | 61391.8 | 58.993 | 57.529 | +0.36% | -0.08% | 1.19x | 0.0 | 2026-11-23T07:01:26.474741+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 10 | DOT/USD | 0.6732 | 58.612 | 45.502 | +1.88% | -0.31% | 2.47x | 1.5 | 2026-11-23T07:01:26.474741+00:00 | Not calibrated | MODERATE 59/100 | HIGH 66/100 | Watch | WATCH |
| 11 | NEAR/USD | 3.002 | 55.124 | 57.933 | +0.68% | -0.09% | 0.76x | 3.7 | 2026-11-23T07:01:26.474741+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | XRP/USD | 0.9385 | 54.148 | 62.845 | +1.18% | -0.12% | 0.19x | 0.9 | 2026-11-23T07:01:26.474741+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | AI/USD | 73.165 | 0.01633 | -0.54% | 0.27x |
| 2 | JUP/USD | 72.418 | 0.23843 | -0.33% | 0.50x |
| 3 | SOL/USD | 66.493 | 71.93 | +0.22% | 0.36x |
| 4 | SUI/USD | 63.000 | 0.6639 | -0.27% | 0.95x |
| 5 | XRP/USD | 62.845 | 0.9385 | -0.12% | 0.19x |
| 6 | NIGHT/USD | 62.634 | 0.05025 | -0.08% | 2.01x |
| 7 | CC/USD | 61.463 | 0.07635 | +0.35% | 0.77x |
| 8 | XDC/USD | 59.957 | 0.02744 | +1.29% | 4.35x |
| 9 | NEAR/USD | 57.933 | 3.002 | -0.09% | 0.76x |
| 10 | XBT/USD | 57.529 | 61391.8 | -0.08% | 1.19x |
| 11 | GBP/USD | 56.709 | 1.3125 | +0.00% | 1.72x |
| 12 | DOT/USD | 45.502 | 0.6732 | -0.31% | 2.47x |

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

- Persisted scans: 1396; predictions: 11519; observations: 845268.
- Matured sampled outcomes across 1/6/24/48h: 18726; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 123 (sampled only; not a success-rate estimate).
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

**Writer:** 45127895071 · **Generation:** 1396 · **Legacy run:** 45127895071
**Main quote time:** 2026-11-23T07:01:33.188027+00:00 · **Legacy report time:** 2026-11-23T07:02:38.645303+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XDC/USD ⭐ | 0.02744 | 81.40 | +1.29% | 4.35x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | NIGHT/USD | 0.05025 | 72.33 | -0.08% | 2.01x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 3 | JUP/USD | 0.23843 | 65.76 | -0.33% | 0.50x | WEAK 33/100 | EXTREME 87/100 | Do nothing |
| 4 | GBP/USD | 1.3125 | 63.89 | +0.00% | 1.72x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 5 | AI/USD | 0.01633 | 63.12 | -0.54% | 0.27x | WEAK 37/100 | EXTREME 88/100 | Do nothing |
| 6 | SOL/USD | 71.93 | 61.23 | +0.22% | 0.36x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 7 | SUI/USD | 0.6639 | 61.19 | -0.27% | 0.95x | WEAK 36/100 | HIGH 68/100 | Watch |
| 8 | CC/USD | 0.07635 | 60.88 | +0.35% | 0.77x | MODERATE 60/100 | HIGH 67/100 | Watch |
| 9 | XBT/USD | 61391.8 | 58.99 | -0.08% | 1.19x | WEAK 39/100 | HIGH 68/100 | Watch |
| 10 | DOT/USD | 0.6732 | 58.61 | -0.31% | 2.47x | MODERATE 59/100 | HIGH 66/100 | Watch |
| 11 | NEAR/USD | 3.002 | 55.12 | -0.09% | 0.76x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 12 | XRP/USD | 0.9385 | 54.15 | -0.12% | 0.19x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XDC/USD ⭐ | 0.02744 | 81.36 | +1.29% | 4.35x | 2363 | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | BLESS/USD | 0.018325 | 77.09 | +0.54% | 1.01x | 5753 | MODERATE 59/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** XDC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
