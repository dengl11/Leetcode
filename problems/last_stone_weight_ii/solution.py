class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {0}
        for x in stones:
            dp = {y+x for y in dp} | {y-x for y in dp}
        return min(abs(x) for x in dp)