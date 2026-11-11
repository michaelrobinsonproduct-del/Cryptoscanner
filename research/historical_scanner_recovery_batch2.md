# Batch 2 findings

Current prefilter screens 24h move 0.25 to 12 percent, spread at most 45 basis points and notional at least 100000 USD before OHLC checks. This can miss early movers.

Current shadow ranking favors high notional and tight spreads. Latest shadow top 12 included EUR/USD and GBP/USD fiat pairs, indicating a universe-filter issue.

Latest historical validation had 5008 rows but only eight distinct timestamps, and correctly blocked promotion. Existing recall comparisons have unequal selection budgets.

Hypotheses: relative-volume anomalies, price acceleration, broader precursor discovery, and separation of watch from trade approval may explain older successes. These are not proven causes. September alert version attribution remains unresolved.

Batch 3 should test shadow-only, exclude fiat bases, compare top 12 versus top 12 using past-only features and future labels, report missing features, and preserve production.
