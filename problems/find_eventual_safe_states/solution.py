class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # 0: undecided
        # 1: safe
        # 2: not safe
        colors = [0] * n
        for i, e in enumerate(graph):
            if not e: colors[i] = 1
        def explore(node, visited):
            if colors[node]: return colors[node]
            for n in graph[node]:
                if n in visited or colors[n] == 2:
                    for x in visited:
                        colors[x] = 2
                    return 2
                visited.add(n)
                if explore(n, visited) == 2:
                    return 2
                visited.remove(n)
            colors[node] = 1
            return 1
                
        for i in range(n):
            explore(i, {i})
            # print(i, colors)
        return [i for i in range(n) if colors[i] != 2]
            