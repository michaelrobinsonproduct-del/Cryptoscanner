# Actual PAPER miss analysis: ESPORTS/USD and two nontradeable-looking movers (2026-11-01)

This is **real market-data analysis**, not fixtures. Recovered GitHub Actions `public-paper-ledger-*` ZIP artifacts and independently checked each internal `SHA256SUMS`. Source is client-observed Kraken ticker quotes (not exchange-complete highs, not executable fills). No production changes.

## Data examined

- PAPER generation **44**, [real native scheduled writer #41362641742](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41362641742), source `7c0ff63f2e6ed1a193f120ba94141aa0e50837c7`, ledger SHA256 `817234e10a3543b9dba45e5167a5939ce795db10a453e9790490558d28c73c6a`, 44 scans, 26,644 market observations, 520 WATCH predictions.
- Independent reconstruction from all market quotes, requiring 45m maximum interior spacing and an observed target anchor within 45m after target, plus mature 45m delay: **12,065 eligible 1h market/run windows** (6 sampled +20%, 0 +30%, 0 WATCH +20%) and **5,421 eligible 6h market/run windows** (29 sampled +20%, 11 +30%, 0 WATCH +20%). These are **overlapping windows**, not independent successes. Six-hour +30% windows belong to only **three distinct markets**: ESPORTS, DEBIT, UNFI.
- For as-of market metadata, independently verified real `latest.json` artifacts from [gen14 #41259778481](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41259778481), [gen15 #41263997201](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41263997201), [gen16 #41270952492](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41270952492), [gen21 #41307201989](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41307201989), [gen22 #41309654993](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41309654993), [gen23 #41311926367](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41311926367), [gen24 #41314165370](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41314165370), [gen25 #41316423836](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41316423836), [gen26 #41319133932](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41319133932). All their inner checksums passed.


**Independent cross-check:** The automatically triggered read-only [learning run #41362926978](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41362926978), artifact `paper-learning-shadow-41362926978` (#13106240605), passed all three internal SHA256 checks and bound to exact PAPER writer #41362641742, generation 44 and ledger SHA256 `817234e10a3543b9dba45e5167a5939ce795db10a453e9790490558d28c73c6a`. Its own official coverage calculation **exactly agrees** with the independent reconstruction: 1h matured 12,065 / +20% 6 / +30% 0; 6h matured 5,421 / +20% 29 / +30% 11; **zero WATCH hits**. This is a confirmed retrospective miss census, not a proven strategy improvement.

## A concrete missed potentially actionable mover: ESPORTS/USD

| UTC observation | Price | 24h notional (USD) | Spread (bps) | Current WATCH? |
|---|---:|---:|---:|---|
| 01:09 | $0.00872 | $323,095 | 11.47 | No |
| 02:10 | $0.00881 | $337,958 | 22.75 | No |
| 03:54 | $0.01154 | $555,855 | 70.11 | No |
| 12:36 | $0.01325 | $872,987 | 52.87 | No |
| 13:08 | $0.01416 | $968,793 | 92.40 | No |
| 13:36 | $0.01492 | $1,098,734 | 33.62 | No |
| 17:37 | $0.02080 | — | — | No |

From 01:09 to 03:54, observed endpoint price rose **32.34%**; from 02:10 to 03:54 it rose **30.99%**. Both early observations satisfied the scanner's **spread <=45bps and notional >=$100,000** gates but were not WATCH. The interval to 03:54 contained a >45m scan gap; these endpoint moves **must not be relabeled as fully observed continuous 1/6h outcomes**. They still warrant investigating the other prefilters, early signal and selection budget.

From 12:36 to 17:37, client-observed price rose **56.98%**, with continuous <=45m observations. At 12:36 spread **52.87bps**, only **7.87bps** above the scanner's 45bps cutoff, despite $873k notional. At 13:36 spread **33.62bps** and notional **$1.10m** passed both liquidity gates, yet ESPORTS was still not WATCH. The exact UTC-open move, original 24-candidate OHLC selection, and candle-validity reason for each exclusion are **not persisted for all rejected pairs**. Do not falsely claim which of these gates excluded it. This missing rejection-feature evidence is a specific learning instrumentation deficiency.

## Why three +30% names are not three equally useful opportunities

At 12:36, **DEBIT/USD** had only **$1,612** reported 24h notional and **164.53bps** spread; **UNFI/USD** had only **$1,527** notional and **1,694.21bps** spread. Both later had sampled +30% 6h windows but failed practical liquidity/spread gates dramatically. Relaxing every gate to catch these would likely degrade real recommendation quality.

ESPORTS is the higher-priority miss because it had substantial reported liquidity and tight early spreads before a large observed move. This suggests **a specific early-stage selection problem** worth investigating, rather than blindly broadening all filters.

## Immediate experimental change to test (research only)

1. Persist a **read-only full-universe feature and rejection-reason audit** for every USD pair at each scan: UTC-open return, 5/15/60m returns, trade-count and volume acceleration, volatility, spread, notional, stage of rejection and OHLC selection status. Keep canonical as-of source timestamps; do not change writer or live ranking.
2. Replay ESPORTS and all similarly liquid missed movers with **two competing research lanes**: (A) quiet-but-accelerating pre-surge, and (B) controlled breakout/continuation. Evaluate each against the existing top-12 budget on disjoint chronological samples, with a cap on extension and explicit spread/liquidity eligibility.
3. Report how many **distinct liquid mover episodes** are caught early, how many non-movers are falsely selected, and how much lead time exists. No claim of live lift or tradeable +30% until prospective results exist.

**Caveats:** current ledger has no historical spread/notional per observation; as-of market snapshots above were recovered from exact earlier scan artifacts. The 6h windows overlap heavily and cover a short 32h history. No model was promoted. Independent legacy shadow #41362644177 at 23:33 generated BNB only; PAPER #41362641742 at 23:35 ranked BNB #5, an actual dual-signal overlap, not evidence of future performance.
