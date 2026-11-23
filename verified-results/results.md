# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T23:32:10.646180+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45289264228
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c47fb4e080017ba7cb3894f8d3f3f9bd449d84a5 (atomic ledger/results publication)
**Ledger generation:** 1496 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 154.8 | 90.309 | 95.478 | +7.92% | -0.44% | 0.70x | 9.0 | 2026-11-23T23:32:02.082515+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | LTC/USD | 41.37 | 89.883 | 73.672 | +3.01% | +0.24% | 4.62x | 4.8 | 2026-11-23T23:32:02.082515+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ALGO/USD | 0.0814 | 87.948 | 91.975 | +7.91% | +0.35% | 0.42x | 6.1 | 2026-11-23T23:32:02.082515+00:00 | Not calibrated | STRONG 74/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | SUI/USD | 0.6726 | 82.325 | 71.554 | +2.58% | +0.52% | 1.82x | 3.0 | 2026-11-23T23:32:02.082515+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | SOL/USD | 72.11 | 77.591 | 68.975 | +2.10% | +0.28% | 1.72x | 1.4 | 2026-11-23T23:32:02.082515+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | CAP/USD | 0.100817 | 73.026 | 76.038 | +7.74% | -0.77% | 1.09x | 6.2 | 2026-11-23T23:32:02.082515+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | XRP/USD | 0.94213 | 71.725 | 65.958 | +1.57% | +0.10% | 1.53x | 0.1 | 2026-11-23T23:32:02.082515+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 8 | ATOM/USD | 1.2715 | 68.892 | 71.508 | +8.49% | +0.13% | 0.68x | 13.4 | 2026-11-23T23:32:02.082515+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 9 | SHX/USD | 0.0036 | 68.347 | 72.187 | +6.67% | -0.08% | 0.66x | 8.3 | 2026-11-23T23:32:02.082515+00:00 | Not calibrated | WEAK 39/100 | EXTREME 88/100 | Do nothing | WATCH |
| 10 | XDG/USD | 0.0563967 | 62.331 | 68.888 | +2.01% | +0.27% | 0.21x | 0.4 | 2026-11-23T23:32:02.082515+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XBT/USD | 61460.7 | 57.508 | 58.317 | +0.48% | +0.14% | 0.85x | 0.0 | 2026-11-23T23:32:02.082515+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 12 | DOT/USD | 0.6746 | 47.140 | 48.905 | +2.09% | +0.28% | 0.68x | 1.5 | 2026-11-23T23:32:02.082515+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 95.478 | 154.8 | -0.44% | 0.70x |
| 2 | ALGO/USD | 91.975 | 0.0814 | +0.35% | 0.42x |
| 3 | CAP/USD | 76.038 | 0.100817 | -0.77% | 1.09x |
| 4 | LTC/USD | 73.672 | 41.37 | +0.24% | 4.62x |
| 5 | SHX/USD | 72.187 | 0.0036 | -0.08% | 0.66x |
| 6 | SUI/USD | 71.554 | 0.6726 | +0.52% | 1.82x |
| 7 | ATOM/USD | 71.508 | 1.2715 | +0.13% | 0.68x |
| 8 | SOL/USD | 68.975 | 72.11 | +0.28% | 1.72x |
| 9 | XDG/USD | 68.888 | 0.0563967 | +0.27% | 0.21x |
| 10 | XRP/USD | 65.958 | 0.94213 | +0.10% | 1.53x |
| 11 | XBT/USD | 58.317 | 61460.7 | +0.14% | 0.85x |
| 12 | DOT/USD | 48.905 | 0.6746 | +0.28% | 0.68x |

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

- Persisted scans: 1496; predictions: 12719; observations: 906166.
- Matured sampled outcomes across 1/6/24/48h: 23176; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45289264228 · **Generation:** 1496 · **Legacy run:** 45289264228
**Main quote time:** 2026-11-23T23:32:10.646180+00:00 · **Legacy report time:** 2026-11-23T23:32:58.447123+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 154.8 | 90.31 | -0.44% | 0.70x | MODERATE 50/100 | VERY_HIGH 76/100 | Watch |
| 2 | LTC/USD ⭐ | 41.37 | 89.88 | +0.24% | 4.62x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ALGO/USD | 0.0814 | 87.95 | +0.35% | 0.42x | STRONG 74/100 | VERY_HIGH 70/100 | Watch |
| 4 | SUI/USD ⭐ | 0.6726 | 82.32 | +0.52% | 1.82x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 5 | SOL/USD ⭐ | 72.11 | 77.59 | +0.28% | 1.72x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 6 | CAP/USD | 0.100817 | 73.03 | -0.77% | 1.09x | MODERATE 47/100 | VERY_HIGH 73/100 | Watch |
| 7 | XRP/USD | 0.94213 | 71.72 | +0.10% | 1.53x | STRONG 71/100 | HIGH 55/100 | Watch |
| 8 | ATOM/USD | 1.2715 | 68.89 | +0.13% | 0.68x | MODERATE 49/100 | VERY_HIGH 81/100 | Watch |
| 9 | SHX/USD | 0.0036 | 68.35 | -0.08% | 0.66x | WEAK 39/100 | EXTREME 88/100 | Do nothing |
| 10 | XDG/USD | 0.0563967 | 62.33 | +0.27% | 0.21x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 11 | XBT/USD | 61460.7 | 57.51 | +0.14% | 0.85x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 12 | DOT/USD | 0.6746 | 47.14 | +0.28% | 0.68x | MODERATE 54/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD | 2.3232 | 96.43 | +1.14% | 3.37x | 16259 | STRONG 98/100 | HIGH 61/100 | Consider small entry |
| 2 | LTC/USD ⭐ | 41.35 | 91.45 | +0.24% | 4.62x | 12797 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SUI/USD ⭐ | 0.6726 | 84.78 | +0.52% | 1.82x | 12385 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 4 | SOL/USD ⭐ | 72.03 | 76.73 | +0.28% | 1.72x | 45899 | STRONG 93/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** LTC/USD, SUI/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
