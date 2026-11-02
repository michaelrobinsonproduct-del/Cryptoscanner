"""Read-only GitHub native-schedule deficit and recovery-correlation diagnostics.

No scheduler, dispatch, ledger, Kraken or production writes. A deficit is
an as-of creation deficit, NOT proof GitHub permanently dropped named slots.
GitHub does not expose the originating scheduled hour.
"""
import datetime as dt

from paper_pov.cadence_provenance import timestamp, WRITER_WORKFLOW, WRITER_BRANCH

UTC = dt.timezone.utc
MINUTES = (9, 39)


def diagnose(runs, checked_at, lookback_hours=6, grace_minutes=15,
             listing_complete=False):
    """Conservative lower bound on absent native run creations as of observation.

    Caller must authenticate a complete, nontruncated GitHub workflow run
    listing covering [checked_at-lookback_hours, checked_at]. Delayed runs
    from older slots are counted in favor of native coverage. Reruns count
    as one originating run, not a second native trigger.
    """
    base = {"status": "UNVERIFIED_INCOMPLETE_API_COVERAGE",
            "per_slot_origin_verified": False, "permanent_miss_verified": False,
            "recovery_or_owner_manual_attributed": False}
    if listing_complete is not True:
        return base
    if (not isinstance(runs, list) or type(lookback_hours) is not int or
            not 1 <= lookback_hours <= 168 or type(grace_minutes) is not int or
            not 1 <= grace_minutes <= 120):
        return {**base, "status": "UNVERIFIED_INVALID_INPUT"}
    try:
        now = timestamp(checked_at)
        cutoff = now - dt.timedelta(hours=lookback_hours)
        mature = now - dt.timedelta(minutes=grace_minutes)
        ids, native, dispatch = set(), [], []
        for row in runs:
            if not isinstance(row, dict) or type(row.get("id")) is not int or row["id"] <= 0:
                raise ValueError("invalid run identity")
            rid = row["id"]
            if rid in ids:
                raise ValueError("duplicate GitHub run ID")
            ids.add(rid)
            created = timestamp(row["created_at"])
            if created > now:
                raise ValueError("future GitHub run")
            if created < cutoff:
                continue
            if (row.get("path") != WRITER_WORKFLOW or
                    row.get("head_branch") != WRITER_BRANCH or
                    row.get("event") not in ("schedule", "workflow_dispatch") or
                    type(row.get("run_attempt")) is not int or
                    row["run_attempt"] < 1 or
                    not isinstance(row.get("head_sha"), str) or
                    len(row["head_sha"]) != 40 or
                    any(c not in "0123456789abcdef" for c in row["head_sha"])):
                raise ValueError("untrusted run origin")
            (native if row["event"] == "schedule" else dispatch).append(rid)
        slots = []
        hour = cutoff.replace(minute=0, second=0, microsecond=0)
        while hour <= mature:
            for minute in MINUTES:
                slot = hour.replace(minute=minute)
                if cutoff <= slot <= mature:
                    slots.append(slot.isoformat())
            hour += dt.timedelta(hours=1)
        deficit = max(0, len(slots) - len(native))
        return {**base,
                "status": ("FAILED_NATIVE_CREATION_DEFICIT_AS_OF" if deficit else
                           "NO_NATIVE_CREATION_COUNT_DEFICIT_NOT_SLOT_ATTESTED"),
                "checked_at": now.isoformat(),
                "window_start": cutoff.isoformat(),
                "grace_minutes": grace_minutes,
                "matured_nominal_slot_count": len(slots),
                "nominal_slots": slots,
                "native_api_run_count": len(native),
                "native_api_run_ids": sorted(native),
                "dispatch_api_run_count": len(dispatch),
                "dispatch_api_run_ids": sorted(dispatch),
                "minimum_unrepresented_native_creations_as_of": deficit,
                "all_run_ids_unique_in_sample": True,
                "api_event_not_executed_log_provenance": True,
                "notes": [
                    "Run creation deficit is a lower bound as of the check, not permanent dropped-event proof",
                    "No specific cron hour is assigned to a delayed or early schedule event",
                    "Recovery dispatch never counts toward native :09/:39 creation coverage",
                    "A GitHub workflow_dispatch event does not authenticate owner-manual intent",
                    "No scanner persistence, quote freshness, external-writer isolation or user delivery is proven"] }
    except (ValueError, TypeError, KeyError, OverflowError, AttributeError):
        return {**base, "status": "UNVERIFIED_MALFORMED_OR_CONTRADICTORY_API_RUNS"}


