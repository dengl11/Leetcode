from collections import defaultdict
from bisect import bisect_left
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        idx = defaultdict(list)
        for i, c in enumerate(source):
            idx[c].append(i)
        ans = 1
        i = -1
        for c in target:
            if c not in idx: return -1
            j = bisect_left(idx[c], i)
            if j >= len(idx[c]):
                ans += 1
                i = idx[c][0] + 1
            else:
                i = idx[c][j] + 1
        return ans