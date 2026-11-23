# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T19:42:28.889003+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45251222319
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** abddaa9fceab90f1ae12ca17bdca1ac8b6f232e6 (atomic ledger/results publication)
**Ledger generation:** 1473 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ALGO/USD | 0.08214 | 100.761 | 90.672 | +8.90% | -0.36% | 2.19x | 6.1 | 2026-11-23T19:42:20.018786+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | QNT/USD | 158.04 | 90.685 | 96.832 | +10.18% | -0.94% | 0.85x | 6.3 | 2026-11-23T19:42:20.018786+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 3 | ATOM/USD | 1.2487 | 87.222 | 72.862 | +6.54% | -0.13% | 3.08x | 9.6 | 2026-11-23T19:42:20.018786+00:00 | Not calibrated | STRONG 74/100 | HIGH 66/100 | Watch | WATCH |
| 4 | SUI/USD | 0.6738 | 81.558 | 72.838 | +2.76% | -1.26% | 2.66x | 3.0 | 2026-11-23T19:42:20.018786+00:00 | Not calibrated | STRONG 71/100 | HIGH 65/100 | Do nothing | WATCH |
| 5 | KAS/USD | 0.02738 | 81.114 | 71.430 | +6.08% | -0.15% | 2.04x | 14.6 | 2026-11-23T19:42:20.018786+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0564133 | 79.199 | 69.018 | +2.04% | -0.96% | 5.33x | 0.6 | 2026-11-23T19:42:20.018786+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 7 | JUP/USD | 0.23838 | 76.483 | 74.665 | +6.15% | -0.70% | 1.53x | 8.9 | 2026-11-23T19:42:20.018786+00:00 | Not calibrated | MODERATE 58/100 | HIGH 66/100 | Watch | WATCH |
| 8 | INJ/USD | 6.484 | 75.887 | 79.301 | +4.11% | -1.52% | 1.42x | 4.6 | 2026-11-23T19:42:20.018786+00:00 | Not calibrated | MODERATE 58/100 | HIGH 65/100 | Do nothing | WATCH |
| 9 | SHX/USD | 0.003681 | 70.969 | 70.844 | +9.07% | -1.00% | 1.51x | 10.9 | 2026-11-23T19:42:20.018786+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 83/100 | Watch | WATCH |
| 10 | LTC/USD | 41.23 | 68.683 | 71.224 | +2.66% | -1.01% | 1.25x | 4.9 | 2026-11-23T19:42:20.018786+00:00 | Not calibrated | WEAK 44/100 | HIGH 65/100 | Watch | WATCH |
| 11 | HYPE/USD | 64.1 | 66.939 | 65.764 | +1.65% | -0.83% | 1.53x | 1.6 | 2026-11-23T19:42:20.018786+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 12 | SOL/USD | 72.41 | 65.521 | 71.951 | +2.52% | -1.04% | 0.88x | 1.4 | 2026-11-23T19:42:20.018786+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 72/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 96.832 | 158.04 | -0.94% | 0.85x |
| 2 | ALGO/USD | 90.672 | 0.08214 | -0.36% | 2.19x |
| 3 | INJ/USD | 79.301 | 6.484 | -1.52% | 1.42x |
| 4 | JUP/USD | 74.665 | 0.23838 | -0.70% | 1.53x |
| 5 | ATOM/USD | 72.862 | 1.2487 | -0.13% | 3.08x |
| 6 | SUI/USD | 72.838 | 0.6738 | -1.26% | 2.66x |
| 7 | SOL/USD | 71.951 | 72.41 | -1.04% | 0.88x |
| 8 | KAS/USD | 71.430 | 0.02738 | -0.15% | 2.04x |
| 9 | LTC/USD | 71.224 | 41.23 | -1.01% | 1.25x |
| 10 | SHX/USD | 70.844 | 0.003681 | -1.00% | 1.51x |
| 11 | XDG/USD | 69.018 | 0.0564133 | -0.96% | 5.33x |
| 12 | HYPE/USD | 65.764 | 64.1 | -0.83% | 1.53x |

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

- Persisted scans: 1473; predictions: 12443; observations: 892159.
- Matured sampled outcomes across 1/6/24/48h: 22048; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45251222319 · **Generation:** 1473 · **Legacy run:** 45251222319
**Main quote time:** 2026-11-23T19:42:28.889003+00:00 · **Legacy report time:** 2026-11-23T19:43:19.820409+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD | 0.08214 | 100.76 | -0.36% | 2.19x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | QNT/USD | 158.04 | 90.69 | -0.94% | 0.85x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 3 | ATOM/USD | 1.2487 | 87.22 | -0.13% | 3.08x | STRONG 74/100 | HIGH 66/100 | Watch |
| 4 | SUI/USD | 0.6738 | 81.56 | -1.26% | 2.66x | STRONG 71/100 | HIGH 65/100 | Do nothing |
| 5 | KAS/USD | 0.02738 | 81.11 | -0.15% | 2.04x | MODERATE 66/100 | VERY_HIGH 72/100 | Watch |
| 6 | XDG/USD | 0.0564133 | 79.20 | -0.96% | 5.33x | STRONG 70/100 | HIGH 61/100 | Watch |
| 7 | JUP/USD | 0.23838 | 76.48 | -0.70% | 1.53x | MODERATE 58/100 | HIGH 66/100 | Watch |
| 8 | INJ/USD | 6.484 | 75.89 | -1.52% | 1.42x | MODERATE 58/100 | HIGH 65/100 | Do nothing |
| 9 | SHX/USD | 0.003681 | 70.97 | -1.00% | 1.51x | MODERATE 50/100 | VERY_HIGH 83/100 | Watch |
| 10 | LTC/USD | 41.23 | 68.68 | -1.01% | 1.25x | WEAK 44/100 | HIGH 65/100 | Watch |
| 11 | HYPE/USD | 64.1 | 66.94 | -0.83% | 1.53x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 12 | SOL/USD | 72.41 | 65.52 | -1.04% | 0.88x | WEAK 38/100 | VERY_HIGH 72/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CAP/USD | 0.105514 | 76.62 | +0.25% | 1.91x | 6002 | STRONG 73/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
