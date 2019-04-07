from itertools import groupby
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        i = 0
        ans = []
        for k, l in groupby(S):
            curr = len(list(l))
            nexti = i + curr
            if curr >= 3:
                ans.append([i, nexti-1])
            i = nexti
        return ans