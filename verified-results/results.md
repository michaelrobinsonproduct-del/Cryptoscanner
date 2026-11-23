# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T14:01:39.600553+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45189427112
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1e1fe44d13e4756dc413bc059d57cd72296b5c1a (atomic ledger/results publication)
**Ledger generation:** 1439 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SOL/USD | 75.75 | 138.679 | 98.679 | +7.25% | +5.50% | 9.97x | 2.6 | 2026-11-23T14:01:33.244181+00:00 | Not calibrated | STRONG 100/100 | HIGH 65/100 | Consider small entry | WATCH |
| 2 | SUI/USD | 0.7021 | 135.019 | 95.019 | +7.08% | +5.87% | 3.68x | 10.0 | 2026-11-23T14:01:33.244181+00:00 | Not calibrated | STRONG 100/100 | HIGH 65/100 | Consider small entry | WATCH |
| 3 | HYPE/USD | 66.7 | 131.260 | 93.906 | +5.77% | +4.47% | 8.26x | 3.0 | 2026-11-23T14:01:33.244181+00:00 | Not calibrated | STRONG 100/100 | HIGH 65/100 | Consider small entry | WATCH |
| 4 | XRP/USD | 0.97753 | 126.018 | 86.018 | +5.39% | +5.00% | 15.20x | 13.4 | 2026-11-23T14:01:33.244181+00:00 | Not calibrated | STRONG 100/100 | VERY_HIGH 71/100 | Watch | WATCH |
| 5 | XDG/USD | 0.0579513 | 122.407 | 82.572 | +4.83% | +4.97% | 26.20x | 7.5 | 2026-11-23T14:01:33.244181+00:00 | Not calibrated | STRONG 100/100 | HIGH 65/100 | Consider small entry | WATCH |
| 6 | NEAR/USD | 3.1134 | 121.781 | 81.903 | +4.42% | +4.98% | 13.53x | 8.0 | 2026-11-23T14:01:33.244181+00:00 | Not calibrated | STRONG 100/100 | HIGH 65/100 | Consider small entry | WATCH |
| 7 | INJ/USD | 6.646 | 121.673 | 81.673 | +6.71% | +5.08% | 3.89x | 10.5 | 2026-11-23T14:01:33.244181+00:00 | Not calibrated | STRONG 100/100 | VERY_HIGH 71/100 | Watch | WATCH |
| 8 | ETH/USD | 1797.36 | 120.872 | 80.872 | +4.40% | +5.05% | 6.66x | 9.9 | 2026-11-23T14:01:33.244181+00:00 | Not calibrated | STRONG 100/100 | HIGH 65/100 | Consider small entry | WATCH |
| 9 | ZEC/USD | 840.53 | 119.601 | 79.601 | +5.39% | +6.61% | 34.51x | 26.3 | 2026-11-23T14:01:33.244181+00:00 | Not calibrated | STRONG 95/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 10 | ADA/USD | 0.150304 | 114.671 | 78.638 | +3.94% | +4.21% | 7.69x | 7.9 | 2026-11-23T14:01:33.244181+00:00 | Not calibrated | STRONG 100/100 | HIGH 65/100 | Consider small entry | WATCH |
| 11 | LTC/USD | 42.25 | 114.613 | 80.364 | +5.20% | +3.85% | 5.02x | 2.4 | 2026-11-23T14:01:33.244181+00:00 | Not calibrated | STRONG 100/100 | HIGH 65/100 | Consider small entry | WATCH |
| 12 | CC/USD | 0.07878 | 110.882 | 78.374 | +7.52% | +3.50% | 4.14x | 3.8 | 2026-11-23T14:01:33.244181+00:00 | Not calibrated | STRONG 100/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SOL/USD | 98.679 | 75.75 | +5.50% | 9.97x |
| 2 | SUI/USD | 95.019 | 0.7021 | +5.87% | 3.68x |
| 3 | HYPE/USD | 93.906 | 66.7 | +4.47% | 8.26x |
| 4 | XRP/USD | 86.018 | 0.97753 | +5.00% | 15.20x |
| 5 | XDG/USD | 82.572 | 0.0579513 | +4.97% | 26.20x |
| 6 | NEAR/USD | 81.903 | 3.1134 | +4.98% | 13.53x |
| 7 | INJ/USD | 81.673 | 6.646 | +5.08% | 3.89x |
| 8 | ETH/USD | 80.872 | 1797.36 | +5.05% | 6.66x |
| 9 | LTC/USD | 80.364 | 42.25 | +3.85% | 5.02x |
| 10 | ZEC/USD | 79.601 | 840.53 | +6.61% | 34.51x |
| 11 | ADA/USD | 78.638 | 0.150304 | +4.21% | 7.69x |
| 12 | CC/USD | 78.374 | 0.07878 | +3.50% | 4.14x |

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

