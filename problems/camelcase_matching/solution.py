class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        n = len(pattern)
        def match(w):
            i = 0
            for c in pattern:
                while i < len(w) and w[i] != c:
                    if w[i].isupper(): return False
                    i += 1
                if i >= len(w): return False
                i += 1
            return i >= len(w) or w[i:].islower()
        return [match(w) for w in queries]
            