from itertools import product
class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        ans = []
        S = S[1:-1]
        def construct(s):
            if len(s) == 1: return [s]
            if s[-1] == "0":
                return [s] if s[0] != "0" else []
            if s[0] == "0":
                return ["0."+s[1:]]
            ans = [s]
            for i in range(1, len(s)):
                ans.append(s[:i] + "."+s[i:])
            return ans
                    
                
        for i in range(1, len(S)):
            left = construct(S[:i])
            right = construct(S[i:])
            for l, r in product(left, right):
                ans.append("({}, {})".format(l, r))
                
        return ans
        