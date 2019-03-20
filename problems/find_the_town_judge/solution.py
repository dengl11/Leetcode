from collections import defaultdict
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        candidates = set(range(1, N + 1))
        trustedBy = defaultdict(set)
        for a, b in trust:
            if a in candidates:
                candidates.remove(a)
            if a != b:
                trustedBy[b].add(a)
        if len(candidates) == 1:
            ans = list(candidates)[0]
            if len(trustedBy[ans]) == N -1: return ans
        return -1
            
        