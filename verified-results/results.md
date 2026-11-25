# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T10:32:35.678040+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45595023027
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 5a48105999c5660b5e911d208d9622fce67a55cc (atomic ledger/results publication)
**Ledger generation:** 1706 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.33684 | 72.710 | 82.810 | +7.18% | -0.34% | 0.16x | 0.3 | 2026-11-25T10:32:29.840634+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | MON/USD | 0.00993 | 66.275 | 73.278 | +4.86% | -0.60% | 0.60x | 20.2 | 2026-11-25T10:32:29.840634+00:00 | Not calibrated | WEAK 28/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | BABY/USD | 0.00858 | 53.370 | 52.822 | +3.87% | -0.69% | 1.40x | 11.7 | 2026-11-25T10:32:29.840634+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | VVV/USD | 24.798 | 52.248 | 57.590 | +1.06% | +0.25% | 0.34x | 9.7 | 2026-11-25T10:32:29.840634+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 82.810 | 0.33684 | -0.34% | 0.16x |
| 2 | MON/USD | 73.278 | 0.00993 | -0.60% | 0.60x |
| 3 | VVV/USD | 57.590 | 24.798 | +0.25% | 0.34x |
| 4 | BABY/USD | 52.822 | 0.00858 | -0.69% | 1.40x |

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

- Persisted scans: 1706; predictions: 14453; observations: 1034033.
- Matured sampled outcomes across 1/6/24/48h: 31301; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45595023027 · **Generation:** 1706 · **Legacy run:** 45595023027
**Main quote time:** 2026-11-25T10:32:35.678040+00:00 · **Legacy report time:** 2026-11-25T10:33:28.199675+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.33684 | 72.71 | -0.34% | 0.16x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 2 | MON/USD | 0.00993 | 66.28 | -0.60% | 0.60x | WEAK 28/100 | EXTREME 88/100 | Do nothing |
| 3 | BABY/USD | 0.00858 | 53.37 | -0.69% | 1.40x | WEAK 42/100 | VERY_HIGH 79/100 | Watch |
| 4 | VVV/USD | 24.798 | 52.25 | +0.25% | 0.34x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
