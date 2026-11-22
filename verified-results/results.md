# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T00:01:26.064361+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44964424315
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 2dc2d07996721b9670da182249c120f6fcbedcd2 (atomic ledger/results publication)
**Ledger generation:** 1205 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 607; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 143.1 | 73.947 | 73.400 | +3.13% | -0.35% | 1.23x | 7.0 | 2026-11-22T00:01:17.471534+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 2 | AVAX/USD | 6.571 | 48.844 | 57.082 | +1.00% | -0.05% | 0.20x | 1.5 | 2026-11-22T00:01:17.471534+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 3 | SHX/USD | 0.003448 | 35.776 | 39.871 | +2.83% | +0.23% | 0.47x | 23.3 | 2026-11-22T00:01:17.471534+00:00 | Not calibrated | WEAK 38/100 | EXTREME 94/100 | Do nothing | WATCH |
| 4 | SPX/USD | 0.2802 | 26.127 | 24.474 | +0.29% | -0.25% | 1.29x | 21.5 | 2026-11-22T00:01:17.471534+00:00 | Not calibrated | WEAK 13/100 | VERY_HIGH 78/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 73.400 | 143.1 | -0.35% | 1.23x |
| 2 | AVAX/USD | 57.082 | 6.571 | -0.05% | 0.20x |
| 3 | SHX/USD | 39.871 | 0.003448 | +0.23% | 0.47x |
| 4 | SPX/USD | 24.474 | 0.2802 | -0.25% | 1.29x |

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

- Persisted scans: 1205; predictions: 9761; observations: 728998.
- Matured sampled outcomes across 1/6/24/48h: 13163; gap abstentions: 21681. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 20; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44964424315 · **Generation:** 1205 · **Legacy run:** 44964424315
**Main quote time:** 2026-11-22T00:01:26.064361+00:00 · **Legacy report time:** 2026-11-22T00:02:32.166258+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 143.1 | 73.95 | -0.35% | 1.23x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 2 | AVAX/USD | 6.571 | 48.84 | -0.05% | 0.20x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 3 | SHX/USD | 0.003448 | 35.78 | +0.23% | 0.47x | WEAK 38/100 | EXTREME 94/100 | Do nothing |
| 4 | SPX/USD | 0.2802 | 26.13 | -0.25% | 1.29x | WEAK 13/100 | VERY_HIGH 78/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 492.71 | 48.13 | +0.22% | 1.14x | 11667 | MODERATE 59/100 | HIGH 62/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
