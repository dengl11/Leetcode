from collections import defaultdict
from functools import lru_cache
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = set(words)
        nbrs = defaultdict(list)
        chrs = [chr(97+i) for i in range(26)]
        for w in words:
            for i in range(len(w)+1):
                for c in chrs:
                    cw = w[:i]+ c + w[i:]
                    if cw in words:
                        nbrs[w].append(cw)
        @lru_cache(None)
        def query(w):
            ans = 1
            for nw in nbrs[w]:
                ans = max(ans, query(nw) + 1)
            return ans
        return max(query(w) for w in words)