from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        indexes = deque(range(len(deck)))
        ans = [None] * len(deck)
        for x in sorted(deck):
            ans[indexes.popleft()] = x
            indexes.rotate(-1)
        return ans
            