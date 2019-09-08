from bisect import bisect_right as br
from collections import defaultdict
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {-1: 0} # {val: ops}
        arr2.sort()
        for x in arr1:
            curr = defaultdict(lambda: float('inf'))
            for val, ops in dp.items():
                if x > val:
                    curr[x] = min(curr[x], ops)
                idx = br(arr2, val)
                if idx < len(arr2):
                    v2 = arr2[idx]
                    curr[v2] = min(curr[v2], ops + 1)
            dp = curr
        if dp: return min(dp.values())
        return -1
                