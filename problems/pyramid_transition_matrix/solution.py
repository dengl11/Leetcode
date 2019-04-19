from collections import defaultdict
from itertools import product
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        blocks = defaultdict(list)
        for x in allowed:
            blocks[x[:2]].append(x[-1])
        def explore(s):
            if len(s) == 2: return s in blocks
            for it in product(*[blocks[s[i:i+2]] for i in range(0, len(s)-1)]):
                if explore("".join(it)): return True
            return False
        return explore(bottom)
            
        