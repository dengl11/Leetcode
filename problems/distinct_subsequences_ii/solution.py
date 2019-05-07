from collections import Counter
class Solution:
    def distinctSubseqII(self, S: str) -> int:
        ans = 0
        ending = Counter()
        for i, c in enumerate(S):
            ans, ending[c] = ans * 2 - ending[c] + 1, ans + 1
        return ans % (10**9   + 7)
