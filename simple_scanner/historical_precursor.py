"""Read-only precursor research. Only prior market observations are features."""
import math

FIAT = {"USD","EUR","GBP","JPY","CHF","CAD","AUD","NZD","ZUSD","ZEUR","ZGBP","ZJPY","ZCAD","ZAUD"}
STABLE = {"USDT","USDC","DAI","PYUSD","EURC","RLUSD","TUSD","FDUSD","USDD","USDE",
          "USDG","USDS","UST","USTC"}
ALIASES = {"XXBT":"BTC","XETH":"ETH","XXRP":"XRP","XXDG":"DOGE","XBT":"BTC"}

def crypto_pair(pair, asset_pairs=None):
    """Exclude known fiat/stable bases; prefer Kraken AssetPairs metadata if supplied.

    Historical rows currently lack canonical asset IDs. The legacy suffix path
    remains a compatibility fallback until canonical IDs are persisted.
    """
    name = str(pair).upper()
    if asset_pairs is not None:
        meta = asset_pairs.get(pair) or asset_pairs.get(name)
        if meta is None or not isinstance(meta, dict) or not meta.get("base"):
            return False  # Never guess identity when authoritative metadata was requested.
        base = str(meta["base"]).upper()
        base = ALIASES.get(base, base)
        return base not in FIAT | STABLE
    if name.endswith("ZUSD"):
        base = name[:-4]
    elif name.endswith("USD"):
        base = name[:-3]
    else:
        return False
    base = ALIASES.get(base, base)
    return bool(base) and base not in FIAT | STABLE

def rank_precursors(rows, limit=12):
    """Rows: (pair, move24, spread, notional, previous_price, current_price,
    older_price). Relative volume and cross-venue features are unavailable."""
    candidates=[]
    for pair, move24, spread, notional, previous, current, older in rows:
        if not crypto_pair(pair): continue
        vals=(move24,spread,notional,previous,current,older)
        if not all(isinstance(v,(int,float)) and math.isfinite(v) for v in vals): continue
        if min(previous,current,older)<=0 or notional<25000 or spread<0 or spread>125: continue
        if move24 < -8 or move24 > 20: continue
        recent=100*(current/previous-1)
        earlier=100*(previous/older-1)
        acceleration=recent-earlier
        if recent < -3 or recent > 6: continue
        score=(min(40,max(0,acceleration)*18)+min(25,max(0,recent)*12)
               +max(0,20-spread/6)+min(15,max(0,math.log10(max(1,notional/25000)))*8)
               -max(0,move24-8)*3)
        candidates.append({"pair":pair,"score":round(score,3),
                           "recent_change_pct":round(recent,4),
                           "acceleration_pct":round(acceleration,4)})
    return sorted(candidates,key=lambda x:(-x["score"],x["pair"]))[:limit]

def precursor_feature_audit(rows):
    """Read-only diagnostic of existing precursor feature availability.

    Does not modify scoring, ranking, promotion, or production outputs.
    """
    counts = {"rows": 0, "eligible_identity": 0, "valid_numeric": 0,
              "valid_price_history": 0, "liquid_spread": 0,
              "move24_in_range": 0, "recent_move_in_range": 0,
              "positive_acceleration": 0}
    for pair, move24, spread, notional, previous, current, older in rows:
        counts["rows"] += 1
        if not crypto_pair(pair):
            continue
        counts["eligible_identity"] += 1
        vals = (move24, spread, notional, previous, current, older)
        if not all(isinstance(v, (int, float)) and math.isfinite(v) for v in vals):
            continue
        counts["valid_numeric"] += 1
        if min(previous, current, older) <= 0:
            continue
        counts["valid_price_history"] += 1
        if notional < 25000 or spread < 0 or spread > 125:
            continue
        counts["liquid_spread"] += 1
        if move24 < -8 or move24 > 20:
            continue
        counts["move24_in_range"] += 1
        recent = 100 * (current / previous - 1)
        earlier = 100 * (previous / older - 1)
        if recent < -3 or recent > 6:
            continue
        counts["recent_move_in_range"] += 1
        if recent > earlier:
            counts["positive_acceleration"] += 1
    return {"mode": "OBSERVE_ONLY", "counts": counts,
            "available": ["recent_change_pct", "acceleration_pct",
                          "move24_pct", "spread_bps", "notional_24h_usd"],
            "not_available": ["completed_5m_candles", "trade_acceleration",
                              "relative_volume", "order_book_imbalance",
                              "cross_venue_flow"],
            "score_adjustment": 0, "promotion_eligible": False}

def evaluate_precursor(con):
    tables={r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    if not {"market_signals","market_observations"}.issubset(tables):
        return {"status":"AWAITING_HISTORY","promotion_eligible":False}
    latest=con.execute("SELECT MAX(run_at) FROM market_signals").fetchone()[0]
    if not latest: return {"status":"AWAITING_HISTORY","promotion_eligible":False}
    rows=con.execute("""SELECT s.pair,s.move24_pct,s.spread_bps,s.notional_24h_usd,
       (SELECT p.price FROM market_observations p WHERE p.pair=s.pair AND p.run_at<s.run_at
         ORDER BY p.run_at DESC LIMIT 1), n.price,
       (SELECT p.price FROM market_observations p WHERE p.pair=s.pair AND p.run_at<s.run_at
         ORDER BY p.run_at DESC LIMIT 1 OFFSET 1)
       FROM market_signals s JOIN market_observations n ON n.pair=s.pair AND n.run_at=s.run_at
       WHERE s.run_at=?""",(latest,)).fetchall()
    ranked=rank_precursors(rows)
    audit=precursor_feature_audit(rows)
    return {"feature_audit":audit,"status":"SHADOW_PRECURSOR_RESEARCH","observed_at":latest,
            "universe_observed":len(rows),"candidates":ranked,"selection_budget":12,
            "features_unavailable":["relative_volume_full_market","cross_venue_flow","open_interest"],
            "comparison_status":"AWAITING_EQUAL_BUDGET_FORWARD_OUTCOMES",
            "promotion_eligible":False,"live_weights_modified":False,"buy_approved":False}
