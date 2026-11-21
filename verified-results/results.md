# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T14:00:50.190029+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44911588657
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** b9b54351bdda81b1e98c74f1d1662eb49a2acc70 (atomic ledger/results publication)
**Ledger generation:** 1142 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ETH/USD | 1701.04 | 106.231 | 90.296 | +5.05% | +0.19% | 2.70x | 0.1 | 2026-11-21T14:00:42.310832+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | ZEC/USD | 800.31 | 100.582 | 92.660 | +5.59% | +0.28% | 1.65x | 3.0 | 2026-11-21T14:00:42.310832+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | TAO/USD | 188.1257 | 96.754 | 79.253 | +4.22% | +0.50% | 2.84x | 10.6 | 2026-11-21T14:00:42.310832+00:00 | Not calibrated | STRONG 98/100 | HIGH 61/100 | Consider small entry | WATCH |
| 4 | SOL/USD | 70.67 | 91.749 | 74.260 | +2.85% | +0.50% | 3.26x | 1.4 | 2026-11-21T14:00:42.310832+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | XBT/USD | 60528.2 | 90.701 | 75.487 | +2.93% | +0.23% | 2.40x | 0.0 | 2026-11-21T14:00:42.310832+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | USELESS/USD | 0.08018 | 90.551 | 79.905 | +7.62% | +0.01% | 2.06x | 11.2 | 2026-11-21T14:00:42.310832+00:00 | Not calibrated | STRONG 85/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XRP/USD | 0.93078 | 89.673 | 71.840 | +2.43% | +0.57% | 2.65x | 0.3 | 2026-11-21T14:00:42.310832+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | UNI/USD | 4.7085 | 89.283 | 89.522 | +5.40% | +0.05% | 0.95x | 6.6 | 2026-11-21T14:00:42.310832+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 9 | XMR/USD | 473.46 | 86.836 | 76.478 | +3.76% | -0.71% | 2.39x | 9.7 | 2026-11-21T14:00:42.310832+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 10 | AVAX/USD | 6.662 | 85.362 | 70.283 | +2.40% | +0.38% | 2.32x | 3.0 | 2026-11-21T14:00:42.310832+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 11 | TRX/USD | 0.306086 | 81.802 | 65.622 | +1.52% | +0.24% | 8.74x | 0.0 | 2026-11-21T14:00:42.310832+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 12 | LINK/USD | 8.66755 | 81.389 | 63.934 | +1.62% | +0.49% | 3.19x | 4.8 | 2026-11-21T14:00:42.310832+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 92.660 | 800.31 | +0.28% | 1.65x |
| 2 | ETH/USD | 90.296 | 1701.04 | +0.19% | 2.70x |
| 3 | UNI/USD | 89.522 | 4.7085 | +0.05% | 0.95x |
| 4 | USELESS/USD | 79.905 | 0.08018 | +0.01% | 2.06x |
| 5 | TAO/USD | 79.253 | 188.1257 | +0.50% | 2.84x |
| 6 | XMR/USD | 76.478 | 473.46 | -0.71% | 2.39x |
| 7 | XBT/USD | 75.487 | 60528.2 | +0.23% | 2.40x |
| 8 | SOL/USD | 74.260 | 70.67 | +0.50% | 3.26x |
| 9 | XRP/USD | 71.840 | 0.93078 | +0.57% | 2.65x |
| 10 | AVAX/USD | 70.283 | 6.662 | +0.38% | 2.32x |
| 11 | TRX/USD | 65.622 | 0.306086 | +0.24% | 8.74x |
| 12 | LINK/USD | 63.934 | 8.66755 | +0.49% | 3.19x |

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

- Persisted scans: 1142; predictions: 9013; observations: 690695.
- Matured sampled outcomes across 1/6/24/48h: 11830; gap abstentions: 20448. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44911588657 · **Generation:** 1142 · **Legacy run:** 44911588657
**Main quote time:** 2026-11-21T14:00:50.190029+00:00 · **Legacy report time:** 2026-11-21T14:01:37.004680+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD ⭐ | 1701.04 | 106.23 | +0.19% | 2.70x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD ⭐ | 800.31 | 100.58 | +0.28% | 1.65x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | TAO/USD ⭐ | 188.1257 | 96.75 | +0.50% | 2.84x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 4 | SOL/USD ⭐ | 70.67 | 91.75 | +0.50% | 3.26x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | XBT/USD ⭐ | 60528.2 | 90.70 | +0.23% | 2.40x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | USELESS/USD | 0.08018 | 90.55 | +0.01% | 2.06x | STRONG 85/100 | HIGH 61/100 | Watch |
| 7 | XRP/USD ⭐ | 0.93078 | 89.67 | +0.57% | 2.65x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | UNI/USD | 4.7085 | 89.28 | +0.05% | 0.95x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 9 | XMR/USD | 473.46 | 86.84 | -0.71% | 2.39x | STRONG 73/100 | HIGH 61/100 | Watch |
| 10 | AVAX/USD ⭐ | 6.662 | 85.36 | +0.38% | 2.32x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 11 | TRX/USD | 0.306086 | 81.80 | +0.24% | 8.74x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 12 | LINK/USD | 8.66755 | 81.39 | +0.49% | 3.19x | STRONG 96/100 | HIGH 55/100 | Consider small entry |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD ⭐ | 1702.58 | 100.00 | +0.19% | 2.70x | 101530 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | XBT/USD ⭐ | 60599.9 | 94.88 | +0.23% | 2.40x | 278471 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SOL/USD ⭐ | 70.76 | 94.47 | +0.50% | 3.26x | 58162 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | TAO/USD ⭐ | 188.2 | 93.86 | +0.50% | 2.84x | 16540 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | VVV/USD | 23.261 | 89.00 | +0.38% | 1.71x | 15087 | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 6 | ZEC/USD ⭐ | 800.32 | 88.70 | +0.28% | 1.65x | 57247 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 7 | AAVE/USD | 101.34 | 87.23 | +0.55% | 3.15x | 8559 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 8 | XRP/USD ⭐ | 0.93097 | 83.05 | +0.57% | 2.65x | 68943 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | AVAX/USD ⭐ | 6.662 | 81.18 | +0.38% | 2.32x | 8842 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 10 | NEAR/USD | 2.9137 | 74.97 | +0.40% | 1.52x | 29518 | STRONG 82/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ETH/USD, ZEC/USD, TAO/USD, SOL/USD, XBT/USD, XRP/USD, AVAX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
