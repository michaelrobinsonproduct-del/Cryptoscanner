# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T03:01:15.151718+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45103299834
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 514e20eb3be209639cb340b4f5cb161fe141d363 (atomic ledger/results publication)
**Ledger generation:** 1372 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.3673 | 56.021 | 53.688 | +4.29% | +0.16% | 1.15x | 19.1 | 2026-11-23T03:01:11.796782+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | AUD/USD | 0.66329 | 53.642 | 39.849 | +0.26% | +0.04% | 2.36x | 4.7 | 2026-11-23T03:01:11.796782+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 3 | DRV/USD | 0.3698 | 46.534 | 46.403 | +0.26% | -0.66% | 1.34x | 0.3 | 2026-11-23T03:01:11.796782+00:00 | Not calibrated | WEAK 43/100 | HIGH 61/100 | Watch | WATCH |
| 4 | BLESS/USD | 0.016859 | 45.349 | 50.471 | +4.76% | -0.22% | 0.60x | 42.9 | 2026-11-23T03:01:11.796782+00:00 | Not calibrated | WEAK 13/100 | EXTREME 98/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ICNT/USD | 53.688 | 0.3673 | +0.16% | 1.15x |
| 2 | BLESS/USD | 50.471 | 0.016859 | -0.22% | 0.60x |
| 3 | DRV/USD | 46.403 | 0.3698 | -0.66% | 1.34x |
| 4 | AUD/USD | 39.849 | 0.66329 | +0.04% | 2.36x |

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

- Persisted scans: 1372; predictions: 11235; observations: 830653.
- Matured sampled outcomes across 1/6/24/48h: 18061; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 88 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45103299834 · **Generation:** 1372 · **Legacy run:** 45103299834
**Main quote time:** 2026-11-23T03:01:15.151718+00:00 · **Legacy report time:** 2026-11-23T03:02:00.793405+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.3673 | 56.02 | +0.16% | 1.15x | MODERATE 58/100 | VERY_HIGH 73/100 | Watch |
| 2 | AUD/USD | 0.66329 | 53.64 | +0.04% | 2.36x | STRONG 72/100 | HIGH 55/100 | Watch |
| 3 | DRV/USD | 0.3698 | 46.53 | -0.66% | 1.34x | WEAK 43/100 | HIGH 61/100 | Watch |
| 4 | BLESS/USD | 0.016859 | 45.35 | -0.22% | 0.60x | WEAK 13/100 | EXTREME 98/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.3653 | 69.65 | +0.16% | 1.15x | 2670 | MODERATE 60/100 | VERY_HIGH 79/100 | Watch |
| 2 | PAXG/USD | 3579.09 | 48.53 | +0.27% | 1.46x | 7048 | MODERATE 69/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ICNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
