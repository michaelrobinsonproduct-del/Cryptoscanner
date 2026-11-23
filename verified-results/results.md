# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T06:01:38.525655+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45121180746
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d6c6c18ed9c26746ace5d94cc54cfe8dccc6c7c9 (atomic ledger/results publication)
**Ledger generation:** 1390 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SOL/USD | 71.96 | 81.513 | 67.486 | +1.88% | -0.19% | 3.01x | 1.4 | 2026-11-23T06:01:29.808572+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 2 | JUP/USD | 0.24354 | 79.793 | 74.363 | +8.45% | +0.07% | 1.51x | 9.9 | 2026-11-23T06:01:29.808572+00:00 | Not calibrated | STRONG 75/100 | HIGH 60/100 | Watch | WATCH |
| 3 | XMR/USD | 501.35 | 79.058 | 65.134 | +1.55% | -0.22% | 7.25x | 1.4 | 2026-11-23T06:01:29.808572+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XBT/USD | 61664.7 | 75.337 | 60.652 | +0.81% | -0.06% | 4.14x | 0.0 | 2026-11-23T06:01:29.808572+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ETH/USD | 1731.59 | 73.192 | 59.029 | +0.58% | -0.17% | 3.48x | 0.1 | 2026-11-23T06:01:29.808572+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XRP/USD | 0.94321 | 72.562 | 66.561 | +1.69% | +0.10% | 1.55x | 0.5 | 2026-11-23T06:01:29.808572+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6674 | 70.692 | 65.992 | +1.78% | -0.09% | 1.51x | 3.0 | 2026-11-23T06:01:29.808572+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XLM/USD | 0.12833 | 64.697 | 58.052 | +0.63% | -0.22% | 1.77x | 0.5 | 2026-11-23T06:01:29.808572+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 9 | NEAR/USD | 3.0219 | 62.217 | 63.776 | +1.35% | -0.76% | 1.22x | 1.3 | 2026-11-23T06:01:29.808572+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 10 | PAXG/USD | 3608.12 | 58.566 | 51.012 | +1.01% | -0.19% | 1.85x | 1.4 | 2026-11-23T06:01:29.808572+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |
| 11 | DOT/USD | 0.6713 | 57.782 | 43.229 | +1.59% | -0.09% | 44.51x | 1.5 | 2026-11-23T06:01:29.808572+00:00 | Not calibrated | MODERATE 59/100 | HIGH 66/100 | Watch | WATCH |
| 12 | AI/USD | 0.01605 | 56.929 | 66.652 | +9.78% | -1.48% | 0.77x | 18.7 | 2026-11-23T06:01:29.808572+00:00 | Not calibrated | WEAK 28/100 | EXTREME 90/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | JUP/USD | 74.363 | 0.24354 | +0.07% | 1.51x |
| 2 | SOL/USD | 67.486 | 71.96 | -0.19% | 3.01x |
| 3 | AI/USD | 66.652 | 0.01605 | -1.48% | 0.77x |
| 4 | XRP/USD | 66.561 | 0.94321 | +0.10% | 1.55x |
| 5 | SUI/USD | 65.992 | 0.6674 | -0.09% | 1.51x |
| 6 | XMR/USD | 65.134 | 501.35 | -0.22% | 7.25x |
| 7 | NEAR/USD | 63.776 | 3.0219 | -0.76% | 1.22x |
| 8 | XBT/USD | 60.652 | 61664.7 | -0.06% | 4.14x |
| 9 | ETH/USD | 59.029 | 1731.59 | -0.17% | 3.48x |
| 10 | XLM/USD | 58.052 | 0.12833 | -0.22% | 1.77x |
| 11 | PAXG/USD | 51.012 | 3608.12 | -0.19% | 1.85x |
| 12 | DOT/USD | 43.229 | 0.6713 | -0.09% | 44.51x |

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

- Persisted scans: 1390; predictions: 11447; observations: 841614.
- Matured sampled outcomes across 1/6/24/48h: 18574; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 117 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45121180746 · **Generation:** 1390 · **Legacy run:** 45121180746
**Main quote time:** 2026-11-23T06:01:38.525655+00:00 · **Legacy report time:** 2026-11-23T06:02:44.132493+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD | 71.96 | 81.51 | -0.19% | 3.01x | STRONG 71/100 | HIGH 61/100 | Watch |
| 2 | JUP/USD ⭐ | 0.24354 | 79.79 | +0.07% | 1.51x | STRONG 85/100 | HIGH 60/100 | Watch |
| 3 | XMR/USD | 501.35 | 79.06 | -0.22% | 7.25x | STRONG 70/100 | HIGH 61/100 | Watch |
| 4 | XBT/USD | 61664.7 | 75.34 | -0.06% | 4.14x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 5 | ETH/USD | 1731.59 | 73.19 | -0.17% | 3.48x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 6 | XRP/USD ⭐ | 0.94321 | 72.56 | +0.10% | 1.55x | STRONG 81/100 | HIGH 55/100 | Watch |
| 7 | SUI/USD | 0.6674 | 70.69 | -0.09% | 1.51x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 8 | XLM/USD | 0.12833 | 64.70 | -0.22% | 1.77x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 9 | NEAR/USD | 3.0219 | 62.22 | -0.76% | 1.22x | WEAK 41/100 | HIGH 68/100 | Watch |
| 10 | PAXG/USD | 3608.12 | 58.57 | -0.19% | 1.85x | MODERATE 49/100 | HIGH 61/100 | Watch |
| 11 | DOT/USD | 0.6713 | 57.78 | -0.09% | 44.51x | MODERATE 59/100 | HIGH 66/100 | Watch |
| 12 | AI/USD | 0.01605 | 56.93 | -1.48% | 0.77x | WEAK 28/100 | EXTREME 90/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | JUP/USD ⭐ | 0.24365 | 74.82 | +0.07% | 1.51x | 3107 | STRONG 82/100 | HIGH 60/100 | Watch |
| 2 | XRP/USD ⭐ | 0.94145 | 72.28 | +0.10% | 1.55x | 20218 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** JUP/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
