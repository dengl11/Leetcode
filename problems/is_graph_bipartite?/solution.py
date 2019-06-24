from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {} # node: color
        def color(node, c):
            if node in colors: return True
            q = deque([(node, c)])
            while q:
                node, c = q.popleft()
                colors[node] = c
                for n in graph[node]:
                    if n in colors:
                        if colors[n] != 1-c: return False
                        continue
                    q.append((n, 1-c))
            return True
        
        return all(color(x, 1) for x in range(len(graph)))