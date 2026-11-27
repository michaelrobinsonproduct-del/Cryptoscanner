# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T04:41:46.744258+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45941229674
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 5a15778c6867cd902d50a32d217277cf3c908b24 (atomic ledger/results publication)
**Ledger generation:** 1960 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 759.58 | 113.700 | 98.025 | +11.43% | +0.13% | 5.73x | 3.9 | 2026-11-27T04:41:38.479055+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | HYPE/USD | 65.98 | 108.521 | 95.786 | +6.04% | -0.45% | 3.98x | 3.0 | 2026-11-27T04:41:38.479055+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LINK/USD | 9.60809 | 96.533 | 77.868 | +3.66% | +0.73% | 15.99x | 5.6 | 2026-11-27T04:41:38.479055+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | ETH/USD | 1735.35 | 91.677 | 74.743 | +2.82% | +0.39% | 4.62x | 0.1 | 2026-11-27T04:41:38.479055+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | XMR/USD | 470.76 | 75.970 | 69.878 | +3.02% | +0.53% | 1.34x | 12.6 | 2026-11-27T04:41:38.479055+00:00 | Not calibrated | STRONG 78/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SUI/USD | 0.6836 | 70.936 | 70.102 | +2.38% | +0.40% | 0.89x | 2.9 | 2026-11-27T04:41:38.479055+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 7 | UNI/USD | 4.8497 | 69.179 | 71.027 | +4.29% | +0.23% | 0.70x | 3.9 | 2026-11-27T04:41:38.479055+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XRP/USD | 0.96048 | 68.206 | 67.852 | +1.88% | +0.11% | 0.98x | 0.6 | 2026-11-27T04:41:38.479055+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 9 | ADA/USD | 0.151784 | 66.627 | 67.614 | +2.24% | +0.39% | 0.70x | 2.7 | 2026-11-27T04:41:38.479055+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SOL/USD | 72.85 | 65.829 | 73.160 | +2.69% | +0.21% | 0.16x | 1.4 | 2026-11-27T04:41:38.479055+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | VVV/USD | 26.985 | 63.527 | 72.544 | +3.06% | -0.39% | 0.29x | 7.8 | 2026-11-27T04:41:38.479055+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | NEAR/USD | 3.1116 | 61.916 | 67.699 | +2.09% | +0.04% | 0.40x | 3.9 | 2026-11-27T04:41:38.479055+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.025 | 759.58 | +0.13% | 5.73x |
| 2 | HYPE/USD | 95.786 | 65.98 | -0.45% | 3.98x |
| 3 | LINK/USD | 77.868 | 9.60809 | +0.73% | 15.99x |
| 4 | ETH/USD | 74.743 | 1735.35 | +0.39% | 4.62x |
| 5 | SOL/USD | 73.160 | 72.85 | +0.21% | 0.16x |
| 6 | VVV/USD | 72.544 | 26.985 | -0.39% | 0.29x |
| 7 | UNI/USD | 71.027 | 4.8497 | +0.23% | 0.70x |
| 8 | SUI/USD | 70.102 | 0.6836 | +0.40% | 0.89x |
| 9 | XMR/USD | 69.878 | 470.76 | +0.53% | 1.34x |
| 10 | XRP/USD | 67.852 | 0.96048 | +0.11% | 0.98x |
| 11 | NEAR/USD | 67.699 | 3.1116 | +0.04% | 0.40x |
| 12 | ADA/USD | 67.614 | 0.151784 | +0.39% | 0.70x |

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

- Persisted scans: 1960; predictions: 17222; observations: 1187044.
- Matured sampled outcomes across 1/6/24/48h: 37922; gap abstentions: 25514. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45941229674 · **Generation:** 1960 · **Legacy run:** 45941229674
**Main quote time:** 2026-11-27T04:41:46.744258+00:00 · **Legacy report time:** 2026-11-27T04:42:38.966692+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 759.58 | 113.70 | +0.13% | 5.73x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | HYPE/USD | 65.98 | 108.52 | -0.45% | 3.98x | STRONG 80/100 | HIGH 61/100 | Watch |
| 3 | LINK/USD ⭐ | 9.60809 | 96.53 | +0.73% | 15.99x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | ETH/USD ⭐ | 1735.35 | 91.68 | +0.39% | 4.62x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | XMR/USD | 470.76 | 75.97 | +0.53% | 1.34x | STRONG 78/100 | HIGH 61/100 | Watch |
| 6 | SUI/USD | 0.6836 | 70.94 | +0.40% | 0.89x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 7 | UNI/USD | 4.8497 | 69.18 | +0.23% | 0.70x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 8 | XRP/USD | 0.96048 | 68.21 | +0.11% | 0.98x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 9 | ADA/USD | 0.151784 | 66.63 | +0.39% | 0.70x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 10 | SOL/USD | 72.85 | 65.83 | +0.21% | 0.16x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 11 | VVV/USD | 26.985 | 63.53 | -0.39% | 0.29x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 12 | NEAR/USD | 3.1116 | 61.92 | +0.04% | 0.40x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 758.25 | 98.11 | +0.13% | 5.73x | 38917 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | LINK/USD ⭐ | 9.59175 | 96.45 | +0.73% | 15.99x | 7450 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ETH/USD ⭐ | 1734.18 | 94.11 | +0.39% | 4.62x | 32211 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | PEPE/USD | 3.582e-06 | 83.20 | +0.25% | 3.24x | 5166 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 5 | LTC/USD | 44.55 | 70.45 | +0.18% | 1.05x | 14443 | MODERATE 60/100 | HIGH 62/100 | Watch |

**Same-run overlap:** ZEC/USD, LINK/USD, ETH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
