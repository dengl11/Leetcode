class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def A(n, m):
            ans = 1
            for i in range(m):
                ans *= n-i
            for i in range(m):
                ans //= i + 1
            return ans
        return A(m + n - 2, n - 1)
        