# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T17:30:46.647628+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44930324903
**Source SHA:** 7ac7b40f8385b7b363a3015feba153e001ac4fc4
**Previous ledger commit:** 91872c7522068d0818287945e6860580f784701d (atomic ledger/results publication)
**Ledger generation:** 1164 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04519 | 100.575 | 89.814 | +7.03% | +0.92% | 1.62x | 4.4 | 2026-11-21T17:30:39.637098+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XMR/USD | 481.63 | 92.922 | 91.069 | +5.55% | -0.55% | 1.46x | 5.6 | 2026-11-21T17:30:39.637098+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 3 | UNI/USD | 4.7286 | 91.615 | 92.255 | +5.85% | +0.28% | 0.80x | 7.4 | 2026-11-21T17:30:39.637098+00:00 | Not calibrated | STRONG 76/100 | HIGH 62/100 | Watch | WATCH |
| 4 | PEARL/USD | 1.9095 | 80.779 | 69.644 | +4.44% | +1.68% | 1.27x | 13.6 | 2026-11-21T17:30:39.637098+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XBT/USD | 60049.2 | 77.784 | 69.319 | +2.11% | +0.09% | 1.80x | 0.9 | 2026-11-21T17:30:39.637098+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 6 | ETH/USD | 1680.28 | 77.138 | 81.322 | +3.76% | +0.04% | 0.56x | 0.1 | 2026-11-21T17:30:39.637098+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SOL/USD | 70.59 | 72.963 | 72.736 | +2.74% | +0.08% | 0.98x | 2.8 | 2026-11-21T17:30:39.637098+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 8 | ZEC/USD | 785.84 | 72.940 | 79.332 | +3.69% | -0.36% | 0.54x | 2.9 | 2026-11-21T17:30:39.637098+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | XRP/USD | 0.93256 | 72.538 | 72.568 | +2.62% | +0.50% | 0.75x | 1.6 | 2026-11-21T17:30:39.637098+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | PAXG/USD | 3548.1 | 71.140 | 57.948 | +0.47% | -0.02% | 2.33x | 0.0 | 2026-11-21T17:30:39.637098+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 11 | SHX/USD | 0.003505 | 70.781 | 62.085 | +4.53% | -0.09% | 1.91x | 2.9 | 2026-11-21T17:30:39.637098+00:00 | Not calibrated | MODERATE 55/100 | HIGH 66/100 | Watch | WATCH |
| 12 | TRX/USD | 0.30498 | 70.088 | 55.012 | +1.15% | +0.02% | 4.18x | 0.0 | 2026-11-21T17:30:39.637098+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UNI/USD | 92.255 | 4.7286 | +0.28% | 0.80x |
| 2 | XMR/USD | 91.069 | 481.63 | -0.55% | 1.46x |
| 3 | NIGHT/USD | 89.814 | 0.04519 | +0.92% | 1.62x |
| 4 | ETH/USD | 81.322 | 1680.28 | +0.04% | 0.56x |
| 5 | ZEC/USD | 79.332 | 785.84 | -0.36% | 0.54x |
| 6 | SOL/USD | 72.736 | 70.59 | +0.08% | 0.98x |
| 7 | XRP/USD | 72.568 | 0.93256 | +0.50% | 0.75x |
| 8 | PEARL/USD | 69.644 | 1.9095 | +1.68% | 1.27x |
| 9 | XBT/USD | 69.319 | 60049.2 | +0.09% | 1.80x |
| 10 | SHX/USD | 62.085 | 0.003505 | -0.09% | 1.91x |
| 11 | PAXG/USD | 57.948 | 3548.1 | -0.02% | 2.33x |
| 12 | TRX/USD | 55.012 | 0.30498 | +0.02% | 4.18x |

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

- Persisted scans: 1164; predictions: 9277; observations: 704071.
- Matured sampled outcomes across 1/6/24/48h: 12214; gap abstentions: 20942. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44930324903 · **Generation:** 1164 · **Legacy run:** 44930324903
**Main quote time:** 2026-11-21T17:30:46.647628+00:00 · **Legacy report time:** 2026-11-21T17:31:26.083394+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04519 | 100.57 | +0.92% | 1.62x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD | 481.63 | 92.92 | -0.55% | 1.46x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 3 | UNI/USD | 4.7286 | 91.61 | +0.28% | 0.80x | STRONG 76/100 | HIGH 62/100 | Watch |
| 4 | PEARL/USD ⭐ | 1.9095 | 80.78 | +1.68% | 1.27x | STRONG 80/100 | HIGH 61/100 | Watch |
| 5 | XBT/USD ⭐ | 60049.2 | 77.78 | +0.09% | 1.80x | STRONG 84/100 | HIGH 55/100 | Watch |
| 6 | ETH/USD | 1680.28 | 77.14 | +0.04% | 0.56x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 7 | SOL/USD | 70.59 | 72.96 | +0.08% | 0.98x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 8 | ZEC/USD | 785.84 | 72.94 | -0.36% | 0.54x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 9 | XRP/USD | 0.93256 | 72.54 | +0.50% | 0.75x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 10 | PAXG/USD | 3548.1 | 71.14 | -0.02% | 2.33x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 11 | SHX/USD | 0.003505 | 70.78 | -0.09% | 1.91x | MODERATE 55/100 | HIGH 66/100 | Watch |
| 12 | TRX/USD | 0.30498 | 70.09 | +0.02% | 4.18x | STRONG 80/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04512 | 95.89 | +0.92% | 1.62x | 11072 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | PEARL/USD ⭐ | 1.9143 | 85.37 | +1.68% | 1.27x | 12126 | STRONG 83/100 | HIGH 61/100 | Watch |
| 3 | XBT/USD ⭐ | 60051.5 | 80.85 | +0.09% | 1.80x | 246541 | STRONG 85/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NIGHT/USD, PEARL/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
