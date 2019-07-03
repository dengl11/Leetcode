class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == k: return min(nums)
        if 1 == k: return max(nums)
        pivot = nums[0]
        left = [x for x in nums if x < pivot]
        right = [x for x in nums if x > pivot]
        middle = [x for x in nums if x == pivot]
        if len(right) >= k: return self.findKthLargest(right, k)
        if len(right) < k and len(right) + len(middle) >= k: return pivot
        return self.findKthLargest(left, k - len(right) - len(middle))