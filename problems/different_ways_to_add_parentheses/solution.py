from functools import lru_cache
from itertools import product
def f(op, x, y):
    if op == "+": return x + y
    if op == "-": return x - y
    return x * y

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        @lru_cache(None)
        def query(s):
            ans = []
            for j in range(len(s)):
                if s[j] in ["*", "-", "+"]:
                    left = query(s[:j])
                    right = query(s[j+1:])
                    for l, r in product(left, right):
                        ans.append(f(s[j], l, r))
            if not ans: return [int(s)]
            return ans
        
        return query(input)
                    
                    
                    
                    
        