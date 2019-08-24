from heapq import heappush, heappop
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        q = []
        for x in sticks:
            heappush(q, x)
        ans = 0
        while len(q) > 1:
            x = heappop(q)
            y = heappop(q)
            ans += x + y
            heappush(q, x + y)
        return ans