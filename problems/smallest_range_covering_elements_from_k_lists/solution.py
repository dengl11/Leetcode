from heapq import heappush, heappop
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        q = []
        n = len(nums)
        right = -float('inf')
        for j, arr in enumerate(nums):
            heappush(q, (arr[0], j, 0))
            right = max(right, arr[0])
            
        ans = (q[0][0], right)
        while q:
            v, i, j = heappop(q)
            if right - v < ans[1]-ans[0]:
                ans = (v, right)
            if j + 1 < len(nums[i]):
                heappush(q, (nums[i][j+1], i, j+1))
                right = max(right, nums[i][j+1])
            else:
                break
        return ans
        