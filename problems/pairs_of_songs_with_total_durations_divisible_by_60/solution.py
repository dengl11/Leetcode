from collections import Counter
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pairs = Counter()
        n = 0
        for t in time:
            t = t % 60
            n += pairs[(60 - t) % 60]
            pairs[t] += 1
        return n
        
            
        