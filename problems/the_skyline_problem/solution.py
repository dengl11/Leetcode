from heapq import heappop, heappush, heapify
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = sorted([(l, -h, r) for (l, r, h) in buildings] + \
                       [(r, 0, None) for (l, r, h) in buildings])
        ans = [(0, 0)]
        heights = [(0, float('inf'))]
        for l, nh, r in events:
            while l >= heights[0][1]:
                heappop(heights)
            if nh:
                heappush(heights, (nh, r))
            if ans[-1][1] + heights[0][0]:
                ans.append((l, -heights[0][0]))
        return ans[1:]
                