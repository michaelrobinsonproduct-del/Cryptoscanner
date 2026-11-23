# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T16:01:40.468389+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45211393964
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 36597d62a52e03b80fb71d74b25033455750c865 (atomic ledger/results publication)
**Ledger generation:** 1451 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ADA/USD | 0.153794 | 111.972 | 96.565 | +6.36% | +0.08% | 2.89x | 5.9 | 2026-11-23T16:01:31.787456+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | SOL/USD | 75.52 | 101.839 | 99.338 | +6.92% | -0.11% | 1.30x | 1.3 | 2026-11-23T16:01:31.787456+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ZEC/USD | 853.57 | 96.012 | 98.008 | +7.03% | -1.15% | 1.38x | 4.0 | 2026-11-23T16:01:31.787456+00:00 | Not calibrated | MODERATE 68/100 | HIGH 65/100 | Watch | WATCH |
| 4 | XDG/USD | 0.0588179 | 92.988 | 96.934 | +6.39% | +0.12% | 0.55x | 5.6 | 2026-11-23T16:01:31.787456+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | XRP/USD | 0.98913 | 92.342 | 99.596 | +6.64% | -0.50% | 0.52x | 0.8 | 2026-11-23T16:01:31.787456+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | SUI/USD | 0.7134 | 90.787 | 97.895 | +8.80% | -0.15% | 0.37x | 4.2 | 2026-11-23T16:01:31.787456+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | INJ/USD | 6.734 | 88.208 | 94.297 | +8.12% | -0.89% | 0.84x | 5.9 | 2026-11-23T16:01:31.787456+00:00 | Not calibrated | MODERATE 49/100 | HIGH 68/100 | Watch | WATCH |
| 8 | LINK/USD | 9.25791 | 87.242 | 85.543 | +5.07% | -0.09% | 1.22x | 5.1 | 2026-11-23T16:01:31.787456+00:00 | Not calibrated | MODERATE 54/100 | HIGH 68/100 | Watch | WATCH |
| 9 | XLM/USD | 0.13428 | 82.104 | 89.302 | +5.29% | -0.16% | 0.36x | 5.5 | 2026-11-23T16:01:31.787456+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | UNI/USD | 5.0728 | 81.884 | 90.964 | +8.37% | -0.49% | 0.34x | 8.7 | 2026-11-23T16:01:31.787456+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | LTC/USD | 42.44 | 81.320 | 91.206 | +5.68% | -0.26% | 0.14x | 7.1 | 2026-11-23T16:01:31.787456+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | HYPE/USD | 66.41 | 81.285 | 89.928 | +5.31% | -1.43% | 0.85x | 4.5 | 2026-11-23T16:01:31.787456+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 72/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 99.596 | 0.98913 | -0.50% | 0.52x |
| 2 | SOL/USD | 99.338 | 75.52 | -0.11% | 1.30x |
| 3 | ZEC/USD | 98.008 | 853.57 | -1.15% | 1.38x |
| 4 | SUI/USD | 97.895 | 0.7134 | -0.15% | 0.37x |
| 5 | XDG/USD | 96.934 | 0.0588179 | +0.12% | 0.55x |
| 6 | ADA/USD | 96.565 | 0.153794 | +0.08% | 2.89x |
| 7 | INJ/USD | 94.297 | 6.734 | -0.89% | 0.84x |
| 8 | LTC/USD | 91.206 | 42.44 | -0.26% | 0.14x |
| 9 | UNI/USD | 90.964 | 5.0728 | -0.49% | 0.34x |
| 10 | HYPE/USD | 89.928 | 66.41 | -1.43% | 0.85x |
| 11 | XLM/USD | 89.302 | 0.13428 | -0.16% | 0.36x |
| 12 | LINK/USD | 85.543 | 9.25791 | -0.09% | 1.22x |

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

- Persisted scans: 1451; predictions: 12179; observations: 878761.
- Matured sampled outcomes across 1/6/24/48h: 20956; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45211393964 · **Generation:** 1451 · **Legacy run:** 45211393964
**Main quote time:** 2026-11-23T16:01:40.468389+00:00 · **Legacy report time:** 2026-11-23T16:02:28.608790+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.153794 | 111.97 | +0.08% | 2.89x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | SOL/USD | 75.52 | 101.84 | -0.11% | 1.30x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | ZEC/USD | 853.57 | 96.01 | -1.15% | 1.38x | MODERATE 68/100 | HIGH 65/100 | Watch |
| 4 | XDG/USD | 0.0588179 | 92.99 | +0.12% | 0.55x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 5 | XRP/USD | 0.98913 | 92.34 | -0.50% | 0.52x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 6 | SUI/USD | 0.7134 | 90.79 | -0.15% | 0.37x | MODERATE 50/100 | VERY_HIGH 76/100 | Watch |
| 7 | INJ/USD | 6.734 | 88.21 | -0.89% | 0.84x | MODERATE 49/100 | HIGH 68/100 | Watch |
| 8 | LINK/USD | 9.25791 | 87.24 | -0.09% | 1.22x | MODERATE 54/100 | HIGH 68/100 | Watch |
| 9 | XLM/USD | 0.13428 | 82.10 | -0.16% | 0.36x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 10 | UNI/USD | 5.0728 | 81.88 | -0.49% | 0.34x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 11 | LTC/USD | 42.44 | 81.32 | -0.26% | 0.14x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 12 | HYPE/USD | 66.41 | 81.29 | -1.43% | 0.85x | MODERATE 46/100 | VERY_HIGH 72/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.153538 | 99.46 | +0.08% | 2.89x | 11817 | STRONG 100/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
