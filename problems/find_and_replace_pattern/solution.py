class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def hash(w):
            seen = dict()
            ans = []
            for c in w:
                if c not in seen:
                    seen[c] = len(seen)
                ans.append(seen[c])
            return tuple(ans)  
        pattern = hash(pattern)
        return [w for w in words if hash(w) == pattern]