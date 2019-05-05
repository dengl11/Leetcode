from collections import defaultdict, Counter
from functools import reduce
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def find(i):
            if uf.get(i, i) != i:
                uf[i] = find(uf[i])
            return uf.get(i, i)
        
        def union(i, j):
            uf[find(i)] = find(j)
        
        facs = []
        for i, x in enumerate(A):
            j = 2
            curr = []
            while j * j <= x:
                if x % j == 0:
                    while x % j == 0:
                        x //= j
                    curr.append(j)
                j += 1
            if x > 1 or not curr:
                curr.append(x)
            facs.append(curr)
        # primes = list({p for f in facs for p in f})
        # fac2idx = {p: i for i, p in enumerate(primes)}
        
        fac2idx = {x:i for (i, x) in enumerate(list({p for f in facs for p in f}))}
        uf = {i:i for i in range(len(fac2idx))}
        for f in facs:
            for x in f:
                union(fac2idx[x], fac2idx[f[0]])
        
        clusters = Counter(find(fac2idx[f[0]]) for f in facs)
        
        return max(clusters.values())