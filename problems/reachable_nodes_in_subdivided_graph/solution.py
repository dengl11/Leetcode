from collections import defaultdict
from heapq import heappush, heappop
class Solution(object):
    def reachableNodes(self, edges, M, N):
        """
        :type edges: List[List[int]]
        :type M: int
        :type N: int
        :rtype: int
        """
        visited = set() # {i}
        graph = defaultdict(dict)
        for i, j, n in edges:
            graph[i][j] = n
            graph[j][i] = n
        q = [(-M, 0)]
        ans = 0
        while q:
            m, i = heappop(q)
            if i in visited: continue
            visited.add(i)
            m = -m
            ans += 1
            if m == 0: continue
            for j in list(graph[i].keys()):
                n = graph[i][j]
                if n < m:
                    if n > 0:
                        ans += n
                        graph[j][i] = 0
                        graph[i][j] = 0
                    if j not in visited:
                        heappush(q, (n+1-m, j))
                else:
                    ans += m
                    graph[j][i] = n-m
        return ans
        