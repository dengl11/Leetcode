from collections import Counter
from bisect import bisect_right
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f = lambda s: Counter(s)[min(s)]
        queries = [f(w) for w in queries]
        words = sorted([f(w) for w in words])
        
        def n_greater(i):
            idx = bisect_right(words, i)
            return len(words) - idx
        
        return [n_greater(x) for x in queries]
            
        
        