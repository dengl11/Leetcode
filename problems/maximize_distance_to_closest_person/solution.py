from itertools import groupby
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans = 1
        i = 0
        groups = list((k, len(list(v))) for (k, v) in groupby(seats))
        for (x, c) in groups:
            if x == 0:
                if i == 0 or i == len(groups) - 1:
                    ans = max(ans, c)
                else:
                    
                    ans = max(ans, (c + c % 2)//2)
            i += 1
        return ans
                
            