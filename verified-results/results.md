# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T20:42:19.670219+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46065124384
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** b57e6164a3c2b5308bd7d4a2b7bbb1aa82b73d2d (atomic ledger/results publication)
**Ledger generation:** 2058 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 740.68 | 114.766 | 98.582 | +8.66% | +0.24% | 3.83x | 2.8 | 2026-11-27T20:42:13.295453+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | SKY/USD | 0.05118 | 108.115 | 76.082 | +10.28% | +3.41% | 3.64x | 9.8 | 2026-11-27T20:42:13.295453+00:00 | Not calibrated | STRONG 100/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | HYPE/USD | 64.05 | 90.354 | 74.807 | +2.94% | +0.11% | 2.81x | 1.6 | 2026-11-27T20:42:13.295453+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 4 | UNI/USD | 4.8446 | 79.354 | 79.986 | +4.18% | +0.29% | 0.79x | 3.7 | 2026-11-27T20:42:13.295453+00:00 | Not calibrated | STRONG 70/100 | HIGH 62/100 | Watch | WATCH |
| 5 | INJ/USD | 6.396 | 71.243 | 63.002 | +3.29% | +0.69% | 1.48x | 4.7 | 2026-11-27T20:42:13.295453+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.05005 | 69.401 | 75.820 | +3.26% | -0.62% | 0.67x | 4.0 | 2026-11-27T20:42:13.295453+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0577322 | 67.189 | 71.781 | +2.41% | +0.29% | 0.40x | 0.2 | 2026-11-27T20:42:13.295453+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | PAXG/USD | 3643.13 | 66.420 | 59.295 | +2.43% | -0.02% | 1.72x | 1.6 | 2026-11-27T20:42:13.295453+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 9 | SOL/USD | 71.96 | 65.020 | 64.370 | +1.44% | +0.07% | 1.03x | 1.4 | 2026-11-27T20:42:13.295453+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 10 | RENDER/USD | 1.407 | 62.404 | 64.745 | +5.55% | +0.29% | 0.62x | 14.2 | 2026-11-27T20:42:13.295453+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 11 | SUI/USD | 0.6734 | 58.934 | 60.233 | +0.85% | +0.24% | 0.75x | 1.5 | 2026-11-27T20:42:13.295453+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 12 | PENGU/USD | 0.004471 | 55.949 | 44.859 | +2.03% | +0.43% | 1.90x | 2.2 | 2026-11-27T20:42:13.295453+00:00 | Not calibrated | STRONG 73/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.582 | 740.68 | +0.24% | 3.83x |
| 2 | UNI/USD | 79.986 | 4.8446 | +0.29% | 0.79x |
| 3 | SKY/USD | 76.082 | 0.05118 | +3.41% | 3.64x |
| 4 | NIGHT/USD | 75.820 | 0.05005 | -0.62% | 0.67x |
| 5 | HYPE/USD | 74.807 | 64.05 | +0.11% | 2.81x |
| 6 | XDG/USD | 71.781 | 0.0577322 | +0.29% | 0.40x |
| 7 | RENDER/USD | 64.745 | 1.407 | +0.29% | 0.62x |
| 8 | SOL/USD | 64.370 | 71.96 | +0.07% | 1.03x |
| 9 | INJ/USD | 63.002 | 6.396 | +0.69% | 1.48x |
| 10 | SUI/USD | 60.233 | 0.6734 | +0.24% | 0.75x |
| 11 | PAXG/USD | 59.295 | 3643.13 | -0.02% | 1.72x |
| 12 | PENGU/USD | 44.859 | 0.004471 | +0.43% | 1.90x |

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

- Persisted scans: 2058; predictions: 18398; observations: 1246199.
- Matured sampled outcomes across 1/6/24/48h: 41627; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46065124384 · **Generation:** 2058 · **Legacy run:** 46065124384
**Main quote time:** 2026-11-27T20:42:19.670219+00:00 · **Legacy report time:** 2026-11-27T20:43:05.018292+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 740.68 | 114.77 | +0.24% | 3.83x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SKY/USD ⭐ | 0.05118 | 108.11 | +3.41% | 3.64x | STRONG 100/100 | VERY_HIGH 70/100 | Watch |
| 3 | HYPE/USD ⭐ | 64.05 | 90.35 | +0.11% | 2.81x | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | UNI/USD | 4.8446 | 79.35 | +0.29% | 0.79x | STRONG 70/100 | HIGH 62/100 | Watch |
| 5 | INJ/USD ⭐ | 6.396 | 71.24 | +0.69% | 1.48x | STRONG 91/100 | HIGH 55/100 | Watch |
| 6 | NIGHT/USD | 0.05005 | 69.40 | -0.62% | 0.67x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 7 | XDG/USD | 0.0577322 | 67.19 | +0.29% | 0.40x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 8 | PAXG/USD | 3643.13 | 66.42 | -0.02% | 1.72x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 9 | SOL/USD ⭐ | 71.96 | 65.02 | +0.07% | 1.03x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 10 | RENDER/USD | 1.407 | 62.40 | +0.29% | 0.62x | MODERATE 56/100 | VERY_HIGH 81/100 | Watch |
| 11 | SUI/USD | 0.6734 | 58.93 | +0.24% | 0.75x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 12 | PENGU/USD | 0.004471 | 55.95 | +0.43% | 1.90x | STRONG 73/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 741.25 | 100.00 | +0.24% | 3.83x | 38709 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HYPE/USD ⭐ | 64.06 | 91.94 | +0.11% | 2.81x | 19638 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | SKY/USD ⭐ | 0.05127 | 89.60 | +3.41% | 3.64x | 6812 | STRONG 100/100 | VERY_HIGH 76/100 | Watch |
| 4 | INJ/USD ⭐ | 6.406 | 80.47 | +0.69% | 1.48x | 6131 | STRONG 95/100 | HIGH 55/100 | Watch |
| 5 | SOL/USD ⭐ | 71.96 | 66.80 | +0.07% | 1.03x | 45135 | MODERATE 68/100 | HIGH 62/100 | Watch |

**Same-run overlap:** ZEC/USD, SKY/USD, HYPE/USD, INJ/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
