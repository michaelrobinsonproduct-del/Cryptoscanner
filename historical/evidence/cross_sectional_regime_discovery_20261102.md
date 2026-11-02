# Role A — crypto cross-sectional early-mover discovery (shadow only)

**Hypothesis:** Short-term momentum and trading acceleration may predict different outcomes depending on independent peer breadth, market state, relative strength and catch-up behavior. This experiment tests seven fixed ranking rules plus an alphabetic negative control against a frozen absolute-60-minute momentum proxy. **No gains are presumed.**

## Research basis
- Guo et al. (2024), *Cross-cryptocurrency return predictability*, Journal of Economic Dynamics and Control 163, 104863: https://smusg.elsevierpure.com/en/publications/cross-cryptocurrency-return-predictability/ . This study tests **contemporaneous** peer context, not causal lead/lag.
- Mercik et al. (2025), *Cross-Sectional Interactions in Cryptocurrency Returns*, International Review of Financial Analysis 97, 103809: https://doi.org/10.1016/j.irfa.2024.103809 . Return/liquidity/risk interactions can matter, but liquidity and costs can eliminate tradability.
- *State transitions and momentum effect in cryptocurrency market* (2025), Finance Research Letters 86, 108356: https://doi.org/10.1016/j.frl.2025.108356 . Crypto momentum is state-dependent.

## Provenance and design
Uses strict retained Kraken historical source GitHub Actions run #38029912468, artifact #11662155953; existing loader validates SHA256 `research.ndjson=0f42814dcf1cc63167f24dbc571534964fbaad564ef3e5ae7ed321a19bda905d` and `research_training.ndjson=766683bae34744d825f0ee68335fd2e474ccc77d77849e46b2e4a8ecaf81778c`. Source contains sampled 15m USD anchors ending June 2026, **not** November 2026 data.

At each timestamp peer means/breadth exclude the focal asset, use only same-UTC data and require >=5 independent peers. No future label or target candle enters features. Train ends February 27; validation March 1-April 29; test May 1-June 29, with 24h embargo. Same top-12 candidate budget per timestamp, plus top-3 diagnostic because sampled universe is small. Measure +20/+30 sampled 24h future-close hits, false positives, unique positive pair-days, cooldown-positive picks and new/lost pair-days relative to baseline. Choose rule **only** on validation; never tune on test. Include negative control.

**Limitations:** These 24h future maximum 5m close labels are overlapping and not executable fills; peer cross-section is incomplete relative to 604 live USD markets; historical spread, orderbook, notional, funding, social/news catalysts and exact UTC-open gate unavailable. Any apparent improvement must survive episode-level analysis and independent validation. No live scoring/writer/ledger/trading/Railway changes.

## Result
Await exact-source CI artifact and adversarial tests. Record actual numerical results and negative findings in this file after verification. **No production promotion.**
