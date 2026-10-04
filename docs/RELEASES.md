# Immutable releases and rollback

A promoted challenger receives a versioned release tag/commit. The prior production control is retained as rollback baseline. Deployment metadata must record source commit, evaluation sample, control/challenger metrics, promotion reason and timestamp. Rollback is favored over live patching when a promoted release regresses reliability or freshness.

No autonomous agent may bypass the promotion policy by directly editing production.
