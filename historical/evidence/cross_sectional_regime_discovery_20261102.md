# Role A — cross-sectional crypto early-mover discovery: VERIFIED NEGATIVE RESULT

**2026-11-02 UTC, research-only. No production scoring promotion.** Scope lease issue #34 comment #6566581096. PR #119, branch `research/role-a-cross-sectional-20261102`.

## Scientific motivation
- Guo et al. (2024), *Cross-cryptocurrency return predictability*, Journal of Economic Dynamics and Control 163, 104863: https://smusg.elsevierpure.com/en/publications/cross-cryptocurrency-return-predictability/ . Tests here use contemporaneous peers, NOT proof of causal lead/lag.
- Mercik et al. (2025), *Cross-Sectional Interactions in Cryptocurrency Returns*, International Review of Financial Analysis 97, 103809: https://doi.org/10.1016/j.irfa.2024.103809 . Trading costs/liquidity can eliminate apparent signals.
- *State transitions and momentum effect in cryptocurrency market* (2025), Finance Research Letters 86, 108356: https://doi.org/10.1016/j.frl.2025.108356 . Momentum may depend on persistent up states.

## Actual reproducible source and test design
Strict retained Kraken historical GitHub Actions run #38029912468 artifact #11662155953; independently SHA-validated `research.ndjson` `0f42814dcf1cc63167f24dbc571534964fbaad564ef3e5ae7ed321a19bda905d`, training SHA `766683bae34744d825f0ee68335fd2e474ccc77d77849e46b2e4a8ecaf81778c`. **391,356** eligible USD anchors after requiring >=5 other same-UTC observed assets; 180 USD pairs. Peer return and breadth exclude focal asset and use only same-timestamp observations, no future data. Seven fixed hypotheses plus alphabetic negative control; 7/7 adversarial tests passed.

Frozen absolute 60m momentum baseline versus leave-one-out peer relative strength, peer breadth + acceleration, quiet/high-activity market-up, laggard catch-up, peer divergence, market-down relative strength. Train through Feb27, validation Mar1-Apr29, untouched test May1-Jun29, 24h embargo. Same top-12 budget per timestamp, top-3 diagnostic, +20/+30 maximum sampled 5m CLOSE in following 24h, false positives, distinct +30 pair-days and 24h cooldown. Select only on validation, not test.

## Exact-source GitHub CI evidence
[Push CI #41370587068](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41370587068) and [PR CI #41370591777](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41370591777) **SUCCESS**, including real retained-source replay, 7/7 adversarial tests, downloadable 90-day research artifact. Full split metrics and compact artifact logged; compact JSON SHA256 `5f99a2c404589637424989da682407ad1af14a377049fc1f25c93f368e00280f`, full JSON SHA256 `5e77ad5eea7cf9cad8bb95b70794f46eb9f178fb0cf0515037ebebf18bba8e45`. Separate aggregate audit PR CI #41370591844 SUCCESS. These are research CI passes, NOT live lift or four-workflow release acceptance.

### Train / validation / untouched test, same top-12 budget

| Rule | Train +30 picks / unique positive pair-days | Validation +30 picks / pair-days | Test +30 picks / pair-days | Test false positives |
|---|---|---|---|---|
| Absolute 60m momentum baseline | 4,029 / 187 | 1,019 / 39 | **1,962 / 89** | 64,999 |
| Laggard catch-up | 4,031 / 187 | 1,019 / 39 | 1,965 / 89 | 64,996 |
| Quiet high-activity market-up | 4,023 / 187 | 1,019 / 39 | 1,964 / 89 | 64,997 |
| Peer breadth acceleration | 3,940 / 186 | 1,008 / 39 | 1,928 / 89 | 65,033 |
| Peer relative strength | 3,343 / 166 | 869 / 39 | 1,628 / 87 | 65,333 |
| Alphabetic negative control | 2,587 / 111 | 873 / 31 | 1,125 / 49 | 65,836 |

Train picks=158,139; validation picks=66,298; test picks=66,961 **for each rule**. Baseline validation-selected for both top-12 and top-3. All six substantive challengers discovered **zero new unique +30 positive pair-days** on test versus baseline; peer relative strength lost two pair-days. Baseline and laggard each 48 24h-cooldown-positive picks on test. Top-3 baseline 1,587 +30 overlapping windows / 86 pair-days; laggard 1,545 / 86; peer relative 1,068 / 79. Therefore the +3 overlapping test windows for laggard are **NOT** an independent mover improvement. No promotion.

## Important limitations and next hypothesis
Sampled 15m anchors contain only ~15 USD assets per timestamp, far below live 604 eligible USD markets. Top-12 nearly saturates that small cross-section. Outcomes are overlapping 24h sampled-close maxima, not executable fills; 24h cooldown counts remain correlated. Historical source ends June 2026, not November. No authenticated historical spread, true ticker UTC-open, order-book depth, funding, on-chain flow, news or social evidence. The peer signals tested are contemporaneous; lagged leader-follower dynamics have **not** been tested.

**Next experiment:** collect timestamped, liquid as-of full-universe market breadth and 5/15/60m lagged leader/sector signals from actual Kraken live snapshots, then test earlier pre-surge 1h/6h outcomes with unique episode lead-time and false-positive metrics. Retain this negative result so the same rules are not blindly retried. Production ranker, ledger, trading and Railway unchanged. Independent Role V expected-head review required.
