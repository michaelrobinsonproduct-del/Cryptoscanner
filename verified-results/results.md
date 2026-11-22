# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T05:00:54.676301+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44987416031
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** d896679d971694f2c27075efb2a44920fbb62645 (atomic ledger/results publication)
**Ledger generation:** 1236 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.33982 | 60.175 | 46.457 | +1.38% | +1.40% | 1.67x | 18.3 | 2026-11-22T05:00:51.769165+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 2 | TRUMP/USD | 0.89 | 47.263 | 32.263 | +0.45% | +0.00% | 3.10x | 11.2 | 2026-11-22T05:00:51.769165+00:00 | Not calibrated | MODERATE 64/100 | HIGH 66/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04442 | 39.575 | 46.783 | +0.32% | -0.18% | 0.37x | 6.8 | 2026-11-22T05:00:51.769165+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | SPX/USD | 0.2806 | 23.898 | 19.519 | +0.43% | +0.07% | 1.40x | 32.1 | 2026-11-22T05:00:51.769165+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 72/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 46.783 | 0.04442 | -0.18% | 0.37x |
| 2 | DRV/USD | 46.457 | 0.33982 | +1.40% | 1.67x |
| 3 | TRUMP/USD | 32.263 | 0.89 | +0.00% | 3.10x |
| 4 | SPX/USD | 19.519 | 0.2806 | +0.07% | 1.40x |

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

- Persisted scans: 1236; predictions: 9917; observations: 747846.
- Matured sampled outcomes across 1/6/24/48h: 14048; gap abstentions: 21977. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 39 (sampled only; not a success-rate estimate).
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

**Writer:** 44987416031 · **Generation:** 1236 · **Legacy run:** 44987416031
**Main quote time:** 2026-11-22T05:00:54.676301+00:00 · **Legacy report time:** 2026-11-22T05:01:40.487151+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.33982 | 60.18 | +1.40% | 1.67x | STRONG 80/100 | HIGH 61/100 | Consider small entry |
| 2 | TRUMP/USD | 0.89 | 47.26 | +0.00% | 3.10x | MODERATE 64/100 | HIGH 66/100 | Watch |
| 3 | NIGHT/USD | 0.04442 | 39.58 | -0.18% | 0.37x | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | SPX/USD ⭐ | 0.2806 | 23.90 | +0.07% | 1.40x | MODERATE 47/100 | VERY_HIGH 72/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.33982 | 55.00 | +1.40% | 1.67x | 15279 | STRONG 77/100 | HIGH 61/100 | Consider small entry |
| 2 | SPX/USD ⭐ | 0.2804 | 21.54 | +0.07% | 1.40x | 1666 | MODERATE 46/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** DRV/USD, SPX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
