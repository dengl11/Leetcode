class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        pre = None
        ans = []
        for i, x in enumerate(nums):
            if i == len(nums) - 1 or x + 1 < nums[i + 1]:
                if pre is None or pre == x:
                    ans.append(str(x))
                else:
                    ans.append("{}->{}".format(pre, x))
                if i + 1 < len(nums):
                    pre = nums[i + 1]
            if pre is None:
                pre = x
        return ans
        