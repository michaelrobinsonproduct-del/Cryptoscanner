# B2 isolated shadow artifact contract (not production promotion)

The server's manual `GET /cycle` and internal scheduled cycle share the same runner. Set `SHADOW_ARTIFACT_URL` to a read-only HTTPS JSON object and `SHADOW_TRUSTED_SOURCE_SHA` to the independently verified 64-character SHA-256 of its historical source. Do not set the trusted SHA by copying an unverified claim from the downloaded artifact. Without both, the runner preserves the baseline cycle and marks shadow candidates ABSTAIN.

JSON fields:
- `evidence`: `version`, `source_sha`, `outcome_ledger_sha`, `qualified`, `held_out_samples`, `held_out_lift`, `outcome_rows`.
- `outcomes`: array of `{pair,observed_at,label,source_sha}` with label HIT/MISS/ABSTAIN. `outcome_ledger_sha` is SHA-256 over UTF-8 `JSON.stringify(outcomes)` in original order, not pretty-printed JSON. Count must equal `outcome_rows`.
- `scores`: optional array of `{pair,observed_at,computed_at,version,score,source_sha}`; scores must be genuine model outputs, 0–100, generated no later than candidate discovery time. Historical held-out lift is a metric, **not** a score increment.

Only a single unique matching non-ABSTAIN outcome with matching source, plus a single unique as-of challenger score, can produce a shadow-only comparison. This is not evidence of historical performance or permission to trade. The HTTP handler does not write the ledger, promote a rule, or modify the control scanner. A failed artifact read, invalid digest, untrusted source, missing score, or later-generated score abstains while retaining baseline output.

The digest confirms ledger consistency; the externally pinned source SHA must come from independent source verification. It does not prove that an upstream evaluator truthfully qualified a rule. Until independently authenticated historical labels and genuine challenger score artifacts exist, the correct outcome is **no qualified challenger**. The current fixture tests are synthetic; do not report them as live Kraken data.
