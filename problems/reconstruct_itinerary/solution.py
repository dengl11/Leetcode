from collections import defaultdict, Counter
from functools import lru_cache
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        G = defaultdict(list)
        for s, t in sorted(tickets, reverse=True):
            G[s].append(t)
        L = []
        def query(s):
            while G[s]:
                query(G[s].pop())
            L.append(s)
        query("JFK")
        return L[::-1]
        