# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T10:11:00.867645+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45011042508
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** cbc968949471f88b8b50b7476c31f3f8b360c39b (atomic ledger/results publication)
**Ledger generation:** 1268 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TAO/USD | 192.6102 | 93.649 | 76.602 | +3.71% | +0.41% | 2.54x | 8.7 | 2026-11-22T10:10:53.344616+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 800.46 | 86.676 | 69.305 | +2.86% | +0.47% | 7.01x | 11.5 | 2026-11-22T10:10:53.344616+00:00 | Not calibrated | STRONG 93/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | SUI/USD | 0.6605 | 86.108 | 67.761 | +2.04% | +0.67% | 6.53x | 3.0 | 2026-11-22T10:10:53.344616+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | PEARL/USD | 2.0287 | 84.915 | 70.260 | +4.13% | +1.46% | 1.74x | 2.5 | 2026-11-22T10:10:53.344616+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | NEAR/USD | 2.9527 | 84.362 | 67.206 | +2.30% | +0.43% | 9.07x | 7.8 | 2026-11-22T10:10:53.344616+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | VVV/USD | 25.356 | 84.025 | 66.833 | +1.83% | +0.44% | 4.69x | 2.0 | 2026-11-22T10:10:53.344616+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | XBT/USD | 60984.5 | 83.452 | 65.413 | +1.49% | +0.61% | 5.09x | 0.0 | 2026-11-22T10:10:53.344616+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | ETH/USD | 1711.92 | 83.446 | 66.428 | +1.76% | +0.40% | 7.92x | 1.8 | 2026-11-22T10:10:53.344616+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | XDG/USD | 0.0555522 | 74.421 | 56.349 | +0.67% | +0.61% | 23.91x | 0.5 | 2026-11-22T10:10:53.344616+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 10 | AVAX/USD | 6.688 | 73.766 | 56.438 | +1.90% | +0.47% | 15.34x | 3.0 | 2026-11-22T10:10:53.344616+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 11 | PUMP/USD | 0.00246 | 72.182 | 68.851 | +4.95% | +1.15% | 0.76x | 16.3 | 2026-11-22T10:10:53.344616+00:00 | Not calibrated | MODERATE 61/100 | HIGH 68/100 | Watch | WATCH |
| 12 | JTO/USD | 0.23843 | 71.726 | 65.427 | +7.17% | +1.59% | 0.84x | 21.5 | 2026-11-22T10:10:53.344616+00:00 | Not calibrated | MODERATE 56/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TAO/USD | 76.602 | 192.6102 | +0.41% | 2.54x |
| 2 | PEARL/USD | 70.260 | 2.0287 | +1.46% | 1.74x |
| 3 | ZEC/USD | 69.305 | 800.46 | +0.47% | 7.01x |
| 4 | PUMP/USD | 68.851 | 0.00246 | +1.15% | 0.76x |
| 5 | SUI/USD | 67.761 | 0.6605 | +0.67% | 6.53x |
| 6 | NEAR/USD | 67.206 | 2.9527 | +0.43% | 9.07x |
| 7 | VVV/USD | 66.833 | 25.356 | +0.44% | 4.69x |
| 8 | ETH/USD | 66.428 | 1711.92 | +0.40% | 7.92x |
| 9 | JTO/USD | 65.427 | 0.23843 | +1.59% | 0.84x |
| 10 | XBT/USD | 65.413 | 60984.5 | +0.61% | 5.09x |
| 11 | AVAX/USD | 56.438 | 6.688 | +0.47% | 15.34x |
| 12 | XDG/USD | 56.349 | 0.0555522 | +0.61% | 23.91x |

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

- Persisted scans: 1268; predictions: 10136; observations: 767321.
- Matured sampled outcomes across 1/6/24/48h: 14585; gap abstentions: 22183. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 59 (sampled only; not a success-rate estimate).
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

**Writer:** 45011042508 · **Generation:** 1268 · **Legacy run:** 45011042508
**Main quote time:** 2026-11-22T10:11:00.867645+00:00 · **Legacy report time:** 2026-11-22T10:11:42.904677+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD ⭐ | 192.6102 | 93.65 | +0.41% | 2.54x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 800.46 | 86.68 | +0.47% | 7.01x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | SUI/USD ⭐ | 0.6605 | 86.11 | +0.67% | 6.53x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | PEARL/USD ⭐ | 2.0287 | 84.91 | +1.46% | 1.74x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 5 | NEAR/USD ⭐ | 2.9527 | 84.36 | +0.43% | 9.07x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | VVV/USD | 25.356 | 84.03 | +0.44% | 4.69x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 7 | XBT/USD | 60984.5 | 83.45 | +0.61% | 5.09x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 8 | ETH/USD ⭐ | 1711.92 | 83.45 | +0.40% | 7.92x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | XDG/USD | 0.0555522 | 74.42 | +0.61% | 23.91x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 10 | AVAX/USD | 6.688 | 73.77 | +0.47% | 15.34x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 11 | PUMP/USD | 0.00246 | 72.18 | +1.15% | 0.76x | MODERATE 61/100 | HIGH 68/100 | Watch |
| 12 | JTO/USD | 0.23843 | 71.73 | +1.59% | 0.84x | MODERATE 56/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD ⭐ | 192.2803 | 87.18 | +0.41% | 2.54x | 7277 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | PEARL/USD ⭐ | 2.0287 | 85.10 | +1.46% | 1.74x | 8239 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 3 | SUI/USD ⭐ | 0.6604 | 83.27 | +0.67% | 6.53x | 7657 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | ZEC/USD ⭐ | 801.08 | 82.26 | +0.47% | 7.01x | 27868 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | ETH/USD ⭐ | 1711.06 | 80.69 | +0.40% | 7.92x | 46051 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | HYPE/USD | 62.25 | 78.90 | +0.77% | 21.66x | 14143 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 7 | ENA/USD | 0.1018 | 78.38 | +1.09% | 14.15x | 2441 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 8 | NEAR/USD ⭐ | 2.946 | 77.97 | +0.43% | 9.07x | 12568 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | RENDER/USD | 1.351 | 74.92 | +1.04% | 1.64x | 3575 | STRONG 77/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** TAO/USD, ZEC/USD, SUI/USD, PEARL/USD, NEAR/USD, ETH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
