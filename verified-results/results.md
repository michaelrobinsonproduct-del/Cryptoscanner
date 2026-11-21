# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T23:34:27.855391+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44962044585
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 785541bc45529d2d1ad6b69eccd83a0051d59066 (atomic ledger/results publication)
**Ledger generation:** 1202 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 491.14 | 115.420 | 98.981 | +7.64% | +0.29% | 2.70x | 2.0 | 2026-11-21T23:34:19.527301+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | UNI/USD | 4.7342 | 96.269 | 94.385 | +5.98% | +0.30% | 1.04x | 4.9 | 2026-11-21T23:34:19.527301+00:00 | Not calibrated | STRONG 83/100 | HIGH 62/100 | Watch | WATCH |
| 3 | ETH/USD | 1680.58 | 91.076 | 81.452 | +3.78% | -0.02% | 1.97x | 0.1 | 2026-11-21T23:34:19.527301+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04431 | 90.853 | 77.508 | +4.95% | -0.25% | 2.46x | 9.0 | 2026-11-21T23:34:19.527301+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XRP/USD | 0.93187 | 84.682 | 72.572 | +2.55% | +0.23% | 2.10x | 0.5 | 2026-11-21T23:34:19.527301+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | XLM/USD | 0.128814 | 79.032 | 63.838 | +1.27% | +0.04% | 2.83x | 0.1 | 2026-11-21T23:34:19.527301+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 7 | PEARL/USD | 1.9592 | 78.085 | 77.160 | +7.16% | -0.11% | 1.15x | 21.5 | 2026-11-21T23:34:19.527301+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0550621 | 75.372 | 65.142 | +1.45% | +0.04% | 2.01x | 0.0 | 2026-11-21T23:34:19.527301+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 9 | HYPE/USD | 61.22 | 74.518 | 58.208 | +0.57% | +0.26% | 12.54x | 1.6 | 2026-11-21T23:34:19.527301+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 10 | SOL/USD | 70.19 | 73.843 | 69.365 | +2.15% | -0.01% | 1.45x | 1.4 | 2026-11-21T23:34:19.527301+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 11 | ZEC/USD | 779.68 | 73.741 | 73.375 | +2.87% | -0.26% | 1.17x | 3.5 | 2026-11-21T23:34:19.527301+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 12 | XBT/USD | 60140.2 | 69.290 | 70.868 | +2.27% | -0.07% | 0.88x | 0.0 | 2026-11-21T23:34:19.527301+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 98.981 | 491.14 | +0.29% | 2.70x |
| 2 | UNI/USD | 94.385 | 4.7342 | +0.30% | 1.04x |
| 3 | ETH/USD | 81.452 | 1680.58 | -0.02% | 1.97x |
| 4 | NIGHT/USD | 77.508 | 0.04431 | -0.25% | 2.46x |
| 5 | PEARL/USD | 77.160 | 1.9592 | -0.11% | 1.15x |
| 6 | ZEC/USD | 73.375 | 779.68 | -0.26% | 1.17x |
| 7 | XRP/USD | 72.572 | 0.93187 | +0.23% | 2.10x |
| 8 | XBT/USD | 70.868 | 60140.2 | -0.07% | 0.88x |
| 9 | SOL/USD | 69.365 | 70.19 | -0.01% | 1.45x |
| 10 | XDG/USD | 65.142 | 0.0550621 | +0.04% | 2.01x |
| 11 | XLM/USD | 63.838 | 0.128814 | +0.04% | 2.83x |
| 12 | HYPE/USD | 58.208 | 61.22 | +0.26% | 12.54x |

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

- Persisted scans: 1202; predictions: 9733; observations: 727175.
- Matured sampled outcomes across 1/6/24/48h: 13086; gap abstentions: 21641. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44962044585 · **Generation:** 1202 · **Legacy run:** 44962044585
**Main quote time:** 2026-11-21T23:34:27.855391+00:00 · **Legacy report time:** 2026-11-21T23:35:14.173411+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 491.14 | 115.42 | +0.29% | 2.70x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UNI/USD | 4.7342 | 96.27 | +0.30% | 1.04x | STRONG 83/100 | HIGH 62/100 | Watch |
| 3 | ETH/USD | 1680.58 | 91.08 | -0.02% | 1.97x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 4 | NIGHT/USD | 0.04431 | 90.85 | -0.25% | 2.46x | STRONG 75/100 | HIGH 61/100 | Watch |
| 5 | XRP/USD ⭐ | 0.93187 | 84.68 | +0.23% | 2.10x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | XLM/USD | 0.128814 | 79.03 | +0.04% | 2.83x | STRONG 85/100 | HIGH 55/100 | Watch |
| 7 | PEARL/USD | 1.9592 | 78.09 | -0.11% | 1.15x | WEAK 39/100 | VERY_HIGH 80/100 | Watch |
| 8 | XDG/USD | 0.0550621 | 75.37 | +0.04% | 2.01x | STRONG 83/100 | HIGH 55/100 | Watch |
| 9 | HYPE/USD | 61.22 | 74.52 | +0.26% | 12.54x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 10 | SOL/USD | 70.19 | 73.84 | -0.01% | 1.45x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 11 | ZEC/USD | 779.68 | 73.74 | -0.26% | 1.17x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 12 | XBT/USD | 60140.2 | 69.29 | -0.07% | 0.88x | WEAK 40/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.9323 | 86.85 | +0.26% | 1.78x | 45195 | STRONG 98/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
