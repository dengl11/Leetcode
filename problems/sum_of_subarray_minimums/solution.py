class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        ans = 0
        n = len(A)
        stack = []
        left, right = [-1] * n, [n] * n
        for i, a in enumerate(A):
            while stack and stack[-1][0] > a:
                cx, ci= stack.pop()
                right[ci] = i
            stack.append((a, i))
        stack = []
        for i, a in enumerate(A[::-1]):
            while stack and stack[-1][0] >= a:
                cx, ci= stack.pop()
                left[ci] = n-1-i
            stack.append((a, n-1-i))
        for i in range(n):
            ans += A[i] * (i - left[i]) * (right[i] - i)
        return ans % (10**9 + 7)