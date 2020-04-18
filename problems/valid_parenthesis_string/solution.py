from functools import lru_cache
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        @lru_cache(None)
        def check(i, j):
            if i > j or i >= n: return True
            if i == j: return s[i] == '*'
            if s[i] == ')': return False
            if s[i] == '*':
                if check(i + 1, j): return True
            for k in range(i+1, j+1):
                if s[k] in [')', '*'] and check(i+1, k-1) and check(k+1, j): return True
            return False
        return check(0, n - 1)
            