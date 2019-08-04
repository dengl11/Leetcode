class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        ans = float('inf')
        for start in [0, 1]:
            curr = 0
            for i in range(start, len(nums), 2):
                diff = 0
                if i > 0:             diff = max(nums[i] - nums[i-1] + 1, diff)
                if i + 1 < len(nums): diff = max(nums[i] - nums[i+1] + 1, diff)
                curr += diff
            ans = min(ans, curr)
        return ans
        

