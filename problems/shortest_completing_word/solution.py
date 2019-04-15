from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        c = Counter()
        for ch in licensePlate:
            if ch.isalpha():
                c[ch.lower()] += 1
        ans = None
        for w in words:
            curr = Counter(w.lower())
            if all(curr[k] >= c[k] for k in c):
                if ans is None or len(w) < len(ans):
                    ans = w
        return ans
        