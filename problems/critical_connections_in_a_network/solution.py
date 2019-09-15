from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        nbrs = defaultdict(set)
        for i, j in connections:
            nbrs[i].add(j)
            nbrs[j].add(i)
        parent = [n]*n
        lowest = [n]*n
        visited = [False] * n
        depth = [n]*n
        ans = []
        self.depth = 0
        def dfs(node):
            lowest[node] = self.depth
            visited[node] = True
            depth[node] = self.depth
            self.depth += 1
            for v in nbrs[node]:
                if not visited[v]:
                    parent[v] = node
                    dfs(v)
                    if lowest[v] > depth[node]:
                        ans.append([node, v])
                if parent[node] != v:
                    lowest[node] = min(lowest[node], lowest[v])
        dfs(0)
        return ans