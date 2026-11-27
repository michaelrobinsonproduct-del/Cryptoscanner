# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T16:02:09.819723+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46029721999
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 164f75fb4a15d42b1520a19f2163a029f2eaeaf5 (atomic ledger/results publication)
**Ledger generation:** 2029 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 739.33 | 88.572 | 94.926 | +8.46% | -0.32% | 0.52x | 10.1 | 2026-11-27T16:02:01.059810+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | UNI/USD | 4.7678 | 71.317 | 67.296 | +2.53% | -0.11% | 1.46x | 7.8 | 2026-11-27T16:02:01.059810+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LINK/USD | 9.32066 | 69.438 | 56.230 | +0.56% | -0.36% | 2.76x | 5.4 | 2026-11-27T16:02:01.059810+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SPACE/USD | 0.004138 | 67.498 | 68.430 | +6.87% | -0.19% | 1.00x | 14.5 | 2026-11-27T16:02:01.059810+00:00 | Not calibrated | WEAK 39/100 | EXTREME 86/100 | Do nothing | WATCH |
| 5 | HYPE/USD | 64.13 | 65.448 | 75.710 | +3.07% | -0.42% | 0.18x | 1.6 | 2026-11-27T16:02:01.059810+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0576242 | 61.805 | 69.875 | +2.22% | -0.20% | 0.30x | 1.3 | 2026-11-27T16:02:01.059810+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | VVV/USD | 26.929 | 61.747 | 65.117 | +2.85% | -0.69% | 1.01x | 12.2 | 2026-11-27T16:02:01.059810+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 8 | PAXG/USD | 3607.29 | 57.269 | 52.909 | +1.42% | -0.09% | 1.48x | 0.4 | 2026-11-27T16:02:01.059810+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |
| 9 | XRP/USD | 0.95158 | 57.183 | 60.821 | +0.94% | +0.15% | 0.56x | 1.5 | 2026-11-27T16:02:01.059810+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SOL/USD | 71.99 | 57.153 | 64.666 | +1.48% | +0.03% | 0.23x | 1.4 | 2026-11-27T16:02:01.059810+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | SUI/USD | 0.6696 | 53.275 | 55.499 | +0.28% | -0.21% | 0.88x | 3.0 | 2026-11-27T16:02:01.059810+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | TAO/USD | 184.6797 | 47.785 | 50.050 | +0.49% | -0.30% | 0.92x | 7.7 | 2026-11-27T16:02:01.059810+00:00 | Not calibrated | WEAK 29/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 94.926 | 739.33 | -0.32% | 0.52x |
| 2 | HYPE/USD | 75.710 | 64.13 | -0.42% | 0.18x |
| 3 | XDG/USD | 69.875 | 0.0576242 | -0.20% | 0.30x |
| 4 | SPACE/USD | 68.430 | 0.004138 | -0.19% | 1.00x |
| 5 | UNI/USD | 67.296 | 4.7678 | -0.11% | 1.46x |
| 6 | VVV/USD | 65.117 | 26.929 | -0.69% | 1.01x |
| 7 | SOL/USD | 64.666 | 71.99 | +0.03% | 0.23x |
| 8 | XRP/USD | 60.821 | 0.95158 | +0.15% | 0.56x |
| 9 | LINK/USD | 56.230 | 9.32066 | -0.36% | 2.76x |
| 10 | SUI/USD | 55.499 | 0.6696 | -0.21% | 0.88x |
| 11 | PAXG/USD | 52.909 | 3607.29 | -0.09% | 1.48x |
| 12 | TAO/USD | 50.050 | 184.6797 | -0.30% | 0.92x |

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

- Persisted scans: 2029; predictions: 18050; observations: 1228654.
- Matured sampled outcomes across 1/6/24/48h: 40373; gap abstentions: 25951. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 46029721999 · **Generation:** 2029 · **Legacy run:** 46029721999
**Main quote time:** 2026-11-27T16:02:09.819723+00:00 · **Legacy report time:** 2026-11-27T16:02:54.383923+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 739.33 | 88.57 | -0.32% | 0.52x | WEAK 44/100 | VERY_HIGH 82/100 | Watch |
| 2 | UNI/USD | 4.7678 | 71.32 | -0.11% | 1.46x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 3 | LINK/USD | 9.32066 | 69.44 | -0.36% | 2.76x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 4 | SPACE/USD | 0.004138 | 67.50 | -0.19% | 1.00x | WEAK 39/100 | EXTREME 86/100 | Do nothing |
| 5 | HYPE/USD | 64.13 | 65.45 | -0.42% | 0.18x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 6 | XDG/USD | 0.0576242 | 61.81 | -0.20% | 0.30x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 7 | VVV/USD | 26.929 | 61.75 | -0.69% | 1.01x | WEAK 36/100 | VERY_HIGH 74/100 | Watch |
| 8 | PAXG/USD | 3607.29 | 57.27 | -0.09% | 1.48x | MODERATE 49/100 | HIGH 61/100 | Watch |
| 9 | XRP/USD | 0.95158 | 57.18 | +0.15% | 0.56x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 10 | SOL/USD | 71.99 | 57.15 | +0.03% | 0.23x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 11 | SUI/USD | 0.6696 | 53.27 | -0.21% | 0.88x | WEAK 32/100 | HIGH 68/100 | Do nothing |
| 12 | TAO/USD | 184.6797 | 47.79 | -0.30% | 0.92x | WEAK 29/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MOODENG/USD | 0.02973 | 60.87 | +0.61% | 1.10x | 1190 | MODERATE 60/100 | VERY_HIGH 80/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
