from bisect import bisect_right

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        n = len(nums)
        def find_smaller(d):
            ans = 0
            for i in range(n-1):
                j = bisect_right(nums, nums[i] + d)
                ans += j-i-1
            return ans
        while low < high:
            mid = (low + high) // 2
            curr = find_smaller(mid)
            if curr < k:
                low = mid + 1
            else:
                high = mid
        return low
                
