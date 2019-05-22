from heapq import heappop,heappush
class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        pq = []
        n = len(A)
        for i in range(1, n):
            heappush(pq, (1/A[i], 0, i))
        while K > 0:
            _, p, q = heappop(pq)
            K -= 1
            if K == 0: return[A[p], A[q]]
            p += 1
            if p < q:
                heappush(pq, (A[p]/A[q], p, q))
        