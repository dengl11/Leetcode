class Solution:
    def isBipartite(self, edges: List[List[int]]) -> bool:
        n = len(edges)
        colors = [-1] * n
        def color(node):
            if colors[node] != -1: return True
            color = 1
            q = [node]
            while q:
                nq = []
                for node in q:
                    colors[node] = color
                    for i in edges[node]:
                        if colors[i]>= 0 and colors[i]==colors[node]: return False
                        if colors[i] < 0:
                            nq.append(i)
                q = nq
                color = 1-color
            return True
        return all(color(i) for i in range(n))
        
                        