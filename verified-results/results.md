# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T11:51:41.533349+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45168640026
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7a341de3c90950b2cc7f7cbba69706319c4622c7 (atomic ledger/results publication)
**Ledger generation:** 1426 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 154.74 | 97.779 | 90.234 | +7.88% | -0.46% | 1.98x | 5.2 | 2026-11-23T11:51:35.087818+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XMR/USD | 504.3 | 81.384 | 66.642 | +2.15% | -0.05% | 3.42x | 6.7 | 2026-11-23T11:51:35.087818+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ALGO/USD | 0.08312 | 78.701 | 76.907 | +10.19% | +0.69% | 0.83x | 6.0 | 2026-11-23T11:51:35.087818+00:00 | Not calibrated | MODERATE 69/100 | HIGH 67/100 | Watch | WATCH |
| 4 | CC/USD | 0.07628 | 76.153 | 60.365 | +4.11% | +0.16% | 3.42x | 6.6 | 2026-11-23T11:51:35.087818+00:00 | Not calibrated | STRONG 83/100 | HIGH 60/100 | Watch | WATCH |
| 5 | SOL/USD | 72.55 | 75.342 | 73.340 | +2.72% | +0.04% | 1.18x | 1.4 | 2026-11-23T11:51:35.087818+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0557302 | 66.778 | 52.457 | +0.81% | -0.14% | 13.59x | 0.4 | 2026-11-23T11:51:35.087818+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6724 | 66.465 | 72.084 | +2.55% | +0.27% | 0.30x | 1.5 | 2026-11-23T11:51:35.087818+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XLM/USD | 0.128985 | 63.680 | 61.603 | +1.14% | +0.18% | 1.12x | 1.6 | 2026-11-23T11:51:35.087818+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 9 | HYPE/USD | 64.09 | 61.257 | 64.874 | +1.63% | -0.14% | 0.71x | 3.1 | 2026-11-23T11:51:35.087818+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XRP/USD | 0.94037 | 60.327 | 64.417 | +1.38% | +0.06% | 0.56x | 0.5 | 2026-11-23T11:51:35.087818+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | NEAR/USD | 3.0124 | 56.005 | 60.212 | +1.03% | +0.03% | 0.56x | 4.0 | 2026-11-23T11:51:35.087818+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XBT/USD | 61377.8 | 53.110 | 57.369 | +0.34% | -0.01% | 0.58x | 0.0 | 2026-11-23T11:51:35.087818+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 90.234 | 154.74 | -0.46% | 1.98x |
| 2 | ALGO/USD | 76.907 | 0.08312 | +0.69% | 0.83x |
| 3 | SOL/USD | 73.340 | 72.55 | +0.04% | 1.18x |
| 4 | SUI/USD | 72.084 | 0.6724 | +0.27% | 0.30x |
| 5 | XMR/USD | 66.642 | 504.3 | -0.05% | 3.42x |
| 6 | HYPE/USD | 64.874 | 64.09 | -0.14% | 0.71x |
| 7 | XRP/USD | 64.417 | 0.94037 | +0.06% | 0.56x |
| 8 | XLM/USD | 61.603 | 0.128985 | +0.18% | 1.12x |
| 9 | CC/USD | 60.365 | 0.07628 | +0.16% | 3.42x |
| 10 | NEAR/USD | 60.212 | 3.0124 | +0.03% | 0.56x |
| 11 | XBT/USD | 57.369 | 61377.8 | -0.01% | 0.58x |
| 12 | XDG/USD | 52.457 | 0.0557302 | -0.14% | 13.59x |

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

- Persisted scans: 1426; predictions: 11879; observations: 863537.
- Matured sampled outcomes across 1/6/24/48h: 19755; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45168640026 · **Generation:** 1426 · **Legacy run:** 45168640026
**Main quote time:** 2026-11-23T11:51:41.533349+00:00 · **Legacy report time:** 2026-11-23T11:52:48.132818+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 154.74 | 97.78 | -0.46% | 1.98x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 2 | XMR/USD | 504.3 | 81.38 | -0.05% | 3.42x | STRONG 71/100 | HIGH 61/100 | Watch |
| 3 | ALGO/USD | 0.08312 | 78.70 | +0.69% | 0.83x | MODERATE 69/100 | HIGH 67/100 | Watch |
| 4 | CC/USD ⭐ | 0.07628 | 76.15 | +0.16% | 3.42x | STRONG 93/100 | HIGH 60/100 | Watch |
| 5 | SOL/USD | 72.55 | 75.34 | +0.04% | 1.18x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 6 | XDG/USD | 0.0557302 | 66.78 | -0.14% | 13.59x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 7 | SUI/USD | 0.6724 | 66.47 | +0.27% | 0.30x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 8 | XLM/USD | 0.128985 | 63.68 | +0.18% | 1.12x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 9 | HYPE/USD | 64.09 | 61.26 | -0.14% | 0.71x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 10 | XRP/USD | 0.94037 | 60.33 | +0.06% | 0.56x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 11 | NEAR/USD | 3.0124 | 56.00 | +0.03% | 0.56x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 12 | XBT/USD | 61377.8 | 53.11 | -0.01% | 0.58x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.07629 | 91.17 | +0.16% | 3.42x | 4000 | STRONG 100/100 | HIGH 60/100 | Watch |
| 2 | INJ/USD | 6.437 | 72.72 | +0.64% | 1.56x | 4381 | STRONG 81/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
