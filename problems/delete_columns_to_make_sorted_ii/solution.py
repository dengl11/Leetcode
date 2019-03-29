class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        m, n = len(A), len(A[0])
        ans = 0
        done = [False] * m
        for col in zip(*A):
            if all(done[i] or col[i] <= col[i + 1] for i in range(m - 1)):
                for i in range(m - 1):
                    if col[i] < col[i + 1]:
                        done[i] = True
            else:
                ans += 1
        return ans
