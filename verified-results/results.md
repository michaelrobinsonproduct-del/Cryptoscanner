# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T14:52:39.667334+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45638292034
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 5f085fd54c3c3c80cc91517636247d069bc726d3 (atomic ledger/results publication)
**Ledger generation:** 1732 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MOODENG/USD | 0.02649 | 84.119 | 68.455 | +8.88% | +1.72% | 1.71x | 18.9 | 2026-11-25T14:52:35.637268+00:00 | Not calibrated | STRONG 82/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 24.935 | 67.177 | 60.910 | +1.62% | +1.23% | 1.01x | 10.8 | 2026-11-25T14:52:35.637268+00:00 | Not calibrated | MODERATE 64/100 | HIGH 68/100 | Watch | WATCH |
| 3 | MON/USD | 0.00985 | 62.760 | 62.299 | +4.01% | +0.51% | 0.79x | 20.3 | 2026-11-25T14:52:35.637268+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 4 | XPL/USD | 0.0448 | 49.396 | 36.674 | +1.82% | +0.45% | 2.05x | 22.3 | 2026-11-25T14:52:35.637268+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | DRV/USD | 0.31982 | 46.252 | 48.782 | +1.76% | -0.35% | 0.92x | 2.5 | 2026-11-25T14:52:35.637268+00:00 | Not calibrated | WEAK 28/100 | HIGH 68/100 | Do nothing | WATCH |
| 6 | CT/USD | 0.1294 | 46.032 | 40.575 | +2.45% | -0.31% | 1.70x | 15.4 | 2026-11-25T14:52:35.637268+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 79/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MOODENG/USD | 68.455 | 0.02649 | +1.72% | 1.71x |
| 2 | MON/USD | 62.299 | 0.00985 | +0.51% | 0.79x |
| 3 | VVV/USD | 60.910 | 24.935 | +1.23% | 1.01x |
| 4 | DRV/USD | 48.782 | 0.31982 | -0.35% | 0.92x |
| 5 | CT/USD | 40.575 | 0.1294 | -0.31% | 1.70x |
| 6 | XPL/USD | 36.674 | 0.0448 | +0.45% | 2.05x |

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

- Persisted scans: 1732; predictions: 14587; observations: 1049841.
- Matured sampled outcomes across 1/6/24/48h: 32202; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45638292034 · **Generation:** 1732 · **Legacy run:** 45638292034
**Main quote time:** 2026-11-25T14:52:39.667334+00:00 · **Legacy report time:** 2026-11-25T14:53:44.786106+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MOODENG/USD ⭐ | 0.02649 | 84.12 | +1.72% | 1.71x | STRONG 92/100 | HIGH 66/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 24.935 | 67.18 | +1.23% | 1.01x | STRONG 74/100 | HIGH 68/100 | Watch |
| 3 | MON/USD | 0.00985 | 62.76 | +0.51% | 0.79x | MODERATE 51/100 | VERY_HIGH 74/100 | Watch |
| 4 | XPL/USD ⭐ | 0.0448 | 49.40 | +0.45% | 2.05x | STRONG 80/100 | VERY_HIGH 72/100 | Watch |
| 5 | DRV/USD | 0.31982 | 46.25 | -0.35% | 0.92x | WEAK 28/100 | HIGH 68/100 | Do nothing |
| 6 | CT/USD | 0.1294 | 46.03 | -0.31% | 1.70x | WEAK 38/100 | VERY_HIGH 79/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MOODENG/USD ⭐ | 0.02643 | 72.58 | +1.72% | 1.71x | 1783 | STRONG 81/100 | VERY_HIGH 72/100 | Watch |
| 2 | VVV/USD ⭐ | 24.914 | 59.13 | +1.23% | 1.01x | 12753 | STRONG 75/100 | HIGH 62/100 | Watch |
| 3 | XPL/USD ⭐ | 0.0448 | 44.65 | +0.45% | 2.05x | 1710 | STRONG 77/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** MOODENG/USD, VVV/USD, XPL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
