class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        _degrees = [len(graph[i]) for i in range(n)]
        starts = [i for i in range(n) if len(graph[i]) == min(_degrees)]
        
        def search(i, visited):
            visited.add(i)
            if len(visited) == n: return 1
            ans = 1
            for j in graph[i]:
                degrees[j] -= 1
            candidates = []
            for j in graph[i]:
                if j in visited: continue
                candidates.append((j, degrees[j]))
            for j, _ in sorted(candidates, key = lambda x:x[1]):
                if j in visited: continue
                t = search(j, visited)
                ans += abs(t)
                if t >= 0: return ans
                ans += 1
            return -ans
        ans = float('inf')
        for x in starts:
            degrees = _degrees[:]
            ans = min(ans, search(x, set()))
        return ans - 1 if ans != float('inf') else 0
            
                
                
                
            
            
        