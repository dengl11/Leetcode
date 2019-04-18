class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        N = len(graph)
        def dfs(node, path, visited):
            if node == N-1:
                ans.append(path[:])
            else:
                for n in graph[node]:
                    if n in visited: continue
                    visited.add(n)
                    path.append(n)
                    dfs(n, path, visited)
                    visited.remove(n)
                    path.pop()
        
        dfs(0, [0], {0})
        return ans
                
        