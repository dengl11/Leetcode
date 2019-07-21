from collections import defaultdict, deque
from functools import lru_cache
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red_sources = defaultdict(set)
        blue_sources = defaultdict(set)
        for s, t in red_edges:
            red_sources[s].add(t)
        for s, t in blue_edges:
            blue_sources[s].add(t)
        
        ans = [-1 for i in range(n)]
        q = deque([(0, 0, None)])
        done = set([(0, "red"), (0, "blue")])
        while q:
            node, cost, color = q.popleft()
            # print(node, cost, color)
            if ans[node] == -1: 
                ans[node] = cost
            if color != "red": 
                for t in red_sources[node]:
                    if (t, "red") not in done:
                        q.append((t, cost + 1, "red"))
                        done.add((t, "red"))
            if color != "blue": 
                for t in blue_sources[node]:
                    if (t, "blue") not in done:
                        q.append((t, cost + 1, "blue"))
                        done.add((t, "blue"))
        return ans
                        
            
        
            