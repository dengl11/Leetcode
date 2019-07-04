from collections import defaultdict, Counter
from functools import lru_cache
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        G = defaultdict(Counter)
        for s, t in tickets:
            G[s][t] += 1
        
        def query(s):
            if not G[s]: 
                if all(not x for x in G.values()):
                    return [s]
                return []
            for t in sorted(G[s]):
                G[s][t] -= 1
                if G[s][t] == 0: del G[s][t]
                curr = query(t)
                if curr: return [s] + curr
                G[s][t] += 1
            return []
        return query("JFK")
        