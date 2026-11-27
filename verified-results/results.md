# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T08:12:05.435756+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45963521811
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2ea3d73c884fb60e0223ee9fe230a7b87a11fc2f (atomic ledger/results publication)
**Ledger generation:** 1981 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 746.16 | 95.885 | 97.853 | +9.46% | +0.94% | 0.33x | 4.3 | 2026-11-27T08:11:56.679067+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | LINK/USD | 9.60748 | 95.002 | 80.362 | +3.66% | -0.07% | 8.27x | 0.5 | 2026-11-27T08:11:56.679067+00:00 | Not calibrated | STRONG 78/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XRP/USD | 0.97723 | 94.519 | 80.499 | +3.66% | -0.20% | 4.10x | 0.2 | 2026-11-27T08:11:56.679067+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 4 | UNI/USD | 4.8956 | 93.553 | 79.562 | +5.28% | -0.20% | 3.30x | 3.5 | 2026-11-27T08:11:56.679067+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 5 | HYPE/USD | 65.66 | 90.911 | 92.940 | +5.53% | +0.66% | 0.47x | 1.5 | 2026-11-27T08:11:56.679067+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | SOL/USD | 73.19 | 90.522 | 76.519 | +3.17% | +0.04% | 2.38x | 1.4 | 2026-11-27T08:11:56.679067+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 7 | W/USD | 0.00962 | 82.574 | 73.522 | +9.19% | +0.31% | 1.75x | 10.4 | 2026-11-27T08:11:56.679067+00:00 | Not calibrated | STRONG 81/100 | HIGH 66/100 | Consider small entry | WATCH |
| 8 | ADA/USD | 0.152869 | 73.203 | 70.852 | +2.97% | -0.11% | 1.29x | 2.7 | 2026-11-27T08:11:56.679067+00:00 | Not calibrated | MODERATE 47/100 | HIGH 61/100 | Watch | WATCH |
| 9 | VVV/USD | 27.108 | 72.875 | 76.962 | +3.53% | +0.39% | 0.40x | 5.5 | 2026-11-27T08:11:56.679067+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XBT/USD | 61783.3 | 71.537 | 69.864 | +2.12% | +0.21% | 1.06x | 0.0 | 2026-11-27T08:11:56.679067+00:00 | Not calibrated | STRONG 71/100 | HIGH 62/100 | Watch | WATCH |
| 11 | PAXG/USD | 3647.28 | 71.436 | 56.668 | +2.55% | -0.05% | 3.85x | 1.4 | 2026-11-27T08:11:56.679067+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 12 | ETH/USD | 1733.91 | 70.656 | 74.146 | +2.74% | +0.07% | 0.61x | 0.1 | 2026-11-27T08:11:56.679067+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.853 | 746.16 | +0.94% | 0.33x |
| 2 | HYPE/USD | 92.940 | 65.66 | +0.66% | 0.47x |
| 3 | XRP/USD | 80.499 | 0.97723 | -0.20% | 4.10x |
| 4 | LINK/USD | 80.362 | 9.60748 | -0.07% | 8.27x |
| 5 | UNI/USD | 79.562 | 4.8956 | -0.20% | 3.30x |
| 6 | VVV/USD | 76.962 | 27.108 | +0.39% | 0.40x |
| 7 | SOL/USD | 76.519 | 73.19 | +0.04% | 2.38x |
| 8 | ETH/USD | 74.146 | 1733.91 | +0.07% | 0.61x |
| 9 | W/USD | 73.522 | 0.00962 | +0.31% | 1.75x |
| 10 | ADA/USD | 70.852 | 0.152869 | -0.11% | 1.29x |
| 11 | XBT/USD | 69.864 | 61783.3 | +0.21% | 1.06x |
| 12 | PAXG/USD | 56.668 | 3647.28 | -0.05% | 3.85x |

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

- Persisted scans: 1981; predictions: 17474; observations: 1199696.
- Matured sampled outcomes across 1/6/24/48h: 38657; gap abstentions: 25666. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45963521811 · **Generation:** 1981 · **Legacy run:** 45963521811
**Main quote time:** 2026-11-27T08:12:05.435756+00:00 · **Legacy report time:** 2026-11-27T08:12:53.082822+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 746.16 | 95.88 | +0.94% | 0.33x | STRONG 78/100 | VERY_HIGH 70/100 | Watch |
| 2 | LINK/USD | 9.60748 | 95.00 | -0.07% | 8.27x | STRONG 78/100 | HIGH 61/100 | Watch |
| 3 | XRP/USD | 0.97723 | 94.52 | -0.20% | 4.10x | STRONG 77/100 | HIGH 61/100 | Watch |
| 4 | UNI/USD | 4.8956 | 93.55 | -0.20% | 3.30x | STRONG 77/100 | HIGH 61/100 | Watch |
| 5 | HYPE/USD | 65.66 | 90.91 | +0.66% | 0.47x | STRONG 75/100 | VERY_HIGH 70/100 | Watch |
| 6 | SOL/USD | 73.19 | 90.52 | +0.04% | 2.38x | STRONG 90/100 | HIGH 55/100 | Watch |
| 7 | W/USD | 0.00962 | 82.57 | +0.31% | 1.75x | STRONG 81/100 | HIGH 66/100 | Consider small entry |
| 8 | ADA/USD | 0.152869 | 73.20 | -0.11% | 1.29x | MODERATE 47/100 | HIGH 61/100 | Watch |
| 9 | VVV/USD | 27.108 | 72.87 | +0.39% | 0.40x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 10 | XBT/USD ⭐ | 61783.3 | 71.54 | +0.21% | 1.06x | STRONG 81/100 | HIGH 62/100 | Watch |
| 11 | PAXG/USD | 3647.28 | 71.44 | -0.05% | 3.85x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 12 | ETH/USD | 1733.91 | 70.66 | +0.07% | 0.61x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 3.608e-06 | 89.91 | +0.42% | 2.13x | 5215 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XBT/USD ⭐ | 61742.8 | 77.54 | +0.21% | 1.06x | 137695 | STRONG 84/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
