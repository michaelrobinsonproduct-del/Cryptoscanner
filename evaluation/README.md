# Shadow evaluation

GitHub Actions runs the challenger on a free scheduled cadence against the existing production control endpoints. It does not change, restart, or disable production. Each scheduled run emits an immutable JSON artifact for prospective evaluation.

The schedule is intentionally separate from the :00/:15/:30/:45 production tasks. Promotion remains disabled until prospective evidence satisfies docs/PROMOTION_POLICY.md.
