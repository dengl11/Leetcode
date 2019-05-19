from collections import defaultdict
class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        if not A: return 0
        m = len(A)
        n = len(A[0])
        idx = {w:i for (i,w) in enumerate(A)}
        def valid(w1, w2):
            diffs = [i for i in range(n) if w1[i] != w2[i]]
            return len(diffs) == 2
        
        uf = {i:i for i in range(m)}
        def find(i):
            if uf[i] != i:
                uf[i] = find(uf[i])
            return uf[i]
        
        def union(i, j):
            uf[find(i)] = find(j)
        if m < n:
            for i in range(m):
                for j in range(i+1, m):
                    if valid(A[i], A[j]):
                        union(i, j)
        else:
            for i, w in enumerate(A):
                for j in range(len(w)):
                    for k in range(j+1, len(w)):
                        cw = w[:j]+w[k]+w[j+1:k]+w[j]+w[k+1:]
                        if cw in idx:
                            union(i, idx[cw])
                    
        return len(set(find(i) for i in range(m)))