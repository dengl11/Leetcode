from heapq import heappush, heappop
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = [(q, w, w/q) for (w, q) in zip(wage, quality)]
        workers.sort()
        pq = []
        ans = sum(x[0] for x in workers[:K]) * max(x[-1] for x in workers[:K])
        Q = 0
        for q, w, ratio in workers:
            heappush(pq, (-ratio, -q))
            Q += q
            if len(pq) > K:
                nr, nq = heappop(pq)
                Q += nq
                ans = min(ans, Q * (-pq[0][0]))
        return ans