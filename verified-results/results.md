# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T05:41:32.983594+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45947109817
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2ad009b216607b22e34efa5dd5535696859ab77a (atomic ledger/results publication)
**Ledger generation:** 1966 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 602; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 27.216 | 96.900 | 79.308 | +3.95% | +0.52% | 3.57x | 6.6 | 2026-11-27T05:41:26.764330+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 757.08 | 90.545 | 97.426 | +11.06% | -0.27% | 0.45x | 5.1 | 2026-11-27T05:41:26.764330+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | HYPE/USD | 65.74 | 88.636 | 93.841 | +5.66% | -0.20% | 0.58x | 1.5 | 2026-11-27T05:41:26.764330+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | XRP/USD | 0.96657 | 86.315 | 72.635 | +2.53% | +0.32% | 2.21x | 0.1 | 2026-11-27T05:41:26.764330+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | SUI/USD | 0.685 | 86.205 | 72.369 | +2.59% | +0.01% | 2.38x | 1.5 | 2026-11-27T05:41:26.764330+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 6 | LTC/USD | 44.63 | 82.563 | 68.123 | +2.03% | -0.11% | 3.25x | 2.2 | 2026-11-27T05:41:26.764330+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 7 | LINK/USD | 9.65589 | 82.247 | 81.999 | +4.18% | -0.16% | 1.10x | 4.5 | 2026-11-27T05:41:26.764330+00:00 | Not calibrated | MODERATE 51/100 | HIGH 68/100 | Watch | WATCH |
| 8 | SOL/USD | 73.03 | 79.156 | 74.939 | +2.95% | -0.15% | 1.50x | 1.4 | 2026-11-27T05:41:26.764330+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 9 | XBT/USD | 61642 | 75.986 | 68.229 | +1.89% | +0.01% | 1.77x | 0.0 | 2026-11-27T05:41:26.764330+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 10 | ETH/USD | 1740.65 | 72.956 | 75.965 | +3.14% | -0.22% | 0.81x | 2.0 | 2026-11-27T05:41:26.764330+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 11 | ADA/USD | 0.1522 | 70.525 | 69.144 | +2.52% | +0.00% | 1.14x | 3.9 | 2026-11-27T05:41:26.764330+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XAUT/USD | 3639.8 | 64.008 | 48.651 | +2.25% | +0.07% | 8.34x | 1.4 | 2026-11-27T05:41:26.764330+00:00 | Not calibrated | STRONG 77/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.426 | 757.08 | -0.27% | 0.45x |
| 2 | HYPE/USD | 93.841 | 65.74 | -0.20% | 0.58x |
| 3 | LINK/USD | 81.999 | 9.65589 | -0.16% | 1.10x |
| 4 | VVV/USD | 79.308 | 27.216 | +0.52% | 3.57x |
| 5 | ETH/USD | 75.965 | 1740.65 | -0.22% | 0.81x |
| 6 | SOL/USD | 74.939 | 73.03 | -0.15% | 1.50x |
| 7 | XRP/USD | 72.635 | 0.96657 | +0.32% | 2.21x |
| 8 | SUI/USD | 72.369 | 0.685 | +0.01% | 2.38x |
| 9 | ADA/USD | 69.144 | 0.1522 | +0.00% | 1.14x |
| 10 | XBT/USD | 68.229 | 61642 | +0.01% | 1.77x |
| 11 | LTC/USD | 68.123 | 44.63 | -0.11% | 3.25x |
| 12 | XAUT/USD | 48.651 | 3639.8 | +0.07% | 8.34x |

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

- Persisted scans: 1966; predictions: 17294; observations: 1190654.
- Matured sampled outcomes across 1/6/24/48h: 38150; gap abstentions: 25549. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45947109817 · **Generation:** 1966 · **Legacy run:** 45947109817
**Main quote time:** 2026-11-27T05:41:32.983594+00:00 · **Legacy report time:** 2026-11-27T05:42:14.001232+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 27.216 | 96.90 | +0.52% | 3.57x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD | 757.08 | 90.55 | -0.27% | 0.45x | MODERATE 50/100 | VERY_HIGH 76/100 | Watch |
| 3 | HYPE/USD | 65.74 | 88.64 | -0.20% | 0.58x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |
| 4 | XRP/USD ⭐ | 0.96657 | 86.31 | +0.32% | 2.21x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | SUI/USD | 0.685 | 86.20 | +0.01% | 2.38x | STRONG 88/100 | HIGH 55/100 | Watch |
| 6 | LTC/USD | 44.63 | 82.56 | -0.11% | 3.25x | STRONG 71/100 | HIGH 61/100 | Watch |
| 7 | LINK/USD | 9.65589 | 82.25 | -0.16% | 1.10x | MODERATE 51/100 | HIGH 68/100 | Watch |
| 8 | SOL/USD | 73.03 | 79.16 | -0.15% | 1.50x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 9 | XBT/USD | 61642 | 75.99 | +0.01% | 1.77x | STRONG 73/100 | HIGH 55/100 | Watch |
| 10 | ETH/USD | 1740.65 | 72.96 | -0.22% | 0.81x | WEAK 41/100 | HIGH 68/100 | Watch |
| 11 | ADA/USD | 0.1522 | 70.52 | +0.00% | 1.14x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 12 | XAUT/USD | 3639.8 | 64.01 | +0.07% | 8.34x | STRONG 77/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 27.239 | 94.56 | +0.52% | 3.57x | 11662 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | WLD/USD | 0.2515 | 89.84 | +0.84% | 4.08x | 2579 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | XRP/USD ⭐ | 0.96741 | 88.97 | +0.32% | 2.21x | 21530 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | TIA/USD | 0.3484 | 83.90 | +0.35% | 8.46x | 2598 | STRONG 97/100 | HIGH 67/100 | Consider small entry |
| 5 | PEPE/USD | 3.585e-06 | 77.07 | +0.34% | 1.00x | 5280 | STRONG 74/100 | HIGH 62/100 | Watch |

**Same-run overlap:** VVV/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
