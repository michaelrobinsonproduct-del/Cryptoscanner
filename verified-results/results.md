# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T11:01:09.972258+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45015075134
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** d00e407a4e82bf59a5307479830ef7ba659e3beb (atomic ledger/results publication)
**Ledger generation:** 1273 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INJ/USD | 6.222 | 87.686 | 68.799 | +4.17% | +0.78% | 6.06x | 4.8 | 2026-11-22T11:01:03.981547+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | PUMP/USD | 0.00246 | 84.417 | 70.836 | +4.95% | -0.28% | 10.73x | 12.2 | 2026-11-22T11:01:03.981547+00:00 | Not calibrated | MODERATE 67/100 | HIGH 67/100 | Watch | WATCH |
| 3 | NEAR/USD | 3.0043 | 79.404 | 79.787 | +4.09% | +0.82% | 0.55x | 7.7 | 2026-11-22T11:01:03.981547+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | JTO/USD | 0.23868 | 77.484 | 66.353 | +7.28% | +0.22% | 2.00x | 19.7 | 2026-11-22T11:01:03.981547+00:00 | Not calibrated | STRONG 89/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | LINK/USD | 8.80839 | 75.096 | 66.613 | +2.48% | +0.24% | 1.73x | 6.9 | 2026-11-22T11:01:03.981547+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | CRV/USD | 0.18419 | 73.752 | 63.029 | +3.27% | +0.15% | 2.00x | 10.3 | 2026-11-22T11:01:03.981547+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XLM/USD | 0.129693 | 70.260 | 53.757 | +0.70% | +0.30% | 3.18x | 4.2 | 2026-11-22T11:01:03.981547+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | SUI/USD | 0.6596 | 69.440 | 66.785 | +1.90% | +0.38% | 1.08x | 3.0 | 2026-11-22T11:01:03.981547+00:00 | Not calibrated | STRONG 70/100 | HIGH 62/100 | Watch | WATCH |
| 9 | TAO/USD | 190.6067 | 67.492 | 71.169 | +2.63% | +0.27% | 0.50x | 4.4 | 2026-11-22T11:01:03.981547+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XBT/USD | 60766.4 | 59.537 | 62.222 | +1.13% | +0.21% | 0.63x | 1.3 | 2026-11-22T11:01:03.981547+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | HYPE/USD | 62.28 | 59.197 | 65.281 | +1.70% | -0.08% | 0.43x | 3.2 | 2026-11-22T11:01:03.981547+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0554479 | 59.119 | 53.179 | +0.48% | +0.17% | 1.51x | 4.8 | 2026-11-22T11:01:03.981547+00:00 | Not calibrated | MODERATE 65/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 79.787 | 3.0043 | +0.82% | 0.55x |
| 2 | TAO/USD | 71.169 | 190.6067 | +0.27% | 0.50x |
| 3 | PUMP/USD | 70.836 | 0.00246 | -0.28% | 10.73x |
| 4 | INJ/USD | 68.799 | 6.222 | +0.78% | 6.06x |
| 5 | SUI/USD | 66.785 | 0.6596 | +0.38% | 1.08x |
| 6 | LINK/USD | 66.613 | 8.80839 | +0.24% | 1.73x |
| 7 | JTO/USD | 66.353 | 0.23868 | +0.22% | 2.00x |
| 8 | HYPE/USD | 65.281 | 62.28 | -0.08% | 0.43x |
| 9 | CRV/USD | 63.029 | 0.18419 | +0.15% | 2.00x |
| 10 | XBT/USD | 62.222 | 60766.4 | +0.21% | 0.63x |
| 11 | XLM/USD | 53.757 | 0.129693 | +0.30% | 3.18x |
| 12 | XDG/USD | 53.179 | 0.0554479 | +0.17% | 1.51x |

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

- Persisted scans: 1273; predictions: 10196; observations: 770366.
- Matured sampled outcomes across 1/6/24/48h: 14701; gap abstentions: 22199. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 60 (sampled only; not a success-rate estimate).
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

**Writer:** 45015075134 · **Generation:** 1273 · **Legacy run:** 45015075134
**Main quote time:** 2026-11-22T11:01:09.972258+00:00 · **Legacy report time:** 2026-11-22T11:02:13.463551+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 6.222 | 87.69 | +0.78% | 6.06x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | PUMP/USD | 0.00246 | 84.42 | -0.28% | 10.73x | MODERATE 67/100 | HIGH 67/100 | Watch |
| 3 | NEAR/USD | 3.0043 | 79.40 | +0.82% | 0.55x | STRONG 70/100 | VERY_HIGH 70/100 | Watch |
| 4 | JTO/USD | 0.23868 | 77.48 | +0.22% | 2.00x | STRONG 89/100 | VERY_HIGH 73/100 | Watch |
| 5 | LINK/USD ⭐ | 8.80839 | 75.10 | +0.24% | 1.73x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 6 | CRV/USD ⭐ | 0.18419 | 73.75 | +0.15% | 2.00x | STRONG 77/100 | HIGH 61/100 | Watch |
| 7 | XLM/USD | 0.129693 | 70.26 | +0.30% | 3.18x | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 8 | SUI/USD ⭐ | 0.6596 | 69.44 | +0.38% | 1.08x | STRONG 80/100 | HIGH 62/100 | Watch |
| 9 | TAO/USD | 190.6067 | 67.49 | +0.27% | 0.50x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 10 | XBT/USD | 60766.4 | 59.54 | +0.21% | 0.63x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 11 | HYPE/USD | 62.28 | 59.20 | -0.08% | 0.43x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | XDG/USD | 0.0554479 | 59.12 | +0.17% | 1.51x | MODERATE 65/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 6.222 | 87.55 | +0.78% | 6.06x | 6741 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | LINK/USD ⭐ | 8.80839 | 79.79 | +0.24% | 1.73x | 6297 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 3 | CRV/USD ⭐ | 0.18419 | 74.84 | +0.15% | 2.00x | 6901 | STRONG 77/100 | HIGH 61/100 | Watch |
| 4 | SUI/USD ⭐ | 0.6591 | 69.25 | +0.38% | 1.08x | 7729 | STRONG 80/100 | HIGH 62/100 | Watch |

**Same-run overlap:** INJ/USD, LINK/USD, CRV/USD, SUI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
