# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T01:25:33.364048+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44653403233
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 295dd7f9b13f18f87abfeaec7a27fb05b3fe711b (atomic ledger/results publication)
**Ledger generation:** 897 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04568 | 71.187 | 49.427 | +2.06% | +1.35% | 7.89x | 11.0 | 2026-11-20T01:25:25.796747+00:00 | Not calibrated | STRONG 86/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | SUI/USD | 0.713 | 69.758 | 55.318 | +0.45% | -0.11% | 4.80x | 2.8 | 2026-11-20T01:25:25.796747+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XMR/USD | 503.57 | 69.242 | 63.172 | +1.22% | +0.11% | 1.55x | 0.8 | 2026-11-20T01:25:25.796747+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 4 | XBT/USD | 62417.5 | 68.771 | 60.690 | +0.81% | -0.03% | 1.82x | 0.0 | 2026-11-20T01:25:25.796747+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ADA/USD | 0.152379 | 68.676 | 55.360 | +0.41% | -0.34% | 2.52x | 5.0 | 2026-11-20T01:25:25.796747+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 6 | LINK/USD | 9.02172 | 64.448 | 51.478 | +0.27% | -0.41% | 12.13x | 4.8 | 2026-11-20T01:25:25.796747+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0583314 | 61.597 | 47.217 | +0.36% | -0.12% | 2.94x | 0.0 | 2026-11-20T01:25:25.796747+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XLM/USD | 0.134261 | 58.658 | 60.850 | +1.18% | +0.05% | 0.75x | 4.8 | 2026-11-20T01:25:25.796747+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 9 | XRP/USD | 0.96805 | 55.936 | 60.182 | +0.92% | +0.08% | 0.53x | 2.5 | 2026-11-20T01:25:25.796747+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | ETH/USD | 1762.48 | 53.420 | 56.478 | +0.41% | -0.20% | 0.80x | 2.7 | 2026-11-20T01:25:25.796747+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |
| 11 | BAT/USD | 0.08868 | 40.304 | 25.361 | +0.28% | -0.01% | 3.79x | 15.8 | 2026-11-20T01:25:25.796747+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 12 | CAP/USD | 0.097281 | 40.180 | 33.562 | +0.69% | +0.67% | 1.33x | 11.6 | 2026-11-20T01:25:25.796747+00:00 | Not calibrated | MODERATE 60/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 63.172 | 503.57 | +0.11% | 1.55x |
| 2 | XLM/USD | 60.850 | 0.134261 | +0.05% | 0.75x |
| 3 | XBT/USD | 60.690 | 62417.5 | -0.03% | 1.82x |
| 4 | XRP/USD | 60.182 | 0.96805 | +0.08% | 0.53x |
| 5 | ETH/USD | 56.478 | 1762.48 | -0.20% | 0.80x |
| 6 | ADA/USD | 55.360 | 0.152379 | -0.34% | 2.52x |
| 7 | SUI/USD | 55.318 | 0.713 | -0.11% | 4.80x |
| 8 | LINK/USD | 51.478 | 9.02172 | -0.41% | 12.13x |
| 9 | NIGHT/USD | 49.427 | 0.04568 | +1.35% | 7.89x |
| 10 | XDG/USD | 47.217 | 0.0583314 | -0.12% | 2.94x |
| 11 | CAP/USD | 33.562 | 0.097281 | +0.67% | 1.33x |
| 12 | BAT/USD | 25.361 | 0.08868 | -0.01% | 3.79x |

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

- Persisted scans: 897; predictions: 7833; observations: 542016.
- Matured sampled outcomes across 1/6/24/48h: 8602; gap abstentions: 16206. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44653403233 · **Generation:** 897 · **Legacy run:** 44653403233
**Main quote time:** 2026-11-20T01:25:33.364048+00:00 · **Legacy report time:** 2026-11-20T01:26:39.301942+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04568 | 71.19 | +1.35% | 7.89x | STRONG 96/100 | HIGH 61/100 | Consider small entry |
| 2 | SUI/USD | 0.713 | 69.76 | -0.11% | 4.80x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 3 | XMR/USD ⭐ | 503.57 | 69.24 | +0.11% | 1.55x | STRONG 80/100 | HIGH 55/100 | Watch |
| 4 | XBT/USD | 62417.5 | 68.77 | -0.03% | 1.82x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 5 | ADA/USD | 0.152379 | 68.68 | -0.34% | 2.52x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 6 | LINK/USD | 9.02172 | 64.45 | -0.41% | 12.13x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 7 | XDG/USD | 0.0583314 | 61.60 | -0.12% | 2.94x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 8 | XLM/USD | 0.134261 | 58.66 | +0.05% | 0.75x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 9 | XRP/USD | 0.96805 | 55.94 | +0.08% | 0.53x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 10 | ETH/USD | 1762.48 | 53.42 | -0.20% | 0.80x | WEAK 32/100 | HIGH 68/100 | Do nothing |
| 11 | BAT/USD | 0.08868 | 40.30 | -0.01% | 3.79x | MODERATE 45/100 | VERY_HIGH 79/100 | Watch |
| 12 | CAP/USD | 0.097281 | 40.18 | +0.67% | 1.33x | MODERATE 60/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04526 | 55.48 | +1.35% | 7.89x | 7831 | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD ⭐ | 503.51 | 54.75 | +0.11% | 1.55x | 7984 | STRONG 72/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NIGHT/USD, XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
