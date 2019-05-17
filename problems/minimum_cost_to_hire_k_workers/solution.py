from heapq import heappop,heappush
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        pairs = sorted((w/q, q) for w,q in zip(wage, quality))
        wqs = [p[0] for p in pairs]
        qs = [p[1] for p in pairs]
        q = []
        for j in range(K):
            heappush(q, -qs[j])
        accQs = sum(qs[:K])
        ans = accQs * wqs[K-1]
        for k in range(K, len(qs)):
            accQs += qs[k] + heappop(q)
            heappush(q, -qs[k])
            ans = min(ans, wqs[k] * accQs)
        return ans
        
        
        