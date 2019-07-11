from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return  []
        q = deque()
        def push(i):
            if q and q[0] <= i-k: q.popleft()
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            
        ans = []
        for i in range(len(nums)):
            push(i)
            ans.append(nums[q[0]])
            
        return ans[k-1:]