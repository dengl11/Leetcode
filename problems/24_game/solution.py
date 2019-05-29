from itertools import permutations
from math import isclose
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) == 1: return isclose(nums[0], 24)
        for a, b, *remain in permutations(nums, len(nums)):
            for x in set([a + b, a - b, a * b, b and a/b]):
                if self.judgePoint24([x] + remain): return True
        return False
        