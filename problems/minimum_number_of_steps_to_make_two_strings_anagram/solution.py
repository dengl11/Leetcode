from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sc = Counter(s)
        st = Counter(t)
        pos = 0
        for k in range(26):
            c = chr(k + 97)
            ic, it = sc[c], st[c]
            if ic > it:
                pos += ic - it
        return pos