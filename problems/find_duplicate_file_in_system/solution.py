from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        F = defaultdict(list)
        for p in paths:
            eles = p.split()
            dirname, files = eles[0], eles[1:]
            for f in files:
                content = f[f.index('('):-1]
                F[content].append(dirname + "/" + f[:f.index('(')])
        return list(v for v in F.values() if len(v) > 1)