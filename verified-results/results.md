# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T05:01:33.094971+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45115027766
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** ae41b8c9266da520c342e5e2bb3a373289207550 (atomic ledger/results publication)
**Ledger generation:** 1384 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 501.88 | 79.318 | 63.392 | +1.65% | +0.43% | 2.38x | 6.4 | 2026-11-23T05:01:24.581174+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NIGHT/USD | 0.04993 | 73.156 | 58.298 | +1.55% | +0.38% | 2.29x | 6.0 | 2026-11-23T05:01:24.581174+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | JUP/USD | 0.23184 | 63.258 | 50.397 | +3.24% | +0.49% | 2.04x | 12.1 | 2026-11-23T05:01:24.581174+00:00 | Not calibrated | STRONG 82/100 | HIGH 66/100 | Watch | WATCH |
| 4 | AI/USD | 0.01584 | 61.589 | 69.718 | +8.34% | -1.26% | 0.81x | 12.7 | 2026-11-23T05:01:24.581174+00:00 | Not calibrated | WEAK 31/100 | EXTREME 90/100 | Do nothing | WATCH |
| 5 | LTC/USD | 40.34 | 60.153 | 45.277 | +0.45% | -0.02% | 2.51x | 2.5 | 2026-11-23T05:01:24.581174+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 6 | LINK/USD | 8.89114 | 60.074 | 46.935 | +0.91% | -0.02% | 2.32x | 6.1 | 2026-11-23T05:01:24.581174+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 7 | NEAR/USD | 3.0018 | 58.456 | 57.723 | +0.67% | -0.38% | 1.26x | 4.0 | 2026-11-23T05:01:24.581174+00:00 | Not calibrated | WEAK 39/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ETH/USD | 1726.62 | 54.910 | 57.008 | +0.29% | +0.00% | 0.79x | 0.1 | 2026-11-23T05:01:24.581174+00:00 | Not calibrated | MODERATE 47/100 | HIGH 62/100 | Watch | WATCH |
| 9 | SOL/USD | 71.34 | 54.479 | 61.336 | +1.01% | -0.01% | 0.32x | 1.4 | 2026-11-23T05:01:24.581174+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | SUI/USD | 0.6602 | 53.410 | 59.047 | +0.69% | -0.03% | 0.45x | 1.5 | 2026-11-23T05:01:24.581174+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | XRP/USD | 0.93298 | 52.548 | 58.570 | +0.59% | -0.02% | 0.41x | 1.1 | 2026-11-23T05:01:24.581174+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | DOT/USD | 0.6638 | 48.318 | 34.995 | +0.45% | +0.06% | 2.30x | 1.5 | 2026-11-23T05:01:24.581174+00:00 | Not calibrated | MODERATE 69/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | AI/USD | 69.718 | 0.01584 | -1.26% | 0.81x |
| 2 | XMR/USD | 63.392 | 501.88 | +0.43% | 2.38x |
| 3 | SOL/USD | 61.336 | 71.34 | -0.01% | 0.32x |
| 4 | SUI/USD | 59.047 | 0.6602 | -0.03% | 0.45x |
| 5 | XRP/USD | 58.570 | 0.93298 | -0.02% | 0.41x |
| 6 | NIGHT/USD | 58.298 | 0.04993 | +0.38% | 2.29x |
| 7 | NEAR/USD | 57.723 | 3.0018 | -0.38% | 1.26x |
| 8 | ETH/USD | 57.008 | 1726.62 | +0.00% | 0.79x |
| 9 | JUP/USD | 50.397 | 0.23184 | +0.49% | 2.04x |
| 10 | LINK/USD | 46.935 | 8.89114 | -0.02% | 2.32x |
| 11 | LTC/USD | 45.277 | 40.34 | -0.02% | 2.51x |
| 12 | DOT/USD | 34.995 | 0.6638 | +0.06% | 2.30x |

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

- Persisted scans: 1384; predictions: 11375; observations: 837961.
- Matured sampled outcomes across 1/6/24/48h: 18394; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 104 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45115027766 · **Generation:** 1384 · **Legacy run:** 45115027766
**Main quote time:** 2026-11-23T05:01:33.094971+00:00 · **Legacy report time:** 2026-11-23T05:02:40.078453+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 501.88 | 79.32 | +0.43% | 2.38x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NIGHT/USD ⭐ | 0.04993 | 73.16 | +0.38% | 2.29x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | JUP/USD ⭐ | 0.23184 | 63.26 | +0.49% | 2.04x | STRONG 92/100 | HIGH 66/100 | Consider small entry |
| 4 | AI/USD | 0.01584 | 61.59 | -1.26% | 0.81x | WEAK 31/100 | EXTREME 90/100 | Do nothing |
| 5 | LTC/USD | 40.34 | 60.15 | -0.02% | 2.51x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 6 | LINK/USD | 8.89114 | 60.07 | -0.02% | 2.32x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 7 | NEAR/USD | 3.0018 | 58.46 | -0.38% | 1.26x | WEAK 39/100 | HIGH 61/100 | Watch |
| 8 | ETH/USD | 1726.62 | 54.91 | +0.00% | 0.79x | MODERATE 47/100 | HIGH 62/100 | Watch |
| 9 | SOL/USD | 71.34 | 54.48 | -0.01% | 0.32x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | SUI/USD | 0.6602 | 53.41 | -0.03% | 0.45x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | XRP/USD | 0.93298 | 52.55 | -0.02% | 0.41x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | DOT/USD | 0.6638 | 48.32 | +0.06% | 2.30x | MODERATE 69/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BLESS/USD | 0.017755 | 85.72 | +3.91% | 1.60x | 5712 | STRONG 73/100 | EXTREME 87/100 | Do nothing |
| 2 | JUP/USD ⭐ | 0.2318 | 68.53 | +0.49% | 2.04x | 2842 | STRONG 94/100 | HIGH 66/100 | Consider small entry |
| 3 | XMR/USD ⭐ | 501.48 | 62.93 | +0.43% | 2.38x | 8438 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 4 | NIGHT/USD ⭐ | 0.04993 | 59.16 | +0.38% | 2.29x | 10731 | STRONG 90/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** XMR/USD, NIGHT/USD, JUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
