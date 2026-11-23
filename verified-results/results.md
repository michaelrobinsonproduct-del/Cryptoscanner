# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T13:01:40.271945+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45179502366
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7e75eba8101461bf074b88fea3fc0527644e97b3 (atomic ledger/results publication)
**Ledger generation:** 1433 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 156.4 | 97.338 | 87.849 | +9.04% | -0.08% | 1.99x | 9.6 | 2026-11-23T13:01:31.115269+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SOL/USD | 72.14 | 79.367 | 69.272 | +2.14% | +0.21% | 1.91x | 1.4 | 2026-11-23T13:01:31.115269+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | XMR/USD | 502.76 | 77.050 | 65.742 | +1.83% | +0.06% | 2.10x | 4.2 | 2026-11-23T13:01:31.115269+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ALGO/USD | 0.08339 | 72.059 | 76.011 | +10.55% | +0.53% | 0.34x | 9.6 | 2026-11-23T13:01:31.115269+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 5 | PEARL/USD | 2.2721 | 69.088 | 78.969 | +10.60% | -2.04% | 1.03x | 18.6 | 2026-11-23T13:01:31.115269+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 6 | UAI/USD | 0.03198 | 68.897 | 72.690 | +8.15% | +1.01% | 0.12x | 6.3 | 2026-11-23T13:01:31.115269+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 7 | XRP/USD | 0.94026 | 68.878 | 64.546 | +1.37% | +0.22% | 1.32x | 0.1 | 2026-11-23T13:01:31.115269+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6664 | 65.035 | 65.672 | +1.63% | -0.10% | 0.99x | 1.5 | 2026-11-23T13:01:31.115269+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 9 | GRT/USD | 0.01692 | 62.344 | 65.496 | +5.82% | +0.71% | 0.33x | 11.8 | 2026-11-23T13:01:31.115269+00:00 | Not calibrated | MODERATE 56/100 | EXTREME 88/100 | Do nothing | WATCH |
| 10 | CC/USD | 0.07644 | 61.344 | 64.506 | +4.33% | +0.03% | 0.67x | 1.3 | 2026-11-23T13:01:31.115269+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 11 | ADA/USD | 0.145337 | 59.667 | 52.147 | +0.51% | +0.18% | 1.66x | 2.0 | 2026-11-23T13:01:31.115269+00:00 | Not calibrated | MODERATE 65/100 | HIGH 55/100 | Watch | WATCH |
| 12 | TRX/USD | 0.307114 | 57.467 | 42.449 | +0.64% | +0.00% | 4.02x | 1.1 | 2026-11-23T13:01:31.115269+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 87.849 | 156.4 | -0.08% | 1.99x |
| 2 | PEARL/USD | 78.969 | 2.2721 | -2.04% | 1.03x |
| 3 | ALGO/USD | 76.011 | 0.08339 | +0.53% | 0.34x |
| 4 | UAI/USD | 72.690 | 0.03198 | +1.01% | 0.12x |
| 5 | SOL/USD | 69.272 | 72.14 | +0.21% | 1.91x |
| 6 | XMR/USD | 65.742 | 502.76 | +0.06% | 2.10x |
| 7 | SUI/USD | 65.672 | 0.6664 | -0.10% | 0.99x |
| 8 | GRT/USD | 65.496 | 0.01692 | +0.71% | 0.33x |
| 9 | XRP/USD | 64.546 | 0.94026 | +0.22% | 1.32x |
| 10 | CC/USD | 64.506 | 0.07644 | +0.03% | 0.67x |
| 11 | ADA/USD | 52.147 | 0.145337 | +0.18% | 1.66x |
| 12 | TRX/USD | 42.449 | 0.307114 | +0.00% | 4.02x |

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

- Persisted scans: 1433; predictions: 11963; observations: 867800.
- Matured sampled outcomes across 1/6/24/48h: 20095; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45179502366 · **Generation:** 1433 · **Legacy run:** 45179502366
**Main quote time:** 2026-11-23T13:01:40.271945+00:00 · **Legacy report time:** 2026-11-23T13:02:25.794666+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 156.4 | 97.34 | -0.08% | 1.99x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 2 | SOL/USD ⭐ | 72.14 | 79.37 | +0.21% | 1.91x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 3 | XMR/USD ⭐ | 502.76 | 77.05 | +0.06% | 2.10x | STRONG 94/100 | HIGH 55/100 | Watch |
| 4 | ALGO/USD | 0.08339 | 72.06 | +0.53% | 0.34x | MODERATE 66/100 | VERY_HIGH 75/100 | Watch |
| 5 | PEARL/USD | 2.2721 | 69.09 | -2.04% | 1.03x | WEAK 40/100 | VERY_HIGH 78/100 | Do nothing |
| 6 | UAI/USD | 0.03198 | 68.90 | +1.01% | 0.12x | MODERATE 64/100 | VERY_HIGH 82/100 | Watch |
| 7 | XRP/USD ⭐ | 0.94026 | 68.88 | +0.22% | 1.32x | STRONG 89/100 | HIGH 55/100 | Watch |
| 8 | SUI/USD | 0.6664 | 65.03 | -0.10% | 0.99x | WEAK 38/100 | HIGH 68/100 | Watch |
| 9 | GRT/USD | 0.01692 | 62.34 | +0.71% | 0.33x | MODERATE 56/100 | EXTREME 88/100 | Do nothing |
| 10 | CC/USD | 0.07644 | 61.34 | +0.03% | 0.67x | MODERATE 51/100 | VERY_HIGH 75/100 | Watch |
| 11 | ADA/USD | 0.145337 | 59.67 | +0.18% | 1.66x | MODERATE 65/100 | HIGH 55/100 | Watch |
| 12 | TRX/USD | 0.307114 | 57.47 | +0.00% | 4.02x | STRONG 74/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD ⭐ | 72.06 | 77.77 | +0.21% | 1.91x | 29295 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD ⭐ | 502.4 | 70.94 | +0.06% | 2.10x | 8287 | STRONG 90/100 | HIGH 55/100 | Watch |
| 3 | XRP/USD ⭐ | 0.93879 | 67.01 | +0.22% | 1.32x | 20062 | STRONG 89/100 | HIGH 55/100 | Watch |

**Same-run overlap:** SOL/USD, XMR/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
