# Owner E — verified retained OHLC cohort phase-sensitivity (2026-11-02 UTC)

**Purpose:** test whether the previously reported fixed-stride, non-overlapping hindsight +30% cohort is stable when its starting offset changes. This is a descriptive historical robustness test, not a trading signal, an authenticated first-entry episode, or a model promotion.

## Source integrity and exact-code tests

- Reused retained GitHub Actions artifact **13024232238** from [run 41154739332](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41154739332). Actual outer ZIP SHA256 **f69a0d1a8611ed10259f4884f4427c5e131c39d82c556dbe1602d1b7aa298b59** and embedded `reusable_ohlc_evidence.zip` SHA256 **704513836ee4b35680fde0ff93a3bb3e8ed6e39469a7183afd89b1ddb01a52a2** were independently recomputed and matched prior evidence. Each of 48 retained member payloads was checked against its manifest SHA256; 341,233 retained candles overall.
- Implemented `phase_sensitivity` in `research/retained_first_entry_candidates.py`, plus three adversarial tests and fixed the PR workflow trigger to include the actual retained-candidate source and test paths. Exact-code commit **b15f64b8dfe6016f4ca56b97b842ce611f4ba1e7**; [CI 41533089927](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41533089927), job 125578023099 **COMPLETED SUCCESS**, exact SHA printed and **92/92 tests passed**.
- Independently recomputed phase offsets from the actual authenticated retained artifact with a bounded read-only deque-max implementation. Future outcome is the highest high of subsequent candles (entry candle excluded); entry proxy is 5m close. Each entry has 12 prior uninterrupted candles, a complete uninterrupted future horizon, and one phase `(index-12) % horizon_candles`. Per-phase cohorts are non-overlapping **within each continuous market segment**. This independent calculation reproduced all four previous fixed-phase cohort counts and all overlapping-window counts.

## Measured cohort sensitivity on actual retained bytes

| Horizon | All contiguous entry windows | All hindsight +30% windows | Fixed phase entries / +30% | Offsets evaluated | Entries across offsets (min–max) | +30% per offset (min–max) | Offsets with any +30% |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1h | 54,007 | 330 | 3,583 / 11 | 12 | 2,900–3,583 | 6–11 | 12 |
| 6h | 22,721 | 224 | 368 / 5 | 72 | 238–368 | 0–7 | 61 |
| 24h | 11,150 | 85 | 45 / 1 | 288 | 33–45 | 0–1 | 72 |
| 48h | 9,129 | 1 | 17 / 0 | 576 | 14–17 | 0–0 | 0 |

**New finding:** the selected 6h fixed phase has 5 positive hindsight proxies, but another valid non-overlapping offset can have **zero**, while others have up to 7. At 24h, only 72/288 offsets contain even one positive; at 48h none of the fixed-stride phases select the sole overlapping positive window. Therefore the prior fixed-phase sample is too phase-sensitive and sparse for a credible learning rule or out-of-sample claim. The fixed-phase counts were not erroneous; the *interpretation* needs this robustness bound.

## Eligibility and next data requirement

**Authenticated first-entry episodes certifiable from these artifacts: 0**, strictly because the evidence does not include historical quote **first-observed-at**, complete authenticated trade-bucket coverage, or as-of bid/ask spread/depth/volume. Zero certifiable is not zero real opportunities. These OHLC cohorts are hindsight-only, with no observed fill, cost model, or held-out predictive lift.

**Next concrete data step:** obtain an authenticated complete 48-market trade-bucket export, preserving same-timestamp trade ordering, and historical first-observed quote plus entry-time liquidity. If first-observed timestamps were never recorded, classify old OHLC as descriptive research and begin bounded prospective first-observed/quote/depth capture on a separate, authorized path; do not reconstruct or invent historical observation times.

B cross-evaluator parity was already verified at `c4e70cf6c2df84a91159885bf2485dceaa0441d5` via [CI 41499755352](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41499755352), completed success; no redundant PAPER analysis. No main merge, live scan, writer/ledger, scheduling, trading, scoring or production change.
