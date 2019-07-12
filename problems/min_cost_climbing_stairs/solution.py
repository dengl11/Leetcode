class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pre, curr = 0, 0
        for i in range(2, len(cost) + 1):
            curr, pre = min(pre + cost[i-2], curr + cost[i-1]), curr
        return curr
        