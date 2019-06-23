from itertools import product
class Solution:
    def braceExpansionII(self, exp: str) -> List[str]:
        groups = [[]]
        start = 0
        level = 0
        for i, c in enumerate(exp):
            if c == "{":
                level += 1
                if level == 1:
                    start = i+1
            elif c == "}":
                level -= 1
                if level == 0:
                    groups[-1].append(self.braceExpansionII(exp[start:i]))
            elif c == "," and level == 0:
                groups.append([])
            elif level == 0:
                groups[-1].append([c])
        ans = set()
        for g in groups:
            ans |= set("".join(x) for x in product(*g))
        return sorted(ans)
                    