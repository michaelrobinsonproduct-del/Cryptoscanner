# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T00:12:35.323011+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46086376648
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1257d925de73fcf6dd7a1fc7d7e273aa7253c783 (atomic ledger/results publication)
**Ledger generation:** 2079 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SKY/USD | 0.05298 | 78.189 | 49.443 | +2.08% | +3.02% | 2.36x | 9.4 | 2026-11-28T00:12:29.754194+00:00 | Not calibrated | STRONG 94/100 | HIGH 65/100 | Consider small entry | WATCH |
| 2 | XLM/USD | 0.127258 | 53.916 | 50.369 | +0.43% | +0.39% | 1.16x | 1.5 | 2026-11-28T00:12:29.754194+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 3 | SPX/USD | 0.2736 | 43.946 | 26.004 | +0.44% | +0.59% | 3.70x | 18.3 | 2026-11-28T00:12:29.754194+00:00 | Not calibrated | STRONG 72/100 | HIGH 66/100 | Watch | WATCH |
| 4 | SENT/USD | 0.023797 | 25.776 | 32.106 | +0.35% | +0.21% | 0.26x | 2.1 | 2026-11-28T00:12:29.754194+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | PORTAL/USD | 0.04154 | 18.482 | 19.779 | +0.44% | +0.66% | 0.54x | 43.5 | 2026-11-28T00:12:29.754194+00:00 | Not calibrated | WEAK 24/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XLM/USD | 50.369 | 0.127258 | +0.39% | 1.16x |
| 2 | SKY/USD | 49.443 | 0.05298 | +3.02% | 2.36x |
| 3 | SENT/USD | 32.106 | 0.023797 | +0.21% | 0.26x |
| 4 | SPX/USD | 26.004 | 0.2736 | +0.59% | 3.70x |
| 5 | PORTAL/USD | 19.779 | 0.04154 | +0.66% | 0.54x |

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

- Persisted scans: 2079; predictions: 18634; observations: 1258921.
- Matured sampled outcomes across 1/6/24/48h: 42668; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 154 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 17; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46086376648 · **Generation:** 2079 · **Legacy run:** 46086376648
**Main quote time:** 2026-11-28T00:12:35.323011+00:00 · **Legacy report time:** 2026-11-28T00:13:31.923896+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.05298 | 78.19 | +3.02% | 2.36x | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 2 | XLM/USD ⭐ | 0.127258 | 53.92 | +0.39% | 1.16x | STRONG 72/100 | HIGH 62/100 | Watch |
| 3 | SPX/USD | 0.2736 | 43.95 | +0.59% | 3.70x | STRONG 72/100 | HIGH 66/100 | Watch |
| 4 | SENT/USD | 0.023797 | 25.78 | +0.21% | 0.26x | WEAK 43/100 | VERY_HIGH 82/100 | Watch |
| 5 | PORTAL/USD | 0.04154 | 18.48 | +0.66% | 0.54x | WEAK 24/100 | EXTREME 92/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.05315 | 70.14 | +3.02% | 2.36x | 9902 | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 2 | XDG/USD | 0.0578012 | 62.32 | +0.30% | 2.80x | 13375 | STRONG 86/100 | HIGH 55/100 | Watch |
| 3 | SUI/USD | 0.6735 | 56.22 | +0.18% | 2.26x | 8033 | STRONG 73/100 | HIGH 55/100 | Watch |
| 4 | ETH/USD | 1664.03 | 55.09 | +0.28% | 1.03x | 46751 | MODERATE 63/100 | HIGH 62/100 | Watch |
| 5 | XLM/USD ⭐ | 0.12728 | 54.24 | +0.39% | 1.16x | 8677 | STRONG 72/100 | HIGH 62/100 | Watch |
| 6 | AVAX/USD | 6.612 | 46.60 | +0.23% | 2.12x | 4137 | STRONG 78/100 | HIGH 55/100 | Watch |

**Same-run overlap:** SKY/USD, XLM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
