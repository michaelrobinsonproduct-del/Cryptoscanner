# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T13:24:10.634162+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45622415534
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 3601a06c42a2975ffdf6d0f9e7af49c724d30e82 (atomic ledger/results publication)
**Ledger generation:** 1723 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.433 | 82.684 | 76.794 | +3.65% | +0.10% | 1.54x | 7.5 | 2026-11-25T13:24:06.619823+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 2 | MON/USD | 0.00982 | 69.809 | 63.685 | +3.70% | +0.10% | 1.56x | 20.3 | 2026-11-25T13:24:06.619823+00:00 | Not calibrated | MODERATE 60/100 | HIGH 67/100 | Watch | WATCH |
| 3 | DRV/USD | 0.33238 | 64.174 | 69.534 | +5.76% | -0.55% | 0.74x | 17.5 | 2026-11-25T13:24:06.619823+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 4 | MOODENG/USD | 0.02719 | 61.922 | 64.644 | +11.76% | +0.41% | 0.52x | 25.8 | 2026-11-25T13:24:06.619823+00:00 | Not calibrated | MODERATE 51/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | INX/USD | 0.004001 | 40.444 | 49.222 | +4.44% | -0.10% | 0.17x | 25.1 | 2026-11-25T13:24:06.619823+00:00 | Not calibrated | WEAK 15/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 76.794 | 25.433 | +0.10% | 1.54x |
| 2 | DRV/USD | 69.534 | 0.33238 | -0.55% | 0.74x |
| 3 | MOODENG/USD | 64.644 | 0.02719 | +0.41% | 0.52x |
| 4 | MON/USD | 63.685 | 0.00982 | +0.10% | 1.56x |
| 5 | INX/USD | 49.222 | 0.004001 | -0.10% | 0.17x |

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

- Persisted scans: 1723; predictions: 14538; observations: 1044369.
- Matured sampled outcomes across 1/6/24/48h: 31894; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45622415534 · **Generation:** 1723 · **Legacy run:** 45622415534
**Main quote time:** 2026-11-25T13:24:10.634162+00:00 · **Legacy report time:** 2026-11-25T13:25:06.104873+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.433 | 82.68 | +0.10% | 1.54x | STRONG 86/100 | HIGH 55/100 | Watch |
| 2 | MON/USD ⭐ | 0.00982 | 69.81 | +0.10% | 1.56x | STRONG 70/100 | HIGH 67/100 | Watch |
| 3 | DRV/USD | 0.33238 | 64.17 | -0.55% | 0.74x | WEAK 32/100 | VERY_HIGH 82/100 | Do nothing |
| 4 | MOODENG/USD | 0.02719 | 61.92 | +0.41% | 0.52x | MODERATE 51/100 | EXTREME 87/100 | Do nothing |
| 5 | INX/USD | 0.004001 | 40.44 | -0.10% | 0.17x | WEAK 15/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.439 | 88.50 | +0.92% | 1.96x | 12194 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 2 | MON/USD ⭐ | 0.00989 | 86.70 | +0.82% | 1.84x | 19255 | STRONG 88/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** VVV/USD, MON/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
