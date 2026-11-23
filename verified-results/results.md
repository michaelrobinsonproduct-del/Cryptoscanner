# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T08:01:40.832154+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45135097997
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 920aa2b251f71f3cffe856b5d6342f34c5759a06 (atomic ledger/results publication)
**Ledger generation:** 1402 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | KAS/USD | 0.02722 | 80.419 | 66.471 | +5.46% | +0.59% | 2.10x | 11.0 | 2026-11-23T08:01:32.141295+00:00 | Not calibrated | STRONG 90/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | SUI/USD | 0.6666 | 80.212 | 65.886 | +1.66% | -0.13% | 8.81x | 1.5 | 2026-11-23T08:01:32.141295+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XLM/USD | 0.128922 | 66.603 | 62.388 | +1.09% | -0.04% | 1.44x | 0.1 | 2026-11-23T08:01:32.141295+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SOL/USD | 72.02 | 64.174 | 68.082 | +1.97% | -0.01% | 0.62x | 1.4 | 2026-11-23T08:01:32.141295+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | BLESS/USD | 0.017721 | 62.560 | 67.728 | +10.12% | -0.62% | 0.79x | 31.6 | 2026-11-23T08:01:32.141295+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 6 | XRP/USD | 0.93615 | 57.725 | 61.444 | +0.93% | -0.08% | 0.67x | 0.1 | 2026-11-23T08:01:32.141295+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | XBT/USD | 61398.3 | 55.752 | 57.603 | +0.37% | -0.06% | 0.84x | 0.0 | 2026-11-23T08:01:32.141295+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 8 | NIGHT/USD | 0.05015 | 55.502 | 60.945 | +1.99% | -0.57% | 0.74x | 8.0 | 2026-11-23T08:01:32.141295+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | XMR/USD | 497.97 | 52.436 | 60.538 | +0.86% | -0.49% | 0.43x | 1.0 | 2026-11-23T08:01:32.141295+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | NEAR/USD | 3.0129 | 51.122 | 60.500 | +1.05% | -0.05% | 0.09x | 3.6 | 2026-11-23T08:01:32.141295+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | ADA/USD | 0.146112 | 51.008 | 55.612 | +1.04% | -0.22% | 0.65x | 0.9 | 2026-11-23T08:01:32.141295+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | PAXG/USD | 3607.46 | 46.363 | 51.251 | +0.99% | -0.15% | 0.58x | 1.0 | 2026-11-23T08:01:32.141295+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SOL/USD | 68.082 | 72.02 | -0.01% | 0.62x |
| 2 | BLESS/USD | 67.728 | 0.017721 | -0.62% | 0.79x |
| 3 | KAS/USD | 66.471 | 0.02722 | +0.59% | 2.10x |
| 4 | SUI/USD | 65.886 | 0.6666 | -0.13% | 8.81x |
| 5 | XLM/USD | 62.388 | 0.128922 | -0.04% | 1.44x |
| 6 | XRP/USD | 61.444 | 0.93615 | -0.08% | 0.67x |
| 7 | NIGHT/USD | 60.945 | 0.05015 | -0.57% | 0.74x |
| 8 | XMR/USD | 60.538 | 497.97 | -0.49% | 0.43x |
| 9 | NEAR/USD | 60.500 | 3.0129 | -0.05% | 0.09x |
| 10 | XBT/USD | 57.603 | 61398.3 | -0.06% | 0.84x |
| 11 | ADA/USD | 55.612 | 0.146112 | -0.22% | 0.65x |
| 12 | PAXG/USD | 51.251 | 3607.46 | -0.15% | 0.58x |

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

- Persisted scans: 1402; predictions: 11591; observations: 848922.
- Matured sampled outcomes across 1/6/24/48h: 18881; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 127 (sampled only; not a success-rate estimate).
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

**Writer:** 45135097997 · **Generation:** 1402 · **Legacy run:** 45135097997
**Main quote time:** 2026-11-23T08:01:40.832154+00:00 · **Legacy report time:** 2026-11-23T08:02:49.320210+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | KAS/USD ⭐ | 0.02722 | 80.42 | +0.59% | 2.10x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | SUI/USD | 0.6666 | 80.21 | -0.13% | 8.81x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | XLM/USD | 0.128922 | 66.60 | -0.04% | 1.44x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 4 | SOL/USD | 72.02 | 64.17 | -0.01% | 0.62x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 5 | BLESS/USD | 0.017721 | 62.56 | -0.62% | 0.79x | WEAK 26/100 | VERY_HIGH 80/100 | Do nothing |
| 6 | XRP/USD | 0.93615 | 57.72 | -0.08% | 0.67x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | XBT/USD | 61398.3 | 55.75 | -0.06% | 0.84x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 8 | NIGHT/USD | 0.05015 | 55.50 | -0.57% | 0.74x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | XMR/USD | 497.97 | 52.44 | -0.49% | 0.43x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | NEAR/USD | 3.0129 | 51.12 | -0.05% | 0.09x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | ADA/USD | 0.146112 | 51.01 | -0.22% | 0.65x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | PAXG/USD | 3607.46 | 46.36 | -0.15% | 0.58x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | KAS/USD ⭐ | 0.02726 | 78.42 | +0.59% | 2.10x | 2818 | STRONG 99/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** KAS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
