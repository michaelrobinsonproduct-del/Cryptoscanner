# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T20:35:55.189193+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45696270346
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7c9fdd8edc8849b77dd87ec52390ebf89d51bf6e (atomic ledger/results publication)
**Ledger generation:** 1764 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 27.401 | 97.359 | 95.620 | +11.67% | -1.56% | 1.95x | 8.8 | 2026-11-25T20:35:48.502756+00:00 | Not calibrated | MODERATE 69/100 | HIGH 65/100 | Do nothing | WATCH |
| 2 | NEAR/USD | 2.9876 | 85.159 | 74.826 | +3.57% | -0.93% | 3.33x | 10.4 | 2026-11-25T20:35:48.502756+00:00 | Not calibrated | MODERATE 68/100 | HIGH 67/100 | Watch | WATCH |
| 3 | LTC/USD | 42.49 | 83.673 | 81.925 | +4.01% | -0.14% | 1.25x | 2.4 | 2026-11-25T20:35:48.502756+00:00 | Not calibrated | MODERATE 52/100 | HIGH 68/100 | Watch | WATCH |
| 4 | HYPE/USD | 61.23 | 74.381 | 70.085 | +2.27% | -0.39% | 1.62x | 1.6 | 2026-11-25T20:35:48.502756+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 5 | DRV/USD | 0.34893 | 73.806 | 75.023 | +11.03% | -0.43% | 1.09x | 18.4 | 2026-11-25T20:35:48.502756+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 6 | LINK/USD | 9.07009 | 69.087 | 63.308 | +2.59% | -0.07% | 1.61x | 5.3 | 2026-11-25T20:35:48.502756+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XBT/USD | 59911.2 | 64.877 | 56.982 | +0.28% | +0.00% | 1.79x | 0.0 | 2026-11-25T20:35:48.502756+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 8 | XMR/USD | 518.14 | 63.541 | 62.968 | +1.68% | -0.04% | 1.08x | 7.5 | 2026-11-25T20:35:48.502756+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 9 | ZEC/USD | 753.81 | 61.514 | 66.945 | +2.02% | -0.27% | 0.59x | 4.4 | 2026-11-25T20:35:48.502756+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XPL/USD | 0.0473 | 60.786 | 71.771 | +7.50% | -1.25% | 0.53x | 21.1 | 2026-11-25T20:35:48.502756+00:00 | Not calibrated | WEAK 25/100 | EXTREME 92/100 | Do nothing | WATCH |
| 11 | SUI/USD | 0.6611 | 60.486 | 68.947 | +2.10% | -0.33% | 0.32x | 1.5 | 2026-11-25T20:35:48.502756+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | XLM/USD | 0.127454 | 58.433 | 61.832 | +2.74% | -0.13% | 0.72x | 2.7 | 2026-11-25T20:35:48.502756+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 95.620 | 27.401 | -1.56% | 1.95x |
| 2 | LTC/USD | 81.925 | 42.49 | -0.14% | 1.25x |
| 3 | DRV/USD | 75.023 | 0.34893 | -0.43% | 1.09x |
| 4 | NEAR/USD | 74.826 | 2.9876 | -0.93% | 3.33x |
| 5 | XPL/USD | 71.771 | 0.0473 | -1.25% | 0.53x |
| 6 | HYPE/USD | 70.085 | 61.23 | -0.39% | 1.62x |
| 7 | SUI/USD | 68.947 | 0.6611 | -0.33% | 0.32x |
| 8 | ZEC/USD | 66.945 | 753.81 | -0.27% | 0.59x |
| 9 | LINK/USD | 63.308 | 9.07009 | -0.07% | 1.61x |
| 10 | XMR/USD | 62.968 | 518.14 | -0.04% | 1.08x |
| 11 | XLM/USD | 61.832 | 0.127454 | -0.13% | 0.72x |
| 12 | XBT/USD | 56.982 | 59911.2 | +0.00% | 1.79x |

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

- Persisted scans: 1764; predictions: 14912; observations: 1069320.
- Matured sampled outcomes across 1/6/24/48h: 32654; gap abstentions: 22996. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45696270346 · **Generation:** 1764 · **Legacy run:** 45696270346
**Main quote time:** 2026-11-25T20:35:55.189193+00:00 · **Legacy report time:** 2026-11-25T20:36:56.421976+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 27.401 | 97.36 | -1.56% | 1.95x | MODERATE 69/100 | HIGH 65/100 | Do nothing |
| 2 | NEAR/USD | 2.9876 | 85.16 | -0.93% | 3.33x | MODERATE 68/100 | HIGH 67/100 | Watch |
| 3 | LTC/USD | 42.49 | 83.67 | -0.14% | 1.25x | MODERATE 52/100 | HIGH 68/100 | Watch |
| 4 | HYPE/USD | 61.23 | 74.38 | -0.39% | 1.62x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 5 | DRV/USD | 0.34893 | 73.81 | -0.43% | 1.09x | WEAK 42/100 | VERY_HIGH 74/100 | Watch |
| 6 | LINK/USD | 9.07009 | 69.09 | -0.07% | 1.61x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 7 | XBT/USD | 59911.2 | 64.88 | +0.00% | 1.79x | MODERATE 67/100 | HIGH 55/100 | Watch |
| 8 | XMR/USD | 518.14 | 63.54 | -0.04% | 1.08x | WEAK 42/100 | HIGH 68/100 | Watch |
| 9 | ZEC/USD | 753.81 | 61.51 | -0.27% | 0.59x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 10 | XPL/USD | 0.0473 | 60.79 | -1.25% | 0.53x | WEAK 25/100 | EXTREME 92/100 | Do nothing |
| 11 | SUI/USD | 0.6611 | 60.49 | -0.33% | 0.32x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | XLM/USD | 0.127454 | 58.43 | -0.13% | 0.72x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
