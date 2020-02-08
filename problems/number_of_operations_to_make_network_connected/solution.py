class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1: return -1
        uf = [i for i in range(n)]
        def find(i):
            if uf[i] == i: return i
            return find(uf[i])
        
        def union(i, j):
            uf[find(i)] = find(j)
        
        for i, j in connections:
            union(i, j)
        
        nComponents = len(set(find(i) for i in range(n)))
        return (nComponents - 1)
        
        