# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T04:27:18.265562+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45546572272
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2d4f5bde5bc13a0a7a356cdc07b74fa6bf00801c (atomic ledger/results publication)
**Ledger generation:** 1669 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.00992 | 92.533 | 76.605 | +4.75% | +2.05% | 1.57x | 10.1 | 2026-11-25T04:27:11.959900+00:00 | Not calibrated | STRONG 86/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | DRV/USD | 0.33342 | 72.212 | 67.265 | +6.09% | +2.15% | 0.42x | 22.2 | 2026-11-25T04:27:11.959900+00:00 | Not calibrated | MODERATE 56/100 | EXTREME 87/100 | Do nothing | WATCH |
| 3 | XMR/USD | 512.87 | 55.935 | 56.657 | +0.64% | +0.35% | 0.75x | 2.1 | 2026-11-25T04:27:11.959900+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 4 | RE/USD | 0.20244 | 53.014 | 30.109 | +0.91% | +1.84% | 2.37x | 13.9 | 2026-11-25T04:27:11.959900+00:00 | Not calibrated | STRONG 77/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | SKY/USD | 0.04153 | 36.773 | 39.680 | +1.34% | +0.51% | 0.45x | 7.2 | 2026-11-25T04:27:11.959900+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 6 | DOT/USD | 0.6534 | 28.773 | 33.421 | +0.29% | +0.46% | 0.30x | 1.5 | 2026-11-25T04:27:11.959900+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 7 | SYRUP/USD | 0.07126 | 27.562 | 30.995 | +2.28% | +0.15% | 0.58x | 33.5 | 2026-11-25T04:27:11.959900+00:00 | Not calibrated | WEAK 24/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 76.605 | 0.00992 | +2.05% | 1.57x |
| 2 | DRV/USD | 67.265 | 0.33342 | +2.15% | 0.42x |
| 3 | XMR/USD | 56.657 | 512.87 | +0.35% | 0.75x |
| 4 | SKY/USD | 39.680 | 0.04153 | +0.51% | 0.45x |
| 5 | DOT/USD | 33.421 | 0.6534 | +0.46% | 0.30x |
| 6 | SYRUP/USD | 30.995 | 0.07126 | +0.15% | 0.58x |
| 7 | RE/USD | 30.109 | 0.20244 | +1.84% | 2.37x |

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

- Persisted scans: 1669; predictions: 14190; observations: 1011512.
- Matured sampled outcomes across 1/6/24/48h: 29977; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 17; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45546572272 · **Generation:** 1669 · **Legacy run:** 45546572272
**Main quote time:** 2026-11-25T04:27:18.265562+00:00 · **Legacy report time:** 2026-11-25T04:28:12.291663+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.00992 | 92.53 | +2.05% | 1.57x | STRONG 96/100 | HIGH 61/100 | Consider small entry |
| 2 | DRV/USD | 0.33342 | 72.21 | +2.15% | 0.42x | MODERATE 56/100 | EXTREME 87/100 | Do nothing |
| 3 | XMR/USD | 512.87 | 55.93 | +0.35% | 0.75x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 4 | RE/USD | 0.20244 | 53.01 | +1.84% | 2.37x | STRONG 77/100 | VERY_HIGH 73/100 | Watch |
| 5 | SKY/USD | 0.04153 | 36.77 | +0.51% | 0.45x | MODERATE 48/100 | VERY_HIGH 75/100 | Watch |
| 6 | DOT/USD | 0.6534 | 28.77 | +0.46% | 0.30x | WEAK 44/100 | VERY_HIGH 75/100 | Watch |
| 7 | SYRUP/USD | 0.07126 | 27.56 | +0.15% | 0.58x | WEAK 24/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.00991 | 89.45 | +2.05% | 1.57x | 18633 | STRONG 90/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** MON/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
