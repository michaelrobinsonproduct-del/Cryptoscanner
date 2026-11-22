# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T00:21:07.539976+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44966060486
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** bdc221bda010dc0f32e6cee9aa80a12b5dcfd142 (atomic ledger/results publication)
**Ledger generation:** 1207 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZRO/USD | 1.186 | 61.805 | 43.409 | +1.11% | +0.68% | 4.33x | 8.5 | 2026-11-22T00:21:01.703587+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 2 | XMR/USD | 493.27 | 53.631 | 56.180 | +0.30% | +0.13% | 0.68x | 1.8 | 2026-11-22T00:21:01.703587+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | HYPE/USD | 61.43 | 49.733 | 56.358 | +0.31% | +0.20% | 0.24x | 1.6 | 2026-11-22T00:21:01.703587+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | ICNT/USD | 0.3508 | 46.346 | 33.858 | +0.98% | +0.69% | 1.90x | 14.2 | 2026-11-22T00:21:01.703587+00:00 | Not calibrated | MODERATE 63/100 | HIGH 66/100 | Watch | WATCH |
| 5 | ZBCN/USD | 0.00176 | 42.198 | 34.493 | +1.91% | +1.50% | 1.02x | 22.8 | 2026-11-22T00:21:01.703587+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 6 | BLESS/USD | 0.012407 | 33.101 | 33.245 | +0.58% | -1.08% | 1.53x | 21.0 | 2026-11-22T00:21:01.703587+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 77/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | HYPE/USD | 56.358 | 61.43 | +0.20% | 0.24x |
| 2 | XMR/USD | 56.180 | 493.27 | +0.13% | 0.68x |
| 3 | ZRO/USD | 43.409 | 1.186 | +0.68% | 4.33x |
| 4 | ZBCN/USD | 34.493 | 0.00176 | +1.50% | 1.02x |
| 5 | ICNT/USD | 33.858 | 0.3508 | +0.69% | 1.90x |
| 6 | BLESS/USD | 33.245 | 0.012407 | -1.08% | 1.53x |

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

- Persisted scans: 1207; predictions: 9770; observations: 730214.
- Matured sampled outcomes across 1/6/24/48h: 13215; gap abstentions: 21713. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44966060486 · **Generation:** 1207 · **Legacy run:** 44966060486
**Main quote time:** 2026-11-22T00:21:07.539976+00:00 · **Legacy report time:** 2026-11-22T00:21:56.480508+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZRO/USD ⭐ | 1.186 | 61.80 | +0.68% | 4.33x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD | 493.27 | 53.63 | +0.13% | 0.68x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 3 | HYPE/USD | 61.43 | 49.73 | +0.20% | 0.24x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 4 | ICNT/USD ⭐ | 0.3508 | 46.35 | +0.69% | 1.90x | STRONG 73/100 | HIGH 66/100 | Watch |
| 5 | ZBCN/USD ⭐ | 0.00176 | 42.20 | +1.50% | 1.02x | MODERATE 56/100 | VERY_HIGH 79/100 | Watch |
| 6 | BLESS/USD | 0.012407 | 33.10 | -1.08% | 1.53x | WEAK 27/100 | VERY_HIGH 77/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZBCN/USD ⭐ | 0.001762 | 52.43 | +1.50% | 1.02x | 3242 | MODERATE 61/100 | VERY_HIGH 79/100 | Watch |
| 2 | ZRO/USD ⭐ | 1.186 | 51.26 | +0.68% | 4.33x | 4042 | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 3 | ADA/USD | 0.144349 | 48.46 | +0.18% | 1.30x | 14364 | MODERATE 49/100 | HIGH 55/100 | Watch |
| 4 | ICNT/USD ⭐ | 0.3512 | 43.28 | +0.69% | 1.90x | 3658 | STRONG 72/100 | HIGH 66/100 | Watch |

**Same-run overlap:** ZRO/USD, ICNT/USD, ZBCN/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
