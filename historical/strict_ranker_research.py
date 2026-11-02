"""Research-only chronological +30% early-mover ranking experiment.

Input: exact Kraken 2026Q2 strict research_training.ndjson artifact.
No trading, production scorer, remote writes, or model promotion.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path


def run(source):
    import numpy as np
    import pandas as pd
    from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler

    raw = Path(source).read_bytes()
    source_sha = hashlib.sha256(raw).hexdigest()
    if source_sha != '766683bae34744d825f0ee68335fd2e474ccc77d77849e46b2e4a8ecaf81778c':
        raise ValueError('strict historical source checksum mismatch')
    fields = ['pre_return_5m_pct', 'pre_return_15m_pct', 'pre_return_60m_pct',
              'volume_accel', 'trade_accel', 'volatility_pct']
    rows = []
    for line in raw.splitlines():
        r = json.loads(line)
        if not r.get('control_sampled') or not r['pair'].endswith('USD'):
            continue
        if any(r.get(k) is None or not isinstance(r[k], (int, float)) or
               not math.isfinite(r[k]) for k in (*fields, 'max_forward_return_pct')):
            continue
        rows.append({k: r[k] for k in fields} | {
            'pair': r['pair'], 'at': r['anchor_at'], 'date': r['anchor_at'][:10],
            'hit20': int(r['max_forward_return_pct'] >= 20),
            'hit30': int(r['max_forward_return_pct'] >= 30)})
    df = pd.DataFrame(rows).sort_values('at').reset_index(drop=True)
    if len(df) < 10000:
        raise ValueError('representative USD control anchors missing')
    # 24-hour embargo avoids target-horizon crossing between splits.
    df['split'] = np.select([
        df.date < '2026-02-28',
        (df.date >= '2026-03-01') & (df.date < '2026-04-30'),
        df.date >= '2026-05-01'], ['train', 'val', 'test'], default='embargo')
    X = df[fields].copy()
    for k in ('volume_accel', 'trade_accel'):
        X[k] = np.log1p(X[k].clip(lower=0, upper=100))
    for k in ('pre_return_5m_pct', 'pre_return_15m_pct',
              'pre_return_60m_pct', 'volatility_pct'):
        X[k] = X[k].clip(-100, 100)
    train, val, test = (df.split == s for s in ('train', 'val', 'test'))
    models = {
        'logistic': make_pipeline(StandardScaler(), LogisticRegression(
            max_iter=1000, C=.2, class_weight='balanced')),
        'hist_gb': HistGradientBoostingClassifier(max_iter=100, max_depth=3,
            learning_rate=.05, min_samples_leaf=40, l2_regularization=10,
            random_state=42),
        'random_forest': RandomForestClassifier(n_estimators=120, max_depth=6,
            min_samples_leaf=35, max_features=3, class_weight='balanced_subsample',
            random_state=42, n_jobs=2),
    }
    scores = {
        'prior60_abs': df.pre_return_60m_pct.abs().to_numpy(),
        'prior60_positive': df.pre_return_60m_pct.to_numpy(),
        'trade2': df.trade_accel.to_numpy(),
        'volume2': df.volume_accel.to_numpy(),
        'early_trades': np.where(df.pre_return_60m_pct.abs() <= 3,
                                 df.trade_accel, -1000000),
    }
    for name, model in models.items():
        model.fit(X.loc[train], df.loc[train, 'hit30'])
        scores[name] = model.predict_proba(X)[:, 1]

    def selected(mask, score, early=False):
        d = df.loc[mask, ['at', 'date', 'pair', 'hit20', 'hit30',
                          'pre_return_60m_pct']].copy()
        d['score'] = np.asarray(score)[mask]
        if early:
            d = d[d.pre_return_60m_pct.abs() <= 3]
        return d.sort_values(['at', 'score', 'pair'], ascending=[True, False, True]
            ).groupby('at', sort=False).head(1)

    def metrics(p):
        positives = p[p.hit30 == 1]
        return {'picks': len(p), 'hits20': int(p.hit20.sum()),
                'hits30': int(p.hit30.sum()),
                'precision30': round(float(p.hit30.mean()), 6),
                'positive_pairs': int(positives.pair.nunique()),
                'positive_pairdays': int(positives.groupby(['pair', 'date']).ngroups)}

    validation = {name: metrics(selected(val, score)) for name, score in scores.items()}
    winner = sorted(validation, key=lambda name:
        (-validation[name]['hits30'], -validation[name]['hits20'], name))[0]
    test_metrics = {name: metrics(selected(test, scores[name]))
                    for name in ('prior60_abs', 'prior60_positive', 'trade2',
                                 'volume2', 'early_trades', winner)}
    early_test = {name: metrics(selected(test, scores[name], early=True))
                  for name in ('prior60_abs', 'trade2', winner)}
    ablations = {}
    for name, ff in {
        'no_volatility': [f for f in fields if f != 'volatility_pct'],
        'no_trade_accel': [f for f in fields if f != 'trade_accel'],
        'volatility_only': ['volatility_pct'],
        'momentum_only': fields[:3],
    }.items():
        model = make_pipeline(StandardScaler(), LogisticRegression(
            max_iter=1000, C=.2, class_weight='balanced'))
        model.fit(X.loc[train, ff], df.loc[train, 'hit30'])
        ablations[name] = metrics(selected(test, model.predict_proba(X[ff])[:, 1]))
    return {'schema': 1, 'source_sha256': source_sha,
            'source_run': 38029912468, 'source_artifact': 11662155953,
            'label': 'max_forward_24h_5m_close_return_ge_30pct',
            'usd_control_rows': len(df),
            'split_counts': {s: int((df.split == s).sum())
                             for s in ('train', 'val', 'test', 'embargo')},
            'validation': validation, 'selected_on_validation': winner,
            'test': test_metrics, 'test_early_only': early_test,
            'post_test_ablation_exploratory': ablations,
            'limitations': ['historical sampled USD controls, not full live 604 markets',
                'overlapping labels and correlated pair-days',
                'no historical spread, orderbook, fills, or lead-time evidence',
                'post-test ablation is hypothesis generation only',
                'not approved for live scoring or trading']}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('source', help='strict October 10 research_training.ndjson')
    p.add_argument('--output')
    a = p.parse_args()
    result = json.dumps(run(a.source), indent=2, sort_keys=True) + '\n'
    if a.output:
        Path(a.output).write_text(result)
    else:
        print(result, end='')


if __name__ == '__main__':
    main()
