from heapq import heappush, heappop
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        q = [(0, 0, src)] # [(accPrice, nStops, src)]
        while q:
            accPrice, nStops, curr = heappop(q)
            if curr == dst: return accPrice
            if nStops <= K:
                for (v, w) in graph[curr]:
                    heappush(q, (accPrice + w, nStops + 1, v))
        return -1
        