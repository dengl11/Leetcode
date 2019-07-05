from bisect import bisect_left
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        ans = -1
        for i, x in enumerate(A):
            j = bisect_left(A, K - x, lo = 0, hi = i) - 1
            if j >= 0:
                ans = max(ans, A[j] + x)
        return ans
            
            