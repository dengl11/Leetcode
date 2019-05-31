from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def query(s):
            if len(s) == 1:
                return 9 if s[0] == '*' else int(s[0]!='0')
            if s[0] =='*':
                if s[1] == '*': return 15
                else:
                    if int(s[1]) < 7: return 2
                    else:return 1
            if s[1] =='*':
                if int(s[0]) == 1: return 9
                if int(s[0]) == 2: return 6
                return 0
            if s[0] =='0': return 0
            return 1 if int(s) < 27 else 0
        
        if len(s) < 2: return query(s)
        pre2, pre = query(s[0]), query(s[0]) * query(s[1]) + query(s[:2])
        p = s[1]
        for c in s[2:]:
            pre, pre2 = pre * query(c) + pre2 * query(p + c), pre
            p = c
        return pre % (10**9 + 7)