from heapq import heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = []
        for s in stones:
            heappush(q, -s)
        while len(q) > 1:
            y, x = -heappop(q),  -heappop(q)
            if x == y: continue
            heappush(q, -abs(x-y))
        return 0 if not q else -q[0]