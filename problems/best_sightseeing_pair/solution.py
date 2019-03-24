class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ans = 0
        curr = 0
        for x in A:
            ans = max(ans, curr + x)
            curr = max(curr, x) - 1
        return ans