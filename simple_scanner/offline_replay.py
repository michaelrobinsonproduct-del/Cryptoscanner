"""Pure chronological cohort selection for offline replay; no production writes."""
import math

def cohort_split(rows, holdout_fraction=0.3, embargo_cohorts=1):
    """Split complete timestamp cohorts, not individual rows.

    Rows are (timestamp, pair, ...). Refuse sparse or invalid input and
    exclude embargoed cohorts between train and holdout.
    """
    if not 0 < holdout_fraction < 1 or embargo_cohorts < 1:
        raise ValueError("invalid split parameters")
    times = sorted({r[0] for r in rows})
    if len(times) < 4 + embargo_cohorts:
        raise ValueError("insufficient timestamp cohorts")
    cut = int(len(times) * (1 - holdout_fraction))
    if cut <= embargo_cohorts or cut >= len(times):
        raise ValueError("insufficient train/holdout cohorts")
    train_times = set(times[:cut - embargo_cohorts])
    test_times = set(times[cut:])
    train = [r for r in rows if r[0] in train_times]
    test = [r for r in rows if r[0] in test_times]
    if not train or not test:
        raise ValueError("empty train or holdout")
    return {'train': train, 'holdout': test, 'embargoed_timestamps': times[cut - embargo_cohorts:cut],
            'train_timestamps': len(train_times), 'holdout_timestamps': len(test_times),
            'promotion_eligible': False}

def replay_feasibility(connection):
    """Read-only counts across ALL archived timestamps; no arbitrary row cap."""
    required = {'market_signals', 'market_observations'}
    tables = {r[0] for r in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    if not required.issubset(tables):
        return {'status': 'MISSING_TABLES', 'promotion_eligible': False}
    signals, timestamps = connection.execute(
        "SELECT COUNT(*),COUNT(DISTINCT run_at) FROM market_signals").fetchone()
    observations = connection.execute("SELECT COUNT(*) FROM market_observations").fetchone()[0]
    return {'status': 'FEASIBILITY_ONLY', 'signal_rows': signals, 'signal_timestamps': timestamps,
            'observation_rows': observations, 'full_replay_verified': False,
            'promotion_eligible': False}
