from collections import deque
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        step = 0
        reach = 0
        end = 0
        for i in range(n-1):
            reach = max(reach, i + nums[i])
            if i == end:
                step += 1
                end = reach
        return step
            