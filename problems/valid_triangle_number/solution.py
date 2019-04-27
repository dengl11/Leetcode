class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        ans = 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == 0: continue
            k = i + 2
            for j in range(i+1, len(nums)-1):
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    ans += k - j
                    k += 1
                    
        return ans
                
        