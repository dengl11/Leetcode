class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        diff1, diff2 = b-a, c-b
        if min(diff1, diff2) == 2: mi = 1
        else: mi = (diff1>1) + (diff2>1)
        ma = diff2 + diff1 - 2
        return [mi, ma]