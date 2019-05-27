from collections import Counter, deque
from functools import reduce
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse(s):
            ans = Counter()
            i = 0
            j = 1
            while j < len(s): # s[i] is the previous captical letter
                if s[j].isdigit() or s[j].isupper():
                    ele = s[i:j]
                    if s[j].isupper():
                        i = j
                        j += 1
                        d = 1
                    else:
                        k = j+1
                        while k < len(s) and s[k].isdigit():
                            k += 1
                        d = int(s[j:k])
                        i = k
                        j = i+1
                    ans[ele] += d
                else:
                    j += 1
            if i < len(s) and i < j:
                ans[s[i:j]] += 1
            return ans
        
        stack = []
        f = deque(formula)
        while f:
            if f[0] == "(":
                f.popleft()
                stack.append(None)
            elif f[0] == ')':
                j = 1
                while j < len(formula) and formula[j].isdigit():
                    j += 1
                f.popleft()
                d = ""
                while f and f[0].isdigit(): d += f.popleft()
                d = int(d) if d else 1
                pre = stack.pop()
                while stack and stack[-1] is not None:
                    pre += stack.pop()
                    # print(pre)
                stack.pop()
                for k in pre:
                    pre[k] *= d
                stack.append(pre)
            else:
                curr = ""
                while f and f[0] not in ['(', ')']:
                    curr += f.popleft()
                stack.append(parse(curr))
                # print(stack)
        # print(stack)
        c = reduce(lambda x,y: x+y, stack, Counter())
        ans = ""
        for k in sorted(c.keys()):
            ans += k
            if c[k] > 1:
                ans += str(c[k])
        return ans
            
        