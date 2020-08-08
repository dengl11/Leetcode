from collections import Counter
class Solution:
    def numSplits(self, s: str) -> int:
        left, right = Counter(), Counter(s)
        ans = 0
        for c in s:
            left[c] += 1
            right[c] -= 1
            if right[c] == 0:
                del right[c]
            if len(left) == len(right):
                ans += 1
        return ans