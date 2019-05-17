from collections import deque
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        inf = float('inf')
        ans = inf
        n = len(A)
        preSum = [0]
        for k in range(n):
            preSum.append(preSum[-1] + A[k])
        q = deque()
        for i in range(n+1):
            while q and preSum[i] - preSum[q[0]] >= K:
                ans = min(ans, i-q.popleft())
            while q and preSum[q[-1]] >= preSum[i]: q.pop()
            q.append(i)
        return ans if ans != inf else -1
