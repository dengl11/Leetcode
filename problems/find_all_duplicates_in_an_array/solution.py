class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i, x in enumerate(nums, 1):
            if x == i: continue
            nums[i-1] = 0
            while x:
                t = nums[x-1]
                if t == x:
                    ans.append(x)
                    break
                nums[x-1] = x
                x = t
        return ans
                
        