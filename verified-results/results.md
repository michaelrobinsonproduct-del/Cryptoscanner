# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T21:01:07.886061+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45069513676
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** a901b40e8604f45f56a1d6a0384611a56b5bd1c7 (atomic ledger/results publication)
**Ledger generation:** 1335 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.37387 | 99.712 | 83.600 | +11.54% | +0.22% | 3.00x | 11.2 | 2026-11-22T21:00:59.863122+00:00 | Not calibrated | STRONG 100/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | NIGHT/USD | 0.04859 | 95.814 | 91.938 | +9.73% | +0.91% | 0.93x | 2.1 | 2026-11-22T21:00:59.863122+00:00 | Not calibrated | STRONG 78/100 | HIGH 62/100 | Watch | WATCH |
| 3 | HYPE/USD | 62.72 | 87.719 | 71.120 | +2.42% | +0.32% | 2.69x | 1.6 | 2026-11-22T21:00:59.863122+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | VVV/USD | 26.053 | 80.281 | 83.774 | +4.63% | +0.10% | 0.60x | 7.3 | 2026-11-22T21:00:59.863122+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | PUMP/USD | 0.002575 | 78.883 | 82.673 | +9.85% | +0.43% | 0.41x | 7.8 | 2026-11-22T21:00:59.863122+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | ETH/USD | 1717.86 | 74.245 | 69.776 | +2.12% | +0.33% | 1.28x | 0.1 | 2026-11-22T21:00:59.863122+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 7 | STBL/USD | 0.01707 | 73.224 | 67.501 | +6.66% | -0.10% | 1.62x | 17.0 | 2026-11-22T21:00:59.863122+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 8 | NEAR/USD | 2.9726 | 69.926 | 73.742 | +2.99% | +0.35% | 0.44x | 4.4 | 2026-11-22T21:00:59.863122+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XBT/USD | 60823.2 | 63.931 | 63.534 | +1.22% | +0.48% | 0.80x | 0.0 | 2026-11-22T21:00:59.863122+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 10 | WLD/USD | 0.2398 | 62.094 | 66.950 | +5.31% | +0.63% | 0.20x | 8.4 | 2026-11-22T21:00:59.863122+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 11 | LINK/USD | 8.79587 | 55.547 | 58.425 | +2.34% | +0.05% | 0.69x | 2.0 | 2026-11-22T21:00:59.863122+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | SUI/USD | 0.6553 | 54.302 | 62.550 | +1.24% | +0.15% | 0.10x | 1.5 | 2026-11-22T21:00:59.863122+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 91.938 | 0.04859 | +0.91% | 0.93x |
| 2 | VVV/USD | 83.774 | 26.053 | +0.10% | 0.60x |
| 3 | DRV/USD | 83.600 | 0.37387 | +0.22% | 3.00x |
| 4 | PUMP/USD | 82.673 | 0.002575 | +0.43% | 0.41x |
| 5 | NEAR/USD | 73.742 | 2.9726 | +0.35% | 0.44x |
| 6 | HYPE/USD | 71.120 | 62.72 | +0.32% | 2.69x |
| 7 | ETH/USD | 69.776 | 1717.86 | +0.33% | 1.28x |
| 8 | STBL/USD | 67.501 | 0.01707 | -0.10% | 1.62x |
| 9 | WLD/USD | 66.950 | 0.2398 | +0.63% | 0.20x |
| 10 | XBT/USD | 63.534 | 60823.2 | +0.48% | 0.80x |
| 11 | SUI/USD | 62.550 | 0.6553 | +0.15% | 0.10x |
| 12 | LINK/USD | 58.425 | 8.79587 | +0.05% | 0.69x |

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

- Persisted scans: 1335; predictions: 10939; observations: 808123.
- Matured sampled outcomes across 1/6/24/48h: 16665; gap abstentions: 22359. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45069513676 · **Generation:** 1335 · **Legacy run:** 45069513676
**Main quote time:** 2026-11-22T21:01:07.886061+00:00 · **Legacy report time:** 2026-11-22T21:02:00.487390+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.37387 | 99.71 | +0.22% | 3.00x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | NIGHT/USD | 0.04859 | 95.81 | +0.91% | 0.93x | STRONG 78/100 | HIGH 62/100 | Watch |
| 3 | HYPE/USD ⭐ | 62.72 | 87.72 | +0.32% | 2.69x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | VVV/USD | 26.053 | 80.28 | +0.10% | 0.60x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 5 | PUMP/USD | 0.002575 | 78.88 | +0.43% | 0.41x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 6 | ETH/USD ⭐ | 1717.86 | 74.25 | +0.33% | 1.28x | STRONG 82/100 | HIGH 55/100 | Watch |
| 7 | STBL/USD | 0.01707 | 73.22 | -0.10% | 1.62x | MODERATE 52/100 | VERY_HIGH 79/100 | Watch |
| 8 | NEAR/USD | 2.9726 | 69.93 | +0.35% | 0.44x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 9 | XBT/USD | 60823.2 | 63.93 | +0.48% | 0.80x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 10 | WLD/USD | 0.2398 | 62.09 | +0.63% | 0.20x | MODERATE 61/100 | VERY_HIGH 75/100 | Watch |
| 11 | LINK/USD | 8.79587 | 55.55 | +0.05% | 0.69x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 12 | SUI/USD | 0.6553 | 54.30 | +0.15% | 0.10x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.37387 | 87.20 | +0.22% | 3.00x | 17841 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HYPE/USD ⭐ | 62.72 | 82.33 | +0.32% | 2.69x | 9919 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ETH/USD ⭐ | 1716.88 | 78.68 | +0.33% | 1.28x | 38330 | STRONG 84/100 | HIGH 55/100 | Watch |

**Same-run overlap:** DRV/USD, HYPE/USD, ETH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
