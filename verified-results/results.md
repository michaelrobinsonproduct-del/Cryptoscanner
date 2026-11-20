# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T01:30:37.498431+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44653998959
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** d364e4950bc6f66720ae2007046214cdef1a942b (atomic ledger/results publication)
**Ledger generation:** 898 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04524 | 68.418 | 42.485 | +1.07% | +2.19% | 10.50x | 11.1 | 2026-11-20T01:30:29.493191+00:00 | Not calibrated | STRONG 84/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XBT/USD | 62331.9 | 66.587 | 59.722 | +0.68% | -0.04% | 1.71x | 0.0 | 2026-11-20T01:30:29.493191+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XMR/USD | 501.3 | 64.688 | 57.181 | +0.77% | -0.10% | 1.80x | 6.4 | 2026-11-20T01:30:29.493191+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 4 | AVAX/USD | 7.008 | 58.450 | 42.735 | +0.27% | +0.14% | 3.74x | 7.1 | 2026-11-20T01:30:29.493191+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 5 | ETH/USD | 1760.81 | 56.859 | 57.145 | +0.31% | -0.10% | 1.02x | 0.1 | 2026-11-20T01:30:29.493191+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 6 | XLM/USD | 0.133896 | 56.149 | 58.884 | +0.90% | +0.14% | 0.66x | 4.8 | 2026-11-20T01:30:29.493191+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | XRP/USD | 0.96643 | 55.538 | 59.929 | +0.75% | +0.08% | 0.52x | 0.6 | 2026-11-20T01:30:29.493191+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | HBAR/USD | 0.05419 | 37.461 | 40.775 | +0.80% | +0.35% | 0.49x | 3.7 | 2026-11-20T01:30:29.493191+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | ICNT/USD | 0.4313 | 36.418 | 34.581 | +1.22% | +0.23% | 1.07x | 23.2 | 2026-11-20T01:30:29.493191+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 10 | KAS/USD | 0.02655 | 31.288 | 29.643 | +0.42% | +0.30% | 1.01x | 11.3 | 2026-11-20T01:30:29.493191+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 11 | BCH/USD | 207.02 | 28.767 | 35.948 | +0.37% | +0.08% | 0.24x | 6.8 | 2026-11-20T01:30:29.493191+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 12 | CAP/USD | 0.097099 | 26.939 | 30.521 | +0.50% | +0.10% | 0.59x | 15.0 | 2026-11-20T01:30:29.493191+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 59.929 | 0.96643 | +0.08% | 0.52x |
| 2 | XBT/USD | 59.722 | 62331.9 | -0.04% | 1.71x |
| 3 | XLM/USD | 58.884 | 0.133896 | +0.14% | 0.66x |
| 4 | XMR/USD | 57.181 | 501.3 | -0.10% | 1.80x |
| 5 | ETH/USD | 57.145 | 1760.81 | -0.10% | 1.02x |
| 6 | AVAX/USD | 42.735 | 7.008 | +0.14% | 3.74x |
| 7 | NIGHT/USD | 42.485 | 0.04524 | +2.19% | 10.50x |
| 8 | HBAR/USD | 40.775 | 0.05419 | +0.35% | 0.49x |
| 9 | BCH/USD | 35.948 | 207.02 | +0.08% | 0.24x |
| 10 | ICNT/USD | 34.581 | 0.4313 | +0.23% | 1.07x |
| 11 | CAP/USD | 30.521 | 0.097099 | +0.10% | 0.59x |
| 12 | KAS/USD | 29.643 | 0.02655 | +0.30% | 1.01x |

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

- Persisted scans: 898; predictions: 7845; observations: 542619.
- Matured sampled outcomes across 1/6/24/48h: 8626; gap abstentions: 16221. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44653998959 · **Generation:** 898 · **Legacy run:** 44653998959
**Main quote time:** 2026-11-20T01:30:37.498431+00:00 · **Legacy report time:** 2026-11-20T01:31:36.242895+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04524 | 68.42 | +2.19% | 10.50x | STRONG 94/100 | HIGH 61/100 | Consider small entry |
| 2 | XBT/USD | 62331.9 | 66.59 | -0.04% | 1.71x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 3 | XMR/USD | 501.3 | 64.69 | -0.10% | 1.80x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 4 | AVAX/USD ⭐ | 7.008 | 58.45 | +0.14% | 3.74x | STRONG 84/100 | HIGH 55/100 | Watch |
| 5 | ETH/USD | 1760.81 | 56.86 | -0.10% | 1.02x | WEAK 38/100 | HIGH 68/100 | Watch |
| 6 | XLM/USD | 0.133896 | 56.15 | +0.14% | 0.66x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 7 | XRP/USD | 0.96643 | 55.54 | +0.08% | 0.52x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 8 | HBAR/USD | 0.05419 | 37.46 | +0.35% | 0.49x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 9 | ICNT/USD | 0.4313 | 36.42 | +0.23% | 1.07x | WEAK 43/100 | VERY_HIGH 74/100 | Watch |
| 10 | KAS/USD | 0.02655 | 31.29 | +0.30% | 1.01x | MODERATE 46/100 | VERY_HIGH 73/100 | Watch |
| 11 | BCH/USD | 207.02 | 28.77 | +0.08% | 0.24x | WEAK 34/100 | VERY_HIGH 70/100 | Do nothing |
| 12 | CAP/USD | 0.097099 | 26.94 | +0.10% | 0.59x | WEAK 28/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04525 | 62.16 | +2.19% | 10.50x | 7875 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 2 | SYRUP/USD | 0.09835 | 59.13 | +1.22% | 7.04x | 2383 | STRONG 70/100 | VERY_HIGH 82/100 | Watch |
| 3 | AVAX/USD ⭐ | 7.009 | 54.65 | +0.14% | 3.74x | 4854 | STRONG 82/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NIGHT/USD, AVAX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
