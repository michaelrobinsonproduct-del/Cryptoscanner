# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T19:30:58.391953+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44941204702
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** e39b073e67362a33faeb2537d952ce63eb7adc50 (atomic ledger/results publication)
**Ledger generation:** 1176 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XBT/USD | 60198.4 | 86.395 | 71.561 | +2.37% | -0.03% | 2.82x | 0.0 | 2026-11-21T19:30:51.970349+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04546 | 85.942 | 89.103 | +7.67% | +0.20% | 0.58x | 8.8 | 2026-11-21T19:30:51.970349+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | ZEC/USD | 786.91 | 85.663 | 80.451 | +3.83% | -0.10% | 1.57x | 2.7 | 2026-11-21T19:30:51.970349+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 4 | TAO/USD | 185.3019 | 84.959 | 71.384 | +2.66% | -0.29% | 7.39x | 4.4 | 2026-11-21T19:30:51.970349+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XMR/USD | 483.01 | 83.669 | 93.194 | +5.86% | -0.42% | 0.26x | 5.6 | 2026-11-21T19:30:51.970349+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | UNI/USD | 4.6741 | 81.565 | 85.817 | +4.63% | -0.24% | 0.70x | 3.2 | 2026-11-21T19:30:51.970349+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | ETH/USD | 1681.97 | 81.504 | 82.053 | +3.87% | -0.08% | 0.98x | 0.1 | 2026-11-21T19:30:51.970349+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XRP/USD | 0.93168 | 69.394 | 72.372 | +2.53% | -0.30% | 0.85x | 0.6 | 2026-11-21T19:30:51.970349+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 9 | SOL/USD | 70.55 | 69.136 | 73.037 | +2.68% | -0.10% | 0.66x | 1.4 | 2026-11-21T19:30:51.970349+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | HYPE/USD | 61.22 | 66.699 | 58.208 | +0.57% | +0.03% | 1.83x | 1.6 | 2026-11-21T19:30:51.970349+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 11 | XLM/USD | 0.128988 | 66.307 | 64.795 | +1.40% | -0.05% | 1.18x | 0.1 | 2026-11-21T19:30:51.970349+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0550696 | 63.658 | 64.831 | +1.46% | -0.32% | 1.04x | 0.8 | 2026-11-21T19:30:51.970349+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 93.194 | 483.01 | -0.42% | 0.26x |
| 2 | NIGHT/USD | 89.103 | 0.04546 | +0.20% | 0.58x |
| 3 | UNI/USD | 85.817 | 4.6741 | -0.24% | 0.70x |
| 4 | ETH/USD | 82.053 | 1681.97 | -0.08% | 0.98x |
| 5 | ZEC/USD | 80.451 | 786.91 | -0.10% | 1.57x |
| 6 | SOL/USD | 73.037 | 70.55 | -0.10% | 0.66x |
| 7 | XRP/USD | 72.372 | 0.93168 | -0.30% | 0.85x |
| 8 | XBT/USD | 71.561 | 60198.4 | -0.03% | 2.82x |
| 9 | TAO/USD | 71.384 | 185.3019 | -0.29% | 7.39x |
| 10 | XDG/USD | 64.831 | 0.0550696 | -0.32% | 1.04x |
| 11 | XLM/USD | 64.795 | 0.128988 | -0.05% | 1.18x |
| 12 | HYPE/USD | 58.208 | 61.22 | +0.03% | 1.83x |

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

- Persisted scans: 1176; predictions: 9421; observations: 711367.
- Matured sampled outcomes across 1/6/24/48h: 12486; gap abstentions: 21206. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44941204702 · **Generation:** 1176 · **Legacy run:** 44941204702
**Main quote time:** 2026-11-21T19:30:58.391953+00:00 · **Legacy report time:** 2026-11-21T19:31:48.855810+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XBT/USD | 60198.4 | 86.40 | -0.03% | 2.82x | STRONG 73/100 | HIGH 61/100 | Watch |
| 2 | NIGHT/USD | 0.04546 | 85.94 | +0.20% | 0.58x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 3 | ZEC/USD | 786.91 | 85.66 | -0.10% | 1.57x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 4 | TAO/USD | 185.3019 | 84.96 | -0.29% | 7.39x | STRONG 72/100 | HIGH 61/100 | Watch |
| 5 | XMR/USD | 483.01 | 83.67 | -0.42% | 0.26x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 6 | UNI/USD | 4.6741 | 81.56 | -0.24% | 0.70x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 7 | ETH/USD | 1681.97 | 81.50 | -0.08% | 0.98x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 8 | XRP/USD | 0.93168 | 69.39 | -0.30% | 0.85x | WEAK 40/100 | HIGH 68/100 | Watch |
| 9 | SOL/USD | 70.55 | 69.14 | -0.10% | 0.66x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 10 | HYPE/USD | 61.22 | 66.70 | +0.03% | 1.83x | MODERATE 68/100 | HIGH 55/100 | Watch |
| 11 | XLM/USD | 0.128988 | 66.31 | -0.05% | 1.18x | WEAK 43/100 | HIGH 68/100 | Watch |
| 12 | XDG/USD | 0.0550696 | 63.66 | -0.32% | 1.04x | WEAK 42/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SHX/USD | 0.003514 | 89.98 | +0.51% | 15.86x | 2668 | STRONG 100/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
