# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T14:42:47.988173+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45636450441
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a6163fb16a566176aadad908380cc021e97d7770 (atomic ledger/results publication)
**Ledger generation:** 1731 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PIEVERSE/USD | 3.3924 | 96.484 | 60.590 | +10.13% | +7.17% | 2.09x | 31.0 | 2026-11-25T14:42:43.852392+00:00 | Not calibrated | STRONG 93/100 | EXTREME 89/100 | Do nothing | WATCH |
| 2 | MON/USD | 0.00978 | 54.522 | 57.240 | +3.27% | +0.91% | 0.27x | 20.5 | 2026-11-25T14:42:43.852392+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | VVV/USD | 24.671 | 51.233 | 53.911 | +0.54% | -0.14% | 0.80x | 9.8 | 2026-11-25T14:42:43.852392+00:00 | Not calibrated | WEAK 31/100 | HIGH 68/100 | Do nothing | WATCH |
| 4 | MOODENG/USD | 0.02622 | 49.153 | 62.561 | +7.77% | -2.77% | 1.04x | 30.5 | 2026-11-25T14:42:43.852392+00:00 | Not calibrated | WEAK 25/100 | EXTREME 89/100 | Do nothing | WATCH |
| 5 | DRV/USD | 0.3203 | 40.161 | 44.818 | +1.92% | -0.84% | 0.95x | 12.5 | 2026-11-25T14:42:43.852392+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 6 | XPL/USD | 0.0445 | 34.791 | 31.682 | +1.14% | +0.45% | 1.09x | 22.5 | 2026-11-25T14:42:43.852392+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 7 | CT/USD | 0.129 | 30.830 | 34.407 | +2.14% | -0.08% | 0.68x | 23.3 | 2026-11-25T14:42:43.852392+00:00 | Not calibrated | WEAK 10/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MOODENG/USD | 62.561 | 0.02622 | -2.77% | 1.04x |
| 2 | PIEVERSE/USD | 60.590 | 3.3924 | +7.17% | 2.09x |
| 3 | MON/USD | 57.240 | 0.00978 | +0.91% | 0.27x |
| 4 | VVV/USD | 53.911 | 24.671 | -0.14% | 0.80x |
| 5 | DRV/USD | 44.818 | 0.3203 | -0.84% | 0.95x |
| 6 | CT/USD | 34.407 | 0.129 | -0.08% | 0.68x |
| 7 | XPL/USD | 31.682 | 0.0445 | +0.45% | 1.09x |

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

- Persisted scans: 1731; predictions: 14581; observations: 1049233.
- Matured sampled outcomes across 1/6/24/48h: 32166; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45636450441 · **Generation:** 1731 · **Legacy run:** 45636450441
**Main quote time:** 2026-11-25T14:42:47.988173+00:00 · **Legacy report time:** 2026-11-25T14:44:02.847193+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD ⭐ | 3.3924 | 96.48 | +7.17% | 2.09x | STRONG 100/100 | EXTREME 89/100 | Do nothing |
| 2 | MON/USD | 0.00978 | 54.52 | +0.91% | 0.27x | MODERATE 47/100 | VERY_HIGH 82/100 | Watch |
| 3 | VVV/USD | 24.671 | 51.23 | -0.14% | 0.80x | WEAK 31/100 | HIGH 68/100 | Do nothing |
| 4 | MOODENG/USD | 0.02622 | 49.15 | -2.77% | 1.04x | WEAK 25/100 | EXTREME 89/100 | Do nothing |
| 5 | DRV/USD | 0.3203 | 40.16 | -0.84% | 0.95x | WEAK 20/100 | VERY_HIGH 74/100 | Do nothing |
| 6 | XPL/USD ⭐ | 0.0445 | 34.79 | +0.45% | 1.09x | MODERATE 52/100 | VERY_HIGH 79/100 | Watch |
| 7 | CT/USD | 0.129 | 30.83 | -0.08% | 0.68x | WEAK 10/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD ⭐ | 3.4049 | 69.32 | +7.17% | 2.09x | 995 | STRONG 85/100 | EXTREME 99/100 | Do nothing |
| 2 | XPL/USD ⭐ | 0.0445 | 32.55 | +0.45% | 1.09x | 1707 | MODERATE 46/100 | EXTREME 89/100 | Do nothing |

**Same-run overlap:** PIEVERSE/USD, XPL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
