# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T00:45:27.243048+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44845820357
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** fb0b30d5647f730679bc2e806c9ff79f6edd9732 (atomic ledger/results publication)
**Ledger generation:** 1048 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEARL/USD | 1.888 | 73.612 | 62.262 | +3.27% | +2.23% | 1.02x | 19.1 | 2026-11-21T00:45:20.259541+00:00 | Not calibrated | MODERATE 67/100 | HIGH 68/100 | Watch | WATCH |
| 2 | BLESS/USD | 0.014254 | 62.912 | 39.603 | +3.50% | +1.66% | 3.02x | 41.0 | 2026-11-21T00:45:20.259541+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | AKT/USD | 0.5088 | 56.592 | 38.626 | +0.97% | +0.59% | 2.80x | 2.0 | 2026-11-21T00:45:20.259541+00:00 | Not calibrated | STRONG 83/100 | HIGH 60/100 | Watch | WATCH |
| 4 | DRV/USD | 0.24773 | 55.774 | 40.408 | +0.89% | +0.36% | 2.36x | 2.4 | 2026-11-21T00:45:20.259541+00:00 | Not calibrated | STRONG 83/100 | HIGH 60/100 | Watch | WATCH |
| 5 | PIEVERSE/USD | 3.0301 | 55.419 | 36.712 | +1.05% | +0.74% | 2.78x | 10.9 | 2026-11-21T00:45:20.259541+00:00 | Not calibrated | STRONG 78/100 | HIGH 66/100 | Watch | WATCH |
| 6 | XBT/USD | 58957.9 | 54.478 | 56.795 | +0.26% | +0.03% | 0.75x | 0.0 | 2026-11-21T00:45:20.259541+00:00 | Not calibrated | MODERATE 47/100 | HIGH 62/100 | Watch | WATCH |
| 7 | AKE/USD | 0.0061751 | 48.240 | 53.078 | +1.05% | +0.23% | 0.40x | 18.5 | 2026-11-21T00:45:20.259541+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | ZBCN/USD | 0.001604 | 45.627 | 28.436 | +0.82% | +0.44% | 5.35x | 18.8 | 2026-11-21T00:45:20.259541+00:00 | Not calibrated | STRONG 73/100 | HIGH 66/100 | Watch | WATCH |
| 9 | CAP/USD | 0.092002 | 38.595 | 32.359 | +0.50% | -0.04% | 1.64x | 7.7 | 2026-11-21T00:45:20.259541+00:00 | Not calibrated | WEAK 39/100 | HIGH 66/100 | Watch | WATCH |
| 10 | CT/USD | 0.1222 | 30.817 | 30.060 | +0.91% | +1.08% | 0.54x | 16.4 | 2026-11-21T00:45:20.259541+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 11 | BLUR/USD | 0.00732 | 20.456 | 20.229 | +0.27% | -0.14% | 1.09x | 27.3 | 2026-11-21T00:45:20.259541+00:00 | Not calibrated | WEAK 10/100 | EXTREME 85/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 62.262 | 1.888 | +2.23% | 1.02x |
| 2 | XBT/USD | 56.795 | 58957.9 | +0.03% | 0.75x |
| 3 | AKE/USD | 53.078 | 0.0061751 | +0.23% | 0.40x |
| 4 | DRV/USD | 40.408 | 0.24773 | +0.36% | 2.36x |
| 5 | BLESS/USD | 39.603 | 0.014254 | +1.66% | 3.02x |
| 6 | AKT/USD | 38.626 | 0.5088 | +0.59% | 2.80x |
| 7 | PIEVERSE/USD | 36.712 | 3.0301 | +0.74% | 2.78x |
| 8 | CAP/USD | 32.359 | 0.092002 | -0.04% | 1.64x |
| 9 | CT/USD | 30.060 | 0.1222 | +1.08% | 0.54x |
| 10 | ZBCN/USD | 28.436 | 0.001604 | +0.44% | 5.35x |
| 11 | BLUR/USD | 20.229 | 0.00732 | -0.14% | 1.09x |

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

- Persisted scans: 1048; predictions: 8384; observations: 633544.
- Matured sampled outcomes across 1/6/24/48h: 10930; gap abstentions: 19047. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44845820357 · **Generation:** 1048 · **Legacy run:** 44845820357
**Main quote time:** 2026-11-21T00:45:27.243048+00:00 · **Legacy report time:** 2026-11-21T00:46:16.703505+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 1.888 | 73.61 | +2.23% | 1.02x | STRONG 77/100 | HIGH 68/100 | Watch |
| 2 | BLESS/USD ⭐ | 0.014254 | 62.91 | +1.66% | 3.02x | STRONG 81/100 | VERY_HIGH 82/100 | Watch |
| 3 | AKT/USD ⭐ | 0.5088 | 56.59 | +0.59% | 2.80x | STRONG 93/100 | HIGH 60/100 | Consider small entry |
| 4 | DRV/USD ⭐ | 0.24773 | 55.77 | +0.36% | 2.36x | STRONG 93/100 | HIGH 60/100 | Consider small entry |
| 5 | PIEVERSE/USD ⭐ | 3.0301 | 55.42 | +0.74% | 2.78x | STRONG 88/100 | HIGH 66/100 | Consider small entry |
| 6 | XBT/USD | 58957.9 | 54.48 | +0.03% | 0.75x | MODERATE 47/100 | HIGH 62/100 | Watch |
| 7 | AKE/USD | 0.0061751 | 48.24 | +0.23% | 0.40x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |
| 8 | ZBCN/USD | 0.001604 | 45.63 | +0.44% | 5.35x | STRONG 73/100 | HIGH 66/100 | Watch |
| 9 | CAP/USD | 0.092002 | 38.59 | -0.04% | 1.64x | WEAK 39/100 | HIGH 66/100 | Watch |
| 10 | CT/USD | 0.1222 | 30.82 | +1.08% | 0.54x | WEAK 40/100 | VERY_HIGH 81/100 | Watch |
| 11 | BLUR/USD | 0.00732 | 20.46 | -0.14% | 1.09x | WEAK 10/100 | EXTREME 85/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 1.895 | 83.99 | +2.23% | 1.02x | 22002 | STRONG 82/100 | HIGH 68/100 | Watch |
| 2 | BLESS/USD ⭐ | 0.014176 | 72.63 | +1.66% | 3.02x | 2531 | STRONG 86/100 | VERY_HIGH 82/100 | Watch |
| 3 | PIEVERSE/USD ⭐ | 3.0301 | 46.80 | +0.74% | 2.78x | 2724 | STRONG 88/100 | HIGH 60/100 | Consider small entry |
| 4 | UNI/USD | 4.4781 | 45.28 | +0.45% | 1.04x | 9181 | MODERATE 58/100 | HIGH 62/100 | Watch |
| 5 | AKT/USD ⭐ | 0.5088 | 44.33 | +0.59% | 2.80x | 4550 | STRONG 87/100 | HIGH 60/100 | Consider small entry |
| 6 | DRV/USD ⭐ | 0.24773 | 43.70 | +0.36% | 2.36x | 5978 | STRONG 87/100 | HIGH 60/100 | Consider small entry |
| 7 | NIGHT/USD | 0.04227 | 33.79 | +0.09% | 1.12x | 13536 | WEAK 42/100 | HIGH 62/100 | Watch |

**Same-run overlap:** PEARL/USD, BLESS/USD, AKT/USD, DRV/USD, PIEVERSE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
