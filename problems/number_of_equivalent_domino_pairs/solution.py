from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        def hash(d):
            return tuple(sorted(d))
        
        d = defaultdict(int)
        for do in dominoes:
            d[hash(do)] += 1
        return sum(c * (c-1) // 2 for c in d.values())