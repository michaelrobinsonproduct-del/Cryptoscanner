# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T06:21:31.678696+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45951117269
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2e9583dbc6370a9e1c4865628805561ad365e0e5 (atomic ledger/results publication)
**Ledger generation:** 1970 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 66.38 | 101.196 | 98.493 | +6.69% | +0.00% | 1.27x | 3.0 | 2026-11-27T06:21:24.787469+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 2 | ZEC/USD | 758.62 | 91.728 | 97.433 | +11.29% | +0.07% | 0.40x | 5.1 | 2026-11-27T06:21:24.787469+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.05 | 85.542 | 62.932 | +3.16% | +1.52% | 7.07x | 2.0 | 2026-11-27T06:21:24.787469+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | LINK/USD | 9.64959 | 75.758 | 82.087 | +4.11% | -0.26% | 0.50x | 3.4 | 2026-11-27T06:21:24.787469+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | ADA/USD | 0.153228 | 75.539 | 72.398 | +3.21% | +0.27% | 1.18x | 4.2 | 2026-11-27T06:21:24.787469+00:00 | Not calibrated | STRONG 73/100 | HIGH 62/100 | Watch | WATCH |
| 6 | XRP/USD | 0.97083 | 74.947 | 75.026 | +2.98% | +0.37% | 0.81x | 1.6 | 2026-11-27T06:21:24.787469+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 7 | ETH/USD | 1738.92 | 72.724 | 75.160 | +3.04% | -0.02% | 0.76x | 2.2 | 2026-11-27T06:21:24.787469+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 8 | SOL/USD | 73.09 | 72.694 | 75.531 | +3.03% | +0.30% | 0.57x | 1.4 | 2026-11-27T06:21:24.787469+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | PEPE/USD | 3.605e-06 | 69.494 | 67.522 | +3.65% | +0.50% | 0.95x | 2.8 | 2026-11-27T06:21:24.787469+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0581102 | 67.878 | 66.093 | +3.08% | +0.27% | 1.04x | 1.1 | 2026-11-27T06:21:24.787469+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 11 | PAXG/USD | 3631.36 | 67.721 | 52.622 | +2.10% | +0.02% | 3.84x | 2.0 | 2026-11-27T06:21:24.787469+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 12 | XBT/USD | 61761.1 | 66.963 | 69.607 | +2.09% | +0.26% | 0.61x | 0.0 | 2026-11-27T06:21:24.787469+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | HYPE/USD | 98.493 | 66.38 | +0.00% | 1.27x |
| 2 | ZEC/USD | 97.433 | 758.62 | +0.07% | 0.40x |
| 3 | LINK/USD | 82.087 | 9.64959 | -0.26% | 0.50x |
| 4 | SOL/USD | 75.531 | 73.09 | +0.30% | 0.57x |
| 5 | ETH/USD | 75.160 | 1738.92 | -0.02% | 0.76x |
| 6 | XRP/USD | 75.026 | 0.97083 | +0.37% | 0.81x |
| 7 | ADA/USD | 72.398 | 0.153228 | +0.27% | 1.18x |
| 8 | XBT/USD | 69.607 | 61761.1 | +0.26% | 0.61x |
| 9 | PEPE/USD | 67.522 | 3.605e-06 | +0.50% | 0.95x |
| 10 | XDG/USD | 66.093 | 0.0581102 | +0.27% | 1.04x |
| 11 | NIGHT/USD | 62.932 | 0.05 | +1.52% | 7.07x |
| 12 | PAXG/USD | 52.622 | 3631.36 | +0.02% | 3.84x |

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

- Persisted scans: 1970; predictions: 17342; observations: 1193063.
- Matured sampled outcomes across 1/6/24/48h: 38289; gap abstentions: 25572. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45951117269 · **Generation:** 1970 · **Legacy run:** 45951117269
**Main quote time:** 2026-11-27T06:21:31.678696+00:00 · **Legacy report time:** 2026-11-27T06:22:13.268620+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 66.38 | 101.20 | +0.00% | 1.27x | STRONG 75/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD | 758.62 | 91.73 | +0.07% | 0.40x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 3 | NIGHT/USD ⭐ | 0.05 | 85.54 | +1.52% | 7.07x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | LINK/USD | 9.64959 | 75.76 | -0.26% | 0.50x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 5 | ADA/USD ⭐ | 0.153228 | 75.54 | +0.27% | 1.18x | STRONG 83/100 | HIGH 62/100 | Watch |
| 6 | XRP/USD | 0.97083 | 74.95 | +0.37% | 0.81x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 7 | ETH/USD | 1738.92 | 72.72 | -0.02% | 0.76x | WEAK 41/100 | HIGH 68/100 | Watch |
| 8 | SOL/USD | 73.09 | 72.69 | +0.30% | 0.57x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 9 | PEPE/USD | 3.605e-06 | 69.49 | +0.50% | 0.95x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 10 | XDG/USD ⭐ | 0.0581102 | 67.88 | +0.27% | 1.04x | STRONG 79/100 | HIGH 62/100 | Watch |
| 11 | PAXG/USD | 3631.36 | 67.72 | +0.02% | 3.84x | STRONG 79/100 | HIGH 55/100 | Watch |
| 12 | XBT/USD | 61761.1 | 66.96 | +0.26% | 0.61x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04998 | 86.04 | +1.52% | 7.07x | 8948 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | TAO/USD | 188.6589 | 85.18 | +0.37% | 11.16x | 5529 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 3 | XDG/USD ⭐ | 0.0580813 | 83.35 | +0.27% | 1.04x | 5755 | STRONG 87/100 | HIGH 62/100 | Watch |
| 4 | ADA/USD ⭐ | 0.153343 | 78.56 | +0.27% | 1.18x | 9922 | STRONG 84/100 | HIGH 62/100 | Watch |

**Same-run overlap:** NIGHT/USD, ADA/USD, XDG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
