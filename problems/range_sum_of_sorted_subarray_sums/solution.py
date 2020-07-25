from functools import lru_cache
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        nums = [0] + nums
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        arr = sorted([(nums[j] - nums[i]) for i in range(len(nums)) for j in range(i+1, len(nums)) ])
        return sum(arr[left-1:right]) % (10**9 + 7)
        
        