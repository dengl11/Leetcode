from bisect import bisect_left as bl, bisect_right as br
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l, r = bl(nums, target), br(nums, target)
        return (r - l) > n // 2