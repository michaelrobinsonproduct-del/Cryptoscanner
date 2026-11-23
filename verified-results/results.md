# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T04:41:39.287962+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45113172276
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 3fc06d0a74d51458ce596778c353a992bebaebc0 (atomic ledger/results publication)
**Ledger generation:** 1382 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 500.07 | 71.978 | 62.417 | +1.29% | -0.24% | 2.07x | 3.2 | 2026-11-23T04:41:30.568967+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04957 | 68.267 | 52.965 | +0.81% | +0.06% | 2.72x | 6.1 | 2026-11-23T04:41:30.568967+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 3 | PAXG/USD | 3596.1 | 63.345 | 48.477 | +0.67% | -0.03% | 2.60x | 1.3 | 2026-11-23T04:41:30.568967+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 4 | UNI/USD | 4.7814 | 62.228 | 53.950 | +2.14% | -0.50% | 2.08x | 6.1 | 2026-11-23T04:41:30.568967+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XRP/USD | 0.93049 | 60.472 | 56.528 | +0.32% | -0.43% | 1.61x | 1.4 | 2026-11-23T04:41:30.568967+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 6 | ICNT/USD | 0.3683 | 58.757 | 57.152 | +4.57% | +1.41% | 0.46x | 16.4 | 2026-11-23T04:41:30.568967+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | CC/USD | 0.07597 | 56.804 | 57.524 | +3.69% | -0.14% | 1.00x | 6.6 | 2026-11-23T04:41:30.568967+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | VVV/USD | 26.736 | 56.636 | 54.486 | +0.75% | -0.54% | 1.49x | 8.2 | 2026-11-23T04:41:30.568967+00:00 | Not calibrated | MODERATE 48/100 | HIGH 61/100 | Watch | WATCH |
| 9 | SOL/USD | 71.15 | 52.397 | 59.451 | +0.74% | -0.32% | 0.46x | 1.4 | 2026-11-23T04:41:30.568967+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | NEAR/USD | 2.9959 | 52.003 | 55.163 | +0.48% | -0.50% | 0.93x | 6.3 | 2026-11-23T04:41:30.568967+00:00 | Not calibrated | WEAK 31/100 | HIGH 68/100 | Do nothing | WATCH |
| 11 | LTC/USD | 40.33 | 49.336 | 44.895 | +0.42% | -0.22% | 1.56x | 2.5 | 2026-11-23T04:41:30.568967+00:00 | Not calibrated | MODERATE 45/100 | HIGH 61/100 | Watch | WATCH |
| 12 | SUI/USD | 0.6578 | 49.192 | 55.722 | +0.32% | +0.00% | 0.35x | 3.0 | 2026-11-23T04:41:30.568967+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 62.417 | 500.07 | -0.24% | 2.07x |
| 2 | SOL/USD | 59.451 | 71.15 | -0.32% | 0.46x |
| 3 | CC/USD | 57.524 | 0.07597 | -0.14% | 1.00x |
| 4 | ICNT/USD | 57.152 | 0.3683 | +1.41% | 0.46x |
| 5 | XRP/USD | 56.528 | 0.93049 | -0.43% | 1.61x |
| 6 | SUI/USD | 55.722 | 0.6578 | +0.00% | 0.35x |
| 7 | NEAR/USD | 55.163 | 2.9959 | -0.50% | 0.93x |
| 8 | VVV/USD | 54.486 | 26.736 | -0.54% | 1.49x |
| 9 | UNI/USD | 53.950 | 4.7814 | -0.50% | 2.08x |
| 10 | NIGHT/USD | 52.965 | 0.04957 | +0.06% | 2.72x |
| 11 | PAXG/USD | 48.477 | 3596.1 | -0.03% | 2.60x |
| 12 | LTC/USD | 44.895 | 40.33 | -0.22% | 1.56x |

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

- Persisted scans: 1382; predictions: 11351; observations: 836743.
- Matured sampled outcomes across 1/6/24/48h: 18331; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 99 (sampled only; not a success-rate estimate).
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

**Writer:** 45113172276 · **Generation:** 1382 · **Legacy run:** 45113172276
**Main quote time:** 2026-11-23T04:41:39.287962+00:00 · **Legacy report time:** 2026-11-23T04:42:42.773049+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 500.07 | 71.98 | -0.24% | 2.07x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 2 | NIGHT/USD | 0.04957 | 68.27 | +0.06% | 2.72x | STRONG 79/100 | HIGH 55/100 | Watch |
| 3 | PAXG/USD | 3596.1 | 63.35 | -0.03% | 2.60x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 4 | UNI/USD | 4.7814 | 62.23 | -0.50% | 2.08x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 5 | XRP/USD | 0.93049 | 60.47 | -0.43% | 1.61x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 6 | ICNT/USD | 0.3683 | 58.76 | +1.41% | 0.46x | MODERATE 54/100 | VERY_HIGH 81/100 | Watch |
| 7 | CC/USD | 0.07597 | 56.80 | -0.14% | 1.00x | WEAK 38/100 | VERY_HIGH 73/100 | Watch |
| 8 | VVV/USD | 26.736 | 56.64 | -0.54% | 1.49x | MODERATE 48/100 | HIGH 61/100 | Watch |
| 9 | SOL/USD | 71.15 | 52.40 | -0.32% | 0.46x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | NEAR/USD | 2.9959 | 52.00 | -0.50% | 0.93x | WEAK 31/100 | HIGH 68/100 | Do nothing |
| 11 | LTC/USD | 40.33 | 49.34 | -0.22% | 1.56x | MODERATE 45/100 | HIGH 61/100 | Watch |
| 12 | SUI/USD | 0.6578 | 49.19 | +0.00% | 0.35x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
