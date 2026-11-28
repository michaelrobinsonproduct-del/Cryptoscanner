# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T16:52:44.441910+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46167206808
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8e46d601ea417d564450414b45819b71c484e358 (atomic ledger/results publication)
**Ledger generation:** 2180 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 417.18 | 78.183 | 66.400 | +2.43% | +0.44% | 1.96x | 11.3 | 2026-11-28T16:52:40.683071+00:00 | Not calibrated | STRONG 79/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | NIGHT/USD | 0.05145 | 62.168 | 67.711 | +2.41% | +0.06% | 0.42x | 5.8 | 2026-11-28T16:52:40.683071+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | VVV/USD | 26.585 | 57.549 | 60.541 | +3.25% | +0.43% | 0.48x | 8.3 | 2026-11-28T16:52:40.683071+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | LUNA/USD | 4.749e-05 | 47.397 | 56.002 | +4.17% | +0.15% | 0.07x | 8.4 | 2026-11-28T16:52:40.683071+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | SENT/USD | 0.023803 | 22.642 | 30.148 | +0.38% | -0.26% | 0.38x | 7.6 | 2026-11-28T16:52:40.683071+00:00 | Not calibrated | WEAK 16/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 67.711 | 0.05145 | +0.06% | 0.42x |
| 2 | XMR/USD | 66.400 | 417.18 | +0.44% | 1.96x |
| 3 | VVV/USD | 60.541 | 26.585 | +0.43% | 0.48x |
| 4 | LUNA/USD | 56.002 | 4.749e-05 | +0.15% | 0.07x |
| 5 | SENT/USD | 30.148 | 0.023803 | -0.26% | 0.38x |

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

- Persisted scans: 2180; predictions: 19326; observations: 1320126.
- Matured sampled outcomes across 1/6/24/48h: 46783; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 157 (sampled only; not a success-rate estimate).
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

**Writer:** 46167206808 · **Generation:** 2180 · **Legacy run:** 46167206808
**Main quote time:** 2026-11-28T16:52:44.441910+00:00 · **Legacy report time:** 2026-11-28T16:53:22.549935+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 417.18 | 78.18 | +0.44% | 1.96x | STRONG 89/100 | HIGH 61/100 | Consider small entry |
| 2 | NIGHT/USD | 0.05145 | 62.17 | +0.06% | 0.42x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 3 | VVV/USD | 26.585 | 57.55 | +0.43% | 0.48x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 4 | LUNA/USD | 4.749e-05 | 47.40 | +0.15% | 0.07x | WEAK 44/100 | VERY_HIGH 82/100 | Watch |
| 5 | SENT/USD | 0.023803 | 22.64 | -0.26% | 0.38x | WEAK 16/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 417.18 | 76.30 | +0.44% | 1.96x | 15420 | STRONG 93/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
