# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T14:30:48.227558+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44753956751
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** d90b19d56a9be35132144d8f704ecf201207c2ca (atomic ledger/results publication)
**Ledger generation:** 991 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 607; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.022222 | 59.710 | 59.486 | +4.38% | +0.31% | 0.87x | 6.8 | 2026-11-20T14:30:42.769209+00:00 | Not calibrated | MODERATE 60/100 | HIGH 67/100 | Watch | WATCH |
| 2 | BLESS/USD | 0.013043 | 56.050 | 59.340 | +7.00% | +0.84% | 0.25x | 41.7 | 2026-11-20T14:30:42.769209+00:00 | Not calibrated | WEAK 43/100 | EXTREME 97/100 | Do nothing | WATCH |
| 3 | MON/USD | 0.01398 | 55.559 | 37.694 | +1.60% | +0.57% | 3.63x | 14.3 | 2026-11-20T14:30:42.769209+00:00 | Not calibrated | STRONG 78/100 | HIGH 66/100 | Watch | WATCH |
| 4 | DOS/USD | 0.1937 | 36.867 | 56.727 | +5.56% | -2.76% | 0.39x | 25.8 | 2026-11-20T14:30:42.769209+00:00 | Not calibrated | WEAK 13/100 | EXTREME 100/100 | Do nothing | WATCH |
| 5 | MNT/USD | 0.3943 | 34.412 | 27.934 | +0.69% | +0.13% | 1.58x | 15.2 | 2026-11-20T14:30:42.769209+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | CAP/USD | 0.097583 | 24.418 | 30.556 | +1.00% | +0.29% | 0.24x | 19.3 | 2026-11-20T14:30:42.769209+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | ICNT/USD | 0.4297 | 17.629 | 26.897 | +0.84% | -0.07% | 0.11x | 32.6 | 2026-11-20T14:30:42.769209+00:00 | Not calibrated | WEAK 4/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 59.486 | 0.022222 | +0.31% | 0.87x |
| 2 | BLESS/USD | 59.340 | 0.013043 | +0.84% | 0.25x |
| 3 | DOS/USD | 56.727 | 0.1937 | -2.76% | 0.39x |
| 4 | MON/USD | 37.694 | 0.01398 | +0.57% | 3.63x |
| 5 | CAP/USD | 30.556 | 0.097583 | +0.29% | 0.24x |
| 6 | MNT/USD | 27.934 | 0.3943 | +0.13% | 1.58x |
| 7 | ICNT/USD | 26.897 | 0.4297 | -0.07% | 0.11x |

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

- Persisted scans: 991; predictions: 8257; observations: 598891.
- Matured sampled outcomes across 1/6/24/48h: 10135; gap abstentions: 17612. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44753956751 · **Generation:** 991 · **Legacy run:** 44753956751
**Main quote time:** 2026-11-20T14:30:48.227558+00:00 · **Legacy report time:** 2026-11-20T14:31:32.733341+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.022222 | 59.71 | +0.31% | 0.87x | MODERATE 60/100 | HIGH 67/100 | Watch |
| 2 | BLESS/USD | 0.013043 | 56.05 | +0.84% | 0.25x | WEAK 43/100 | EXTREME 97/100 | Do nothing |
| 3 | MON/USD ⭐ | 0.01398 | 55.56 | +0.57% | 3.63x | STRONG 88/100 | HIGH 66/100 | Consider small entry |
| 4 | DOS/USD | 0.1937 | 36.87 | -2.76% | 0.39x | WEAK 13/100 | EXTREME 100/100 | Do nothing |
| 5 | MNT/USD | 0.3943 | 34.41 | +0.13% | 1.58x | MODERATE 47/100 | VERY_HIGH 73/100 | Watch |
| 6 | CAP/USD | 0.097583 | 24.42 | +0.29% | 0.24x | WEAK 37/100 | VERY_HIGH 81/100 | Watch |
| 7 | ICNT/USD | 0.4297 | 17.63 | -0.07% | 0.11x | WEAK 4/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.014 | 54.85 | +0.57% | 3.63x | 3548 | STRONG 87/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** MON/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
