from collections import defaultdict
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T: return 0
        routes = [set(r) for r in routes]
        G = defaultdict(list)
        q = []
        ends = set()
        for i, r in enumerate(routes):
            if S in r: q.append((i, 1))
            if T in r: ends.add(i)
            for j in range(i+1, len(routes)):
                if routes[i] & routes[j]: 
                    G[i].append(j)
                    G[j].append(i)
        visited = set(q)
        for r, m in q:
            if r in ends: return m
            for j in G[r]:
                if j in visited: continue
                visited.add(j)
                q.append((j, m + 1))
        return -1
            
        
        