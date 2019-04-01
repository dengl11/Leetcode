from collections import defaultdict

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        unions = {}
        def find(i):
            if unions[i] != i:
                unions[i] = find(unions[i])
            return unions[i]
        
        def union(i, j):
            unions[find(i)] = find(j)
        
        
        xs = defaultdict(list)
        ys = defaultdict(list)
        for i, (x, y) in enumerate(stones):
            unions[i] = i
            if xs.get(x, []):
                union(i, xs[x][0])
            xs[x].append(i)
            if ys.get(y, []):
                union(i, ys[y][0])
            ys[y].append(i)
        return len(stones) - len(set(find(i) for i in range(len(stones))))
            