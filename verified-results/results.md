# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T21:25:51.117254+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45704073998
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 07b04aea962fc9837925b32de5a2e58ff975963f (atomic ledger/results publication)
**Ledger generation:** 1769 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LTC/USD | 42.46 | 82.300 | 80.235 | +3.94% | +0.12% | 1.15x | 4.7 | 2026-11-25T21:25:43.824037+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 2 | ADA/USD | 0.147011 | 80.347 | 65.741 | +1.84% | -0.08% | 2.63x | 4.3 | 2026-11-25T21:25:43.824037+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XRP/USD | 0.94388 | 79.183 | 70.310 | +2.19% | -0.06% | 1.91x | 0.1 | 2026-11-25T21:25:43.824037+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 4 | NEAR/USD | 3.0028 | 77.531 | 81.710 | +4.10% | -0.03% | 0.60x | 4.0 | 2026-11-25T21:25:43.824037+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | ZEC/USD | 765.66 | 76.117 | 80.100 | +3.62% | +0.67% | 0.27x | 0.5 | 2026-11-25T21:25:43.824037+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XLM/USD | 0.12844 | 73.819 | 67.674 | +3.54% | +0.09% | 1.57x | 2.1 | 2026-11-25T21:25:43.824037+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 7 | HYPE/USD | 61.97 | 72.563 | 78.747 | +3.51% | +0.37% | 0.20x | 1.6 | 2026-11-25T21:25:43.824037+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XDG/USD | 0.056014 | 70.818 | 56.915 | +1.41% | -0.22% | 5.18x | 0.7 | 2026-11-25T21:25:43.824037+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6646 | 68.760 | 72.734 | +2.64% | +0.20% | 0.50x | 1.5 | 2026-11-25T21:25:43.824037+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XMR/USD | 522 | 64.161 | 71.937 | +2.43% | +0.18% | 0.13x | 0.2 | 2026-11-25T21:25:43.824037+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XBT/USD | 60253.9 | 62.483 | 60.998 | +0.86% | +0.07% | 1.11x | 0.0 | 2026-11-25T21:25:43.824037+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 12 | PUMP/USD | 0.002537 | 61.566 | 64.915 | +4.02% | +0.36% | 0.49x | 11.8 | 2026-11-25T21:25:43.824037+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 81.710 | 3.0028 | -0.03% | 0.60x |
| 2 | LTC/USD | 80.235 | 42.46 | +0.12% | 1.15x |
| 3 | ZEC/USD | 80.100 | 765.66 | +0.67% | 0.27x |
| 4 | HYPE/USD | 78.747 | 61.97 | +0.37% | 0.20x |
| 5 | SUI/USD | 72.734 | 0.6646 | +0.20% | 0.50x |
| 6 | XMR/USD | 71.937 | 522 | +0.18% | 0.13x |
| 7 | XRP/USD | 70.310 | 0.94388 | -0.06% | 1.91x |
| 8 | XLM/USD | 67.674 | 0.12844 | +0.09% | 1.57x |
| 9 | ADA/USD | 65.741 | 0.147011 | -0.08% | 2.63x |
| 10 | PUMP/USD | 64.915 | 0.002537 | +0.36% | 0.49x |
| 11 | XBT/USD | 60.998 | 60253.9 | +0.07% | 1.11x |
| 12 | XDG/USD | 56.915 | 0.056014 | -0.22% | 5.18x |

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

- Persisted scans: 1769; predictions: 14972; observations: 1072365.
- Matured sampled outcomes across 1/6/24/48h: 32714; gap abstentions: 23115. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45704073998 · **Generation:** 1769 · **Legacy run:** 45704073998
**Main quote time:** 2026-11-25T21:25:51.117254+00:00 · **Legacy report time:** 2026-11-25T21:26:41.974046+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD ⭐ | 42.46 | 82.30 | +0.12% | 1.15x | STRONG 76/100 | HIGH 62/100 | Watch |
| 2 | ADA/USD | 0.147011 | 80.35 | -0.08% | 2.63x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | XRP/USD | 0.94388 | 79.18 | -0.06% | 1.91x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 4 | NEAR/USD | 3.0028 | 77.53 | -0.03% | 0.60x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 5 | ZEC/USD | 765.66 | 76.12 | +0.67% | 0.27x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 6 | XLM/USD ⭐ | 0.12844 | 73.82 | +0.09% | 1.57x | STRONG 82/100 | HIGH 55/100 | Watch |
| 7 | HYPE/USD | 61.97 | 72.56 | +0.37% | 0.20x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 8 | XDG/USD | 0.056014 | 70.82 | -0.22% | 5.18x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 9 | SUI/USD | 0.6646 | 68.76 | +0.20% | 0.50x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 10 | XMR/USD | 522 | 64.16 | +0.18% | 0.13x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 11 | XBT/USD | 60253.9 | 62.48 | +0.07% | 1.11x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 12 | PUMP/USD | 0.002537 | 61.57 | +0.36% | 0.49x | MODERATE 56/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD ⭐ | 42.49 | 96.24 | +0.12% | 1.15x | 13580 | STRONG 83/100 | HIGH 62/100 | Watch |
| 2 | XLM/USD ⭐ | 0.128418 | 81.56 | +0.09% | 1.57x | 8174 | STRONG 86/100 | HIGH 55/100 | Watch |
| 3 | DRV/USD | 0.35802 | 77.04 | +0.15% | 1.19x | 12146 | MODERATE 59/100 | HIGH 68/100 | Watch |

**Same-run overlap:** LTC/USD, XLM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
