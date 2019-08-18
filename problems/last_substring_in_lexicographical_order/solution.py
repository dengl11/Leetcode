class Solution:
    def lastSubstring(self, s: str) -> str:
        first = max(s)
        starts = [i for i, c in enumerate(s) if c == first]
        return max(s[i:] for i in starts)