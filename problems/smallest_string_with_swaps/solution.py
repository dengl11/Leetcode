from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = dict()
        def find(i):
            if uf.get(i, i) != i:
                uf[i] = find(uf[i])
            return uf.get(i, i)
        
        def union(i, j):
            uf[find(i)] = find(j)

        for i, j in pairs:
            union(i, j)
        
        ans = [None] * len(s)
        groups = defaultdict(list)
        for i in range(len(s)):
            groups[find(i)].append(i)
        
        for arr in groups.values():
            chars = sorted([s[i] for i in arr], reverse= True)
            for i in arr:
                ans[i] = chars.pop()
                
        return "".join(ans)
            