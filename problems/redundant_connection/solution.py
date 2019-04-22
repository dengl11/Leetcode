from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        def dfs(node, cycle):
            for n in graph[node]:
                if n in cycle: 
                    return {k for k in cycle if cycle[k] >= cycle[n]}
                graph[n].remove(node)
                cycle[n] = len(cycle) + 1
                curr = dfs(n, cycle)
                if curr: return curr
                del cycle[n]
            return None
        
        cycle = dfs(1, {1:0})
        for i in range(len(edges)-1, -1, -1):
            e = edges[i]
            if e[0] in cycle and e[1] in cycle: return e
        
        
        