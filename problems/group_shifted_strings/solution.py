from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        def hash(s):
            if not s: return None
            a = []
            base = ord(s[0])
            for c in s:
                a.append((ord(c) - base + 26)%26)
            return tuple(a)
        for i, s in enumerate(strings):
            ans[hash(s)].append((s, i))
            
        ans = list(ans.values())
        ans.sort(key = lambda arr: arr[0][1])
        return [[x[0] for x in r] for r in ans]