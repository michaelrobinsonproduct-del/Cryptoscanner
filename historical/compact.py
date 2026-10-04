import json, os
src="historical/output/research.ndjson"
dst="historical/output/research_training.ndjson"
seen=set(); kept=0
with open(src) as r, open(dst,"w") as w:
    for line in r:
        x=json.loads(line)
        day=x["anchor_at"][:10]
        key=(x["pair"],day)
        keep=False
        if x.get("major_mover") and x.get("still_early"): keep=True
        elif key not in seen:
            seen.add(key); keep=True
        if keep:
            w.write(json.dumps(x,separators=(",",":"))+"\n"); kept+=1
print(json.dumps({"training_rows":kept}))
