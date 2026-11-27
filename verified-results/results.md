# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T18:42:32.628551+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46051108801
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f12d55429d7d5a3b4689d5e5b796326f49a147ab (atomic ledger/results publication)
**Ledger generation:** 2045 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 742.12 | 92.926 | 99.933 | +8.87% | -0.05% | 0.32x | 0.1 | 2026-11-27T18:42:24.109958+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | SPACE/USD | 0.00428 | 80.649 | 71.176 | +10.54% | +0.42% | 1.74x | 9.3 | 2026-11-27T18:42:24.109958+00:00 | Not calibrated | STRONG 85/100 | HIGH 67/100 | Consider small entry | WATCH |
| 3 | NIGHT/USD | 0.04998 | 75.987 | 75.807 | +3.12% | -0.18% | 1.11x | 2.0 | 2026-11-27T18:42:24.109958+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 4 | PAXG/USD | 3627.79 | 70.632 | 56.469 | +2.00% | -0.11% | 2.47x | 0.5 | 2026-11-27T18:42:24.109958+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SOL/USD | 71.7 | 65.462 | 61.802 | +1.07% | +0.13% | 1.30x | 1.4 | 2026-11-27T18:42:24.109958+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 6 | UNI/USD | 4.7904 | 64.045 | 71.772 | +3.02% | -0.00% | 0.23x | 3.3 | 2026-11-27T18:42:24.109958+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0575065 | 59.445 | 68.908 | +2.01% | -0.15% | 0.13x | 0.3 | 2026-11-27T18:42:24.109958+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | HYPE/USD | 63.26 | 56.935 | 65.910 | +1.67% | -0.05% | 0.13x | 1.6 | 2026-11-27T18:42:24.109958+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | LINK/USD | 9.35673 | 54.268 | 60.428 | +0.95% | +0.12% | 0.32x | 2.5 | 2026-11-27T18:42:24.109958+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | RENDER/USD | 1.391 | 52.632 | 56.079 | +4.35% | +0.29% | 0.51x | 14.4 | 2026-11-27T18:42:24.109958+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 11 | FET/USD | 0.1256 | 51.927 | 59.529 | +4.32% | +0.16% | 0.16x | 15.9 | 2026-11-27T18:42:24.109958+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | XAUT/USD | 3632.1 | 50.860 | 51.757 | +2.03% | -0.10% | 0.96x | 0.3 | 2026-11-27T18:42:24.109958+00:00 | Not calibrated | WEAK 30/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 99.933 | 742.12 | -0.05% | 0.32x |
| 2 | NIGHT/USD | 75.807 | 0.04998 | -0.18% | 1.11x |
| 3 | UNI/USD | 71.772 | 4.7904 | -0.00% | 0.23x |
| 4 | SPACE/USD | 71.176 | 0.00428 | +0.42% | 1.74x |
| 5 | XDG/USD | 68.908 | 0.0575065 | -0.15% | 0.13x |
| 6 | HYPE/USD | 65.910 | 63.26 | -0.05% | 0.13x |
| 7 | SOL/USD | 61.802 | 71.7 | +0.13% | 1.30x |
| 8 | LINK/USD | 60.428 | 9.35673 | +0.12% | 0.32x |
| 9 | FET/USD | 59.529 | 0.1256 | +0.16% | 0.16x |
| 10 | PAXG/USD | 56.469 | 3627.79 | -0.11% | 2.47x |
| 11 | RENDER/USD | 56.079 | 1.391 | +0.29% | 0.51x |
| 12 | XAUT/USD | 51.757 | 3632.1 | -0.10% | 0.96x |

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

- Persisted scans: 2045; predictions: 18242; observations: 1238334.
- Matured sampled outcomes across 1/6/24/48h: 41039; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
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

**Writer:** 46051108801 · **Generation:** 2045 · **Legacy run:** 46051108801
**Main quote time:** 2026-11-27T18:42:32.628551+00:00 · **Legacy report time:** 2026-11-27T18:43:14.052848+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 742.12 | 92.93 | -0.05% | 0.32x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 2 | SPACE/USD ⭐ | 0.00428 | 80.65 | +0.42% | 1.74x | STRONG 95/100 | HIGH 67/100 | Consider small entry |
| 3 | NIGHT/USD | 0.04998 | 75.99 | -0.18% | 1.11x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 4 | PAXG/USD | 3627.79 | 70.63 | -0.11% | 2.47x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 5 | SOL/USD ⭐ | 71.7 | 65.46 | +0.13% | 1.30x | STRONG 78/100 | HIGH 55/100 | Watch |
| 6 | UNI/USD | 4.7904 | 64.05 | -0.00% | 0.23x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 7 | XDG/USD | 0.0575065 | 59.45 | -0.15% | 0.13x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 8 | HYPE/USD | 63.26 | 56.93 | -0.05% | 0.13x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | LINK/USD | 9.35673 | 54.27 | +0.12% | 0.32x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 10 | RENDER/USD | 1.391 | 52.63 | +0.29% | 0.51x | MODERATE 51/100 | VERY_HIGH 81/100 | Watch |
| 11 | FET/USD | 0.1256 | 51.93 | +0.16% | 0.16x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 12 | XAUT/USD | 3632.1 | 50.86 | -0.10% | 0.96x | WEAK 30/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SPACE/USD ⭐ | 0.004282 | 74.09 | +0.42% | 1.74x | 2565 | STRONG 92/100 | HIGH 67/100 | Consider small entry |
| 2 | SOL/USD ⭐ | 71.75 | 64.50 | +0.13% | 1.30x | 45295 | STRONG 77/100 | HIGH 55/100 | Watch |

**Same-run overlap:** SPACE/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
