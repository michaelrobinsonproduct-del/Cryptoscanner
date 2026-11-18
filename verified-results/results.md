# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T17:00:11.222697+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44353569584
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** fc5c2a57c32f24dfaa914e1f69285e469eee4500 (atomic ledger/results publication)
**Ledger generation:** 618 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019744 | 71.227 | 69.594 | +5.76% | +1.19% | 0.57x | 3.5 | 2026-11-18T17:00:07.556499+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | TRUST/USD | 0.04929 | 66.977 | 51.875 | +4.54% | +0.02% | 2.77x | 24.4 | 2026-11-18T17:00:07.556499+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | ZAMA/USD | 0.06011 | 46.646 | 31.146 | +0.30% | +0.10% | 2.66x | 5.0 | 2026-11-18T17:00:07.556499+00:00 | Not calibrated | MODERATE 68/100 | HIGH 67/100 | Watch | WATCH |
| 4 | MEGA/USD | 0.05296 | 38.868 | 41.478 | +2.56% | -0.09% | 0.79x | 15.1 | 2026-11-18T17:00:07.556499+00:00 | Not calibrated | WEAK 19/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 69.594 | 0.019744 | +1.19% | 0.57x |
| 2 | TRUST/USD | 51.875 | 0.04929 | +0.02% | 2.77x |
| 3 | MEGA/USD | 41.478 | 0.05296 | -0.09% | 0.79x |
| 4 | ZAMA/USD | 31.146 | 0.06011 | +0.10% | 2.66x |

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

- Persisted scans: 618; predictions: 5281; observations: 373369.
- Matured sampled outcomes across 1/6/24/48h: 4544; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44353569584 · **Generation:** 618 · **Legacy run:** 44353569584
**Main quote time:** 2026-11-18T17:00:11.222697+00:00 · **Legacy report time:** 2026-11-18T17:00:32.706939+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.019744 | 71.23 | +1.19% | 0.57x | MODERATE 66/100 | VERY_HIGH 82/100 | Watch |
| 2 | TRUST/USD | 0.04929 | 66.98 | +0.02% | 2.77x | MODERATE 68/100 | VERY_HIGH 72/100 | Watch |
| 3 | ZAMA/USD ⭐ | 0.06011 | 46.65 | +0.10% | 2.66x | STRONG 78/100 | HIGH 67/100 | Watch |
| 4 | MEGA/USD | 0.05296 | 38.87 | -0.09% | 0.79x | WEAK 19/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZAMA/USD ⭐ | 0.06011 | 45.13 | +0.10% | 2.66x | 2933 | STRONG 78/100 | HIGH 67/100 | Watch |
| 2 | CC/USD | 0.08229 | 30.73 | +0.46% | 1.32x | 4902 | MODERATE 60/100 | HIGH 60/100 | Watch |

**Same-run overlap:** ZAMA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
