from collections import defaultdict, Counter
from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visits = defaultdict(list) # {website: {user...}}
        sequences = Counter()
        for t, u, w in sorted(zip(timestamp, username, website)):
            visits[u].append(w)
        for k, ws in visits.items():
            seen = set()
            for t in combinations(ws, 3):
                if t in seen: continue
                sequences[t] += 1
                seen.add(t)
        m = max(sequences.values())
        ans = [k for k in sequences if sequences[k] == m]
        return min(ans)