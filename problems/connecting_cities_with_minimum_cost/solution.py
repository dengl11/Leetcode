from heapq import heappop, heappush
from collections import defaultdict
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        nbrs = defaultdict(list)
        for i, j, c in connections:
            nbrs[i].append((j, c))
            nbrs[j].append((i, c))
            
        ans = 0
        q = [(0, 1)]
        visited = set()
        while q:
            c, i = heappop(q)
            if i in visited: continue
            visited.add(i)
            ans += c
            if len(visited) == N: return ans
            for j, c in nbrs[i]:
                if j in visited: continue
                heappush(q, (c, j))
        return -1
            
            