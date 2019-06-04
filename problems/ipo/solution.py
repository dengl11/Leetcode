from heapq import heappush, heappop
class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        projects = sorted((c, p) for (c, p) in zip(Capital, Profits))
        i = 0
        q = []
        ans = W
        for _ in range(k):
            while i < len(projects) and projects[i][0] <= ans:
                c, p = projects[i]
                heappush(q, -p)
                i += 1
            if q: ans += -heappop(q)
        return ans