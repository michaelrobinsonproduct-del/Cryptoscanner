# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T14:20:57.615709+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44752356400
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 6773d88c31fb7f6eef2a07556b2ac044f21ffdc7 (atomic ledger/results publication)
**Ledger generation:** 990 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 607; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.022275 | 68.947 | 60.591 | +4.63% | +1.52% | 1.08x | 8.1 | 2026-11-20T14:20:50.929121+00:00 | Not calibrated | MODERATE 69/100 | HIGH 67/100 | Watch | WATCH |
| 2 | MON/USD | 0.01397 | 57.970 | 37.178 | +1.53% | +1.16% | 3.34x | 14.3 | 2026-11-20T14:20:50.929121+00:00 | Not calibrated | STRONG 79/100 | HIGH 66/100 | Watch | WATCH |
| 3 | MNT/USD | 0.3942 | 47.832 | 32.832 | +0.66% | +0.00% | 6.45x | 5.1 | 2026-11-20T14:20:50.929121+00:00 | Not calibrated | MODERATE 69/100 | HIGH 67/100 | Watch | WATCH |
| 4 | CAP/USD | 0.097746 | 42.743 | 38.818 | +1.17% | +0.72% | 1.03x | 5.6 | 2026-11-20T14:20:50.929121+00:00 | Not calibrated | MODERATE 56/100 | HIGH 67/100 | Watch | WATCH |
| 5 | DOS/USD | 0.1943 | 39.908 | 51.325 | +5.89% | -1.10% | 0.41x | 41.3 | 2026-11-20T14:20:50.929121+00:00 | Not calibrated | WEAK 10/100 | EXTREME 100/100 | Do nothing | WATCH |
| 6 | REKT/USD | 7.72e-08 | 28.201 | 34.934 | +2.93% | -0.51% | 0.58x | 39.1 | 2026-11-20T14:20:50.929121+00:00 | Not calibrated | WEAK 4/100 | EXTREME 93/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 60.591 | 0.022275 | +1.52% | 1.08x |
| 2 | DOS/USD | 51.325 | 0.1943 | -1.10% | 0.41x |
| 3 | CAP/USD | 38.818 | 0.097746 | +0.72% | 1.03x |
| 4 | MON/USD | 37.178 | 0.01397 | +1.16% | 3.34x |
| 5 | REKT/USD | 34.934 | 7.72e-08 | -0.51% | 0.58x |
| 6 | MNT/USD | 32.832 | 0.3942 | +0.00% | 6.45x |

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

- Persisted scans: 990; predictions: 8250; observations: 598284.
- Matured sampled outcomes across 1/6/24/48h: 10100; gap abstentions: 17589. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44752356400 · **Generation:** 990 · **Legacy run:** 44752356400
**Main quote time:** 2026-11-20T14:20:57.615709+00:00 · **Legacy report time:** 2026-11-20T14:22:06.879625+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.022275 | 68.95 | +1.52% | 1.08x | STRONG 79/100 | HIGH 67/100 | Watch |
| 2 | MON/USD ⭐ | 0.01397 | 57.97 | +1.16% | 3.34x | STRONG 89/100 | HIGH 66/100 | Consider small entry |
| 3 | MNT/USD | 0.3942 | 47.83 | +0.00% | 6.45x | MODERATE 69/100 | HIGH 67/100 | Watch |
| 4 | CAP/USD ⭐ | 0.097746 | 42.74 | +0.72% | 1.03x | MODERATE 66/100 | HIGH 67/100 | Watch |
| 5 | DOS/USD | 0.1943 | 39.91 | -1.10% | 0.41x | WEAK 10/100 | EXTREME 100/100 | Do nothing |
| 6 | REKT/USD | 7.72e-08 | 28.20 | -0.51% | 0.58x | WEAK 4/100 | EXTREME 93/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.022187 | 76.18 | +1.52% | 1.08x | 6972 | STRONG 78/100 | VERY_HIGH 73/100 | Watch |
| 2 | MON/USD ⭐ | 0.01395 | 52.87 | +1.16% | 3.34x | 3543 | STRONG 91/100 | HIGH 60/100 | Consider small entry |
| 3 | CAP/USD ⭐ | 0.098258 | 46.75 | +0.72% | 1.03x | 5162 | MODERATE 63/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** SENT/USD, MON/USD, CAP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
