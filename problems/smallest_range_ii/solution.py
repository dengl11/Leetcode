class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        ans = A[-1] - A[0]
        for i in range(len(A) - 1):
            mi = min(A[i+1], A[0] + 2 * K)
            ma = max(A[-1], A[i] + 2 * K)
            ans = min(ans, ma - mi)
        return ans