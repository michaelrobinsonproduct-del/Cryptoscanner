# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T00:41:01.012570+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44967693814
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 8a5c828d08c6219c31b2760d1728e7eba930cf51 (atomic ledger/results publication)
**Ledger generation:** 1209 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.399 | 88.517 | 65.484 | +2.00% | +1.61% | 3.04x | 7.1 | 2026-11-22T00:40:52.559456+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | SOL/USD | 70.36 | 64.365 | 56.185 | +0.27% | +0.07% | 1.78x | 1.4 | 2026-11-22T00:40:52.559456+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 3 | PROMPT/USD | 0.01118 | 51.617 | 43.672 | +3.71% | -1.41% | 8.65x | 27.0 | 2026-11-22T00:40:52.559456+00:00 | Not calibrated | MODERATE 46/100 | EXTREME 89/100 | Do nothing | WATCH |
| 4 | NIGHT/USD | 0.04441 | 50.942 | 46.150 | +0.29% | +0.50% | 1.23x | 6.8 | 2026-11-22T00:40:52.559456+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 5 | HYPE/USD | 61.42 | 50.316 | 55.430 | +0.29% | +0.15% | 0.42x | 3.3 | 2026-11-22T00:40:52.559456+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | CAP/USD | 0.092627 | 49.066 | 37.867 | +0.73% | +0.76% | 1.74x | 6.2 | 2026-11-22T00:40:52.559456+00:00 | Not calibrated | STRONG 70/100 | HIGH 60/100 | Watch | WATCH |
| 7 | BNB/USD | 549.06 | 40.313 | 45.580 | +0.30% | +0.09% | 0.43x | 1.6 | 2026-11-22T00:40:52.559456+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | MEGA/USD | 0.04828 | 32.050 | 31.508 | +0.81% | +0.84% | 0.64x | 10.4 | 2026-11-22T00:40:52.559456+00:00 | Not calibrated | WEAK 41/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 65.484 | 25.399 | +1.61% | 3.04x |
| 2 | SOL/USD | 56.185 | 70.36 | +0.07% | 1.78x |
| 3 | HYPE/USD | 55.430 | 61.42 | +0.15% | 0.42x |
| 4 | NIGHT/USD | 46.150 | 0.04441 | +0.50% | 1.23x |
| 5 | BNB/USD | 45.580 | 549.06 | +0.09% | 0.43x |
| 6 | PROMPT/USD | 43.672 | 0.01118 | -1.41% | 8.65x |
| 7 | CAP/USD | 37.867 | 0.092627 | +0.76% | 1.74x |
| 8 | MEGA/USD | 31.508 | 0.04828 | +0.84% | 0.64x |

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

- Persisted scans: 1209; predictions: 9781; observations: 731430.
- Matured sampled outcomes across 1/6/24/48h: 13267; gap abstentions: 21737. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 16; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44967693814 · **Generation:** 1209 · **Legacy run:** 44967693814
**Main quote time:** 2026-11-22T00:41:01.012570+00:00 · **Legacy report time:** 2026-11-22T00:42:06.025034+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.399 | 88.52 | +1.61% | 3.04x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SOL/USD ⭐ | 70.36 | 64.36 | +0.07% | 1.78x | STRONG 77/100 | HIGH 55/100 | Watch |
| 3 | PROMPT/USD | 0.01118 | 51.62 | -1.41% | 8.65x | MODERATE 46/100 | EXTREME 89/100 | Do nothing |
| 4 | NIGHT/USD | 0.04441 | 50.94 | +0.50% | 1.23x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 5 | HYPE/USD | 61.42 | 50.32 | +0.15% | 0.42x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 6 | CAP/USD ⭐ | 0.092627 | 49.07 | +0.76% | 1.74x | STRONG 80/100 | HIGH 60/100 | Consider small entry |
| 7 | BNB/USD | 549.06 | 40.31 | +0.09% | 0.43x | WEAK 40/100 | VERY_HIGH 70/100 | Watch |
| 8 | MEGA/USD | 0.04828 | 32.05 | +0.84% | 0.64x | WEAK 41/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.405 | 86.01 | +1.61% | 3.04x | 15962 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SOL/USD ⭐ | 70.38 | 56.09 | +0.07% | 1.78x | 45923 | STRONG 73/100 | HIGH 55/100 | Watch |
| 3 | PEPE/USD | 3.412e-06 | 46.76 | +0.35% | 3.65x | 5506 | STRONG 78/100 | HIGH 55/100 | Watch |
| 4 | CAP/USD ⭐ | 0.092627 | 42.42 | +0.76% | 1.74x | 7943 | STRONG 76/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** VVV/USD, SOL/USD, CAP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
