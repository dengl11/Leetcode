from collections import Counter
from functools import lru_cache
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickers = [Counter(s) for s in stickers]
        inf = float('inf')
        @lru_cache(None)
        def query(s):
            """
            s: a string
            """
            if not s: return 0
            c = Counter(s)
            ans = inf
            for st in stickers:
                if s[-1] not in st: continue
                ns = ""
                for k, v in c.items():
                    ns += k * (max(0, v - st[k]))
                ans = min(ans, query(ns) + 1)
            return ans
        
        ans = query(target)
        return ans if ans != inf else -1
                
                
            