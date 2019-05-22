class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        left = 0
        right = 1e10
        def n_zero(x):
            ans = 0
            while x:
                ans += x//5
                x //= 5
            return ans
        
        while left < right:
            mid = (left + right) // 2
            if n_zero(mid) < K:
                left = mid + 1
            else:
                right = mid
        if n_zero(left) == K: return 5
        return 0
            