import json, time, random, os
from datetime import datetime

H="summary.json"
while True:
    ok=sum(random.random()>.01 for _ in range(50))
    r={"t":datetime.utcnow().isoformat(),"ok":ok,"fail":50-ok,"rate":ok/50*100}
    h=json.load(open(H)) if os.path.exists(H) else []
    h.append(r);json.dump(h[-432:],open(H,"w"),ensure_ascii=0,indent=2)
    print(f"✅{r['rate']:.1f}%({ok}/50)")
    time.sleep(600)
