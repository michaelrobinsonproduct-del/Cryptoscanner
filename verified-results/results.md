# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T22:52:40.203420+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46078949219
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 5d42612e4a4d1e40cacc0ee3e536cf9b3402aabb (atomic ledger/results publication)
**Ledger generation:** 2071 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 728.3 | 105.170 | 98.420 | +6.84% | +0.59% | 1.38x | 3.2 | 2026-11-27T22:52:34.324927+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.05013 | 74.681 | 76.978 | +3.42% | +0.36% | 0.59x | 4.0 | 2026-11-27T22:52:34.324927+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | UNI/USD | 4.8076 | 73.162 | 73.474 | +3.39% | -0.15% | 1.04x | 4.0 | 2026-11-27T22:52:34.324927+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 4 | WIF/USD | 0.1423 | 66.749 | 60.227 | +4.63% | +1.21% | 1.05x | 7.0 | 2026-11-27T22:52:34.324927+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 5 | LTC/USD | 44.43 | 64.993 | 64.809 | +1.58% | +0.29% | 0.87x | 2.3 | 2026-11-27T22:52:34.324927+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 6 | SPACE/USD | 0.004137 | 64.941 | 69.762 | +6.84% | +0.12% | 0.46x | 12.1 | 2026-11-27T22:52:34.324927+00:00 | Not calibrated | MODERATE 47/100 | EXTREME 88/100 | Do nothing | WATCH |
| 7 | XDG/USD | 0.0573999 | 63.074 | 67.724 | +1.82% | +0.18% | 0.45x | 0.0 | 2026-11-27T22:52:34.324927+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | HYPE/USD | 63.65 | 62.254 | 70.302 | +2.30% | +0.20% | 0.09x | 1.6 | 2026-11-27T22:52:34.324927+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | PAXG/USD | 3647.22 | 58.425 | 62.101 | +2.54% | +0.00% | 0.63x | 0.0 | 2026-11-27T22:52:34.324927+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XRP/USD | 0.94519 | 57.647 | 56.759 | +0.26% | +0.15% | 1.01x | 0.1 | 2026-11-27T22:52:34.324927+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 11 | SOL/USD | 71.5 | 55.846 | 59.826 | +0.79% | +0.10% | 0.55x | 1.4 | 2026-11-27T22:52:34.324927+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | PEPE/USD | 3.534e-06 | 50.042 | 55.201 | +1.61% | +0.23% | 0.37x | 2.8 | 2026-11-27T22:52:34.324927+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.420 | 728.3 | +0.59% | 1.38x |
| 2 | NIGHT/USD | 76.978 | 0.05013 | +0.36% | 0.59x |
| 3 | UNI/USD | 73.474 | 4.8076 | -0.15% | 1.04x |
| 4 | HYPE/USD | 70.302 | 63.65 | +0.20% | 0.09x |
| 5 | SPACE/USD | 69.762 | 0.004137 | +0.12% | 0.46x |
| 6 | XDG/USD | 67.724 | 0.0573999 | +0.18% | 0.45x |
| 7 | LTC/USD | 64.809 | 44.43 | +0.29% | 0.87x |
| 8 | PAXG/USD | 62.101 | 3647.22 | +0.00% | 0.63x |
| 9 | WIF/USD | 60.227 | 0.1423 | +1.21% | 1.05x |
| 10 | SOL/USD | 59.826 | 71.5 | +0.10% | 0.55x |
| 11 | XRP/USD | 56.759 | 0.94519 | +0.15% | 1.01x |
| 12 | PEPE/USD | 55.201 | 3.534e-06 | +0.23% | 0.37x |

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

- Persisted scans: 2071; predictions: 18554; observations: 1254074.
- Matured sampled outcomes across 1/6/24/48h: 42287; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 154 (sampled only; not a success-rate estimate).
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

**Writer:** 46078949219 · **Generation:** 2071 · **Legacy run:** 46078949219
**Main quote time:** 2026-11-27T22:52:40.203420+00:00 · **Legacy report time:** 2026-11-27T22:53:35.472236+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 728.3 | 105.17 | +0.59% | 1.38x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | NIGHT/USD | 0.05013 | 74.68 | +0.36% | 0.59x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 3 | UNI/USD | 4.8076 | 73.16 | -0.15% | 1.04x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 4 | WIF/USD | 0.1423 | 66.75 | +1.21% | 1.05x | MODERATE 68/100 | VERY_HIGH 74/100 | Watch |
| 5 | LTC/USD | 44.43 | 64.99 | +0.29% | 0.87x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 6 | SPACE/USD | 0.004137 | 64.94 | +0.12% | 0.46x | MODERATE 47/100 | EXTREME 88/100 | Do nothing |
| 7 | XDG/USD | 0.0573999 | 63.07 | +0.18% | 0.45x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 8 | HYPE/USD | 63.65 | 62.25 | +0.20% | 0.09x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 9 | PAXG/USD | 3647.22 | 58.42 | +0.00% | 0.63x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 10 | XRP/USD | 0.94519 | 57.65 | +0.15% | 1.01x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 11 | SOL/USD | 71.5 | 55.85 | +0.10% | 0.55x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 12 | PEPE/USD | 3.534e-06 | 50.04 | +0.23% | 0.37x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 727.97 | 100.00 | +0.59% | 1.38x | 37080 | STRONG 100/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
