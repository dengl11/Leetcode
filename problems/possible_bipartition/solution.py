from collections import defaultdict
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list) # {node_id: [node]}
        for i, j in dislikes:
            graph[i].append(j)
            graph[j].append(i)
        colors = dict()
        def dfs(node, color):
            colors[node] = color
            for nbr in graph[node]:
                if nbr in colors:
                    if colors[nbr] == color: return False
                else:
                    colors[nbr] = 1 - color
                    if not dfs(nbr, 1 - color):
                        return False
            return True
        for i in range(1, N + 1):
            if i in colors: continue
            if not dfs(i, 0):
                return False
        return True