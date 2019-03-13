from collections import deque
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        n = len(S)
        ans = []
        nums = deque(range(n+1))
        for i in range(n-1, -1, -1):
            if S[i] == 'D':
                ans.append(nums.popleft())
            else:
                ans.append(nums.pop())
        ans.append(nums.pop())
        return ans[::-1]
        