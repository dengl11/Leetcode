class Solution:
    def bestRotation(self, A: List[int]) -> int:
        n = len(A)
        diff = [1] * n
        for i in range(n):
            diff[(i - A[i] + 1 + n) % n] -= 1
        for i in range(1, n):
            diff[i] += diff[i-1]
        assert(diff[-1] == 0)
        return diff.index(max(diff))
        