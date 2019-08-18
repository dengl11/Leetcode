from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars)
        def ok(w):
            for k, v in Counter(w).items():
                if chars[k] < v: return False
            return True
        return sum(len(w) for w in words if ok(w))