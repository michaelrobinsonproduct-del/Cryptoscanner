# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T21:35:53.313269+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45705596182
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** faf75fab8096a2c34af2eb56194b63b95b6f9fc4 (atomic ledger/results publication)
**Ledger generation:** 1770 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.0138 | 88.358 | 84.219 | +4.48% | +0.49% | 1.17x | 4.3 | 2026-11-25T21:35:47.113046+00:00 | Not calibrated | STRONG 79/100 | HIGH 62/100 | Watch | WATCH |
| 2 | XRP/USD | 0.94334 | 84.572 | 69.847 | +2.14% | -0.06% | 2.86x | 0.2 | 2026-11-25T21:35:47.113046+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LTC/USD | 42.53 | 76.914 | 81.437 | +4.11% | +0.31% | 0.39x | 4.7 | 2026-11-25T21:35:47.113046+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | ZEC/USD | 764.83 | 76.023 | 79.509 | +3.51% | +0.53% | 0.39x | 0.1 | 2026-11-25T21:35:47.113046+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | PUMP/USD | 0.002547 | 70.710 | 71.877 | +4.43% | +0.83% | 0.47x | 3.9 | 2026-11-25T21:35:47.113046+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | HYPE/USD | 61.8 | 69.351 | 76.756 | +3.22% | +0.06% | 0.23x | 1.6 | 2026-11-25T21:35:47.113046+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6631 | 68.991 | 70.357 | +2.41% | -0.14% | 0.93x | 3.0 | 2026-11-25T21:35:47.113046+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 8 | SOL/USD | 70.78 | 66.840 | 66.161 | +1.70% | +0.27% | 0.93x | 1.4 | 2026-11-25T21:35:47.113046+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 9 | XMR/USD | 523.51 | 66.202 | 71.337 | +2.73% | +0.74% | 0.11x | 5.5 | 2026-11-25T21:35:47.113046+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | ETH/USD | 1688.68 | 58.058 | 59.547 | +0.65% | +0.16% | 0.77x | 0.1 | 2026-11-25T21:35:47.113046+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XLM/USD | 0.12809 | 57.371 | 64.618 | +3.25% | -0.37% | 0.46x | 4.2 | 2026-11-25T21:35:47.113046+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | PAXG/USD | 3568.43 | 56.696 | 59.769 | +0.75% | +0.14% | 0.62x | 1.0 | 2026-11-25T21:35:47.113046+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 84.219 | 3.0138 | +0.49% | 1.17x |
| 2 | LTC/USD | 81.437 | 42.53 | +0.31% | 0.39x |
| 3 | ZEC/USD | 79.509 | 764.83 | +0.53% | 0.39x |
| 4 | HYPE/USD | 76.756 | 61.8 | +0.06% | 0.23x |
| 5 | PUMP/USD | 71.877 | 0.002547 | +0.83% | 0.47x |
| 6 | XMR/USD | 71.337 | 523.51 | +0.74% | 0.11x |
| 7 | SUI/USD | 70.357 | 0.6631 | -0.14% | 0.93x |
| 8 | XRP/USD | 69.847 | 0.94334 | -0.06% | 2.86x |
| 9 | SOL/USD | 66.161 | 70.78 | +0.27% | 0.93x |
| 10 | XLM/USD | 64.618 | 0.12809 | -0.37% | 0.46x |
| 11 | PAXG/USD | 59.769 | 3568.43 | +0.14% | 0.62x |
| 12 | ETH/USD | 59.547 | 1688.68 | +0.16% | 0.77x |

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

- Persisted scans: 1770; predictions: 14984; observations: 1072974.
- Matured sampled outcomes across 1/6/24/48h: 32726; gap abstentions: 23140. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45705596182 · **Generation:** 1770 · **Legacy run:** 45705596182
**Main quote time:** 2026-11-25T21:35:53.313269+00:00 · **Legacy report time:** 2026-11-25T21:36:46.931713+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.0138 | 88.36 | +0.49% | 1.17x | STRONG 89/100 | HIGH 62/100 | Watch |
| 2 | XRP/USD | 0.94334 | 84.57 | -0.06% | 2.86x | STRONG 72/100 | HIGH 61/100 | Watch |
| 3 | LTC/USD | 42.53 | 76.91 | +0.31% | 0.39x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 4 | ZEC/USD | 764.83 | 76.02 | +0.53% | 0.39x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 5 | PUMP/USD | 0.002547 | 70.71 | +0.83% | 0.47x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 6 | HYPE/USD | 61.8 | 69.35 | +0.06% | 0.23x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 7 | SUI/USD | 0.6631 | 68.99 | -0.14% | 0.93x | WEAK 39/100 | HIGH 68/100 | Watch |
| 8 | SOL/USD | 70.78 | 66.84 | +0.27% | 0.93x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 9 | XMR/USD | 523.51 | 66.20 | +0.74% | 0.11x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 10 | ETH/USD | 1688.68 | 58.06 | +0.16% | 0.77x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 11 | XLM/USD | 0.12809 | 57.37 | -0.37% | 0.46x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | PAXG/USD | 3568.43 | 56.70 | +0.14% | 0.62x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.017 | 92.20 | +0.49% | 1.17x | 16581 | STRONG 91/100 | HIGH 62/100 | Watch |

**Same-run overlap:** NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
