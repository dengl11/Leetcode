from itertools import groupby
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def hash(w):
            return [(k, len(list(v))) for (k, v) in groupby(w)]
        s = hash(S)
        def match(w):
            w = hash(w)
            if len(w) != len(s): return False
            for i in range(len(w)):
                if w[i][0] != s[i][0]: return False
                if s[i][1] < w[i][1]: return False
                if s[i][1] < 3 and s[i][1] != w[i][1]:
                    return False
            return True
        
        return sum(match(w) for w in words)