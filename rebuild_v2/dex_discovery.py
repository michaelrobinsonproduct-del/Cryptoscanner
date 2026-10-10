"""Isolated, read-only DEX discovery. Never emits executable trade approvals."""
import datetime as dt
import json
import urllib.parse
import urllib.request

BASE="https://api.dexscreener.com"

def get_json(path, timeout=12):
    req=urllib.request.Request(BASE+path,headers={"Accept":"application/json","User-Agent":"cryptoscanner-research/1.0"})
    with urllib.request.urlopen(req,timeout=timeout) as response:
        return json.load(response)

def discover(fetch=get_json, now=None, max_tokens=12):
    """Sample newest token profiles and resolve active DEX pools, research only.

    This is a limited *new-profile sample*, not exhaustive DEX coverage.
    Every quote is independently checked for age, liquidity, and pair identity.
    """
    now=now or dt.datetime.now(dt.timezone.utc)
    report={"status":"COMPLETE","source":"DEXSCREENER_NEW_PROFILES",
            "coverage":"SAMPLED_NEW_PROFILES_NOT_FULL_DEX",
            "fetched_at":now.isoformat(),"profiles_seen":0,
            "profiles_checked":0,"pairs_evaluated":0,"eligible_pairs":0,
            "candidates":[],"errors":[],"entry_approved":False,\n            "rejection_counts":{},"near_miss_samples":[],"candidate_count_total":0}
    try:
        profiles=fetch("/token-profiles/latest/v1")
        if not isinstance(profiles,list):
            raise ValueError("invalid profile response")
        report["profiles_seen"]=len(profiles)
        seen=set()\n        def reject(reason, pair):\n            counts=report["rejection_counts"]\n            counts[reason]=counts.get(reason,0)+1\n            if len(report["near_miss_samples"])<12:\n                report["near_miss_samples"].append({"reason":reason,"chain":chain,"pair_address":pair.get("pairAddress")})
        for profile in profiles:
            if report["profiles_checked"]>=max_tokens:break
            if not isinstance(profile,dict):continue
            chain=profile.get("chainId")
            address=profile.get("tokenAddress")
            if not isinstance(chain,str) or not isinstance(address,str):continue
            if not chain or not address or len(chain)>60 or len(address)>150:continue
            key=(chain,address.lower())
            if key in seen:continue
            seen.add(key)
            report["profiles_checked"]+=1
            try:
                path="/token-pairs/v1/"+urllib.parse.quote(chain,safe="")+"/"+urllib.parse.quote(address,safe="")
                pairs=fetch(path)
                if not isinstance(pairs,list):raise ValueError("invalid pair response")
                for pair in pairs[:25]:
                    report["pairs_evaluated"]+=1
                    if not isinstance(pair,dict):continue\n                    if pair.get("chainId")!=chain:\n                        reject("chain_mismatch",pair);continue
                    base=pair.get("baseToken") or {}
                    quote=pair.get("quoteToken") or {}
                    if address.lower() not in (str(base.get("address","")).lower(),str(quote.get("address","")).lower()):\n                        reject("token_mismatch",pair);continue
                    liquidity=pair.get("liquidity") or {}
                    volume=pair.get("volume") or {}
                    change=pair.get("priceChange") or {}
                    try:
                        usd=float(liquidity.get("usd") or 0)
                        volume24=float(volume.get("h24") or 0)
                        move=float(change.get("h1") or 0)
                        created=int(pair.get("pairCreatedAt") or 0)
                    except (ValueError,TypeError,OverflowError):\n                        reject("invalid_metrics",pair);continue
                    age=(now.timestamp()*1000-created)/1000 if created else -1
                    if not 0<=age<=86400*30:\n                        reject("pool_age",pair);continue\n                    if usd<25000:\n                        reject("low_liquidity",pair);continue\n                    if volume24<10000:\n                        reject("low_volume",pair);continue\n                    if not -30<=move<=100:\n                        reject("extreme_move",pair);continue
                    report["candidates"].append({
                        "chain":chain,"pair_address":pair.get("pairAddress"),
                        "token_address":address,"symbol":base.get("symbol"),
                        "liquidity_usd":round(usd,2),"volume_24h_usd":round(volume24,2),
                        "change_1h_pct":round(move,2),"pair_age_hours":round(age/3600,2),
                        "status":"DEX_RESEARCH_ONLY","entry_approved":False})
            except Exception as exc:
                report["errors"].append({"chain":chain,"token_address":address,"error":str(exc)[:180]})
        report["eligible_pairs"]=len(report["candidates"])\n        report["candidate_count_total"]=len(report["candidates"])
        if report["errors"]:report["status"]="PARTIAL"
    except Exception as exc:
        report["status"]="FAILED"
        report["errors"].append({"error":str(exc)[:180]})
    report["candidates"]=sorted(report["candidates"],key=lambda p:(-p["volume_24h_usd"],-p["liquidity_usd"]))[:20]
    return report
