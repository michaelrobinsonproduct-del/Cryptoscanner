# Owner E — actual retained Kraken evidence audit (2026-11-02 UTC)

**Scope:** isolated read-only research. No model promotion, production changes, trading, writer, cron, or ledger changes. This is *not* a first-entry episode label set.

## Immutable acquisition and exact-code verification

- GitHub Actions run [41154739332](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41154739332) (2026-10-31), artifact `kraken-reusable-ohlc-evidence` **13024232238**, expiry **2026-11-30T01:19:11Z**. Downloaded actual artifact ZIP, independently SHA256 checked **f69a0d1a8611ed10259f4884f4427c5e131c39d82c556dbe1602d1b7aa298b59**, equal GitHub artifact digest. Its inner `reusable_ohlc_evidence.zip` SHA256 is **704513836ee4b35680fde0ff93a3bb3e8ed6e39469a7183afd89b1ddb01a52a2**.
- Executed the **exact** `research/kraken_archive_readiness.py` blob **949f19590f0d38dd0fa4568104391a372ed7ed98** from E PR #125 head `b42df77e49a6c0442a411a887645624716f15270` against actual inner ZIP. Independently checked reconstructed source's Git blob hash equals GitHub's. No duplicate CI dispatched; prior E exact-head [CI 41505325095](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41505325095) 82/82 PASS on synthetic adversarial fixtures.
- Retained ZIP manifest source archive SHA **fc81b54cba6e12af3e9422dde9416179e6ef76af4831d48d839fbdb43018eaa4** is a verified *claim tied to the earlier archive inventory*, not a fresh rehash of the ~9GB source in this run.

## Measured actual retained OHLC evidence

- **48/48 markets, 341,233 retained 5-minute rows**, all retained member SHA256 hashes, manifest identity, timestamps, OHLCVT geometry, row counts and first/last candle metadata verified by the exact E auditor.
- Uninterrupted **candidate candle-window counts**, not independent episodes: **1h 54,007; 6h 22,721; 24h 11,150; 48h 9,129**. Markets with zero candidate windows: **1h 1; 6h 26; 24h 38; 48h 44**.
- Distinguish retained 341,233 rows from **4,807,872 source rows** across the same 48 markets in the independently verified full-archive inventory. Retention is deliberately bounded to <=8,000 rows per market; source inventory has gaps. Do not infer whole-history continuity from these candidate windows.

## Bounded independent trade-member overlap (new descriptive reconciliation)

- Same run artifact `kraken-bounded-independent-trade-members` **13024222325**, expires **2026-11-30T01:19:09Z**. Outer ZIP independently SHA256 checked **77db917e47c3c68ab187c1b9c9e1204399622b12b33943b6f825799775ec570f**, matching GitHub digest; inner trade ZIP SHA256 **bf3884d9e89f33246d470388510ebc72e951e90bbc98b3c7239e809dbbae168b**. Four retained trade members' SHA256 matched their probe manifest.
- Sampled **17,975 trade rows** in four markets: BCHJPY 398, CMETHETH 1,929, DENTEUR 10,424, ELXEUR 5,224. They occupy **5,001 distinct 5-minute buckets**, all overlapping the retained OHLC sample. In **5,001/5,001** overlapping buckets, trade-aggregated high/low, trade count and volume (allowing <=1e-8 absolute or <=1e-12 relative for OHLC export floating-point roundoff) agree with retained OHLC. Complete OHLCVT including first/last price agrees in **4,570/5,001** under that volume tolerance; **431** require source trade ordering/tie-time reconciliation, not automatic label eligibility.
- Trade ZIP explicitly reports **`source_archive_full_sha256_verified=false`**, **`independent_trade_interval_completeness_verified=false`**, and does not provide historical first-observed-at timestamps. Four sampled markets do not certify all 48 or all intervals.

## Learning decision

**Independently certifiable historical first-entry positive/negative episodes: 0 from these artifacts**, meaning *unverifiable*, not zero market surges. `source_timestamp_semantics=candle_open_candidate` is not decision-time observation. No exchange-authenticated complete forward trade path, no as-of bid/ask spread/depth/volume, no first-observed quote provenance, no held-out lift, no production promotion.

**Next executable data requirement:** preserve these two source artifact digests; independently authenticate full Kraken trade archive SHA and trade-bucket completeness on a fixed cohort; resolve the 431 first/last ordering discrepancies with stable trade sequencing; obtain timestamped first-observed market snapshots and point-in-time liquidity. Only then construct first-eligible-entry episodes and matched negatives with complete 1/6/24/48h paths and chronological purged/48h-embargo held-out evaluation. No repeated PAPER replay.
