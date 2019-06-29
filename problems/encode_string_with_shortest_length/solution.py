from functools import lru_cache
class Solution:
    def encode(self, s: str) -> str:
        @lru_cache(None)
        def query(s):
            single = s
            i = (s + s).find(s, 1)
            if i < len(s):
                single = "{}[{}]".format(len(s) // i, query(s[:i]))
            multi = [query(s[:i]) + query(s[i:]) for i in range(1, len(s))]
            return min([s, single] + multi, key = len)
        return query(s)
        