from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        cp = Counter(p)
        counters = [[0 for _ in range(ns+1)] for _ in range(26)] 
        pre = Counter()
        for i, ch in enumerate(s, 1):
            pre[ch] += 1
            for c in range(26):
                counters[c][i] = pre[chr(c + 97)]
            
        ans = []
        for i in range(ns - np + 1):
            ok = all(counters[c][i+np] - counters[c][i] == cp[chr(c+97)] for c in range(26))
            if ok:
                ans.append(i)
        return ans
        