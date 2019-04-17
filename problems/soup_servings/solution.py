class Solution:
    def soupServings(self, N: int) -> float:
        if N >= 4800: return 1
        cache = {}
        def search(a, b):
            if a <= 0 or b <= 0:
                if a <= 0 and b <= 0:
                    return 0.5
                elif a <= 0:
                    return 1
                return 0
            else:
                if (a, b) in cache:
                    return cache[(a, b)]
                ans = (search(a-100, b) + search(a-75, b-25) + search(a-50, b-50) + search(a-25, b-75))/4
                cache[(a, b)] = ans
                return ans
        return search(N,N)
