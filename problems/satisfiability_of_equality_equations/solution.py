import string
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parents = {ch: ch for ch in string.ascii_lowercase}
        def find(ch):
            if parents[ch] != ch:
                parents[ch] = find(parents[ch])
            return parents[ch]
        for e in equations:
            if e[1] == '=':
                a, b = e[0], e[-1]
                parents[find(a)] = find(b)
        for e in equations:
            if e[1] == '!':
                a, b = e[0], e[-1]
                if find(a) == find(b):
                    return False
        return True
        