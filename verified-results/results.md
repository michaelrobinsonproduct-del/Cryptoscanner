# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T00:52:00.469084+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45300278422
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 755cb077e39ce646017928bf51d5a841ca78d7fa (atomic ledger/results publication)
**Ledger generation:** 1503 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XDG/USD | 0.0566122 | 74.681 | 58.809 | +0.55% | +0.17% | 7.29x | 0.0 | 2026-11-24T00:51:51.323088+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 2 | LINK/USD | 9.05145 | 72.261 | 57.333 | +0.52% | -0.01% | 18.99x | 2.6 | 2026-11-24T00:51:51.323088+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XLM/USD | 0.130968 | 70.506 | 58.641 | +0.75% | +0.05% | 2.16x | 3.2 | 2026-11-24T00:51:51.323088+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 4 | UNI/USD | 4.8597 | 67.620 | 52.507 | +0.45% | +0.02% | 6.86x | 4.1 | 2026-11-24T00:51:51.323088+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 5 | PAXG/USD | 3648.81 | 65.003 | 53.019 | +0.77% | +0.16% | 2.12x | 2.5 | 2026-11-24T00:51:51.323088+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 6 | ALGO/USD | 0.08165 | 64.251 | 49.312 | +0.28% | -0.01% | 7.29x | 7.4 | 2026-11-24T00:51:51.323088+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 7 | PEARL/USD | 2.3276 | 62.891 | 53.320 | +0.99% | +1.31% | 1.30x | 17.2 | 2026-11-24T00:51:51.323088+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 8 | LTC/USD | 41.55 | 60.574 | 54.790 | +0.31% | -0.12% | 1.64x | 4.8 | 2026-11-24T00:51:51.323088+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 9 | VVV/USD | 24.639 | 60.366 | 56.813 | +0.78% | +0.28% | 1.21x | 7.3 | 2026-11-24T00:51:51.323088+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 10 | ADA/USD | 0.148904 | 56.576 | 55.408 | +0.31% | +0.03% | 1.10x | 3.5 | 2026-11-24T00:51:51.323088+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |
| 11 | SUI/USD | 0.675 | 56.311 | 55.492 | +0.28% | +0.00% | 1.08x | 3.0 | 2026-11-24T00:51:51.323088+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |
| 12 | TRX/USD | 0.310687 | 54.316 | 43.623 | +0.31% | +0.11% | 2.02x | 0.0 | 2026-11-24T00:51:51.323088+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XDG/USD | 58.809 | 0.0566122 | +0.17% | 7.29x |
| 2 | XLM/USD | 58.641 | 0.130968 | +0.05% | 2.16x |
| 3 | LINK/USD | 57.333 | 9.05145 | -0.01% | 18.99x |
| 4 | VVV/USD | 56.813 | 24.639 | +0.28% | 1.21x |
| 5 | SUI/USD | 55.492 | 0.675 | +0.00% | 1.08x |
| 6 | ADA/USD | 55.408 | 0.148904 | +0.03% | 1.10x |
| 7 | LTC/USD | 54.790 | 41.55 | -0.12% | 1.64x |
| 8 | PEARL/USD | 53.320 | 2.3276 | +1.31% | 1.30x |
| 9 | PAXG/USD | 53.019 | 3648.81 | +0.16% | 2.12x |
| 10 | UNI/USD | 52.507 | 4.8597 | +0.02% | 6.86x |
| 11 | ALGO/USD | 49.312 | 0.08165 | -0.01% | 7.29x |
| 12 | TRX/USD | 43.623 | 0.310687 | +0.11% | 2.02x |

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

- Persisted scans: 1503; predictions: 12793; observations: 910429.
- Matured sampled outcomes across 1/6/24/48h: 23543; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45300278422 · **Generation:** 1503 · **Legacy run:** 45300278422
**Main quote time:** 2026-11-24T00:52:00.469084+00:00 · **Legacy report time:** 2026-11-24T00:53:12.098810+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XDG/USD ⭐ | 0.0566122 | 74.68 | +0.17% | 7.29x | STRONG 92/100 | HIGH 55/100 | Watch |
| 2 | LINK/USD | 9.05145 | 72.26 | -0.01% | 18.99x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 3 | XLM/USD ⭐ | 0.130968 | 70.51 | +0.05% | 2.16x | STRONG 90/100 | HIGH 55/100 | Watch |
| 4 | UNI/USD | 4.8597 | 67.62 | +0.02% | 6.86x | STRONG 79/100 | HIGH 55/100 | Watch |
| 5 | PAXG/USD ⭐ | 3648.81 | 65.00 | +0.16% | 2.12x | STRONG 88/100 | HIGH 55/100 | Watch |
| 6 | ALGO/USD | 0.08165 | 64.25 | -0.01% | 7.29x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 7 | PEARL/USD ⭐ | 2.3276 | 62.89 | +1.31% | 1.30x | STRONG 81/100 | HIGH 61/100 | Watch |
| 8 | LTC/USD | 41.55 | 60.57 | -0.12% | 1.64x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 9 | VVV/USD | 24.639 | 60.37 | +0.28% | 1.21x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 10 | ADA/USD | 0.148904 | 56.58 | +0.03% | 1.10x | MODERATE 53/100 | HIGH 62/100 | Watch |
| 11 | SUI/USD | 0.675 | 56.31 | +0.00% | 1.08x | MODERATE 53/100 | HIGH 62/100 | Watch |
| 12 | TRX/USD ⭐ | 0.310687 | 54.32 | +0.11% | 2.02x | STRONG 82/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XDG/USD ⭐ | 0.0565625 | 65.97 | +0.17% | 7.29x | 10446 | STRONG 88/100 | HIGH 55/100 | Watch |
| 2 | XLM/USD ⭐ | 0.131012 | 58.27 | +0.05% | 2.16x | 17835 | STRONG 84/100 | HIGH 55/100 | Watch |
| 3 | PAXG/USD ⭐ | 3648.36 | 58.13 | +0.16% | 2.12x | 6074 | STRONG 84/100 | HIGH 55/100 | Watch |
| 4 | PEARL/USD ⭐ | 2.3317 | 56.14 | +1.31% | 1.30x | 16023 | MODERATE 68/100 | VERY_HIGH 77/100 | Watch |
| 5 | SOL/USD | 72.01 | 51.89 | +0.19% | 1.19x | 45827 | MODERATE 51/100 | HIGH 62/100 | Watch |
| 6 | TRX/USD ⭐ | 0.310686 | 51.89 | +0.11% | 2.02x | 4000 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XDG/USD, XLM/USD, PAXG/USD, PEARL/USD, TRX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
