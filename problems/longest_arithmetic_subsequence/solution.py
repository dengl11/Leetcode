from collections import defaultdict
from bisect import bisect_right
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        pos = defaultdict(list) # {val: [pos]}
        for i, x in enumerate(A):
            pos[x].append(i)
        ans = 2
        dp = {} # {(i, j): max_subseq_len}
        for j in range(1, len(A)):
            for i in range(j):
                pre = 2*A[i] - A[j]
                pre_idx = bisect_right(pos[pre], i-1) - 1
                if pre_idx >= 0 and pre_idx < len(pos[pre]):
                    dp[(i, j)] = dp[(pos[pre][pre_idx], i)] + 1
                    ans = max(ans, dp[(i, j)])
                else:
                    dp[(i, j)] = 2
        return ans    