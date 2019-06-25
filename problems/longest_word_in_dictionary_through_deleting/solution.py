class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key = lambda s: (-len(s), s))
        def sub(w):
            i = 0
            for c in w:
                while i < len(s) and s[i]!=c: 
                    i += 1
                if i >= len(s):
                    return False
                i += 1
            return True
        for w in d:
            if sub(w): return w
        return ""
            
        