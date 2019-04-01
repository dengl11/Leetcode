from collections import Counter
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        a, b = Counter(A.split()), Counter(B.split())
        ans = []
        for k, v in a.items():
            if v > 1 or k in b: continue
            ans.append(k)
        for k, v in b.items():
            if v > 1 or k in a: continue
            ans.append(k)
        return ans
        