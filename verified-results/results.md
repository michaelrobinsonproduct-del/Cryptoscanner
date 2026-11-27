# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T05:31:38.931082+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45946114309
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 32725f7c8d31e2782d2ca6edc6283c4b0d215ee3 (atomic ledger/results publication)
**Ledger generation:** 1965 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 602; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 760.8 | 112.856 | 96.979 | +11.61% | +0.18% | 3.71x | 6.0 | 2026-11-27T05:31:32.221492+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | SOL/USD | 73.31 | 93.732 | 77.704 | +3.34% | +0.21% | 4.16x | 1.4 | 2026-11-27T05:31:32.221492+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | VVV/USD | 27.12 | 91.954 | 78.023 | +3.58% | -0.21% | 3.01x | 4.1 | 2026-11-27T05:31:32.221492+00:00 | Not calibrated | STRONG 76/100 | HIGH 61/100 | Watch | WATCH |
| 4 | HYPE/USD | 66.01 | 90.731 | 96.881 | +6.09% | -0.02% | 0.39x | 1.5 | 2026-11-27T05:31:32.221492+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6873 | 88.833 | 74.052 | +2.94% | -0.04% | 3.97x | 2.9 | 2026-11-27T05:31:32.221492+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 6 | LTC/USD | 44.73 | 85.142 | 69.726 | +2.26% | +0.18% | 2.45x | 2.2 | 2026-11-27T05:31:32.221492+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 7 | XBT/USD | 61787.9 | 79.465 | 69.917 | +2.13% | +0.19% | 1.86x | 0.0 | 2026-11-27T05:31:32.221492+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 8 | XDG/USD | 0.057999 | 79.410 | 63.811 | +2.88% | +0.12% | 5.04x | 1.3 | 2026-11-27T05:31:32.221492+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 9 | ETH/USD | 1747.55 | 77.204 | 78.974 | +3.55% | +0.30% | 0.67x | 1.7 | 2026-11-27T05:31:32.221492+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | LINK/USD | 9.67822 | 76.063 | 82.352 | +4.42% | +0.41% | 0.17x | 7.2 | 2026-11-27T05:31:32.221492+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ADA/USD | 0.152659 | 74.447 | 71.676 | +2.83% | +0.20% | 1.18x | 3.5 | 2026-11-27T05:31:32.221492+00:00 | Not calibrated | STRONG 72/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XRP/USD | 0.96576 | 71.415 | 71.671 | +2.44% | +0.19% | 0.88x | 0.8 | 2026-11-27T05:31:32.221492+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 96.979 | 760.8 | +0.18% | 3.71x |
| 2 | HYPE/USD | 96.881 | 66.01 | -0.02% | 0.39x |
| 3 | LINK/USD | 82.352 | 9.67822 | +0.41% | 0.17x |
| 4 | ETH/USD | 78.974 | 1747.55 | +0.30% | 0.67x |
| 5 | VVV/USD | 78.023 | 27.12 | -0.21% | 3.01x |
| 6 | SOL/USD | 77.704 | 73.31 | +0.21% | 4.16x |
| 7 | SUI/USD | 74.052 | 0.6873 | -0.04% | 3.97x |
| 8 | ADA/USD | 71.676 | 0.152659 | +0.20% | 1.18x |
| 9 | XRP/USD | 71.671 | 0.96576 | +0.19% | 0.88x |
| 10 | XBT/USD | 69.917 | 61787.9 | +0.19% | 1.86x |
| 11 | LTC/USD | 69.726 | 44.73 | +0.18% | 2.45x |
| 12 | XDG/USD | 63.811 | 0.057999 | +0.12% | 5.04x |

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

- Persisted scans: 1965; predictions: 17282; observations: 1190052.
- Matured sampled outcomes across 1/6/24/48h: 38114; gap abstentions: 25545. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45946114309 · **Generation:** 1965 · **Legacy run:** 45946114309
**Main quote time:** 2026-11-27T05:31:38.931082+00:00 · **Legacy report time:** 2026-11-27T05:32:31.772978+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 760.8 | 112.86 | +0.18% | 3.71x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | SOL/USD ⭐ | 73.31 | 93.73 | +0.21% | 4.16x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | VVV/USD | 27.12 | 91.95 | -0.21% | 3.01x | STRONG 76/100 | HIGH 61/100 | Watch |
| 4 | HYPE/USD | 66.01 | 90.73 | -0.02% | 0.39x | MODERATE 50/100 | VERY_HIGH 76/100 | Watch |
| 5 | SUI/USD | 0.6873 | 88.83 | -0.04% | 3.97x | STRONG 74/100 | HIGH 61/100 | Watch |
| 6 | LTC/USD ⭐ | 44.73 | 85.14 | +0.18% | 2.45x | STRONG 98/100 | HIGH 55/100 | Watch |
| 7 | XBT/USD ⭐ | 61787.9 | 79.46 | +0.19% | 1.86x | STRONG 85/100 | HIGH 55/100 | Watch |
| 8 | XDG/USD ⭐ | 0.057999 | 79.41 | +0.12% | 5.04x | STRONG 95/100 | HIGH 55/100 | Watch |
| 9 | ETH/USD | 1747.55 | 77.20 | +0.30% | 0.67x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 10 | LINK/USD | 9.67822 | 76.06 | +0.41% | 0.17x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 11 | ADA/USD ⭐ | 0.152659 | 74.45 | +0.20% | 1.18x | STRONG 82/100 | HIGH 62/100 | Watch |
| 12 | XRP/USD | 0.96576 | 71.41 | +0.19% | 0.88x | MODERATE 56/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 760.81 | 96.98 | +0.18% | 3.71x | 39426 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | SOL/USD ⭐ | 73.32 | 95.42 | +0.21% | 4.16x | 34314 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XDG/USD ⭐ | 0.0580345 | 88.84 | +0.12% | 5.04x | 5653 | STRONG 99/100 | HIGH 55/100 | Watch |
| 4 | TIA/USD | 0.3489 | 84.88 | +0.14% | 6.72x | 2573 | STRONG 87/100 | HIGH 67/100 | Watch |
| 5 | XBT/USD ⭐ | 61803.9 | 81.88 | +0.19% | 1.86x | 136222 | STRONG 86/100 | HIGH 55/100 | Watch |
| 6 | LTC/USD ⭐ | 44.74 | 81.31 | +0.18% | 2.45x | 14510 | STRONG 96/100 | HIGH 55/100 | Watch |
| 7 | ADA/USD ⭐ | 0.152506 | 77.33 | +0.20% | 1.18x | 10206 | STRONG 84/100 | HIGH 62/100 | Watch |

**Same-run overlap:** ZEC/USD, SOL/USD, LTC/USD, XBT/USD, XDG/USD, ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
