from heapq import heappop, heappush, nsmallest
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        aa = [0] + A + A
        n = len(A)
        for i in range(1, n * 2+1):
            aa[i] += aa[i-1]
        h = []
        ans = A[0]
        for i, x in enumerate(aa):
            if h:
                while h and i - h[0][1] > n:
                    heappop(h)
                if h:
                    ans = max(ans, x - h[0][0])
            heappush(h, (x, i))
        return ans
            
                