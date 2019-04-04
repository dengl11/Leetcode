from collections import Counter
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        ans = need = 0
        for x in A:
            ans += max(need - x, 0)
            need = max(need + 1, x + 1)
        return ans