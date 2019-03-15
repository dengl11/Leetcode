from collections import Counter
from functools import reduce
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A: return []
        counts = Counter(A[0])
        for w in A[1:]:
            curr = Counter(w)
            for k, c in counts.items():
                counts[k] = min(counts[k], curr[k])
        
        return reduce(lambda x,y: x + y, [[k] * c for (k, c) in counts.items()], [])