# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T00:41:18.005211+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45918003785
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** cf5e83cd5c13eef43b9e3d90ee172d11c76c0843 (atomic ledger/results publication)
**Ledger generation:** 1935 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 62.79 | 76.654 | 60.616 | +0.92% | +0.21% | 2.74x | 1.6 | 2026-11-27T00:41:09.174038+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XMR/USD | 460.71 | 73.277 | 56.524 | +0.82% | +0.35% | 2.92x | 8.5 | 2026-11-27T00:41:09.174038+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ADA/USD | 0.148919 | 69.710 | 54.737 | +0.31% | +0.13% | 2.43x | 1.9 | 2026-11-27T00:41:09.174038+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ZEC/USD | 692.29 | 57.459 | 62.809 | +1.56% | +0.40% | 0.26x | 6.2 | 2026-11-27T00:41:09.174038+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | ETH/USD | 1692.88 | 56.813 | 57.127 | +0.31% | +0.19% | 0.87x | 0.1 | 2026-11-27T00:41:09.174038+00:00 | Not calibrated | MODERATE 48/100 | HIGH 62/100 | Watch | WATCH |
| 6 | LTC/USD | 44.01 | 55.931 | 58.185 | +0.62% | +0.23% | 0.66x | 2.3 | 2026-11-27T00:41:09.174038+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SOL/USD | 71.19 | 53.053 | 56.764 | +0.35% | +0.07% | 0.59x | 1.4 | 2026-11-27T00:41:09.174038+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | CRV/USD | 0.17536 | 51.934 | 37.133 | +0.71% | -0.04% | 3.79x | 8.0 | 2026-11-27T00:41:09.174038+00:00 | Not calibrated | MODERATE 56/100 | HIGH 66/100 | Watch | WATCH |
| 9 | LINK/USD | 9.32881 | 51.443 | 58.231 | +0.65% | +0.10% | 0.27x | 2.7 | 2026-11-27T00:41:09.174038+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | VVV/USD | 26.419 | 50.998 | 57.902 | +0.90% | -0.48% | 0.55x | 6.8 | 2026-11-27T00:41:09.174038+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | NIGHT/USD | 0.0486 | 45.442 | 42.468 | +0.27% | +0.70% | 0.95x | 6.2 | 2026-11-27T00:41:09.174038+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |
| 12 | HBAR/USD | 0.05416 | 42.954 | 35.446 | +0.37% | +0.24% | 1.63x | 3.7 | 2026-11-27T00:41:09.174038+00:00 | Not calibrated | MODERATE 66/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 62.809 | 692.29 | +0.40% | 0.26x |
| 2 | HYPE/USD | 60.616 | 62.79 | +0.21% | 2.74x |
| 3 | LINK/USD | 58.231 | 9.32881 | +0.10% | 0.27x |
| 4 | LTC/USD | 58.185 | 44.01 | +0.23% | 0.66x |
| 5 | VVV/USD | 57.902 | 26.419 | -0.48% | 0.55x |
| 6 | ETH/USD | 57.127 | 1692.88 | +0.19% | 0.87x |
| 7 | SOL/USD | 56.764 | 71.19 | +0.07% | 0.59x |
| 8 | XMR/USD | 56.524 | 460.71 | +0.35% | 2.92x |
| 9 | ADA/USD | 54.737 | 0.148919 | +0.13% | 2.43x |
| 10 | NIGHT/USD | 42.468 | 0.0486 | +0.70% | 0.95x |
| 11 | CRV/USD | 37.133 | 0.17536 | -0.04% | 3.79x |
| 12 | HBAR/USD | 35.446 | 0.05416 | +0.24% | 1.63x |

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

- Persisted scans: 1935; predictions: 16922; observations: 1172020.
- Matured sampled outcomes across 1/6/24/48h: 37064; gap abstentions: 25409. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 149 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45918003785 · **Generation:** 1935 · **Legacy run:** 45918003785
**Main quote time:** 2026-11-27T00:41:18.005211+00:00 · **Legacy report time:** 2026-11-27T00:42:00.505609+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 62.79 | 76.65 | +0.21% | 2.74x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD ⭐ | 460.71 | 73.28 | +0.35% | 2.92x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ADA/USD ⭐ | 0.148919 | 69.71 | +0.13% | 2.43x | STRONG 90/100 | HIGH 55/100 | Watch |
| 4 | ZEC/USD | 692.29 | 57.46 | +0.40% | 0.26x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 5 | ETH/USD | 1692.88 | 56.81 | +0.19% | 0.87x | MODERATE 48/100 | HIGH 62/100 | Watch |
| 6 | LTC/USD | 44.01 | 55.93 | +0.23% | 0.66x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 7 | SOL/USD | 71.19 | 53.05 | +0.07% | 0.59x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 8 | CRV/USD | 0.17536 | 51.93 | -0.04% | 3.79x | MODERATE 56/100 | HIGH 66/100 | Watch |
| 9 | LINK/USD | 9.32881 | 51.44 | +0.10% | 0.27x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 10 | VVV/USD | 26.419 | 51.00 | -0.48% | 0.55x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | NIGHT/USD | 0.0486 | 45.44 | +0.70% | 0.95x | MODERATE 53/100 | HIGH 62/100 | Watch |
| 12 | HBAR/USD | 0.05416 | 42.95 | +0.24% | 1.63x | MODERATE 66/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 62.79 | 67.39 | +0.21% | 2.74x | 12676 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD ⭐ | 461.47 | 57.59 | +0.35% | 2.92x | 18038 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 3 | XBT/USD | 60585.8 | 54.09 | +0.11% | 1.02x | 132253 | MODERATE 52/100 | HIGH 62/100 | Watch |
| 4 | ADA/USD ⭐ | 0.148928 | 52.03 | +0.13% | 2.43x | 10078 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** HYPE/USD, XMR/USD, ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
