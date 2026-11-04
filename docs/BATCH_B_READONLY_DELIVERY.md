# Batch B sealed paper delivery (not deployed)

The existing `paper-pipeline.yml` manual/scheduled job produces `sealed-http-bundle.json` and its immutable `receipts/*.json` in the `public-paper-ledger-<run-id>` artifact. The same job is the **only** paper ledger writer. The delivery service below only reads completed GitHub artifacts.

## Required configuration before any deployment approval

1. A reachable host with Python 3.11+, `gh` CLI authenticated with **read access** to `michaelrobinsonproduct-del/Cryptoscanner` Actions artifacts, and a valid TLS certificate/key. Do not grant the delivery service ledger write credentials.
2. A randomly generated secret of at least 32 characters, set as `PAPER_BUNDLE_TOKEN` on both the Python delivery service and Bun HTTP cycle service. Never commit it.
3. Start the opt-in read-only process only after deployment authorization:

```sh
python -m paper_pov.sealed_bundle_https --repo michaelrobinsonproduct-del/Cryptoscanner --host 127.0.0.1 --port 8443 --cert /secure/fullchain.pem --key /secure/privkey.pem
```

Expose it only through an approved HTTPS network path. Set `PAPER_RECEIPT_URL=https://<approved-host>/sealed-paper` on the existing Bun HTTP service. Do not point the Bun reader at GitHub's artifact ZIP: it expects the validated JSON bundle.

## Fail-closed behavior

The Python service selects a successful completed main-branch paper workflow run, checks authenticated run identity, artifact manifest SHA256, slot receipt run ID and source SHA, immutable scan receipt and WATCH/preselection projections, and a 10-minute scan freshness window. It requires a bearer token and returns HTTP 503 rather than stale/unverifiable data. Bun independently checks the SHA256-bound bundle, market coverage and freshness, and exposes `paper_watch` only when accepted. This is source provenance from authenticated GitHub Actions metadata, **not cryptographic signing by Kraken**.

**Known blocker:** the new output format is still on an unmerged integration branch; the main-only workflow has not been shown to produce a compatible artifact. Existing branch A1/A2 and A2 consumer artifacts are not substitutes for the main paper-ledger artifact. No HTTPS service or token is currently configured or deployed.

**Operational caveat:** the delivery process performs an authenticated GitHub artifact download per request. Its read can take longer than the Bun 30-second deadline or be rate-limited; that is a visible `UNAVAILABLE` outcome, not permission to use an older result. No fallback writer or stale cache is allowed.
