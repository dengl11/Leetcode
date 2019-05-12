from collections import defaultdict
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        for i,j in paths:
            edges[i-1].append(j-1)
            edges[j-1].append(i-1)
        colors = [-1]*N
        candidates = [{1,2,3,4} for _ in range(N)]
        for i in range(N):
            colors[i] = min(candidates[i])
            for j in edges[i]:
                if colors[j] < 0:
                    candidates[j].discard(colors[i])
        return colors