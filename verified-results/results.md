# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T01:31:41.775807+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45922859015
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** ae1ec8e12c314943559f33fc277bc65d852438d8 (atomic ledger/results publication)
**Ledger generation:** 1940 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 703.81 | 92.853 | 75.682 | +3.25% | +0.43% | 4.92x | 4.1 | 2026-11-27T01:31:33.912577+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | LTC/USD | 44.26 | 77.191 | 62.191 | +1.19% | +0.00% | 3.18x | 2.3 | 2026-11-27T01:31:33.912577+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 3 | SOL/USD | 71.34 | 67.027 | 58.246 | +0.56% | +0.06% | 1.85x | 1.4 | 2026-11-27T01:31:33.912577+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 4 | XBT/USD | 60667.9 | 65.003 | 56.958 | +0.28% | -0.01% | 1.81x | 0.0 | 2026-11-27T01:31:33.912577+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ETH/USD | 1698.88 | 64.746 | 59.616 | +0.66% | +0.01% | 1.51x | 0.1 | 2026-11-27T01:31:33.912577+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XRP/USD | 0.9463 | 63.688 | 57.055 | +0.38% | +0.02% | 1.65x | 1.2 | 2026-11-27T01:31:33.912577+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 7 | HYPE/USD | 62.91 | 62.362 | 61.968 | +1.11% | -0.06% | 1.07x | 1.6 | 2026-11-27T01:31:33.912577+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0566788 | 58.740 | 44.039 | +0.54% | -0.06% | 4.32x | 1.7 | 2026-11-27T01:31:33.912577+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 9 | PAXG/USD | 3566.25 | 55.148 | 39.143 | +0.27% | +0.20% | 8.59x | 1.6 | 2026-11-27T01:31:33.912577+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 10 | NEAR/USD | 3.0669 | 54.324 | 58.711 | +0.62% | -0.18% | 0.65x | 1.3 | 2026-11-27T01:31:33.912577+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | DOT/USD | 0.6795 | 53.750 | 39.265 | +1.04% | -0.10% | 3.35x | 1.5 | 2026-11-27T01:31:33.912577+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |
| 12 | ADA/USD | 0.149413 | 52.867 | 56.500 | +0.64% | -0.03% | 0.65x | 2.5 | 2026-11-27T01:31:33.912577+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 75.682 | 703.81 | +0.43% | 4.92x |
| 2 | LTC/USD | 62.191 | 44.26 | +0.00% | 3.18x |
| 3 | HYPE/USD | 61.968 | 62.91 | -0.06% | 1.07x |
| 4 | ETH/USD | 59.616 | 1698.88 | +0.01% | 1.51x |
| 5 | NEAR/USD | 58.711 | 3.0669 | -0.18% | 0.65x |
| 6 | SOL/USD | 58.246 | 71.34 | +0.06% | 1.85x |
| 7 | XRP/USD | 57.055 | 0.9463 | +0.02% | 1.65x |
| 8 | XBT/USD | 56.958 | 60667.9 | -0.01% | 1.81x |
| 9 | ADA/USD | 56.500 | 0.149413 | -0.03% | 0.65x |
| 10 | XDG/USD | 44.039 | 0.0566788 | -0.06% | 4.32x |
| 11 | DOT/USD | 39.265 | 0.6795 | -0.10% | 3.35x |
| 12 | PAXG/USD | 39.143 | 3566.25 | +0.20% | 8.59x |

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

- Persisted scans: 1940; predictions: 16982; observations: 1175025.
- Matured sampled outcomes across 1/6/24/48h: 37242; gap abstentions: 25431. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45922859015 · **Generation:** 1940 · **Legacy run:** 45922859015
**Main quote time:** 2026-11-27T01:31:41.775807+00:00 · **Legacy report time:** 2026-11-27T01:32:19.469576+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 703.81 | 92.85 | +0.43% | 4.92x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | LTC/USD | 44.26 | 77.19 | +0.00% | 3.18x | STRONG 84/100 | HIGH 55/100 | Watch |
| 3 | SOL/USD ⭐ | 71.34 | 67.03 | +0.06% | 1.85x | STRONG 79/100 | HIGH 55/100 | Watch |
| 4 | XBT/USD | 60667.9 | 65.00 | -0.01% | 1.81x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 5 | ETH/USD | 1698.88 | 64.75 | +0.01% | 1.51x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 6 | XRP/USD | 0.9463 | 63.69 | +0.02% | 1.65x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 7 | HYPE/USD | 62.91 | 62.36 | -0.06% | 1.07x | WEAK 41/100 | HIGH 68/100 | Watch |
| 8 | XDG/USD | 0.0566788 | 58.74 | -0.06% | 4.32x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 9 | PAXG/USD | 3566.25 | 55.15 | +0.20% | 8.59x | STRONG 83/100 | HIGH 55/100 | Watch |
| 10 | NEAR/USD | 3.0669 | 54.32 | -0.18% | 0.65x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | DOT/USD | 0.6795 | 53.75 | -0.10% | 3.35x | MODERATE 57/100 | HIGH 66/100 | Watch |
| 12 | ADA/USD | 0.149413 | 52.87 | -0.03% | 0.65x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 701.74 | 83.83 | +0.43% | 4.92x | 33780 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SOL/USD ⭐ | 71.28 | 58.51 | +0.06% | 1.85x | 33005 | STRONG 74/100 | HIGH 55/100 | Watch |
| 3 | PEPE/USD | 3.512e-06 | 57.02 | +0.11% | 3.76x | 5323 | STRONG 74/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
