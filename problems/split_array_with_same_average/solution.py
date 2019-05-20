class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        N = len(A)
        S = sum(A)
        A.sort(reverse=True)
        cache = dict()
        def recurse(tgt, i, k):
            if k == 0: return tgt == 0
            if tgt < 0 or i + k >= N or tgt > A[i]*k: return False
            if (tgt, k) in cache and i >= cache[(tgt, k)]: return False
            ans = any(recurse(tgt - A[j], j+1, k-1) or recurse(tgt, j+1, k) for j in range(i, N-k+1))
            if not ans:
                cache[(tgt, k)] = min(i, cache.get((tgt, k), N))
            return ans
        
        return any(recurse(int(S/N*n), 0, n) for n in range(1, N//2 + 1) if (S*n)%N == 0)