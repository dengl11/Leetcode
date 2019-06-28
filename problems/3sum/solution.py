from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            lo, hi = i + 1, len(nums)-1
            tgt = -nums[i]
            while lo < hi:
                if lo > i + 1 and nums[lo] == nums[lo-1]:
                    lo += 1
                    continue
                cur = nums[lo] + nums[hi] 
                if cur == tgt:
                    ans.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                elif cur < tgt:
                    lo += 1
                else:
                    hi -= 1
        return ans
                