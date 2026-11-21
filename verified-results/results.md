# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T22:01:07.246803+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44954359299
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 9e0351a5eb12c49923cb1ea6333662315a7f5fbc (atomic ledger/results publication)
**Ledger generation:** 1192 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 789.87 | 98.395 | 84.455 | +4.22% | -0.21% | 5.44x | 0.1 | 2026-11-21T22:01:00.829267+00:00 | Not calibrated | STRONG 79/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XMR/USD | 492 | 92.957 | 96.642 | +7.83% | +0.13% | 0.57x | 6.7 | 2026-11-21T22:01:00.829267+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | UNI/USD | 4.7263 | 88.183 | 92.530 | +5.80% | +0.17% | 0.48x | 6.1 | 2026-11-21T22:01:00.829267+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | WINGS/USD | 0.001889 | 84.981 | 76.939 | +7.82% | +2.44% | 0.58x | 5.3 | 2026-11-21T22:01:00.829267+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 5 | ETH/USD | 1684.75 | 83.973 | 83.254 | +4.04% | +0.10% | 1.02x | 0.1 | 2026-11-21T22:01:00.829267+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.04514 | 82.358 | 87.641 | +6.92% | +0.33% | 0.30x | 11.1 | 2026-11-21T22:01:00.829267+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | TAO/USD | 185.7196 | 78.579 | 72.309 | +2.89% | -0.07% | 1.66x | 5.8 | 2026-11-21T22:01:00.829267+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XRP/USD | 0.92902 | 76.505 | 69.623 | +2.23% | +0.18% | 1.60x | 2.0 | 2026-11-21T22:01:00.829267+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 9 | SOL/USD | 70.27 | 76.353 | 70.181 | +2.27% | -0.03% | 1.63x | 1.4 | 2026-11-21T22:01:00.829267+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 10 | XBT/USD | 60341.1 | 69.284 | 73.260 | +2.61% | +0.08% | 0.56x | 0.0 | 2026-11-21T22:01:00.829267+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XLM/USD | 0.128801 | 64.710 | 62.524 | +1.26% | +0.03% | 1.20x | 2.6 | 2026-11-21T22:01:00.829267+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XDG/USD | 0.055129 | 63.272 | 65.525 | +1.57% | +0.12% | 0.71x | 1.0 | 2026-11-21T22:01:00.829267+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 96.642 | 492 | +0.13% | 0.57x |
| 2 | UNI/USD | 92.530 | 4.7263 | +0.17% | 0.48x |
| 3 | NIGHT/USD | 87.641 | 0.04514 | +0.33% | 0.30x |
| 4 | ZEC/USD | 84.455 | 789.87 | -0.21% | 5.44x |
| 5 | ETH/USD | 83.254 | 1684.75 | +0.10% | 1.02x |
| 6 | WINGS/USD | 76.939 | 0.001889 | +2.44% | 0.58x |
| 7 | XBT/USD | 73.260 | 60341.1 | +0.08% | 0.56x |
| 8 | TAO/USD | 72.309 | 185.7196 | -0.07% | 1.66x |
| 9 | SOL/USD | 70.181 | 70.27 | -0.03% | 1.63x |
| 10 | XRP/USD | 69.623 | 0.92902 | +0.18% | 1.60x |
| 11 | XDG/USD | 65.525 | 0.055129 | +0.12% | 0.71x |
| 12 | XLM/USD | 62.524 | 0.128801 | +0.03% | 1.20x |

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

- Persisted scans: 1192; predictions: 9613; observations: 721095.
- Matured sampled outcomes across 1/6/24/48h: 12844; gap abstentions: 21503. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44954359299 · **Generation:** 1192 · **Legacy run:** 44954359299
**Main quote time:** 2026-11-21T22:01:07.246803+00:00 · **Legacy report time:** 2026-11-21T22:02:10.104210+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 789.87 | 98.39 | -0.21% | 5.44x | STRONG 79/100 | HIGH 61/100 | Watch |
| 2 | XMR/USD | 492 | 92.96 | +0.13% | 0.57x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 3 | UNI/USD | 4.7263 | 88.18 | +0.17% | 0.48x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 4 | WINGS/USD | 0.001889 | 84.98 | +2.44% | 0.58x | STRONG 72/100 | VERY_HIGH 75/100 | Watch |
| 5 | ETH/USD ⭐ | 1684.75 | 83.97 | +0.10% | 1.02x | STRONG 77/100 | HIGH 62/100 | Watch |
| 6 | NIGHT/USD | 0.04514 | 82.36 | +0.33% | 0.30x | MODERATE 66/100 | VERY_HIGH 76/100 | Watch |
| 7 | TAO/USD | 185.7196 | 78.58 | -0.07% | 1.66x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 8 | XRP/USD ⭐ | 0.92902 | 76.51 | +0.18% | 1.60x | STRONG 83/100 | HIGH 55/100 | Watch |
| 9 | SOL/USD | 70.27 | 76.35 | -0.03% | 1.63x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 10 | XBT/USD | 60341.1 | 69.28 | +0.08% | 0.56x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 11 | XLM/USD | 0.128801 | 64.71 | +0.03% | 1.20x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 12 | XDG/USD | 0.055129 | 63.27 | +0.12% | 0.71x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD ⭐ | 1684.06 | 100.00 | +0.10% | 1.02x | 68252 | STRONG 85/100 | HIGH 62/100 | Watch |
| 2 | XRP/USD ⭐ | 0.92874 | 81.17 | +0.18% | 1.60x | 47184 | STRONG 86/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ETH/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
