from collections import Counter
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        c = Counter(A)
        candidates = [x for x in c if c[x] == 1]
        if not candidates: return -1
        return max(candidates)