from itertools import groupby
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        base = [(x[0], len(list(x[1]))) for x in groupby(S)]
        def valid(w):
            curr = [(x[0], len(list(x[1]))) for x in groupby(w)]
            if len(curr) != len(base): return False
            for (c1, cnt1), (c2, cnt2) in zip(base, curr):
                if c1 != c2 or cnt2 > cnt1: return False
                if cnt1 == cnt2: continue
                if cnt1 < 3: return False
            return True
            
        return len([w for w in words if valid(w)])
            