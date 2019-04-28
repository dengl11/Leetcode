class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        def A(n, c):
            ans = 1
            for _ in range(c):
                ans *= n
                n -= 1
            return ans
        ans = 0
        nums = [int(x) for x in str(N + 1)]
        n = len(nums)
        for i in range(1, n):
            ans += 9 * A(9, i-1)
        
        used = set()
        for i, x in enumerate(nums):
            for j in range(0 if i else 1, x):
                if j in used: continue
                ans += A(9-i, n - i - 1)
            if x in used: break
            used.add(x)
        return N - ans