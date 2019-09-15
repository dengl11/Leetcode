from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        needed = Counter("balloon")
        return min(c[k] // needed[k] for k in needed)