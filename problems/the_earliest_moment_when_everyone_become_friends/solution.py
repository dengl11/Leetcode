class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        logs.sort(key = lambda x:x[0])
        
        uf = {}
        cluster = set(range(N))
        def find(i):
            if uf.get(i, i) != i:
                uf[i] = find(uf[i])
            return uf.get(i, i)
        
        def union(i, j):
            ci, cj = find(i), find(j)
            if ci != cj:
                cluster.remove(ci)
            uf[ci] = cj

        for t, i, j in logs:
            union(i, j)
            if len(cluster) == 1: return t
        return -1