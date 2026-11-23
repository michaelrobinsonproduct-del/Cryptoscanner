# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T01:41:30.742937+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45095797535
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 4bd706dcaa864a1a6dd15483c5d0fcf9206cb167 (atomic ledger/results publication)
**Ledger generation:** 1363 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BLESS/USD | 0.017001 | 69.534 | 55.591 | +5.64% | +2.10% | 1.34x | 44.9 | 2026-11-23T01:41:25.338486+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 2 | DRV/USD | 0.38692 | 66.910 | 71.661 | +4.90% | -0.01% | 0.53x | 15.8 | 2026-11-23T01:41:25.338486+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 3 | PAXG/USD | 3595.65 | 62.515 | 48.119 | +0.66% | -0.12% | 5.26x | 1.5 | 2026-11-23T01:41:25.338486+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 4 | CPOOL/USD | 0.02278 | 54.926 | 42.262 | +2.02% | +2.42% | 1.06x | 8.8 | 2026-11-23T01:41:25.338486+00:00 | Not calibrated | MODERATE 62/100 | HIGH 67/100 | Watch | WATCH |
| 5 | PEARL/USD | 2.105 | 39.625 | 49.429 | +2.46% | -0.42% | 0.23x | 18.6 | 2026-11-23T01:41:25.338486+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 6 | ICNT/USD | 0.3563 | 38.917 | 32.739 | +1.16% | -1.76% | 2.73x | 16.8 | 2026-11-23T01:41:25.338486+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | XAUT/USD | 3593.5 | 35.638 | 36.255 | +0.60% | -0.14% | 1.01x | 1.7 | 2026-11-23T01:41:25.338486+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 8 | CC/USD | 0.0737 | 35.114 | 36.795 | +0.59% | +0.41% | 0.63x | 5.4 | 2026-11-23T01:41:25.338486+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | SPX/USD | 0.2844 | 25.440 | 25.985 | +0.67% | +0.42% | 0.73x | 21.1 | 2026-11-23T01:41:25.338486+00:00 | Not calibrated | WEAK 33/100 | EXTREME 87/100 | Do nothing | WATCH |
| 10 | AUD/USD | 0.66429 | 21.537 | 32.812 | +0.41% | -0.55% | 0.15x | 18.8 | 2026-11-23T01:41:25.338486+00:00 | Not calibrated | WEAK 11/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 71.661 | 0.38692 | -0.01% | 0.53x |
| 2 | BLESS/USD | 55.591 | 0.017001 | +2.10% | 1.34x |
| 3 | PEARL/USD | 49.429 | 2.105 | -0.42% | 0.23x |
| 4 | PAXG/USD | 48.119 | 3595.65 | -0.12% | 5.26x |
| 5 | CPOOL/USD | 42.262 | 0.02278 | +2.42% | 1.06x |
| 6 | CC/USD | 36.795 | 0.0737 | +0.41% | 0.63x |
| 7 | XAUT/USD | 36.255 | 3593.5 | -0.14% | 1.01x |
| 8 | AUD/USD | 32.812 | 0.66429 | -0.55% | 0.15x |
| 9 | ICNT/USD | 32.739 | 0.3563 | -1.76% | 2.73x |
| 10 | SPX/USD | 25.985 | 0.2844 | +0.42% | 0.73x |

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

- Persisted scans: 1363; predictions: 11189; observations: 825173.
- Matured sampled outcomes across 1/6/24/48h: 17752; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 76 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45095797535 · **Generation:** 1363 · **Legacy run:** 45095797535
**Main quote time:** 2026-11-23T01:41:30.742937+00:00 · **Legacy report time:** 2026-11-23T01:42:30.445524+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BLESS/USD | 0.017001 | 69.53 | +2.10% | 1.34x | MODERATE 65/100 | VERY_HIGH 77/100 | Watch |
| 2 | DRV/USD | 0.38692 | 66.91 | -0.01% | 0.53x | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing |
| 3 | PAXG/USD | 3595.65 | 62.52 | -0.12% | 5.26x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 4 | CPOOL/USD ⭐ | 0.02278 | 54.93 | +2.42% | 1.06x | STRONG 72/100 | HIGH 67/100 | Watch |
| 5 | PEARL/USD | 2.105 | 39.63 | -0.42% | 0.23x | WEAK 20/100 | VERY_HIGH 82/100 | Do nothing |
| 6 | ICNT/USD | 0.3563 | 38.92 | -1.76% | 2.73x | WEAK 44/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | XAUT/USD | 3593.5 | 35.64 | -0.14% | 1.01x | WEAK 28/100 | VERY_HIGH 73/100 | Do nothing |
| 8 | CC/USD | 0.0737 | 35.11 | +0.41% | 0.63x | MODERATE 48/100 | VERY_HIGH 75/100 | Watch |
| 9 | SPX/USD | 0.2844 | 25.44 | +0.42% | 0.73x | WEAK 33/100 | EXTREME 87/100 | Do nothing |
| 10 | AUD/USD | 0.66429 | 21.54 | -0.55% | 0.15x | WEAK 11/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CPOOL/USD ⭐ | 0.02259 | 44.98 | +2.42% | 1.06x | 9967 | MODERATE 62/100 | VERY_HIGH 73/100 | Watch |
| 2 | WINGS/USD | 0.001921 | 40.17 | +2.56% | 1.27x | 7518 | MODERATE 50/100 | HIGH 66/100 | Watch |

**Same-run overlap:** CPOOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
