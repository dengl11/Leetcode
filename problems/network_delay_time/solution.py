from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        inf = float('inf')
        ans = [inf] * (N+1) # ans[i]: known time to deliver for the node i}
        ans[K] = 0
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        q = [(K, 0)]
        while q:
            newq = []
            for u, t in q:
                for v, w in edges[u]:
                    if ans[v] > t + w:
                        ans[v] = t + w
                        newq.append((v, t + w))
            q = newq
        ans = max(ans[1:])
        return ans if ans != inf else -1
            
        
        