- Persisted scans: 1439; predictions: 12035; observations: 871453.
- Matured sampled outcomes across 1/6/24/48h: 20381; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45189427112 · **Generation:** 1439 · **Legacy run:** 45189427112
**Main quote time:** 2026-11-23T14:01:39.600553+00:00 · **Legacy report time:** 2026-11-23T14:02:42.294466+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD ⭐ | 75.75 | 138.68 | +5.50% | 9.97x | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 2 | SUI/USD ⭐ | 0.7021 | 135.02 | +5.87% | 3.68x | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 3 | HYPE/USD ⭐ | 66.7 | 131.26 | +4.47% | 8.26x | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 4 | XRP/USD ⭐ | 0.97753 | 126.02 | +5.00% | 15.20x | STRONG 100/100 | VERY_HIGH 71/100 | Watch |
| 5 | XDG/USD ⭐ | 0.0579513 | 122.41 | +4.97% | 26.20x | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 6 | NEAR/USD ⭐ | 3.1134 | 121.78 | +4.98% | 13.53x | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 7 | INJ/USD | 6.646 | 121.67 | +5.08% | 3.89x | STRONG 100/100 | VERY_HIGH 71/100 | Watch |
| 8 | ETH/USD ⭐ | 1797.36 | 120.87 | +5.05% | 6.66x | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 9 | ZEC/USD | 840.53 | 119.60 | +6.61% | 34.51x | STRONG 95/100 | VERY_HIGH 77/100 | Watch |
| 10 | ADA/USD ⭐ | 0.150304 | 114.67 | +4.21% | 7.69x | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 11 | LTC/USD | 42.25 | 114.61 | +3.85% | 5.02x | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 12 | CC/USD | 0.07878 | 110.88 | +3.50% | 4.14x | STRONG 100/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.150627 | 100.00 | +4.21% | 7.69x | 8627 | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 2 | ETH/USD ⭐ | 1800.67 | 100.00 | +5.05% | 6.66x | 42725 | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 3 | HYPE/USD ⭐ | 67.01 | 100.00 | +4.47% | 8.26x | 10896 | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 4 | LINK/USD | 9.28434 | 100.00 | +4.53% | 21.03x | 4879 | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 5 | NEAR/USD ⭐ | 3.1302 | 100.00 | +4.98% | 13.53x | 12718 | STRONG 100/100 | VERY_HIGH 71/100 | Watch |
| 6 | SOL/USD ⭐ | 75.94 | 100.00 | +5.50% | 9.97x | 32463 | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 7 | SUI/USD ⭐ | 0.7045 | 100.00 | +5.87% | 3.68x | 6866 | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 8 | XBT/USD | 63385 | 100.00 | +4.21% | 8.48x | 128119 | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 9 | XDG/USD ⭐ | 0.05816 | 100.00 | +4.97% | 26.20x | 6604 | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 10 | XLM/USD | 0.13306 | 100.00 | +3.88% | 3.03x | 16553 | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 11 | XMR/USD | 513.11 | 100.00 | +3.30% | 6.57x | 8666 | STRONG 100/100 | VERY_HIGH 71/100 | Watch |
| 12 | XRP/USD ⭐ | 0.97833 | 100.00 | +5.00% | 15.20x | 22710 | STRONG 100/100 | HIGH 65/100 | Consider small entry |

**Same-run overlap:** SOL/USD, SUI/USD, HYPE/USD, XRP/USD, XDG/USD, NEAR/USD, ETH/USD, ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
