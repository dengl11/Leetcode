from functools import lru_cache
class Solution(object):
    def canIWin(self, mi, total):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if total <= 0: return True
        if mi * (mi + 1) // 2 < total: return False
        @lru_cache(None)
        def query(state, remain):
            if remain <= 0: return False
            for i in range(1, mi + 1):
                if state & (1 << i): continue
                if not query(state | (1 << i), remain - i): return True
            return False
        return query(0, total)
                
            
                