def recovery_candidates(dispatch_runs, controller_attempts, max_gap_seconds=90):
    """Bound timing candidates, never turn a dispatch into native/owner proof.

    Only a one-to-one, narrowly time-compatible *candidate* is reported.
    GitHub does not expose a controller->dispatch causal identifier here.
    """
    base = {"status": "UNVERIFIED_INVALID_CORRELATION_INPUT"}
    if not isinstance(dispatch_runs, list) or not isinstance(controller_attempts, list):
        return base
    if type(max_gap_seconds) is not int or not 1 <= max_gap_seconds <= 300:
        return base
    try:
        seen_dispatch, seen_controller = set(), set()
        valid_controllers = []
        for attempt in controller_attempts:
            if not isinstance(attempt, dict):
                raise ValueError("invalid controller attempt")
            # An unauthenticated controller marker is not a recovery request.
            if (attempt.get("marker_readback_verified") is not True or
                    attempt.get("dispatch_http_accepted") is not True):
                continue
            cid = attempt.get("controller_run_id")
            if type(cid) is not int or cid <= 0 or cid in seen_controller:
                raise ValueError("ambiguous controller identity")
            seen_controller.add(cid)
            accepted = timestamp(attempt["accepted_at"])
            source = attempt.get("source_sha")
            if source is not None and (not isinstance(source, str) or
                    len(source) != 40 or
                    any(c not in "0123456789abcdef" for c in source)):
                raise ValueError("invalid optional controller source")
            valid_controllers.append((cid, accepted, source))
        provisional = []
        for run in dispatch_runs:
            if (not isinstance(run, dict) or run.get("event") != "workflow_dispatch" or
                    run.get("path") != WRITER_WORKFLOW or
                    run.get("head_branch") != WRITER_BRANCH or
                    type(run.get("run_attempt")) is not int or
                    run["run_attempt"] != 1 or
                    type(run.get("id")) is not int or run["id"] <= 0 or
                    run["id"] in seen_dispatch or
                    not isinstance(run.get("head_sha"), str) or
                    len(run["head_sha"]) != 40 or
                    any(c not in "0123456789abcdef" for c in run["head_sha"])):
                raise ValueError("invalid or duplicate dispatch identity")
            seen_dispatch.add(run["id"])
            when = timestamp(run["created_at"])
            matches = []
            for cid, accepted, source in valid_controllers:
                if source is not None and source != run["head_sha"]:
                    continue
                lag = (when - accepted).total_seconds()
                # GitHub creation/HTTP logging may differ by a few seconds.
                # A dispatch long BEFORE acceptance cannot be attributed.
                if -5 <= lag <= max_gap_seconds:
                    matches.append(cid)
            provisional.append((run["id"], sorted(set(matches))))
        # A single accepted controller request matching multiple writer runs
        # cannot establish one-to-one recovery provenance.
        controller_uses = {}
        for _, matches in provisional:
            for cid in matches:
                controller_uses[cid] = controller_uses.get(cid, 0) + 1
        output = []
        for rid, matches in provisional:
            ambiguous = (len(matches) > 1 or
                         any(controller_uses[cid] > 1 for cid in matches))
            output.append({
                "dispatch_run_id": rid,
                "candidate_controller_run_ids": matches,
                "classification": ("AMBIGUOUS_RECOVERY_CORRELATION" if ambiguous
                                   else "RECOVERY_TIMING_CANDIDATE_NOT_CAUSAL" if matches
                                   else "UNVERIFIED_DISPATCH_ORIGIN"),
                "owner_manual_verified": False,
                "controller_causality_verified": False})
        return {"status": "CANDIDATES_ONLY_NOT_CAUSAL", "dispatches": output}
    except (ValueError, TypeError, KeyError, OverflowError, AttributeError):
        return base
