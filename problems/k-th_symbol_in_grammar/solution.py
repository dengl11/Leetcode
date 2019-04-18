class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        def query(k, n):
            if n == 1: return 0
            halfsize = 1 << (n-2)
            if k <= halfsize: return query(k, n-1)
            parent = query((k-1)//2+1, n-1)
            return parent if k%2 == 1 else 1- parent
        return query(K, N)
            