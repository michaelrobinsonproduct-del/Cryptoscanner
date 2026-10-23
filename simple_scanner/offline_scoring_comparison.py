"""Independent offline comparison of legacy baseline and research challenger.

Consumes historical feature tuples; never reads live storage or promotes models.
"""
def compare_cohorts(rows, challenger_score):
    """Rows: (timestamp,pair,momentum,volume,base_score,future_return).
    Compare one selection per complete timestamp cohort, equal selection budget.
    """
    cohorts = {}
    for row in rows:
        if len(row) != 6:
            raise ValueError('invalid feature row')
        cohorts.setdefault(row[0], []).append(row)
    if not cohorts:
        return {'status': 'INSUFFICIENT_HISTORY', 'promotion_eligible': False}
    baseline, challenger, picks = [], [], []
    for timestamp in sorted(cohorts):
        cohort = cohorts[timestamp]
        # Deterministic tie-breaking independent of original row order.
        old = max(cohort, key=lambda r: (r[4], r[1]))
        new = max(cohort, key=lambda r: (challenger_score(r), r[1]))
        baseline.append(old[5])
        challenger.append(new[5])
        picks.append({'timestamp': timestamp, 'legacy_pair': old[1], 'challenger_pair': new[1]})
    n = len(cohorts)
    return {'status': 'OFFLINE_COMPARISON', 'cohorts': n, 'selection_budget_per_cohort': 1,
            'legacy_avg_return_pct': round(sum(baseline)/n, 4),
            'challenger_avg_return_pct': round(sum(challenger)/n, 4),
            'delta_pct': round((sum(challenger)-sum(baseline))/n, 4),
            'picks': picks, 'promotion_eligible': False,
            'production_scoring_parity_verified': False}
