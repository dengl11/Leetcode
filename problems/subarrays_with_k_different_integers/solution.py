from collections import Counter
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        n = len(A)
        def atLeastK(k):
            c = Counter(A[n-k+1:])
            C = Counter(A[n-k+1:])
            ans = 0
            j = n-1
            for i in range(n-k, -1, -1):
                c[A[i]] += 1
                C[A[i]] += 1
                while len(c) >= k:
                    c[A[j]] -= 1
                    if c[A[j]] == 0: del c[A[j]]
                    j -= 1
                if len(C) >= K:
                    ans += n-j-1
            return ans
        return atLeastK(K) - atLeastK(K + 1)
                