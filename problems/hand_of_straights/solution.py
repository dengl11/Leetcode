from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0: return False
        mins = sorted(list(set(hand)))
        c = Counter(hand)
        for x in mins:
            if c[x] == 0: continue
            for y in range(x+1, x + W):
                c[y] -= c[x]
                if c[y] < 0: return False
        return True
        
        