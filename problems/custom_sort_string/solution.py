from collections import Counter
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        pos = Counter(T)
        ans = ""
        for c in S:
            p = pos.pop(c, 0)
            ans += c * p
        for k, v in pos.items():
            ans += k*v
        return ans