# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T04:45:04.102170+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44239415081
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 44200f79fd7990548cb0efc7c767cd5df322abf5 (atomic ledger/results publication)
**Ledger generation:** 534 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.2892 | 60.934 | 48.202 | +4.74% | -0.45% | 5.91x | 34.7 | 2026-11-18T04:44:57.780341+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 2 | XDC/USD | 0.0309 | 51.923 | 47.910 | +1.91% | +0.91% | 0.95x | 6.5 | 2026-11-18T04:44:57.780341+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 3 | AKT/USD | 0.5131 | 43.347 | 31.734 | +0.75% | -0.68% | 3.04x | 11.7 | 2026-11-18T04:44:57.780341+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | UAI/USD | 0.03361 | 41.276 | 28.381 | +0.69% | +0.42% | 2.08x | 14.9 | 2026-11-18T04:44:57.780341+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | CC/USD | 0.08337 | 38.814 | 41.938 | +1.51% | -0.08% | 0.73x | 8.4 | 2026-11-18T04:44:57.780341+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 6 | SENT/USD | 0.01918 | 38.024 | 45.905 | +2.74% | -0.15% | 0.29x | 8.3 | 2026-11-18T04:44:57.780341+00:00 | Not calibrated | WEAK 24/100 | EXTREME 88/100 | Do nothing | WATCH |
| 7 | PEARL/USD | 1.8377 | 28.916 | 34.860 | +1.50% | +0.21% | 0.30x | 21.3 | 2026-11-18T04:44:57.780341+00:00 | Not calibrated | WEAK 34/100 | EXTREME 87/100 | Do nothing | WATCH |
| 8 | MELANIA/USD | 0.0498 | 11.198 | 26.395 | +2.26% | -1.97% | 0.46x | 40.3 | 2026-11-18T04:44:57.780341+00:00 | Not calibrated | WEAK 0/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ICNT/USD | 48.202 | 0.2892 | -0.45% | 5.91x |
| 2 | XDC/USD | 47.910 | 0.0309 | +0.91% | 0.95x |
| 3 | SENT/USD | 45.905 | 0.01918 | -0.15% | 0.29x |
| 4 | CC/USD | 41.938 | 0.08337 | -0.08% | 0.73x |
| 5 | PEARL/USD | 34.860 | 1.8377 | +0.21% | 0.30x |
| 6 | AKT/USD | 31.734 | 0.5131 | -0.68% | 3.04x |
| 7 | UAI/USD | 28.381 | 0.03361 | +0.42% | 2.08x |
| 8 | MELANIA/USD | 26.395 | 0.0498 | -1.97% | 0.46x |

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

- Persisted scans: 534; predictions: 4512; observations: 322213.
- Matured sampled outcomes across 1/6/24/48h: 3586; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44239415081 · **Generation:** 534 · **Legacy run:** 44239415081
**Main quote time:** 2026-11-18T04:45:04.102170+00:00 · **Legacy report time:** 2026-11-18T04:45:19.685532+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD | 0.2892 | 60.93 | -0.45% | 5.91x | MODERATE 50/100 | VERY_HIGH 78/100 | Watch |
| 2 | XDC/USD | 0.0309 | 51.92 | +0.91% | 0.95x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 3 | AKT/USD | 0.5131 | 43.35 | -0.68% | 3.04x | MODERATE 47/100 | VERY_HIGH 72/100 | Watch |
| 4 | UAI/USD ⭐ | 0.03361 | 41.28 | +0.42% | 2.08x | STRONG 81/100 | VERY_HIGH 73/100 | Watch |
| 5 | CC/USD | 0.08337 | 38.81 | -0.08% | 0.73x | WEAK 24/100 | VERY_HIGH 81/100 | Do nothing |
| 6 | SENT/USD | 0.01918 | 38.02 | -0.15% | 0.29x | WEAK 24/100 | EXTREME 88/100 | Do nothing |
| 7 | PEARL/USD | 1.8377 | 28.92 | +0.21% | 0.30x | WEAK 34/100 | EXTREME 87/100 | Do nothing |
| 8 | MELANIA/USD | 0.0498 | 11.20 | -1.97% | 0.46x | WEAK 0/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | UAI/USD ⭐ | 0.03359 | 31.09 | +0.42% | 2.08x | 2084 | STRONG 76/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** UAI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
