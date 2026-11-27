# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T12:12:41.826346+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45996299344
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2f53e5bfddcdb9c386bc93b78cd286e17321eea1 (atomic ledger/results publication)
**Ledger generation:** 2006 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 65.78 | 108.760 | 94.292 | +5.72% | -0.11% | 2.56x | 1.5 | 2026-11-27T12:12:33.571526+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ZEC/USD | 757.71 | 94.764 | 98.614 | +11.16% | +0.68% | 0.28x | 2.8 | 2026-11-27T12:12:33.571526+00:00 | Not calibrated | STRONG 77/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | ADA/USD | 0.153307 | 89.380 | 73.873 | +3.26% | +0.10% | 2.81x | 2.7 | 2026-11-27T12:12:33.571526+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 4 | XRP/USD | 0.97561 | 83.616 | 79.194 | +3.49% | -0.09% | 1.49x | 0.4 | 2026-11-27T12:12:33.571526+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 5 | INJ/USD | 6.5 | 78.310 | 72.740 | +4.97% | +0.39% | 1.36x | 1.5 | 2026-11-27T12:12:33.571526+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 6 | ENA/USD | 0.1082 | 77.722 | 77.513 | +7.77% | +0.37% | 0.84x | 9.2 | 2026-11-27T12:12:33.571526+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 7 | PAXG/USD | 3656.94 | 75.838 | 60.833 | +2.82% | +0.00% | 16.27x | 0.9 | 2026-11-27T12:12:33.571526+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 8 | SOL/USD | 73.17 | 74.731 | 76.321 | +3.14% | +0.15% | 0.77x | 1.4 | 2026-11-27T12:12:33.571526+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 9 | XLM/USD | 0.129761 | 74.700 | 58.982 | +2.49% | +0.14% | 2.76x | 0.1 | 2026-11-27T12:12:33.571526+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 10 | ETH/USD | 1720.99 | 73.067 | 67.886 | +1.97% | +0.16% | 1.44x | 1.9 | 2026-11-27T12:12:33.571526+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0588522 | 72.748 | 77.546 | +4.40% | +0.14% | 0.45x | 0.4 | 2026-11-27T12:12:33.571526+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | LINK/USD | 9.53741 | 72.053 | 72.142 | +2.90% | +0.01% | 0.99x | 6.3 | 2026-11-27T12:12:33.571526+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.614 | 757.71 | +0.68% | 0.28x |
| 2 | HYPE/USD | 94.292 | 65.78 | -0.11% | 2.56x |
| 3 | XRP/USD | 79.194 | 0.97561 | -0.09% | 1.49x |
| 4 | XDG/USD | 77.546 | 0.0588522 | +0.14% | 0.45x |
| 5 | ENA/USD | 77.513 | 0.1082 | +0.37% | 0.84x |
| 6 | SOL/USD | 76.321 | 73.17 | +0.15% | 0.77x |
| 7 | ADA/USD | 73.873 | 0.153307 | +0.10% | 2.81x |
| 8 | INJ/USD | 72.740 | 6.5 | +0.39% | 1.36x |
| 9 | LINK/USD | 72.142 | 9.53741 | +0.01% | 0.99x |
| 10 | ETH/USD | 67.886 | 1720.99 | +0.16% | 1.44x |
| 11 | PAXG/USD | 60.833 | 3656.94 | +0.00% | 16.27x |
| 12 | XLM/USD | 58.982 | 0.129761 | +0.14% | 2.76x |

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

- Persisted scans: 2006; predictions: 17774; observations: 1214767.
- Matured sampled outcomes across 1/6/24/48h: 39533; gap abstentions: 25823. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45996299344 · **Generation:** 2006 · **Legacy run:** 45996299344
**Main quote time:** 2026-11-27T12:12:41.826346+00:00 · **Legacy report time:** 2026-11-27T12:13:20.660398+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 65.78 | 108.76 | -0.11% | 2.56x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | ZEC/USD | 757.71 | 94.76 | +0.68% | 0.28x | STRONG 77/100 | VERY_HIGH 70/100 | Watch |
| 3 | ADA/USD ⭐ | 0.153307 | 89.38 | +0.10% | 2.81x | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | XRP/USD | 0.97561 | 83.62 | -0.09% | 1.49x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 5 | INJ/USD ⭐ | 6.5 | 78.31 | +0.39% | 1.36x | STRONG 94/100 | HIGH 55/100 | Watch |
| 6 | ENA/USD | 0.1082 | 77.72 | +0.37% | 0.84x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 7 | PAXG/USD | 3656.94 | 75.84 | +0.00% | 16.27x | STRONG 83/100 | HIGH 55/100 | Watch |
| 8 | SOL/USD | 73.17 | 74.73 | +0.15% | 0.77x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 9 | XLM/USD | 0.129761 | 74.70 | +0.14% | 2.76x | STRONG 82/100 | HIGH 55/100 | Watch |
| 10 | ETH/USD ⭐ | 1720.99 | 73.07 | +0.16% | 1.44x | STRONG 82/100 | HIGH 55/100 | Watch |
| 11 | XDG/USD | 0.0588522 | 72.75 | +0.14% | 0.45x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 12 | LINK/USD | 9.53741 | 72.05 | +0.01% | 0.99x | MODERATE 56/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.15336 | 93.41 | +0.10% | 2.81x | 9408 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | TAO/USD | 189.6923 | 81.90 | +0.34% | 1.42x | 5664 | STRONG 86/100 | HIGH 55/100 | Watch |
| 3 | INJ/USD ⭐ | 6.498 | 80.72 | +0.39% | 1.36x | 4890 | STRONG 95/100 | HIGH 55/100 | Watch |
| 4 | NEAR/USD | 3.1205 | 80.22 | +0.19% | 1.57x | 13272 | STRONG 75/100 | HIGH 55/100 | Watch |
| 5 | ETH/USD ⭐ | 1721.15 | 77.92 | +0.16% | 1.44x | 35747 | STRONG 84/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ADA/USD, INJ/USD, ETH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
