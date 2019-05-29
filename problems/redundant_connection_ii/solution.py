from collections import defaultdict
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        edges.reverse()
        nbrs = defaultdict(list)
        parents = defaultdict(list)
        n = 0
        for i, j in edges:
            nbrs[i].append(j)
            parents[j].append(i)
            n = max(n, i, j)
        
        # detect cycle
        visited = set()
        def detect_cycle(i):
            if i in visited: return
            visited.add(i)
            stack = [i]
            def dfs(i, V, path):
                for j in nbrs[i]:
                    if j in V:
                        return path[path.index(j):]
                    V.add(j)
                    visited.add(j)
                    path.append(j)
                    curr = dfs(j, V, path)
                    if curr: return curr
                    V.remove(path.pop())
            return dfs(i, {i}, [i])
                    
        for i in range(1, n+1):
            curr = detect_cycle(i)
            if curr:
                curr = set(curr)
                candidate = None
                for i, j in edges:
                    if i in curr and j in curr:
                        if candidate is None: candidate = [i, j]
                        if len(parents[j]) > 1: return [i, j]
                return candidate
                    
        for i, j in edges:
            if len(parents[j]) > 1:
                return [i, j]
                