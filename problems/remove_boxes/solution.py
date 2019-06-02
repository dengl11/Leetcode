from functools import lru_cache
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def query(i, j, k):
            if j < i: return 0
            m = i
            while m+1 <= j and boxes[m+1] == boxes[m]:
                m += 1
            i, k = m, k + (m-i)
            ans = (k+1) ** 2 + query(m+1, j, 0)
            for y in range(i+2, j+1):
                if boxes[y] == boxes[i]:
                    ans = max(ans, query(y, j, k+1) + query(i+1, y-1, 0))
            return ans
    
        return query(0, len(boxes)-1, 0)