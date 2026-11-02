# Actual as-of liquidity replay: 2026-11-02 (research only)

## Source and integrity

Read original sealed **generation 45** PAPER ledger (GitHub writer [#41366093862](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41366093862), ledger SHA256 `70f60d2be8faa7b967536b5a474b371674facb77418f6f5c2c544f40ceabeeab`), **27,248** actual market observations across **45** scans, 522 predictions. Downloaded and independently verified SHA256SUMS for **10 earlier immutable ledger ZIPs** from real writer runs #41307201989, #41309654993, #41311926367, #41314165370, #41316423836, #41319133932, #41322013186, #41324272237, #41326715230, #41329629549. For every original snapshot, matched as-of UTC, all pairs/prices and report SHA256 against gen45 ledger. These per-run `latest.json` snapshots preserve **actual as-of bid/ask spread and 24-hour notional for all ~603 markets**, including rejected markets. This materially improves on the price-only historical UTC-open proxy from PR #117.

## Six-hour retrospective experiment

Only 8 of the 10 source entry times (2026-11-01 13:36–17:07 UTC) have sufficient prior-price features and fully mature six-hour quote paths with **no >45-minute scan gap** and post-target anchor within 45 minutes. Same as-of liquidity screen for all experimental strategies: spread <=45bps, 24-hour notional >=$100,000. No price-since-UTC-open prefilter (its actual value is unavailable for rejected markets). Eligible pool sizes by time: **102, 103, 101, 103, 104, 98, 101, 94**.

| As-of top-12 selection | +5% windows | +10% | +20% | +30% | Distinct +30% markets |
|---|---:|---:|---:|---:|---:|
| 1h momentum | 6 | 3 | 2 | **2** | 1 (ESPORTS) |
| Trailing 3h volatility | 12 | 7 | 2 | **2** | 1 (ESPORTS) |
| Volatility + direction | 7 | 4 | 2 | **2** | 1 (ESPORTS) |
| Liquidity-adjusted volatility + direction | 3 | 3 | 2 | **2** | 1 (ESPORTS) |
| Actual PAPER WATCH intersected with comparable feature pool | 0 | 0 | 0 | **0** | 0 |

All experimental strategies generated **96 selections** (8 x 12); actual PAPER delivered **95** WATCH selections in those times (one scan had 11). Each experimental strategy's 2 positive windows represent **the same market**, not two independent opportunities. At a +30% threshold, the experimental strategies had **94 nonpositive windows of 96**; actual PAPER had 95 nonpositive of 95. This is *not* statistically persuasive or demonstrated prospective lift.

**Actual liquidity/false-opportunity distinctions from source:**

- ESPORTS/USD at **13:36 UTC**, 24h notional **$1,098,734**, spread **33.62bps**, subsequent observed six-hour peak **+39.41%**. At **15:37 UTC**, notional **$1,415,770**, spread **44.39bps**, subsequent peak **+33.61%**. Both meet the liquidity screen; experimental top-12 strategies selected both, PAPER WATCH did not.
- DEBIT/USD +33.74% repeated sampled windows but notional only **$1,582**, spreads **300–5,743bps**: correctly excluded by liquidity screen.
- UMXM/USD +39.10% window, but notional **$2,175**, spread **476bps**: correctly excluded.
- **Critical early-entry limitation:** ESPORTS at 13:36 had already climbed from **$0.00872 at 01:09 UTC** to **$0.01492** (approximately **+71.1%**) before the experimental signal. At 15:37 it was $0.01586 (+81.9%). Catching a further +30% move after this extension is not the requested *pre-surge* discovery. Earlier ESPORTS at 01:09 and 02:10 had approximately $323k/$338k notional and 11.47/22.75bps spreads but were **not WATCH**; earlier signals require separate investigation.

## Interpretation and next experiment

The new as-of liquidity evidence shows **one genuinely liquid missed market** in the evaluated six-hour cohort; DEBIT and UMXM are misleading apparent winners due to very poor liquidity/spreads. The existing PAPER ranker caught zero of these sampled positive windows. Retrospective volatility/momentum alternatives found ESPORTS, but only **after** a major prior rise. Therefore do **not** promote any alternative.

Next research should compare pre-surge (price extension <5–10% from an authenticated as-of reference) liquidity + changes in volume/trade count + spread compression against actual rejected markets at **01:09/02:10 UTC** and across future disjoint market episodes. Capture full as-of UTC-open and rejection reasons without touching the live writer, or use independent timestamped read-only snapshots. Optimize **distinct liquid movers identified before the first +20%**, not overlapping +30% windows.

## Limitations

Research is retrospective and exploratory, not untouched holdout or live scoring proof. Eight entry times have overlapping six-hour labels. The actual PAPER strategy has a different initial UTC-open/ohlc gate; comparison is not identical opportunity eligibility. Source prices are client-observed quotes, not exchange highs or executable fills; no independent historical order book. Feature availability excludes one possible actual WATCH outside the comparison only if its required lag history is missing; in this sample the count 95 matches delivered total. No trading, scoring promotion, second writer or ledger modification.

## Additional *pre-surge* as-of signal investigation (exploratory, NOT fitted)

Independently downloaded three original immutable per-run ledger artifacts [#41253370263](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41253370263), [#41259778481](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41259778481), and [#41263997201](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41263997201), checked all SHA256SUMS. ESPORTS observations:

| As-of UTC | Price | 24h notional | Spread |
|---|---:|---:|---:|
| Oct 31 23:38 | $0.00878 | $312,834 | 22.73bps |
| Nov 1 01:09 | $0.00872 | $323,095 | 11.47bps |
| Nov 1 02:10 | $0.00881 | $337,958 | 22.75bps |

At **01:09**, ESPORTS price fell **0.68%** while 24h notional increased **3.28%** and spread compressed by approximately **49.5%** (prior/current spread ratio +98.2%). This is much earlier than the volatility ranker's 13:36 selection, when the price had already risen ~71% from 01:09. At **02:10**, price increased only **1.03%** while notional increased **4.60%**. These are concrete pre-surge features, not post-move observations.

Against **all ~602 contemporaneous markets** at 01:09, there were **106** meeting the same as-of spread<=45bps, notional>=$100k and absolute price change<=3% screen. ESPORTS ranked **13th** on (24h notional % change minus absolute price % change), **13th** on spread ratio improvement, and **8th** on a *post-hoc exploratory* combination (notional growth minus absolute price change + 0.1 x percentage spread-ratio improvement). At 02:10, among **100** liquid/quiet markets, ESPORTS ranked **8th** on the first notional-change-minus-price-change metric but **50th** on the combined metric because its spread widened.

**Crucial limitation:** these formulas and thresholds were examined *after* identifying ESPORTS; the 01:09-to-03:54 quote path contains >45-minute observation gaps, so this is a promising hypothesis **not** a valid backtested early-entry hit or proven recommendation improvement. A rolling 24h notional increase can reflect changing volume and price; it is not directly measured five-minute trade acceleration. Before any promotion, freeze the candidate, evaluate all liquid markets over independent future periods with proper target coverage, compare distinct +30% mover episodes, lead time and false positives, and include 5m trade-count/volume when independently available.

## Newly verified 00:00–00:45 UTC live-gate starvation (generation 45 and 46)

Independently downloaded sealed writer [gen45 #41366093862](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41366093862) and [gen46 #41368602217](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41368602217). Verified every internal ZIP SHA256, canonical ledger hash, matching result SHA and remote manifest.

| Actual as-of source | Gen45 00:16 UTC | Gen46 00:44 UTC |
|---|---:|---:|
| Eligible USD pairs | 604 | 604 |
| Liquid by as-of spread<=45bps and notional>=$100k | **105** | **108** |
| Actually selected for 5m OHLC screening | **6** | **5** |
| Surviving WATCH after OHLC validation | **2** | **3** |
| Liquid candidates excluded before OHLC | **99** | **103** |

This is a **concrete algorithmic bottleneck**, not merely an inferred historical proxy. In `paper_pov/scanner.py`, the only additional gate after those liquidity conditions is **+0.25% to +12% price movement from today's UTC opening price**. Because `max_ohlc=24` and the screened pool is smaller than 24, these **99 and 103 liquid candidates were excluded by the UTC-open price gate** before their five-minute momentum/volume acceleration could be examined. This can severely starve the scanner near midnight UTC when most coins have moved <0.25% since the daily open.

The as-of observations do **not** retain each rejected market's exact UTC-open move, so we cannot break the 99/103 into too-low versus too-high or claim that all would have produced valid OHLC/early recommendations. **Next high-value research change:** independent read-only OHLC collection for a bounded set of rejected liquid markets, with exact as-of 5m features and prospective 1h/6h outcome tracking, to test relaxed/alternative entry gates at the same top-12 budget. Do not weaken the live scanner until this produces distinct liquid early-mover lift.


## Independent review repair: future-label-conditioned ranking removed (2026-11-02 01:36 UTC)

Role V correctly identified a lookahead vulnerability in the original exploratory
replay: it dropped candidates with missing forward outcomes *before* ranking.
That code is now corrected: all as-of spread/notional-qualified, lag-feature-complete
markets enter the ranking without consulting any future label. The top-12 list
is frozen first; unavailable forward paths are explicitly counted as
`missing_forward_label_picks`, not replaced by lower-ranked hindsight winners.
Time eligibility depends only on as-of features and elapsed six-hour maturity.
New adversarial tests prove a future-gap **highest-ranked** candidate remains
selected and that changing future labels cannot change picks.

The original authenticated 11-ZIP replay on corrected code at exact head
`cf2fb37853977d4840f331f71547df334d35feb7`
([CI #41373315219](https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/41373315219))
passed all **6** adversarial tests and the source replay. The downloaded
replay JSON (artifact #13110436846) was independently inspected: 8 eligible
entry times, pool sizes 102/103/101/103/104/98/101/94; all four challengers
selected **96**, each with **96 labeled and 0 missing-forward-label picks**,
**2** overlapping +30% windows from **one** distinct market (ESPORTS);
actual PAPER WATCH selected **95**, all 95 labeled, 0 +30% windows.
Thus **this particular historical sample's headline counts did not change**
when the leakage was removed, but the previous methodology was invalid for
future-gap cohorts. Do not interpret the unchanged counts as prospective lift.

The replay is still only eight overlapping six-hour entry times; ESPORTS
was already +71% extended by the first selected entry. No independent early
mover improvement is demonstrated; no scoring promotion is warranted.
