from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
                
        def search(lo, hi):
            i = bisect_left(nums, target, lo = lo, hi = hi)
            if i < len(nums) and nums[i] == target: return i
            return -1
        left = search(0, lo)
        if left >= 0: return left
        return search(lo, len(nums))
        