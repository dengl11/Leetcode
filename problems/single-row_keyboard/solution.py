class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pos = {c:i for i, c in enumerate(keyboard)}
        curr = ans = 0
        for ch in word:
            ans += abs(curr - pos[ch])
            curr = pos[ch]
        return ans