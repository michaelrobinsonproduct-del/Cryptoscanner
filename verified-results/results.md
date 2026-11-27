# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T14:31:57.918612+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46016400657
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 907ccdc475482687039efce282f51656d768e940 (atomic ledger/results publication)
**Ledger generation:** 2020 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 604; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 744.15 | 86.495 | 92.204 | +9.17% | -0.52% | 0.69x | 15.6 | 2026-11-27T14:31:51.019324+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | UNI/USD | 4.8469 | 83.933 | 72.333 | +4.23% | -0.68% | 3.05x | 5.8 | 2026-11-27T14:31:51.019324+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XDG/USD | 0.0581454 | 78.688 | 66.051 | +3.14% | -0.47% | 4.50x | 6.3 | 2026-11-27T14:31:51.019324+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XRP/USD | 0.95732 | 76.688 | 65.766 | +1.55% | -0.19% | 2.19x | 0.1 | 2026-11-27T14:31:51.019324+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ENA/USD | 0.1048 | 72.219 | 62.848 | +4.38% | -1.13% | 2.95x | 9.5 | 2026-11-27T14:31:51.019324+00:00 | Not calibrated | MODERATE 66/100 | HIGH 65/100 | Watch | WATCH |
| 6 | HYPE/USD | 64.88 | 71.399 | 83.387 | +4.28% | -0.86% | 0.23x | 3.1 | 2026-11-27T14:31:51.019324+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | PAXG/USD | 3621.96 | 68.767 | 53.357 | +1.83% | +0.08% | 4.22x | 1.5 | 2026-11-27T14:31:51.019324+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 8 | ETH/USD | 1709.64 | 68.082 | 61.594 | +1.30% | -0.08% | 1.69x | 5.0 | 2026-11-27T14:31:51.019324+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 9 | XAUT/USD | 3628.7 | 65.402 | 49.713 | +1.94% | +0.14% | 91.70x | 0.8 | 2026-11-27T14:31:51.019324+00:00 | Not calibrated | STRONG 78/100 | HIGH 60/100 | Watch | WATCH |
| 10 | SOL/USD | 72.49 | 65.274 | 69.605 | +2.18% | -0.27% | 0.70x | 1.4 | 2026-11-27T14:31:51.019324+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XBT/USD | 60990.8 | 63.468 | 60.694 | +0.81% | -0.12% | 1.34x | 0.0 | 2026-11-27T14:31:51.019324+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 12 | NIGHT/USD | 0.04924 | 59.654 | 62.196 | +1.59% | +0.53% | 0.48x | 2.0 | 2026-11-27T14:31:51.019324+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 92.204 | 744.15 | -0.52% | 0.69x |
| 2 | HYPE/USD | 83.387 | 64.88 | -0.86% | 0.23x |
| 3 | UNI/USD | 72.333 | 4.8469 | -0.68% | 3.05x |
| 4 | SOL/USD | 69.605 | 72.49 | -0.27% | 0.70x |
| 5 | XDG/USD | 66.051 | 0.0581454 | -0.47% | 4.50x |
| 6 | XRP/USD | 65.766 | 0.95732 | -0.19% | 2.19x |
| 7 | ENA/USD | 62.848 | 0.1048 | -1.13% | 2.95x |
| 8 | NIGHT/USD | 62.196 | 0.04924 | +0.53% | 0.48x |
| 9 | ETH/USD | 61.594 | 1709.64 | -0.08% | 1.69x |
| 10 | XBT/USD | 60.694 | 60990.8 | -0.12% | 1.34x |
| 11 | PAXG/USD | 53.357 | 3621.96 | +0.08% | 4.22x |
| 12 | XAUT/USD | 49.713 | 3628.7 | +0.14% | 91.70x |

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

- Persisted scans: 2020; predictions: 17942; observations: 1223212.
- Matured sampled outcomes across 1/6/24/48h: 40049; gap abstentions: 25899. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46016400657 · **Generation:** 2020 · **Legacy run:** 46016400657
**Main quote time:** 2026-11-27T14:31:57.918612+00:00 · **Legacy report time:** 2026-11-27T14:32:31.968276+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 744.15 | 86.50 | -0.52% | 0.69x | WEAK 43/100 | VERY_HIGH 82/100 | Watch |
| 2 | UNI/USD | 4.8469 | 83.93 | -0.68% | 3.05x | STRONG 72/100 | HIGH 61/100 | Watch |
| 3 | XDG/USD | 0.0581454 | 78.69 | -0.47% | 4.50x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 4 | XRP/USD | 0.95732 | 76.69 | -0.19% | 2.19x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 5 | ENA/USD | 0.1048 | 72.22 | -1.13% | 2.95x | MODERATE 66/100 | HIGH 65/100 | Watch |
| 6 | HYPE/USD | 64.88 | 71.40 | -0.86% | 0.23x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 7 | PAXG/USD ⭐ | 3621.96 | 68.77 | +0.08% | 4.22x | STRONG 89/100 | HIGH 55/100 | Watch |
| 8 | ETH/USD | 1709.64 | 68.08 | -0.08% | 1.69x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 9 | XAUT/USD | 3628.7 | 65.40 | +0.14% | 91.70x | STRONG 78/100 | HIGH 60/100 | Watch |
| 10 | SOL/USD | 72.49 | 65.27 | -0.27% | 0.70x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 11 | XBT/USD | 60990.8 | 63.47 | -0.12% | 1.34x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 12 | NIGHT/USD | 0.04924 | 59.65 | +0.53% | 0.48x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PAXG/USD ⭐ | 3625.52 | 72.55 | +0.08% | 4.22x | 3502 | STRONG 91/100 | HIGH 55/100 | Watch |

**Same-run overlap:** PAXG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
